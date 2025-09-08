"""经验值计算工具函数"""

from ..config.experience_config import get_exp_required_for_level, calculate_level_from_total_exp, get_exp_progress_info

def process_experience_gain(current_level: int, current_growth: int, exp_gained: int) -> dict:
    """
    处理经验获得，计算升级结果
    
    Args:
        current_level: 当前等级
        current_growth: 当前成长值（剩余经验）
        exp_gained: 获得的经验值
        
    Returns:
        包含升级信息的字典
    """
    # 计算总经验
    total_current_exp = current_growth
    for level in range(2, current_level + 1):
        total_current_exp += get_exp_required_for_level(level)
    
    # 加上新获得的经验
    new_total_exp = total_current_exp + exp_gained
    
    # 计算新的等级和剩余经验
    new_level, new_growth = calculate_level_from_total_exp(new_total_exp)
    
    # 计算升了多少级
    level_ups = new_level - current_level
    
    # 生成升级消息
    level_up_messages = []
    if level_ups > 0:
        for i in range(level_ups):
            upgrade_level = current_level + i + 1
            level_up_messages.append(f"🎉 升级了！当前等级：{upgrade_level}")
    
    return {
        "new_level": new_level,
        "new_growth": new_growth,
        "level_ups": level_ups,
        "level_up_messages": level_up_messages,
        "exp_gained": exp_gained
    }

def get_level_display_info(level: int, growth: int) -> str:
    """
    获取等级显示信息
    
    Args:
        level: 当前等级
        growth: 当前成长值
        
    Returns:
        格式化的等级显示字符串
    """
    next_level_exp = get_exp_required_for_level(level + 1)
    percentage = round((growth / next_level_exp * 100), 1) if next_level_exp > 0 else 100
    
    return f"Lv.{level} ({growth}/{next_level_exp} - {percentage}%)"

def calculate_remaining_exp_for_next_level(level: int, growth: int) -> int:
    """
    计算距离下一级还需要多少经验
    
    Args:
        level: 当前等级
        growth: 当前成长值
        
    Returns:
        还需要的经验值
    """
    next_level_exp = get_exp_required_for_level(level + 1)
    return max(0, next_level_exp - growth)


# 兼容旧系统的函数
def legacy_level_up_check(current_level: int, current_growth: int, exp_gained: int) -> tuple[int, int, str]:
    """
    兼容旧系统的升级检查函数
    
    Args:
        current_level: 当前等级
        current_growth: 当前成长值
        exp_gained: 获得的经验值
        
    Returns:
        (新等级, 新成长值, 升级消息)
    """
    result = process_experience_gain(current_level, current_growth, exp_gained)
    
    level_up_msg = ""
    if result["level_up_messages"]:
        level_up_msg = "\n" + "\n".join(result["level_up_messages"])
    
    return result["new_level"], result["new_growth"], level_up_msg
