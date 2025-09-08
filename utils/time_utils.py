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
