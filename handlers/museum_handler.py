"""博物馆系统处理器"""

import json
import os
from ..core import data_manager
from ..config.travel_config import MUSEUMS
from ..utils.formatters import format_number


class MuseumHandler:
    """博物馆系统处理器"""
    
    def __init__(self):
        self.museum_data_file = os.path.join('data', 'plugins', 'astrbot_plugin_Twife', 'data', 'museum_donations.json')
        self.museum_donations = self._load_museum_donations()
    
    def _load_museum_donations(self):
        """加载博物馆捐赠记录"""
        try:
            if os.path.exists(self.museum_data_file):
                with open(self.museum_data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                # 创建默认数据结构
                default_data = {}
                for country in MUSEUMS.keys():
                    default_data[country] = {}
                return default_data
        except Exception as e:
            print(f"加载博物馆捐赠记录失败: {e}")
            return {}
    
    def _save_museum_donations(self):
        """保存博物馆捐赠记录"""
        try:
            os.makedirs(os.path.dirname(self.museum_data_file), exist_ok=True)
            with open(self.museum_data_file, 'w', encoding='utf-8') as f:
                json.dump(self.museum_donations, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存博物馆捐赠记录失败: {e}")
    
    async def museum_list(self, event):
        """显示博物馆列表"""
        try:
            result_msg = "🏛️ 【世界博物馆列表】 🏛️\n"

            for country, museum_info in MUSEUMS.items():
                result_msg += f"🏛️ {country}：{museum_info['name']} - {museum_info['description']}\n"

                # 显示捐赠记录 - 简化格式
                if country in self.museum_donations and self.museum_donations[country]:
                    for artifact, donors in self.museum_donations[country].items():
                        # 统计捐赠总数
                        total_count = sum(donors.values())
                        result_msg += f"{artifact}x{total_count}，"
                    # 去掉最后的逗号
                    result_msg = result_msg.rstrip("，") + "\n"
                else:
                    result_msg += "\n"
            
            yield event.plain_result(result_msg)
            
        except Exception as e:
            print(f"[博物馆列表] 执行失败: {e}")
            yield event.plain_result(f"❌ 查看博物馆列表时发生错误: {str(e)}")
    
    async def donate_artifact(self, event):
        """捐赠文物"""
        try:
            user_id = str(event.get_sender_id())
            
            # 检查用户是否有老婆
            if not data_manager.has_wife(user_id):
                yield event.plain_result("❌ 请先抽取老婆再进行文物捐赠~")
                return
            
            # 解析命令参数
            message_str = event.message_str.strip()
            parts = message_str.split()
            
            if len(parts) < 2:
                yield event.plain_result("❌ 请指定要捐赠的文物名称！格式：捐赠文物 文物名称")
                return
            
            artifact_name = " ".join(parts[1:])
            
            # 检查用户历史文物库中是否有该文物
            user_data = data_manager.get_user_data(user_id)
            artifacts = user_data.get("artifacts", {})
            
            if artifact_name not in artifacts or artifacts[artifact_name] <= 0:
                yield event.plain_result(f"❌ 你的历史文物库中没有「{artifact_name}」这件文物！")
                return
            
            # 确定文物属于哪个国家的博物馆
            target_country = None
            target_museum = None
            
            for country, museum_info in MUSEUMS.items():
                if artifact_name in museum_info["artifacts_accepted"]:
                    target_country = country
                    target_museum = museum_info
                    break
            
            if not target_country:
                yield event.plain_result(f"❌ 「{artifact_name}」不是可捐赠的历史文物！")
                return
            
            # 获取用户昵称
            wife_data = data_manager.get_user_wife_data(user_id)
            user_nickname = wife_data[2] if wife_data and len(wife_data) > 2 else f"用户{user_id}"
            
            # 扣除历史文物库中的文物
            new_quantity = artifacts[artifact_name] - 1
            if new_quantity <= 0:
                del artifacts[artifact_name]
            else:
                artifacts[artifact_name] = new_quantity
            
            # 给予捐赠奖励
            rewards = target_museum["donation_rewards"]
            new_coins = user_data["coins"] + rewards["coins"]
            
            # 更新老婆的成长值（经验值）
            new_growth = None
            if wife_data and len(wife_data) > 6:
                current_growth = wife_data[6]
                new_growth = current_growth + rewards["experience"]
                data_manager.update_user_wife_data(user_id, growth=new_growth)
            
            # 更新用户数据
            data_manager.update_user_data(user_id, coins=new_coins, artifacts=artifacts)
            
            # 记录捐赠到博物馆
            if target_country not in self.museum_donations:
                self.museum_donations[target_country] = {}
            
            if artifact_name not in self.museum_donations[target_country]:
                self.museum_donations[target_country][artifact_name] = {}
            
            if user_nickname not in self.museum_donations[target_country][artifact_name]:
                self.museum_donations[target_country][artifact_name][user_nickname] = 0
            
            self.museum_donations[target_country][artifact_name][user_nickname] += 1
            
            # 保存捐赠记录
            self._save_museum_donations()
            
            # 构建结果消息
            result_msg = f"🏛️ 【文物捐赠成功】 🏛️\n\n"
            result_msg += f"🎯 博物馆：{target_museum['name']}\n"
            result_msg += f"🏺 捐赠文物：{artifact_name}\n"
            result_msg += f"👤 捐赠者：{user_nickname}\n\n"
            
            result_msg += f"🎁 【捐赠奖励】\n"
            result_msg += f"💰 获得金币：+{format_number(rewards['coins'])}\n"
            result_msg += f"💳 当前金币：{format_number(new_coins)}\n"
            result_msg += f"⭐ 获得经验：+{format_number(rewards['experience'])}\n"
            if new_growth is not None:
                result_msg += f"📊 当前成长值：{format_number(new_growth)}\n"
            result_msg += "\n"
            
            result_msg += f"📜 你的善举已被记录在{target_museum['name']}史册中！\n"
            result_msg += f"🏛️ 感谢你为人类文明保护做出的贡献！"
            
            # 检查是否达成特殊成就
            user_total_donations = sum(
                sum(artifacts.get(user_nickname, 0) for artifacts in self.museum_donations.get(country, {}).values())
                for country in self.museum_donations
            )
            
            if user_total_donations == 1:
                result_msg += f"\n\n🎉 恭喜获得成就：【文物守护者】- 首次捐赠文物！"
            elif user_total_donations == 10:
                result_msg += f"\n\n🎉 恭喜获得成就：【博物馆之友】- 捐赠文物达到10件！"
            elif user_total_donations == 50:
                result_msg += f"\n\n🎉 恭喜获得成就：【文明使者】- 捐赠文物达到50件！"
            
            yield event.plain_result(result_msg)
            
        except Exception as e:
            print(f"[捐赠文物] 执行失败: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f"❌ 捐赠文物时发生错误: {str(e)}")
    
    async def my_donations(self, event):
        """查看我的捐赠记录"""
        try:
            user_id = str(event.get_sender_id())
            
            # 检查用户是否有老婆
            if not data_manager.has_wife(user_id):
                yield event.plain_result("❌ 请先抽取老婆再查看捐赠记录~")
                return
            
            # 获取用户昵称
            wife_data = data_manager.get_user_wife_data(user_id)
            user_nickname = wife_data[2] if wife_data and len(wife_data) > 2 else f"用户{user_id}"
            
            # 统计用户捐赠记录
            result_msg = f"📜 【{user_nickname} 的捐赠记录】 📜\n"
            
            total_donations = 0
            has_donations = False
            
            for country, museum_info in MUSEUMS.items():
                museum_name = museum_info["name"]
                country_donations = []
                country_total = 0
                
                if country in self.museum_donations:
                    for artifact_name, donors in self.museum_donations[country].items():
                        if user_nickname in donors:
                            count = donors[user_nickname]
                            country_donations.append((artifact_name, count))
                            country_total += count
                            total_donations += count
                
                if country_donations:
                    has_donations = True
                    result_msg += f"🏛️ {museum_name}\n"
                    for artifact_name, count in country_donations:
                        result_msg += f"🏺 {artifact_name} x{count}"
                    result_msg += f"\n📊 小计：{country_total}件\n"
            
            if not has_donations:
                result_msg += "\n😔 暂无捐赠记录\n"
                result_msg += "💡 通过旅行获得历史文物，然后捐赠给博物馆吧！"
            else:
                result_msg += f"\n🎖️ 总捐赠数量：{total_donations}件\n"
                
                # 显示成就等级
                if total_donations >= 50:
                    result_msg += "🏆 当前称号：【文明使者】"
                elif total_donations >= 10:
                    result_msg += "🥇 当前称号：【博物馆之友】"
                elif total_donations >= 1:
                    result_msg += "🥉 当前称号：【文物守护者】"
            
            yield event.plain_result(result_msg)
            
        except Exception as e:
            print(f"[我的捐赠记录] 执行失败: {e}")
            yield event.plain_result(f"❌ 查看捐赠记录时发生错误: {str(e)}")
