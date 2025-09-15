"""学习系统核心模块"""
import random
from datetime import datetime, timedelta
from ..config.education import *
from ..config.properties import get_property_study_bonus
from . import data_manager
from .data_manager import (
    study_status, work_status, offline_completed_studies, 
    load_study_status, load_work_status, save_study_status, save_work_status,
    get_user_wife_data, update_user_wife_data, get_user_data
)
from ..utils.experience_utils import process_experience_gain
from ..config.experience_config import get_exp_required_for_level

def check_study_requirements(user_id: str):
    """检查学习要求"""
    from ..utils.validators import check_wife_status_for_activity
    
    # 检查用户是否有老婆
    wife_data = get_user_wife_data(user_id)
    if not wife_data:
        return False, "你还没有老婆，无法让她出门学习。请先使用'抽老婆'命令获取一个老婆！"

    # 检查老婆状态是否满足学习要求
    status_ok, status_message = check_wife_status_for_activity(wife_data)
    if not status_ok:
        wife_name = wife_data[0]
        wife_display_name = wife_name.split('.')[0]
        return False, f"{wife_display_name}{status_message[3:]}！建议先使用礼物改善她的状态~"

    return True, ""

def check_study_conflict(user_id: str):
    """检查是否与打工冲突"""
    # 确保数据已经加载（防止重启后数据未加载的问题）
    if not data_manager.study_status and not data_manager.work_status:
        print(f"[学习系统] 检查冲突时发现数据未加载，重新初始化")
        # 重新加载学习和工作状态数据
        data_manager.load_study_status()
        data_manager.load_work_status()
    
    print(f"[学习系统] 检查冲突 - 用户ID: {user_id}")
    print(f"[学习系统] 当前学习状态字典: {data_manager.study_status}")
    print(f"[学习系统] 当前打工状态字典中的用户数: {len(data_manager.work_status) if data_manager.work_status else 0}")
    
    # 检查是否已经在打工中
    if user_id in data_manager.work_status and data_manager.work_status[user_id].get('is_working', False):
        print(f"[学习系统] 用户 {user_id} 正在打工中")
        end_time_str = data_manager.work_status[user_id]['end_time']
        end_time = datetime.fromisoformat(end_time_str)
        current_time = datetime.now()
        remaining = end_time - current_time
        if remaining.total_seconds() > 0:
            hours_left = int(remaining.total_seconds() // 3600)
            minutes_left = int((remaining.total_seconds() % 3600) // 60)
            return True, f"你的老婆正在打工中，还需要{hours_left}小时{minutes_left}分钟才能完成！不能同时进行学习。"
        else:
            # 打工已过期，清除状态
            print(f"[学习系统] 用户 {user_id} 的打工已过期，清除状态")
            del data_manager.work_status[user_id]
            data_manager.save_work_status()

    # 检查是否已经在学习中
    if user_id in data_manager.study_status:
        study_data = data_manager.study_status[user_id]
        is_studying = study_data.get('is_studying', False)
        print(f"[学习系统] 用户 {user_id} 在学习状态字典中，is_studying: {is_studying}")
        
        if is_studying:
            print(f"[学习系统] 用户 {user_id} 已在学习状态中")
            end_time_str = study_data['end_time']
            end_time = datetime.fromisoformat(end_time_str)
            current_time = datetime.now()
            remaining = end_time - current_time
            print(f"[学习系统] 学习结束时间: {end_time}, 当前时间: {current_time}, 剩余秒数: {remaining.total_seconds()}")
            if remaining.total_seconds() > 0:
                hours_left = int(remaining.total_seconds() // 3600)
                minutes_left = int((remaining.total_seconds() % 3600) // 60)
                print(f"[学习系统] 学习仍在进行中，剩余 {hours_left}小时{minutes_left}分钟")
                return True, f"你的老婆正在学习中，还需要{hours_left}小时{minutes_left}分钟才能完成！"
            else:
                # 学习已过期，清除状态
                print(f"[学习系统] 用户 {user_id} 的学习已过期，清除状态")
                del data_manager.study_status[user_id]
                data_manager.save_study_status()
        else:
            print(f"[学习系统] 用户 {user_id} 在字典中但is_studying为False，清除过期状态")
            del data_manager.study_status[user_id]
            data_manager.save_study_status()
    else:
        print(f"[学习系统] 用户 {user_id} 不在学习状态字典中")

    print(f"[学习系统] 无冲突，可以开始学习")
    return False, ""

def start_study(user_id: str, hours: int, nickname: str, group_id: str = None):
    """开始学习"""
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=hours)
    
    # 调试日志：打印用户信息
    print(f"[学习系统] 开始学习 - 用户ID: {user_id}, 昵称: {nickname}, 小时数: {hours}")
    print(f"[学习系统] 开始时间: {start_time.isoformat()}, 结束时间: {end_time.isoformat()}")
    
    # 保存学习状态
    data_manager.study_status[user_id] = {
        'is_studying': True,
        'start_time': start_time.isoformat(),
        'end_time': end_time.isoformat(),
        'hours': hours,
        'group_id': group_id,
        'nickname': nickname
    }
    
    # 调试日志：保存前的状态
    print(f"[学习系统] 保存前学习状态字典: {data_manager.study_status}")
    
    data_manager.save_study_status()
    
    # 调试日志：确认保存
    print(f"[学习系统] 学习状态已保存到文件")
    
    # 安排主动通知
    if data_manager.wife_plugin_instance:
        try:
            data_manager.wife_plugin_instance.schedule_task_completion(user_id, "study", end_time)
            print(f"[学习系统] 已安排主动通知，结束时间: {end_time}")
        except Exception as e:
            print(f"[学习系统] 安排主动通知失败: {e}")
    else:
        print(f"[学习系统] 警告：插件实例未找到，无法安排主动通知")
    
    return end_time

def get_study_events():
    """获取学习事件描述"""
    return [
        "背着书包出门了，要去图书馆认真学习！",
        "拿着笔记本去咖啡厅学习，看起来很专注的样子！",
        "参加了学习小组，和小伙伴们一起努力！",
        "去了培训班，老师夸她很聪明呢！",
        "在公园里边散步边看书，劳逸结合！",
        "找到了一个安静的角落专心学习！",
        "今天很有动力，决定好好充实自己！",
        "带着求知的心情出门学习去了！",
        "说要变得更聪明，然后就出门了！",
        "为了提升自己而努力学习中！"
    ]

def calculate_level_based_growth_gain(hours: int, level: int) -> dict:
    """计算基于等级的成长值获取"""
    # 基础成长值：每小时5-10成长值
    base_growth = hours * random.randint(5, 10)
    
    # 等级加成：从4级开始提供额外加成
    # 公式：max(0, (level - 3) * 每小时等级加成)
    level_bonus_per_hour = max(0, (level - 3) * random.randint(4, 10))
    level_bonus = hours * level_bonus_per_hour
    
    total_growth = base_growth + level_bonus
    
    print(f"[成长值计算] 等级{level}, {hours}小时 - 基础:{base_growth}, 等级加成:{level_bonus}, 总计:{total_growth}")
    
    return {
        'base_growth': base_growth,
        'level_bonus': level_bonus,
        'total_growth': total_growth,
        'has_level_bonus': level_bonus > 0
    }

def process_study_completion(user_id: str):
    """处理学习完成"""
    if user_id not in data_manager.study_status:
        return None
        
    study_data = data_manager.study_status[user_id]
    hours = study_data['hours']
    nickname = study_data['nickname']
    group_id = study_data.get('group_id')
    
    # 获取用户老婆数据
    wife_data = get_user_wife_data(user_id)
    if not wife_data:
        # 清除学习状态
        del study_status[user_id]
        save_study_status()
        return None
    
    # 计算学习收益
    base_knowledge_gain = sum(random.randint(20, 30) for _ in range(hours))  # 学习N小时就抽取N次20-30的随机数相加
    current_level = wife_data[5]  # 获取当前等级
    growth_result = calculate_level_based_growth_gain(hours, current_level)  # 使用新的等级加成机制
    growth_gain = growth_result['total_growth']
    
    # 应用房产学习加成到学识
    user_data = get_user_data(user_id)
    property_name = user_data.get("property", "桥洞下的破旧帐篷")
    study_bonus = get_property_study_bonus(property_name)
    
    # 计算最终学识收益（基础学识 + 房产加成）
    knowledge_gain = int(base_knowledge_gain * (1 + study_bonus / 100))
    
    hunger_loss = min(180, hours * 15)               # 每小时减少15饥饿值，最多180
    mood_loss = min(120, hours * 10)                 # 每小时减少10心情值，最多120
    
    # 获取当前属性
    current_knowledge = wife_data[13]
    current_growth = wife_data[6]
    current_hunger = wife_data[7]
    current_mood = wife_data[10]
    current_education = wife_data[12]
    
    # 更新属性
    new_knowledge = current_knowledge + knowledge_gain
    total_growth = current_growth + growth_gain
    new_hunger = max(0, min(1000, current_hunger - hunger_loss))
    new_mood = max(0, min(1000, current_mood - mood_loss))
    
    # 检查学历升级
    education_upgrade = check_education_upgrade(new_knowledge, current_education)
    new_education = education_upgrade["name"] if education_upgrade else current_education
    
    # 使用新的经验系统处理升级
    current_level = wife_data[5]
    current_growth = wife_data[6]
    
    exp_result = process_experience_gain(current_level, current_growth, growth_gain)
    new_level = exp_result["new_level"]
    new_growth = exp_result["new_growth"]
    level_up = exp_result["level_ups"] > 0
    
    # 更新老婆数据
    update_user_wife_data(user_id, 
                        knowledge=new_knowledge,
                        growth=new_growth,
                        hunger=new_hunger,
                        mood=new_mood,
                        education_level=new_education,
                        level=new_level)
    
    # 清除学习状态
    del data_manager.study_status[user_id]
    data_manager.save_study_status()
    
    # 构建完成消息
    wife_name = wife_data[0]
    wife_display_name = wife_name.split('.')[0]
    
    completion_messages = [
        f"{wife_display_name}学习回来了，满载而归！",
        f"{wife_display_name}完成了今天的学习计划，看起来很有成就感！",
        f"{wife_display_name}从学习中回来，眼中闪烁着智慧的光芒！",
        f"{wife_display_name}学习结束了，带着满满的知识回到你身边！",
        f"{wife_display_name}完成学习任务，变得更加聪明了！"
    ]
    
    result_message = f": {random.choice(completion_messages)}\n"
    result_message += f"📚 学习收获：\n"
    
    # 显示学识收益（包含房产加成信息）
    if study_bonus > 0:
        result_message += f"💡 学识 +{base_knowledge_gain} (+{knowledge_gain - base_knowledge_gain}房产加成) = {knowledge_gain} ({current_knowledge} → {new_knowledge})\n"
        result_message += f"🏠 房产学习加成：+{study_bonus}%\n"
    else:
        result_message += f"💡 学识 +{knowledge_gain} ({current_knowledge} → {new_knowledge})\n"
    
    # 显示完整的成长值进度信息
    next_level_exp = get_exp_required_for_level(new_level + 1)
    exp_percentage = round((new_growth / next_level_exp * 100), 1) if next_level_exp > 0 else 100
    if growth_result['has_level_bonus']:
        result_message += f"📈 成长值 +{growth_result['base_growth']} (+{growth_result['level_bonus']}等级加成) = {growth_gain} → {new_growth}/{next_level_exp} ({exp_percentage}%)\n"
        result_message += f"⭐ 等级{current_level}学习加成：+{growth_result['level_bonus']}成长值\n"
    else:
        result_message += f"📈 成长值 +{growth_gain} → {new_growth}/{next_level_exp} ({exp_percentage}%)\n"
    
    result_message += f"💭 学习消耗：\n"
    result_message += f"🍽️ 饥饿值 -{hunger_loss} ({current_hunger} → {new_hunger})\n"
    result_message += f"😊 心情 -{mood_loss} ({current_mood} → {new_mood})\n"
    
    if education_upgrade:
        result_message += f"🎓 恭喜！学历升级：{current_education} → {new_education}！\n"
    
    if exp_result["level_up_messages"]:
        result_message += "⭐ " + "\n⭐ ".join(exp_result["level_up_messages"]) + "\n"
    
    # 状态提醒
    warnings = []
    if new_hunger < 30:
        warnings.append("🍽️ 她看起来有点饿了，记得给她准备点食物")
    if new_mood < 30:
        warnings.append("😊 她的心情不太好，需要你的安慰")
    
    if warnings:
        result_message += f"⚠️ 贴心提醒：" + "、".join(warnings) + "哦~"
    
    return {
        'message': result_message,
        'group_id': group_id,
        'unified_msg_origin': study_data.get('unified_msg_origin', f"aiocqhttp:GroupMessage:{group_id}"),
        'user_id': user_id,
        'nickname': nickname
    }

def process_early_stop_study(user_id: str):
    """处理提前停止学习"""
    if user_id not in data_manager.study_status:
        return None
        
    study_data = data_manager.study_status[user_id]
    
    # 检查是否正在学习
    if not study_data.get('is_studying', False):
        return None
    
    nickname = study_data['nickname']
    group_id = study_data.get('group_id')
    original_hours = study_data['hours']
    
    # 计算实际学习时间（向下取整）
    start_time = datetime.fromisoformat(study_data['start_time'])
    current_time = datetime.now()
    actual_duration = current_time - start_time
    actual_hours = int(actual_duration.total_seconds() // 3600)  # 向下取整到小时
    
    print(f"[提前停止学习] 用户{user_id} 原计划{original_hours}小时，实际学习{actual_hours}小时")
    
    # 如果不到1小时，没有收益
    if actual_hours < 1:
        # 清除学习状态
        del data_manager.study_status[user_id]
        data_manager.save_study_status()
        
        # 取消调度器中的任务
        if data_manager.wife_plugin_instance:
            try:
                job_id = f"study_{user_id}"
                data_manager.wife_plugin_instance.scheduler.remove_job(job_id)
                print(f"[提前停止学习] 已取消调度任务: {job_id}")
            except Exception as e:
                print(f"[提前停止学习] 取消调度任务失败: {e}")
        
        return {
            'message': f': {nickname}，学习时间不足1小时，没有任何收益哦~',
            'group_id': group_id,
            'user_id': user_id,
            'nickname': nickname
        }
    
    # 获取用户老婆数据
    wife_data = get_user_wife_data(user_id)
    if not wife_data:
        # 清除学习状态
        del data_manager.study_status[user_id]
        data_manager.save_study_status()
        return None
    
    # 按实际小时数计算学习收益
    base_knowledge_gain = sum(random.randint(20, 30) for _ in range(actual_hours))  # 实际小时数的学识
    current_level = wife_data[5]  # 获取当前等级
    growth_result = calculate_level_based_growth_gain(actual_hours, current_level)  # 使用新的等级加成机制
    growth_gain = growth_result['total_growth']
    
    # 应用房产学习加成到学识
    user_data = get_user_data(user_id)
    property_name = user_data.get("property", "桥洞下的破旧帐篷")
    study_bonus = get_property_study_bonus(property_name)
    
    # 计算最终学识收益（基础学识 + 房产加成）
    knowledge_gain = int(base_knowledge_gain * (1 + study_bonus / 100))
    
    hunger_loss = min(180, actual_hours * 15)               # 按实际小时计算饥饿值消耗，最多180
    mood_loss = min(120, actual_hours * 10)                 # 按实际小时计算心情消耗，最多120
    
    # 获取当前属性
    current_knowledge = wife_data[13]
    current_growth = wife_data[6]
    current_hunger = wife_data[7]
    current_mood = wife_data[10]
    current_education = wife_data[12]
    
    # 更新属性
    new_knowledge = current_knowledge + knowledge_gain
    total_growth = current_growth + growth_gain
    new_hunger = max(0, min(1000, current_hunger - hunger_loss))
    new_mood = max(0, min(1000, current_mood - mood_loss))
    
    # 检查学历升级
    education_upgrade = check_education_upgrade(new_knowledge, current_education)
    new_education = education_upgrade["name"] if education_upgrade else current_education
    
    # 使用新的经验系统处理升级
    current_level = wife_data[5]
    current_growth = wife_data[6]
    
    exp_result = process_experience_gain(current_level, current_growth, growth_gain)
    new_level = exp_result["new_level"]
    new_growth = exp_result["new_growth"]
    level_up = exp_result["level_ups"] > 0
    
    # 更新老婆数据
    update_user_wife_data(user_id, 
                        knowledge=new_knowledge,
                        growth=new_growth,
                        hunger=new_hunger,
                        mood=new_mood,
                        education_level=new_education,
                        level=new_level)
    
    # 清除学习状态
    del data_manager.study_status[user_id]
    data_manager.save_study_status()
    
    # 取消调度器中的任务
    if data_manager.wife_plugin_instance:
        try:
            job_id = f"study_{user_id}"
            data_manager.wife_plugin_instance.scheduler.remove_job(job_id)
            print(f"[提前停止学习] 已取消调度任务: {job_id}")
        except Exception as e:
            print(f"[提前停止学习] 取消调度任务失败: {e}")
    
    # 构建完成消息
    wife_name = wife_data[0]
    wife_display_name = wife_name.split('.')[0]
    
    result_message = f": {nickname}，你让{wife_display_name}提前结束了学习！\n"
    result_message += f"📚 提前结束学习收获（{actual_hours}小时）：\n"
    
    # 显示学识收益（包含房产加成信息）
    if study_bonus > 0:
        result_message += f"💡 学识 +{base_knowledge_gain} (+{knowledge_gain - base_knowledge_gain}房产加成) = {knowledge_gain} ({current_knowledge} → {new_knowledge})\n"
        result_message += f"🏠 房产学习加成：+{study_bonus}%\n"
    else:
        result_message += f"💡 学识 +{knowledge_gain} ({current_knowledge} → {new_knowledge})\n"
    
    # 显示完整的成长值进度信息
    next_level_exp = get_exp_required_for_level(new_level + 1)
    exp_percentage = round((new_growth / next_level_exp * 100), 1) if next_level_exp > 0 else 100
    if growth_result['has_level_bonus']:
        result_message += f"📈 成长值 +{growth_result['base_growth']} (+{growth_result['level_bonus']}等级加成) = {growth_gain} → {new_growth}/{next_level_exp} ({exp_percentage}%)\n"
        result_message += f"⭐ 等级{current_level}学习加成：+{growth_result['level_bonus']}成长值\n"
    else:
        result_message += f"📈 成长值 +{growth_gain} → {new_growth}/{next_level_exp} ({exp_percentage}%)\n"
    
    result_message += f"💭 学习消耗：\n"
    result_message += f"🍽️ 饥饿值 -{hunger_loss} ({current_hunger} → {new_hunger})\n"
    result_message += f"😊 心情 -{mood_loss} ({current_mood} → {new_mood})\n"
    
    if education_upgrade:
        result_message += f"🎓 恭喜！学历升级：{current_education} → {new_education}！\n"
    
    if exp_result["level_up_messages"]:
        result_message += "⭐ " + "\n⭐ ".join(exp_result["level_up_messages"]) + "\n"
    
    result_message += f"⏰ 原计划学习{original_hours}小时，实际学习{actual_hours}小时\n"
    
    # 状态提醒
    warnings = []
    if new_hunger < 30:
        warnings.append("🍽️ 她看起来有点饿了，记得给她准备点食物")
    if new_mood < 30:
        warnings.append("😊 她的心情不太好，需要你的安慰")
    
    if warnings:
        result_message += f"⚠️ 贴心提醒：" + "、".join(warnings) + "哦~"
    
    return {
        'message': result_message,
        'group_id': group_id,
        'user_id': user_id,
        'nickname': nickname
    }

def check_and_process_completed_studies():
    """检查并处理完成的学习"""
    current_time = datetime.now()
    completed_users = []
    
    for user_id, study_data in data_manager.study_status.items():
        if study_data.get('is_studying', False):
            end_time = datetime.fromisoformat(study_data['end_time'])
            if current_time >= end_time:
                completed_users.append(user_id)
    
    # 处理学习完成的用户
    for user_id in completed_users:
        result = process_study_completion(user_id)
        if result:
            data_manager.offline_completed_studies[user_id] = result