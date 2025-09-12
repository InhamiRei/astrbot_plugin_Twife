"""格式化工具模块"""
from ..config.experience_config import get_exp_required_for_level

def format_number(number: int | float) -> str:
    """格式化数字显示，添加千位分隔符"""
    if isinstance(number, float):
        # 如果是浮点数，保留2位小数并添加千位分隔符
        return f"{number:,.2f}"
    else:
        # 如果是整数，只添加千位分隔符
        return f"{number:,}"

def format_backpack(backpack: dict) -> str:
    """格式化背包显示"""
    if not backpack:
        return "空"
    items = []
    for item, count in backpack.items():
        items.append(f"{item}x{count}")
    return "、".join(items)

def format_artifacts(artifacts: dict) -> str:
    """格式化历史文物显示"""
    if not artifacts:
        return "暂无"
    items = []
    for artifact, count in artifacts.items():
        if count > 1:
            items.append(f"{artifact}x{count}")
        else:
            items.append(artifact)
    return "、".join(items)

def get_status_emoji(value: int) -> str:
    """根据状态值获取emoji"""
    if value >= 80:
        return "💚"  # 绿色，状态很好
    elif value >= 60:
        return "💛"  # 黄色，状态一般
    elif value >= 40:
        return "🧡"  # 橙色，状态较差
    else:
        return "❤️"  # 红色，状态很差

def create_progress_bar(value: int, max_value: int = 100, length: int = 10) -> str:
    """创建带颜色的进度条"""
    # 确保值在有效范围内
    value = max(0, min(value, max_value))
    
    # 计算进度比例
    progress = value / max_value
    filled_length = int(length * progress)
    
    # 根据数值选择颜色和字符
    if value >= 80:
        color_emoji = "💚"
        filled_char = "█"
    elif value >= 60:
        color_emoji = "💛"
        filled_char = "█"
    elif value >= 40:
        color_emoji = "🧡"
        filled_char = "█"
    else:
        color_emoji = "❤️"
        filled_char = "█"
    
    empty_char = "░"
    
    # 构建进度条
    bar = filled_char * filled_length + empty_char * (length - filled_length)
    
    return f"{color_emoji}[{bar}] {value}"

def format_wife_status(level: int, growth: int, hunger: int, cleanliness: int, health: int, mood: int, status: str) -> str:
    """格式化老婆状态显示"""
    status_text = f"🆙 等级：Lv.{level}\n"
    
    # 使用新的经验系统显示成长值
    next_level_exp = get_exp_required_for_level(level + 1)
    exp_percentage = round((growth / next_level_exp * 100), 1) if next_level_exp > 0 else 100
    status_text += f"📈 成长值：{growth}/{next_level_exp} ({exp_percentage}%)\n"
    
    status_text += f"🍽️ 饥饿：{hunger}/1000\n"
    status_text += f"🧼 清洁：{cleanliness}/1000\n"
    status_text += f"❤️ 健康：{health}/1000\n"
    status_text += f"😊 心情：{mood}/1000\n"
    status_text += f"🏷️ 状态：{status}"
    
    return status_text
