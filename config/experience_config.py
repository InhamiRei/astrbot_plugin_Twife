"""经验值系统配置文件"""

def get_exp_required_for_level(level: int) -> int:
    """
    计算指定等级所需的经验值
    
    Args:
        level: 目标等级
        
    Returns:
        该等级需要的经验值
    """
    if level <= 1:
        return 0
    
    # 递增公式：基础经验 + (等级-1) * 增长系数
    # 1级: 0, 2级: 200, 3级: 350, 4级: 550, 5级: 800...
    base_exp = 200  # 基础经验需求
    growth_factor = 50  # 每级增长系数
    level_bonus = (level - 2) * 25  # 额外等级奖励，让高等级增长更快
    
    required_exp = base_exp + (level - 2) * growth_factor + ((level - 2) * (level - 1) // 2) * level_bonus
    
    return required_exp

def get_total_exp_for_level(level: int) -> int:
    """
    计算到达指定等级需要的总经验值
    
    Args:
        level: 目标等级
        
    Returns:
        到达该等级需要的总经验值
    """
    if level <= 1:
        return 0
    
    total_exp = 0
    for i in range(2, level + 1):
        total_exp += get_exp_required_for_level(i)
    
    return total_exp

def calculate_level_from_total_exp(total_exp: int) -> tuple[int, int]:
    """
    根据总经验值计算当前等级和剩余经验
    
    Args:
        total_exp: 总经验值
        
    Returns:
        (当前等级, 当前等级剩余经验)
    """
    if total_exp <= 0:
        return 1, 0
    
    current_level = 1
    remaining_exp = total_exp
    
    # 逐级计算
    while True:
        next_level_exp = get_exp_required_for_level(current_level + 1)
        if remaining_exp >= next_level_exp:
            remaining_exp -= next_level_exp
            current_level += 1
        else:
            break
    
    return current_level, remaining_exp

def get_exp_progress_info(current_growth: int, current_level: int) -> dict:
    """
    获取经验进度信息
    
    Args:
        current_growth: 当前成长值（剩余经验）
        current_level: 当前等级
        
    Returns:
        包含等级、经验进度等信息的字典
    """
    next_level_exp = get_exp_required_for_level(current_level + 1)
    
    return {
        "current_level": current_level,
        "current_exp": current_growth,
        "next_level_exp": next_level_exp,
        "exp_progress": f"{current_growth}/{next_level_exp}",
        "exp_percentage": round((current_growth / next_level_exp * 100), 1) if next_level_exp > 0 else 100
    }

# 经验需求表（前20级）
EXP_REQUIREMENTS = {
    1: 0,      # 1级不需要经验
    2: 200,    # 2级需要200经验
    3: 350,    # 3级需要350经验  
    4: 550,    # 4级需要550经验
    5: 800,    # 5级需要800经验
    6: 1100,   # 6级需要1100经验
    7: 1450,   # 7级需要1450经验
    8: 1850,   # 8级需要1850经验
    9: 2300,   # 9级需要2300经验
    10: 2800,  # 10级需要2800经验
    # 后续等级按公式计算
}

def print_exp_table(max_level: int = 20):
    """打印经验需求表，用于调试"""
    print("等级经验需求表:")
    print("等级\t单级经验\t总经验")
    total = 0
    for level in range(1, max_level + 1):
        level_exp = get_exp_required_for_level(level)
        if level > 1:
            total += level_exp
        print(f"{level}\t{level_exp}\t{total}")

if __name__ == "__main__":
    # 测试经验系统
    print_exp_table(15)
    
    # 测试150经验能升几级
    print("\n测试150经验升级:")
    level, remaining = calculate_level_from_total_exp(150)
    print(f"150经验 -> 等级: {level}, 剩余经验: {remaining}")
    
    # 测试350经验能升几级  
    print("\n测试350经验升级:")
    level, remaining = calculate_level_from_total_exp(350)
    print(f"350经验 -> 等级: {level}, 剩余经验: {remaining}")
