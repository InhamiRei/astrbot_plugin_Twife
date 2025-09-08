"""打工系统核心模块"""
import random
from datetime import datetime, timedelta
from . import data_manager
from .data_manager import WORK_LIST
from ..utils.experience_utils import process_experience_gain
from ..config.experience_config import get_exp_required_for_level

def check_and_process_completed_works():
    """检查并处理完成的打工"""
    current_time = datetime.now()
    completed_users = []
    
    for user_id, work_data in data_manager.work_status.items():
        if work_data.get('is_working', False):
            end_time = datetime.fromisoformat(work_data['end_time'])
            if current_time >= end_time:
                completed_users.append(user_id)
    
    # 处理打工完成的用户
    for user_id in completed_users:
        result = process_work_completion(user_id)
        if result:
            data_manager.offline_completed_works[user_id] = result

def process_work_completion(user_id: str):
    """处理打工完成的用户"""
    print(f"[打工完成] 开始处理用户 {user_id}")
    print(f"[打工完成] 当前work_status中的用户: {list(data_manager.work_status.keys())}")
    
    if user_id not in data_manager.work_status:
        print(f"[打工完成] 用户 {user_id} 不在work_status中")
        return None
        
    work_data = data_manager.work_status[user_id]
    work_id = work_data['work_id']
    nickname = work_data['nickname']
    group_id = work_data.get('group_id')
    
    print(f"[打工完成] 用户 {user_id} 工作ID: {work_id}, 群组: {group_id}")
    
    # 查找对应的工作信息
    print(f"[打工完成] 开始查找工作ID {work_id}")
    print(f"[打工完成] WORK_LIST长度: {len(WORK_LIST) if WORK_LIST else 0}")
    print(f"[打工完成] data_manager.WORK_LIST长度: {len(data_manager.WORK_LIST) if data_manager.WORK_LIST else 0}")
    
    # 优先使用 data_manager.WORK_LIST
    work_list_to_use = data_manager.WORK_LIST if data_manager.WORK_LIST else WORK_LIST
    
    selected_work = None
    for work in work_list_to_use:
        print(f"[打工完成] 检查工作: ID={work['id']}, 名称={work['name']}")
        if work["id"] == work_id:
            selected_work = work
            print(f"[打工完成] 找到匹配的工作: {work['name']}")
            break
    
    if not selected_work:
        print(f"[打工完成] 找不到工作ID {work_id}")
        print(f"[打工完成] 可用的工作ID: {[work['id'] for work in work_list_to_use]}")
        del data_manager.work_status[user_id]
        data_manager.save_work_status()
        return None
    
    # 获取用户老婆数据
    wife_data = data_manager.get_user_wife_data(user_id)
    if not wife_data:
        print(f"[打工完成] 用户 {user_id} 没有老婆数据")
        del data_manager.work_status[user_id]
        data_manager.save_work_status()
        return None
    
    # 计算打工收益和消耗
    pay = selected_work["pay"]
    growth_reward = selected_work["growth_reward"]
    hunger_cost = selected_work["hunger_cost"]
    cleanliness_cost = selected_work["cleanliness_cost"]
    mood_cost = selected_work["mood_cost"]
    health_cost = selected_work["health_cost"]
    
    # 获取当前属性
    current_growth = wife_data[6]
    current_hunger = wife_data[7]
    current_cleanliness = wife_data[8]
    current_health = wife_data[9]
    current_mood = wife_data[10]
    
    # 获取用户金币数据
    user_data_obj = data_manager.get_user_data(user_id)
    current_coins = user_data_obj["coins"]
    
    # 更新属性
    total_growth = current_growth + growth_reward
    new_hunger = max(0, current_hunger - hunger_cost)
    new_cleanliness = max(0, current_cleanliness - cleanliness_cost)
    new_health = max(0, current_health - health_cost)
    new_mood = max(0, current_mood - mood_cost)
    new_coins = current_coins + pay
    
    # 使用新的经验系统处理升级
    current_level = wife_data[5]
    current_growth = wife_data[6]
    
    exp_result = process_experience_gain(current_level, current_growth, growth_reward)
    new_level = exp_result["new_level"]
    new_growth = exp_result["new_growth"]
    level_up = exp_result["level_ups"] > 0
    
    # 更新数据
    data_manager.update_user_wife_data(user_id, 
                        growth=new_growth,
                        hunger=new_hunger,
                        cleanliness=new_cleanliness,
                        health=new_health,
                        mood=new_mood,
                        level=new_level)
    data_manager.update_user_data(user_id, coins=new_coins)
    
    # 清除打工状态
    del data_manager.work_status[user_id]
    data_manager.save_work_status()
    
    # 构建完成消息
    wife_name = wife_data[0]
    wife_display_name = wife_name.split('.')[0]
    
    completion_messages = [
        f"{wife_display_name}打工回来了，辛苦工作后获得了报酬！",
        f"{wife_display_name}完成了今天的工作，虽然有点累但很有成就感！",
        f"{wife_display_name}从工作中回来，眼中闪烁着满足的光芒！",
        f"{wife_display_name}工作结束了，带着满满的收获回到你身边！",
        f"{wife_display_name}完成工作任务，变得更加成熟了！"
    ]
    
    result_message = f": {random.choice(completion_messages)}\n"
    result_message += f"💼 工作收获：\n"
    result_message += f"💰 获得金币 +{pay} ({current_coins} → {new_coins})\n"
    
    # 显示完整的成长值进度信息
    next_level_exp = get_exp_required_for_level(new_level + 1)
    exp_percentage = round((new_growth / next_level_exp * 100), 1) if next_level_exp > 0 else 100
    result_message += f"📈 成长值 +{growth_reward} → {new_growth}/{next_level_exp} ({exp_percentage}%)\n"
    
    result_message += f"🍽️ 饥饿值 -{hunger_cost} ({current_hunger} → {new_hunger})\n"
    result_message += f"🧼 清洁度 -{cleanliness_cost} ({current_cleanliness} → {new_cleanliness})\n"
    result_message += f"😊 心情 -{mood_cost} ({current_mood} → {new_mood})\n"
    result_message += f"❤️ 健康值 -{health_cost} ({current_health} → {new_health})\n"
    
    if exp_result["level_up_messages"]:
        result_message += "⭐ " + "\n⭐ ".join(exp_result["level_up_messages"]) + "\n"
    
    # 给出状态提醒
    warnings = []
    if new_hunger < 30:
        warnings.append("🍽️ 她看起来有点饿了，记得给她准备点食物")
    if new_cleanliness < 30:
        warnings.append("🧼 她需要好好清洁一下了")
    if new_mood < 30:
        warnings.append("😊 她的心情不太好，需要你的安慰")
    if new_health < 30:
        warnings.append("❤️ 她的身体状况不太好，需要休息")
    
    if warnings:
        result_message += f"⚠️ 贴心提醒：" + "、".join(warnings) + "哦~"
    
    print(f"[打工完成] 用户 {user_id} 消息生成完成，群组: {group_id}")
    return {
        'group_id': group_id,
        'message': result_message
    }

def check_and_process_expired_works():
    """检查并处理重启后已过期的打工任务"""
    if not data_manager.work_status:
        print("打工状态为空，跳过检查")
        return
        
    current_time = datetime.now()
    expired_users = []
    
    print(f"重启检查: 当前时间 {current_time}")
    print(f"重启检查: 发现 {len(data_manager.work_status)} 个打工状态")
    
    try:
        for user_id, work_data in data_manager.work_status.items():
            print(f"检查用户 {user_id}: {work_data}")
            if work_data.get('is_working', False):
                try:
                    end_time = datetime.fromisoformat(work_data['end_time'])
                    print(f"用户 {user_id} 打工结束时间: {end_time}")
                    if current_time >= end_time:
                        print(f"用户 {user_id} 打工已过期")
                        expired_users.append(user_id)
                    else:
                        print(f"用户 {user_id} 打工仍在进行中，剩余: {end_time - current_time}")
                except (ValueError, KeyError) as e:
                    print(f"处理用户 {user_id} 的打工数据时出错: {e}")
                    print(f"打工数据: {work_data}")
                    expired_users.append(user_id)
            else:
                print(f"用户 {user_id} 不在打工状态")
        
        # 处理过期的打工任务
        for user_id in expired_users:
            try:
                result = process_expired_work(user_id)
                if result:
                    data_manager.offline_completed_works[user_id] = result
            except Exception as e:
                print(f"处理用户 {user_id} 的过期打工任务时出错: {e}")
                if user_id in data_manager.work_status:
                    del data_manager.work_status[user_id]
                    data_manager.save_work_status()
        
        if expired_users:
            print(f"重启后处理了 {len(expired_users)} 个过期的打工任务")
            
    except Exception as e:
        print(f"检查过期打工任务时出错: {e}")

def process_expired_work(user_id: str):
    """处理单个过期的打工任务"""
    if user_id not in data_manager.work_status:
        return None
        
    work_data = data_manager.work_status[user_id]
    work_id = work_data['work_id']
    nickname = work_data['nickname']
    group_id = work_data.get('group_id')
    
    # 查找对应的工作信息
    selected_work = None
    for work in WORK_LIST:
        if work["id"] == work_id:
            selected_work = work
            break
    
    if not selected_work:
        del data_manager.work_status[user_id]
        data_manager.save_work_status()
        return None
    
    # 获取用户老婆数据
    wife_data = data_manager.get_user_wife_data(user_id)
    if not wife_data:
        del data_manager.work_status[user_id]
        data_manager.save_work_status()
        return None
    
    # 计算打工收益和消耗
    pay = selected_work["pay"]
    growth_reward = selected_work["growth_reward"]
    hunger_cost = selected_work["hunger_cost"]
    cleanliness_cost = selected_work["cleanliness_cost"]
    mood_cost = selected_work["mood_cost"]
    health_cost = selected_work["health_cost"]
    
    # 获取当前属性
    current_growth = wife_data[6]
    current_hunger = wife_data[7]
    current_cleanliness = wife_data[8]
    current_health = wife_data[9]
    current_mood = wife_data[10]
    
    # 获取用户金币数据
    user_data_obj = data_manager.get_user_data(user_id)
    current_coins = user_data_obj["coins"]
    
    # 更新属性
    total_growth = current_growth + growth_reward
    new_hunger = max(0, current_hunger - hunger_cost)
    new_cleanliness = max(0, current_cleanliness - cleanliness_cost)
    new_health = max(0, current_health - health_cost)
    new_mood = max(0, current_mood - mood_cost)
    new_coins = current_coins + pay
    
    # 使用新的经验系统处理升级
    current_level = wife_data[5]
    current_growth = wife_data[6]
    
    exp_result = process_experience_gain(current_level, current_growth, growth_reward)
    new_level = exp_result["new_level"]
    new_growth = exp_result["new_growth"]
    level_up = exp_result["level_ups"] > 0
    
    # 更新数据
    data_manager.update_user_wife_data(user_id, 
                        growth=new_growth,
                        hunger=new_hunger,
                        cleanliness=new_cleanliness,
                        health=new_health,
                        mood=new_mood,
                        level=new_level)
    data_manager.update_user_data(user_id, coins=new_coins)
    
    # 清除打工状态
    del data_manager.work_status[user_id]
    data_manager.save_work_status()
    
    # 构建完成消息
    wife_name = wife_data[0]
    wife_display_name = wife_name.split('.')[0]
    
    completion_messages = [
        f"{wife_display_name}在你离线期间完成了打工，辛苦工作后获得了报酬！",
        f"{wife_display_name}趁你不在的时候努力工作，现在带着收获回来了！",
        f"{wife_display_name}在你离线时完成了工作任务，收获满满！",
        f"{wife_display_name}独自完成了打工，等你回来分享成果！",
        f"{wife_display_name}在你不在的时候也没有偷懒，认真完成了工作！"
    ]
    
    result_message = f": {nickname}，{random.choice(completion_messages)}\n"
    result_message += f"💼 离线打工收获：\n"
    result_message += f"💰 获得金币 +{pay} ({current_coins} → {new_coins})\n"
    
    # 显示完整的成长值进度信息
    next_level_exp = get_exp_required_for_level(new_level + 1)
    exp_percentage = round((new_growth / next_level_exp * 100), 1) if next_level_exp > 0 else 100
    result_message += f"📈 成长值 +{growth_reward} → {new_growth}/{next_level_exp} ({exp_percentage}%)\n"
    
    result_message += f"💥 工作消耗：\n"
    result_message += f"🍽️ 饥饿值 -{hunger_cost} ({current_hunger} → {new_hunger})\n"
    result_message += f"🧼 清洁度 -{cleanliness_cost} ({current_cleanliness} → {new_cleanliness})\n"
    
    if exp_result["level_up_messages"]:
        result_message += "⭐ " + "\n⭐ ".join(exp_result["level_up_messages"]) + "\n"
    
    # 给出状态提醒
    warnings = []
    if new_hunger < 30:
        warnings.append("🍽️ 她看起来有点饿了，记得给她准备点食物")
    if new_cleanliness < 30:
        warnings.append("🧼 她需要好好清洁一下了")
    if new_mood < 30:
        warnings.append("😊 她的心情不太好，需要你的安慰")
    if new_health < 30:
        warnings.append("❤️ 她的身体状况不太好，需要休息")
    
    if warnings:
        result_message += f"⚠️ 贴心提醒：" + "、".join(warnings) + "哦~"
    
    return {
        'group_id': group_id,
        'message': result_message
    }
