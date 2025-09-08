"""时间工具模块"""
from datetime import datetime, timedelta

def get_user_activity_status(user_id: str, study_status: dict, work_status: dict, work_list: list) -> tuple:
    """获取用户当前活动状态和剩余时间
    返回: (activity_type, activity_desc, remaining_time_str)
    """
    
    # 检查是否在学习
    if user_id in study_status and study_status[user_id].get('is_studying', False):
        study_data = study_status[user_id]
        end_time_str = study_data['end_time']
        end_time = datetime.fromisoformat(end_time_str)
        now = datetime.now()
        
        if now < end_time:
            remaining = end_time - now
            hours = int(remaining.total_seconds() // 3600)
            minutes = int((remaining.total_seconds() % 3600) // 60)
            remaining_str = f"{hours}小时{minutes}分钟" if hours > 0 else f"{minutes}分钟"
            return ("studying", "正在努力学习中", remaining_str)
    
    # 检查是否在打工
    if user_id in work_status and work_status[user_id].get('is_working', False):
        work_data = work_status[user_id]
        end_time_str = work_data['end_time']
        end_time = datetime.fromisoformat(end_time_str)
        now = datetime.now()
        
        if now < end_time:
            remaining = end_time - now
            hours = int(remaining.total_seconds() // 3600)
            minutes = int((remaining.total_seconds() % 3600) // 60)
            remaining_str = f"{hours}小时{minutes}分钟" if hours > 0 else f"{minutes}分钟"
            
            # 获取工作名称
            work_id = work_data.get('work_id', 0)
            work_name = "打工"
            for work in work_list:
                if work["id"] == work_id:
                    work_name = work["name"]
                    break
            
            return ("working", f"正在{work_name}中", remaining_str)
    
    # 默认状态
    return ("idle", "正在发呆", "")

def get_dungeon_cooldown_status(user_id: str) -> str:
    """获取地下城冷却状态
    返回: 冷却状态描述字符串
    """
    from ..core.data_manager import get_user_dungeon_data
    from ..config.dungeon_config import DUNGEON_COOLDOWN_HOURS
    
    try:
        user_dungeon_data = get_user_dungeon_data(user_id)
        
        if not user_dungeon_data['last_dungeon_time']:
            return "⚔️ 地下城：随时可进入"
        
        last_time = datetime.fromisoformat(user_dungeon_data['last_dungeon_time'])
        cooldown_end = last_time + timedelta(hours=DUNGEON_COOLDOWN_HOURS)
        current_time = datetime.now()
        
        if current_time >= cooldown_end:
            return "⚔️ 地下城：随时可进入"
        else:
            remaining = cooldown_end - current_time
            hours = int(remaining.total_seconds() // 3600)
            minutes = int((remaining.total_seconds() % 3600) // 60)
            
            if hours > 0:
                return f"⚔️ 地下城：冷却中（还需{hours}小时{minutes}分钟）"
            else:
                return f"⚔️ 地下城：冷却中（还需{minutes}分钟）"
    except Exception as e:
        print(f"获取地下城冷却状态时出错: {e}")
        return "⚔️ 地下城：状态未知"
