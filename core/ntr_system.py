"""NTR系统核心模块"""
import random
from datetime import datetime, timedelta
from ..config.settings import NTR_SUCCESS_RATE
from ..config.messages import NTR_FAIL_EVENTS
from .data_manager import *

def check_ntr_success(user_id: str, group_id: str):
    """检查NTR成功率"""
    current_ntr_possibility = NTR_SUCCESS_RATE  # 默认概率

    if str(group_id) in ntr_feast_active:
        end_time = ntr_feast_active[str(group_id)]
        now = datetime.now()
        if now < end_time:
            # 盛宴激活中，提高成功率
            if user_id == "2675588467":  # 牛头人之王
                current_ntr_possibility = 0.80  # 提高到80%
            else:
                current_ntr_possibility = 0.50  # 提高到50%
        else:
            # 盛宴已过期，清除记录
            del ntr_feast_active[str(group_id)]

    return random.random() < current_ntr_possibility

def get_random_ntr_fail_event():
    """获取随机NTR失败事件"""
    return random.choice(NTR_FAIL_EVENTS)

def record_newly_acquired_wife(user_id: str):
    """记录刚牛来老婆的时间"""
    newly_acquired_wives[user_id] = datetime.now()

def check_purelove_cooldown(user_id: str, cooldown_minutes: int = 5):
    """检查纯爱无敌冷却时间"""
    if user_id in newly_acquired_wives:
        acquired_time = newly_acquired_wives[user_id]
        now = datetime.now()
        cooldown_period = timedelta(minutes=cooldown_minutes)
        if now < acquired_time + cooldown_period:
            remaining = acquired_time + cooldown_period - now
            minutes = remaining.seconds // 60
            seconds = remaining.seconds % 60
            return False, minutes, seconds
    return True, 0, 0

def clear_purelove_cooldown(user_id: str):
    """清除纯爱无敌冷却时间"""
    if user_id in newly_acquired_wives:
        del newly_acquired_wives[user_id]

def activate_ntr_feast(group_id: str, duration_minutes: int = 5):
    """激活牛头人盛宴"""
    end_time = datetime.now() + timedelta(minutes=duration_minutes)
    ntr_feast_active[str(group_id)] = end_time

def check_ntr_feast_active(group_id: str):
    """检查牛头人盛宴是否激活"""
    group_id_str = str(group_id)
    if group_id_str in ntr_feast_active:
        end_time = ntr_feast_active[group_id_str]
        now = datetime.now()
        if now < end_time:
            # 计算剩余时间（分钟和秒）
            remaining = end_time - now
            minutes = remaining.seconds // 60
            seconds = remaining.seconds % 60
            return True, minutes, seconds
        else:
            # 盛宴已结束，清除记录
            del ntr_feast_active[group_id_str]
    return False, 0, 0

def give_ntr_bonus(user_id: str, is_king: bool = False):
    """给予NTR奖励次数"""
    from ..config.settings import NTR_MAX_DAILY
    
    current_ntr_count = get_daily_limit_data(user_id, 'ntr')
    
    # 特殊QQ号是牛头人之王，获得10次机会，其他人获得3次
    if is_king:
        new_count = max(0, current_ntr_count - 10)
        bonus_times = 10
        title = "牛头人之王"
    else:
        new_count = max(0, current_ntr_count - 3)
        bonus_times = 3
        title = "牛头人"

    # 更新每日限制数据
    update_daily_limit_data(user_id, 'ntr', new_count)
    remaining_times = NTR_MAX_DAILY - new_count
    
    return bonus_times, title, remaining_times
