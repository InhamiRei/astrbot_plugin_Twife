"""验证工具模块"""

def check_wife_status_for_activity(wife_data):
    """检查老婆状态是否满足学习或打工的要求"""
    if not wife_data:
        return False, "你还没有老婆，无法进行此活动"
    
    hunger = wife_data[7]      # 饥饿值
    cleanliness = wife_data[8] # 清洁度
    health = wife_data[9]      # 健康值
    mood = wife_data[10]       # 心情
    
    # 检查各项状态是否低于20
    low_status = []
    if hunger < 20:
        low_status.append("饥饿度过低")
    if cleanliness < 20:
        low_status.append("清洁度过低")
    if health < 20:
        low_status.append("健康状况不佳")
    if mood < 20:
        low_status.append("心情太差")
    
    if low_status:
        return False, f"老婆的状态不佳：{', '.join(low_status)}，请先照顾好她再让她出门"
    
    return True, ""
