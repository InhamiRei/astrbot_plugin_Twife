"""旅行系统处理器"""

import random
from datetime import datetime, timedelta
from ..core import data_manager
from ..config.travel_config import TRAVEL_DESTINATIONS, SOUVENIRS, FRAGMENT_CONVERSION
from ..utils.formatters import format_number


class TravelHandler:
    """旅行系统处理器"""
    
    def __init__(self):
        pass
    
    async def travel_list(self, event):
        """显示旅行列表"""
        try:
            user_id = str(event.get_sender_id())
            
            # 检查用户是否有老婆
            if not data_manager.has_wife(user_id):
                yield event.plain_result("❌ 请先抽取老婆再来旅行吧~")
                return
            
            # 构建旅行列表消息
            result_msg = "🌍 【世界旅行列表】 🌍\n\n"
            
            for index, destination in TRAVEL_DESTINATIONS.items():
                country = destination["country"]
                city = destination["city"] 
                description = destination["description"]
                duration = destination["duration"]
                cost = format_number(destination["cost"])
                
                
                result_msg += f"🗺️ {index}. {country}·{city}: {description}\n"
                result_msg += f"⏰ 时长：{duration}\n"
                result_msg += f"💰 费用：{cost}金币\n"
            
            result_msg += "\n💡 使用「出门旅行 序号」开始你的旅程！\n"
            result_msg += "📦 碎片可积攒到100个后赠送给老婆提升属性"
            
            yield event.plain_result(result_msg)
            
        except Exception as e:
            print(f"[旅行列表] 执行失败: {e}")
            yield event.plain_result(f"❌ 查看旅行列表时发生错误: {str(e)}")
    
    async def go_travel(self, event):
        """出门旅行"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
            group_id = str(event.message_obj.group_id)
            unified_msg_origin = event.unified_msg_origin
            
            # 检查用户是否有老婆
            if not data_manager.has_wife(user_id):
                yield event.plain_result("❌ 请先抽取老婆再来旅行吧~")
                return
            
            # 检查是否已经在旅行中
            if user_id in data_manager.travel_status and data_manager.travel_status[user_id].get('is_traveling', False):
                travel_data = data_manager.travel_status[user_id]
                from datetime import datetime
                end_time = datetime.fromisoformat(travel_data['end_time'])
                destination = TRAVEL_DESTINATIONS[travel_data['destination_index']]
                yield event.plain_result(f"❌ 老婆正在{destination['country']}·{destination['city']}旅行中，请等待旅行结束！\n⏰ 预计返回时间：{end_time.strftime('%Y-%m-%d %H:%M:%S')}")
                return
            
            # 解析命令参数
            message_str = event.message_str.strip()
            parts = message_str.split()
            
            if len(parts) < 2:
                yield event.plain_result("❌ 请指定旅行目的地序号！格式：出门旅行 序号")
                return
            
            try:
                destination_index = int(parts[1])
            except ValueError:
                yield event.plain_result("❌ 请输入有效的序号！")
                return
            
            if destination_index not in TRAVEL_DESTINATIONS:
                yield event.plain_result(f"❌ 无效的旅行目的地序号！请输入1-{len(TRAVEL_DESTINATIONS)}之间的数字")
                return
            
            # 获取用户数据
            user_data = data_manager.get_user_data(user_id)
            wife_data = data_manager.get_user_wife_data(user_id)
            
            if not wife_data:
                yield event.plain_result("❌ 找不到老婆数据！")
                return
            
            destination = TRAVEL_DESTINATIONS[destination_index]
            
            # 检查金币是否足够
            if user_data["coins"] < destination["cost"]:
                need_coins = destination["cost"] - user_data["coins"]
                yield event.plain_result(f"❌ 金币不足！还需要{format_number(need_coins)}金币才能前往{destination['country']}·{destination['city']}")
                return
            
            # 检查老婆状态
            wife_hunger = wife_data[7] if len(wife_data) > 7 else 100
            wife_health = wife_data[9] if len(wife_data) > 9 else 100
            wife_mood = wife_data[10] if len(wife_data) > 10 else 100
            
            # 状态检查
            if wife_hunger < 20:
                yield event.plain_result("❌ 老婆太饿了，无法进行长途旅行！请先喂食恢复饥饿值到20以上")
                return
            
            if wife_health < 30:
                yield event.plain_result("❌ 老婆身体状况不佳，无法进行旅行！请先恢复健康值到30以上")
                return
            
            if wife_mood < 30:
                yield event.plain_result("❌ 老婆心情不好，不想去旅行！请先改善心情到30以上")
                return
            
            # 扣除金币
            new_coins = user_data["coins"] - destination["cost"]
            data_manager.update_user_data(user_id, coins=new_coins)
            
            # 设置旅行状态
            from datetime import datetime, timedelta
            
            # 解析duration字符串（如"10h", "8h"）
            duration_str = destination["duration"]
            if duration_str.endswith('h'):
                hours = int(duration_str[:-1])
            else:
                hours = 8  # 默认8小时
            
            start_time = datetime.now()
            end_time = start_time + timedelta(hours=hours)
            
            # 保存旅行状态
            data_manager.travel_status[user_id] = {
                'is_traveling': True,
                'destination_index': destination_index,
                'start_time': start_time.isoformat(),
                'end_time': end_time.isoformat(),
                'nickname': nickname,
                'group_id': group_id,
                'unified_msg_origin': unified_msg_origin
            }
            data_manager.save_travel_status()
            
            # 安排任务完成通知
            if data_manager.wife_plugin_instance:
                data_manager.wife_plugin_instance.schedule_task_completion(user_id, "travel", end_time)
            
            # 获取老婆名称
            wife_name = wife_data[0]
            wife_display_name = wife_name.split('.')[0]
            
            # 构建开始旅行消息
            result_msg = f"✈️ 【开始{destination['country']}·{destination['city']}之旅】 ✈️\n\n"
            result_msg += f"👤 旅行者：{nickname}和{wife_display_name}\n"
            result_msg += f"🎯 目的地：{destination['country']}·{destination['city']}\n"
            result_msg += f"📝 介绍：{destination['description']}\n"
            result_msg += f"⏰ 旅行时长：{destination['duration']}\n"
            result_msg += f"💰 旅行费用：{format_number(destination['cost'])}金币\n"
            result_msg += f"💳 剩余金币：{format_number(new_coins)}金币\n\n"
            
            result_msg += f"📅 出发时间：{start_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
            result_msg += f"🏠 返回时间：{end_time.strftime('%Y-%m-%d %H:%M:%S')}"
            
            yield event.plain_result(result_msg)
            
        except Exception as e:
            print(f"[出门旅行] 执行失败: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f"❌ 旅行时发生错误: {str(e)}")
    
