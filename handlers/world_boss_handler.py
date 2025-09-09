"""世界Boss处理器"""
from astrbot.api.all import *
from astrbot.api.message_components import Record, Plain
from ..core.data_manager import *
from ..core.world_boss_system import *
import os
import random

class WorldBossHandler:
    def __init__(self):
        # 获取可可萝语音文件目录
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.voice_dir = os.path.join(current_dir, "static", "boss", "kkr")

    def get_random_kkr_voice(self):
        """随机选择一个可可萝语音文件"""
        try:
            if not os.path.exists(self.voice_dir):
                return None
            
            # 获取所有音频文件
            voice_files = [f for f in os.listdir(self.voice_dir) 
                          if f.endswith(('.mp3', '.wav', '.ogg'))]
            
            if not voice_files:
                return None
            
            # 随机选择一个语音文件
            selected_voice = random.choice(voice_files)
            return os.path.join(self.voice_dir, selected_voice)
            
        except Exception as e:
            print(f"[World Boss Handler] 获取可可萝语音失败: {e}")
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
                yield event.plain_result("当前没有世界Boss，请等待管理员刷新Boss！")
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
                    
                    # 显示每个人的具体奖励
                    for user_id, reward_info in attack_result["phase_rewards"].items():
                        nickname = reward_info["nickname"]
                        coins = reward_info["coins"]
                        items = reward_info["items"]
                        damage = reward_info["total_damage"]
                        
                        result_msg += f"• {nickname} (伤害{damage:,}) 获得：\n"
                        result_msg += f"  💰 {coins}金币\n"
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

            # 攻击成功后播放可可萝语音，和攻击结果一起发送
            voice_file = self.get_random_kkr_voice()
            if voice_file:
                try:
                    # 将攻击结果和语音一起发送
                    yield event.chain_result([Plain(result_msg), Record(file=voice_file)])
                except Exception as e:
                    print(f"[World Boss Handler] 播放可可萝语音失败: {e}")
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
                
                ranking_msg += "\n🎉 感谢所有勇士的参与！下次世界Boss将在一周后刷新！"
                
                yield event.plain_result(ranking_msg)

        except Exception as e:
            print(f"[World Boss Handler] attack_boss函数发生异常: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f'攻击Boss时出现错误: {str(e)}')
