"""旅行系统核心模块"""
import random
from datetime import datetime, timedelta
from . import data_manager
from ..config.travel_config import TRAVEL_DESTINATIONS, SOUVENIRS, MUSEUMS
from ..utils.formatters import format_number
from ..utils.experience_utils import process_experience_gain
from ..config.experience_config import get_exp_required_for_level


def check_and_process_completed_travels():
    """检查并处理完成的旅行"""
    current_time = datetime.now()
    completed_users = []
    
    for user_id, travel_data in data_manager.travel_status.items():
        if travel_data.get('is_traveling', False):
            end_time = datetime.fromisoformat(travel_data['end_time'])
            if current_time >= end_time:
                completed_users.append(user_id)
    
    # 处理旅行完成的用户
    for user_id in completed_users:
        result = process_travel_completion(user_id)
        if result:
            data_manager.offline_completed_travels[user_id] = result


def process_travel_completion(user_id: str):
    """处理旅行完成的用户"""
    print(f"[旅行完成] 开始处理用户 {user_id}")
    print(f"[旅行完成] 当前travel_status中的用户: {list(data_manager.travel_status.keys())}")
    
    if user_id not in data_manager.travel_status:
        print(f"[旅行完成] 用户 {user_id} 不在travel_status中")
        return None
        
    travel_data = data_manager.travel_status[user_id]
    destination_index = travel_data['destination_index']
    nickname = travel_data['nickname']
    group_id = travel_data.get('group_id')
    
    print(f"[旅行完成] 用户 {user_id} 旅行目的地: {destination_index}, 群组: {group_id}")
    
    # 获取旅行目的地信息
    if destination_index not in TRAVEL_DESTINATIONS:
        print(f"[旅行完成] 无效的旅行目的地: {destination_index}")
        return None
    
    destination = TRAVEL_DESTINATIONS[destination_index]
    
    # 获取用户数据
    user_data = data_manager.get_user_data(user_id)
    wife_data = data_manager.get_user_wife_data(user_id)
    
    if not wife_data:
        print(f"[旅行完成] 用户 {user_id} 没有老婆数据")
        return None
    
    # 计算旅行奖励
    travel_result = calculate_travel_rewards(destination, user_id)
    
    # 获取当前老婆属性
    wife_level = wife_data[5] if len(wife_data) > 5 else 1
    wife_growth = wife_data[6] if len(wife_data) > 6 else 0
    wife_hunger = wife_data[7] if len(wife_data) > 7 else 100
    wife_cleanliness = wife_data[8] if len(wife_data) > 8 else 100
    wife_health = wife_data[9] if len(wife_data) > 9 else 100
    wife_mood = wife_data[10] if len(wife_data) > 10 else 100
    
    # 处理成长值和升级逻辑（无论是否被抓都有基础成长值奖励）
    growth_reward = destination["effects"].get("growth", 0)
    exp_result = None
    new_level = wife_level
    new_growth = wife_growth
    level_up_messages = []
    
    if growth_reward > 0:
        exp_result = process_experience_gain(wife_level, wife_growth, growth_reward)
        new_level = exp_result["new_level"]
        new_growth = exp_result["new_growth"]
        level_up_messages = exp_result.get("level_up_messages", [])
    
    # 如果被抓去咕咕园区，基础属性不变化（但仍有成长值奖励）
    if travel_result.get("captured", False):
        # 被抓了，基础属性不变
        new_hunger = wife_hunger
        new_cleanliness = wife_cleanliness
        new_health = wife_health
        new_mood = wife_mood
    else:
        # 正常旅行，更新老婆属性
        new_hunger = max(0, min(1000, wife_hunger + destination["effects"]["hunger"]))
        new_cleanliness = max(0, min(1000, wife_cleanliness + destination["effects"]["cleanliness"]))
        new_health = max(0, min(1000, wife_health + destination["effects"]["health"]))
        new_mood = max(0, min(1000, wife_mood + destination["effects"]["mood"]))
    
    # 更新数据
    data_manager.update_user_wife_data(
        user_id,
        level=new_level,
        growth=new_growth,
        hunger=new_hunger,
        cleanliness=new_cleanliness, 
        health=new_health,
        mood=new_mood
    )
    
    # 添加奖励物品到背包
    for item_name, quantity in travel_result["items"]:
        data_manager.add_item_to_backpack(user_id, item_name, quantity)
    
    # 清除旅行状态
    del data_manager.travel_status[user_id]
    data_manager.save_travel_status()
    
    # 构建完成消息
    wife_name = wife_data[0]
    wife_display_name = wife_name.split('.')[0]
    
    message = f": {nickname}，{wife_display_name}的{destination['country']}·{destination['city']}之旅结束了！\n\n"
    message += f"🎒 旅行体验：{destination['journey'][:100]}...\n\n"
    
    message += "📊 【老婆属性变化】\n"
    
    # 计算实际变化量
    level_change = new_level - wife_level
    growth_change = new_growth - wife_growth
    hunger_change = new_hunger - wife_hunger
    cleanliness_change = new_cleanliness - wife_cleanliness
    health_change = new_health - wife_health
    mood_change = new_mood - wife_mood
    
    # 格式化变化量显示
    def format_change(change):
        if change > 0:
            return f"(+{change})"
        elif change < 0:
            return f"({change})"
        else:
            return "(+0)"
    
    # 显示等级和成长值变化（如果有）
    if level_change > 0 or growth_change != 0:
        message += f"⭐ 等级：{wife_level} → {new_level} {format_change(level_change)}\n"
        if growth_reward > 0:
            # 显示完整的成长值进度信息
            next_level_exp = get_exp_required_for_level(new_level + 1)
            exp_percentage = round((new_growth / next_level_exp * 100), 1) if next_level_exp > 0 else 100
            message += f"📈 成长值 +{growth_reward} → {new_growth}/{next_level_exp} ({exp_percentage}%)\n"
    
    message += f"🍽️ 饥饿值：{wife_hunger} → {new_hunger} {format_change(hunger_change)}\n"
    message += f"🛁 清洁值：{wife_cleanliness} → {new_cleanliness} {format_change(cleanliness_change)}\n"
    message += f"❤️ 健康值：{wife_health} → {new_health} {format_change(health_change)}\n"
    message += f"😊 心情值：{wife_mood} → {new_mood} {format_change(mood_change)}\n\n"
    
    message += "🎁 【旅行收获】\n"
    for item_name, quantity in travel_result["items"]:
        if quantity > 0:
            message += f"   📦 {item_name} x{quantity}\n"
    
    if travel_result["special_message"]:
        message += f"\n{travel_result['special_message']}"
    
    # 添加升级消息（如果有）
    if level_up_messages:
        wife_name_display = wife_data[0].split('.')[0] if wife_data and wife_data[0] else "老婆"
        level_up_text = "\n" + "\n".join([msg.replace("升级了！", f"{wife_name_display}升级了！") for msg in level_up_messages])
        message += level_up_text + "\n"
    
    message += f"\n💡 碎片可通过「赠送礼物」给老婆使用，满100个可提升对应属性！"
    
    print(f"[旅行完成] 用户 {user_id} 完成旅行，生成消息")
    
    return {
        'message': message,
        'group_id': group_id,
        'unified_msg_origin': travel_data.get('unified_msg_origin', f"aiocqhttp:GroupMessage:{group_id}"),
        'user_id': user_id,
        'nickname': nickname
    }


def calculate_travel_rewards(destination, user_id):
    """计算旅行奖励"""
    result = {
        "items": [],
        "special_message": "",
        "captured": False  # 添加被抓标志
    }
    
    # 缅甸特殊机制：50%概率被抓去咕咕园区，什么都得不到
    if destination["city"] == "仰光":
        if random.random() < 0.5:  # 50%概率
            result["special_message"] = "🚫 被抓去咕咕园区了，获得的东西全部被拿走了！"
            result["captured"] = True  # 标记被抓
            return result  # 直接返回空奖励
    
    # 计算碎片奖励
    if destination["charm_fragments"][0] > 0:
        # 反差萌碎片
        fragment_count = random.randint(destination["charm_fragments"][0], destination["charm_fragments"][1])
        result["items"].append(("反差萌碎片", fragment_count))
    
    if destination["blackening_fragments"][0] > 0:
        # 黑化率碎片
        fragment_count = random.randint(destination["blackening_fragments"][0], destination["blackening_fragments"][1])
        result["items"].append(("黑化率碎片", fragment_count))
    
    # 随机纪念品伴手礼（100%获得）
    city = destination["city"]
    if city in SOUVENIRS:
        souvenir = random.choice(SOUVENIRS[city])
        # 不添加到items列表中，只在special_message中显示
        result["special_message"] += f"🎁 获得纪念品：{souvenir['name']} - {souvenir['description']}\n"
        # 添加到用户背包
        data_manager.add_item_to_backpack(user_id, souvenir["name"], 1)
    
    # 历史文物（10%概率）
    if random.random() < 0.1:  # 10%概率
        artifact = random.choice(destination["artifacts"])
        # 添加到历史文物库，不是背包
        data_manager.add_artifact(user_id, artifact, 1)
        result["special_message"] += f"🏛️ 意外发现历史文物：{artifact}！可捐赠给博物馆获得丰厚奖励！\n"
    
    return result
