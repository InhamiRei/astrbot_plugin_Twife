"""世界Boss处理器"""
from astrbot.api.all import *
from astrbot.api.message_components import Record, Plain
from ..core.data_manager import *
from ..core.world_boss_system import *
import os
import random

class WorldBossHandler:
    def __init__(self):
        # 获取Boss语音文件目录
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.boss_voice_base_dir = os.path.join(current_dir, "static", "boss")

    def get_random_boss_voice(self, boss_name="可可萝（黑化）"):
        """根据Boss类型随机选择语音文件"""
        try:
            # 根据Boss名称确定语音目录
            if "可可萝" in boss_name:
                voice_dir = os.path.join(self.boss_voice_base_dir, "kkr")
                # 可可萝使用小写的mp3文件
                extensions = ('.mp3', '.wav', '.ogg')
            elif "芋头" in boss_name:
                voice_dir = os.path.join(self.boss_voice_base_dir, "taro")
                # 大芋头王使用大写的MP3文件
                extensions = ('.MP3', '.mp3', '.wav', '.ogg')
            else:
                # 默认使用可可萝语音
                voice_dir = os.path.join(self.boss_voice_base_dir, "kkr")
                extensions = ('.mp3', '.wav', '.ogg')
            
            if not os.path.exists(voice_dir):
                print(f"[World Boss Handler] 语音目录不存在: {voice_dir}")
                return None
            
            # 获取所有音频文件
            voice_files = [f for f in os.listdir(voice_dir) 
                          if f.endswith(extensions)]
            
            if not voice_files:
                print(f"[World Boss Handler] 在{voice_dir}中未找到语音文件")
                return None
            
            # 随机选择一个语音文件
            selected_voice = random.choice(voice_files)
            voice_path = os.path.join(voice_dir, selected_voice)
            print(f"[World Boss Handler] 选择了语音文件: {voice_path}")
            return voice_path
            
        except Exception as e:
            print(f"[World Boss Handler] 获取Boss语音失败: {e}")
            return None

    async def world_boss_status(self, event: AstrMessageEvent):
        """查看世界Boss状态"""
        try:
            group_id = event.message_obj.group_id
            if not group_id:
                yield event.plain_result('该功能仅支持群聊，请在群聊中使用。')
                return

            # 获取Boss状态
            boss_status = get_world_boss_status()
            
            if not boss_status.get("exists", False):
                yield event.plain_result("当前没有世界Boss，新Boss将在明天凌晨自动刷新！")
                return
            
            # 构建状态消息
            status_msg = f"🐉 世界Boss状态 🐉\n"
            status_msg += f"Boss名称：{boss_status['name']}\n"
            status_msg += f"Boss描述：{boss_status['description']}\n"
            status_msg += f"当前阶段：第{boss_status['current_phase']}阶段 - {boss_status['phase_name']}\n"
            
            if boss_status.get('is_defeated', False):
                status_msg += "状态：已被击败！\n"
            else:
                hp_percentage = (boss_status['current_hp'] / boss_status['max_hp']) * 100
                status_msg += f"血量：{boss_status['current_hp']:,}/{boss_status['max_hp']:,} ({hp_percentage:.1f}%)\n"
                
                # 血量条显示
                bar_length = 20
                filled_length = int(bar_length * boss_status['current_hp'] / boss_status['max_hp'])
                bar = "█" * filled_length + "░" * (bar_length - filled_length)
                status_msg += f"[{bar}]\n"
            
            status_msg += f"参与人数：{boss_status['total_participants']}\n"
            status_msg += f"总伤害：{boss_status['total_damage_dealt']:,}\n"
            
            # 伤害排行榜
            if boss_status['ranking']:
                status_msg += "\n🏆 伤害排行榜 TOP10 🏆\n"
                for entry in boss_status['ranking']:
                    damage_per_attack = entry['total_damage'] / max(entry['attack_count'], 1)
                    status_msg += f"{entry['rank']}. {entry['nickname']}({entry['wife_name']}) - "
                    status_msg += f"{entry['total_damage']:,}伤害 ({entry['attack_count']}次攻击, 平均{damage_per_attack:.0f})\n"
            
            if not boss_status.get('is_defeated', False):
                status_msg += "\n⚠️ 每次攻击消耗30点健康值"
                status_msg += "\n🔢 每人每天最多可攻击5次"
                status_msg += "\n💪 使用'攻击boss'命令参与战斗！"

            yield event.plain_result(status_msg)

        except Exception as e:
            print(f"[World Boss Handler] world_boss_status函数发生异常: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f'查看世界Boss状态时出现错误: {str(e)}')

    async def attack_boss(self, event: AstrMessageEvent):
        """攻击世界Boss"""
        try:
            group_id = str(event.message_obj.group_id)
            if not group_id:
                yield event.plain_result('该功能仅支持群聊，请在群聊中使用。')
                return

            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()

            # 执行攻击
            attack_result = attack_world_boss(user_id, nickname, group_id)
            
            if not attack_result["success"]:
                yield event.plain_result(attack_result["message"])
                return

            # 构建攻击结果消息
            result_msg = f"⚔️ 战斗结果 ⚔️\n"
            # result_msg += f"攻击者：{nickname}\n"
            result_msg += f"造成伤害：{attack_result['damage']:,}\n"
            # result_msg += f"计算详情：{attack_result['damage_detail']}\n"
            
            # 显示基础奖励
            if 'base_reward_coins' in attack_result and 'base_reward_item' in attack_result:
                result_msg += f"💰 基础奖励：{attack_result['base_reward_coins']}金币\n"
                result_msg += f"🎁 战利品：{attack_result['base_reward_item']} x1\n"
            
            # Boss血量信息
            hp_percentage = (attack_result['boss_current_hp'] / attack_result['boss_max_hp']) * 100 if attack_result['boss_current_hp'] > 0 else 0
            result_msg += f"Boss血量：{max(0, attack_result['boss_current_hp']):,}/{attack_result['boss_max_hp']:,} ({hp_percentage:.1f}%)\n"
            
            # 血量条显示
            if attack_result['boss_current_hp'] > 0:
                bar_length = 20
                filled_length = int(bar_length * attack_result['boss_current_hp'] / attack_result['boss_max_hp'])
                bar = "█" * filled_length + "░" * (bar_length - filled_length)
                result_msg += f"[{bar}]\n"

            # 检查阶段击败
            if attack_result["phase_defeated"]:
                defeated_phase = attack_result.get("defeated_phase", 1)
                result_msg += f"\n🎉 恭喜！成功击败了Boss的第{defeated_phase}阶段！\n"
                
                # 显示阶段奖励
                if attack_result["phase_rewards"]:
                    result_msg += "\n🎁 阶段奖励发放：\n"
                    reward_count = len(attack_result["phase_rewards"])
                    result_msg += f"共有{reward_count}名勇士获得了奖励！\n"
                    
                    # 按排名顺序显示奖励
                    sorted_rewards = sorted(attack_result["phase_rewards"].items(), 
                                          key=lambda x: x[1].get("rank", 999))
                    
                    for user_id, reward_info in sorted_rewards:
                        nickname = reward_info["nickname"]
                        base_coins = reward_info["coins"]
                        ranking_bonus = reward_info.get("ranking_bonus", 0)
                        total_coins = reward_info.get("total_coins", base_coins)
                        items = reward_info["items"]
                        damage = reward_info["total_damage"]
                        rank = reward_info.get("rank", 0)
                        
                        # 添加排名图标
                        rank_icon = ""
                        if rank == 1:
                            rank_icon = "🥇"
                        elif rank == 2:
                            rank_icon = "🥈"
                        elif rank == 3:
                            rank_icon = "🥉"
                        else:
                            rank_icon = f"#{rank}"
                        
                        result_msg += f"• {rank_icon} {nickname} (伤害{damage:,}) 获得：\n"
                        if ranking_bonus > 0:
                            result_msg += f"  💰 基础奖励{base_coins}金币 + 排名奖励{ranking_bonus}金币 = {total_coins}金币\n"
                        else:
                            result_msg += f"  💰 {total_coins}金币\n"
                        for item in items:
                            result_msg += f"  📦 {item} x1\n"

                # 检查Boss是否完全被击败
                if attack_result["boss_defeated"]:
                    result_msg += "\n🏆 世界Boss已完全被击败！\n"
                    result_msg += "最终排行榜将在下一条消息中显示。\n"
                else:
                    # 显示下一阶段信息
                    result_msg += f"\n⚠️ Boss进入第{attack_result['next_phase']}阶段：{attack_result['next_phase_name']}\n"
                    # result_msg += f"新阶段血量：{attack_result['next_phase_hp']:,}\n"
                    # result_msg += "继续战斗吧勇士们！"

            # 根据是否击败阶段决定是否播放语音
            if attack_result["phase_defeated"]:
                # 击败阶段时只发送总结信息，不播放语音
                yield event.plain_result(result_msg)
            else:
                # 普通攻击时播放Boss对应的语音，和攻击结果一起发送
                boss_name = attack_result.get("boss_name", "可可萝（黑化）")
                
                voice_file = self.get_random_boss_voice(boss_name)
                if voice_file:
                    try:
                        # 将攻击结果和语音一起发送
                        yield event.chain_result([Plain(result_msg), Record(file=voice_file)])
                    except Exception as e:
                        print(f"[World Boss Handler] 播放Boss语音失败: {e}")
                        # 如果语音发送失败，至少发送攻击结果
                        yield event.plain_result(result_msg)
                else:
                    # 如果没有语音文件，只发送攻击结果
                    yield event.plain_result(result_msg)

            # 如果Boss完全被击败，发送最终排行榜
            if attack_result.get("boss_defeated", False) and attack_result.get("final_rewards"):
                final_ranking = attack_result["final_rewards"]
                
                ranking_msg = "🏆 最终排行榜 🏆\n"
                ranking_msg += f"总参与人数：{final_ranking['total_participants']}\n"
                ranking_msg += f"总伤害：{final_ranking['total_damage']:,}\n\n"
                
                ranking_msg += "🥇 伤害排行榜 🥇\n"
                for entry in final_ranking["ranking"][:10]:  # 只显示前10名
                    damage_per_attack = entry['total_damage'] / max(entry['attack_count'], 1)
                    medal = ""
                    if entry['rank'] == 1:
                        medal = "🥇"
                    elif entry['rank'] == 2:
                        medal = "🥈"
                    elif entry['rank'] == 3:
                        medal = "🥉"
                    
                    ranking_msg += f"{medal}{entry['rank']}. {entry['nickname']}({entry['wife_name']}) - "
                    ranking_msg += f"{entry['total_damage']:,}伤害 (共{entry['attack_count']}次攻击, 平均{damage_per_attack:.0f})\n"
                
                ranking_msg += "\n🎉 感谢所有勇士的参与！新的世界Boss将在明天凌晨自动刷新！"
                
                yield event.plain_result(ranking_msg)

        except Exception as e:
            print(f"[World Boss Handler] attack_boss函数发生异常: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f'攻击Boss时出现错误: {str(e)}')
