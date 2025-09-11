"""房产等级配置"""

# 房产升级系统
PROPERTY_LEVELS = [
    {"name": "桥洞下的破旧帐篷", "cost": 0, "description": "😰 风餐露宿的起点，偶尔有野猫来串门", 
     "space": 50, "sell_bonus": 0, "study_bonus": 0, "value": 0},
    {"name": "城中村握手楼单间", "cost": 20000, "description": "🏚️ 墙皮斑驳的老房子，楼上偶尔滴水，但至少有张床", 
     "space": 200, "sell_bonus": 1, "study_bonus": 10, "value": 20000},
    {"name": "老式筒子楼两居", "cost": 100000, "description": "🏘️ 上世纪的建筑，楼道声音很吵，但有独立厨房了", 
     "space": 400, "sell_bonus": 2, "study_bonus": 20, "value": 100000},
    {"name": "普通小区三居室", "cost": 300000, "description": "🏢 90年代小区，电梯偶尔罢工，但邻里和睦", 
     "space": 600, "sell_bonus": 3, "study_bonus": 30, "value": 300000},
    {"name": "精装小高层三居", "cost": 600000, "description": "🏢 电梯房，装修现代，采光不错，周边有商场", 
     "space": 700, "sell_bonus": 4, "study_bonus": 40, "value": 600000},
    {"name": "市区精装修大三居", "cost": 1000000, "description": "🏡 装修不错的房子，偶尔能听到楼上小孩跑步声", 
     "space": 800, "sell_bonus": 5, "study_bonus": 50, "value": 1000000},
    {"name": "高档小区复式楼", "cost": 1500000, "description": "🏨 带阁楼的复式，楼下是客厅楼上是卧室，很有层次感", 
     "space": 1000, "sell_bonus": 8, "study_bonus": 60, "value": 1500000},
    {"name": "市中心大平层", "cost": 5000000, "description": "🏙️ 180平的大平层，落地窗视野不错，偶尔能看到对面楼的生活", 
     "space": 1200, "sell_bonus": 10, "study_bonus": 70, "value": 5000000},
    {"name": "高端住宅顶层复式", "cost": 5200000, "description": "🌆 顶层复式带露台，可以种花养草，还能看城市夜景", 
     "space": 1500, "sell_bonus": 12, "study_bonus": 80, "value": 5200000},
    {"name": "市区独栋别墅", "cost": 6000000, "description": "🏖️ 带小花园的独栋别墅，有车库和地下室，邻居都很有钱", 
     "space": 2000, "sell_bonus": 15, "study_bonus": 90, "value": 6000000},
    {"name": "郊区豪华别墅", "cost": 8000000, "description": "🌳 环境优美的大别墅，有泳池和大花园，偶尔有小鹿来访", 
     "space": 2500, "sell_bonus": 18, "study_bonus": 100, "value": 8000000},
    {"name": "湖景奢华庄园", "cost": 15000000, "description": "🏞️ 临湖而建的私人庄园，有专业园丁和管家，生活如诗如画", 
     "space": 3000, "sell_bonus": 20, "study_bonus": 110, "value": 15000000},
    {"name": "市中心豪华顶层公寓", "cost": 18000000, "description": "🌆 顶层公寓，带全景阳台和私人电梯，真正的都市奢华", 
     "space": 3500, "sell_bonus": 25, "study_bonus": 120, "value": 18000000},
    {"name": "山顶私人庄园", "cost": 20000000, "description": "⛰️ 半山腰的超级豪宅，俯瞰整个城市，有私人健身房和酒窖", 
     "space": 4000, "sell_bonus": 30, "study_bonus": 130, "value": 20000000},
    {"name": "城市地标全景豪宅", "cost": 35000000, "description": "🌐 世界级地标建筑的环形顶层，360°城市景观尽收眼底", 
     "space": 4500, "sell_bonus": 40, "study_bonus": 140, "value": 35000000},
    {"name": "海景私人岛屿别墅", "cost": 50000000, "description": "🏝️ 私人小岛上的豪华别墅，有私人海滩和游艇码头", 
     "space": 5000, "sell_bonus": 50, "study_bonus": 150, "value": 50000000},
    {"name": "市中心摩天大楼顶层", "cost": 100000000, "description": "🏙️ 摩天大楼的整个顶层，360度城市全景，真正的空中豪宅", 
     "space": 8000, "sell_bonus": 70, "study_bonus": 200, "value": 100000000},
    {"name": "皇家庄园级豪宅", "cost": 200000000, "description": "👑 占地数百亩的城市边缘庄园，带私人高尔夫球场与马场", 
     "space": 10000, "sell_bonus": 80, "study_bonus": 300, "value": 200000000},
    {"name": "暴雪帝国皇家宫殿", "cost": 8888888888, "description": "🚩 星战军团的权力核心，恢宏的皇家宫殿俯瞰全城，镶满能量水晶，象征着无上的统治",
     "space": 50000, "sell_bonus": 200, "study_bonus": 500, "value": 1000000000}
]

def get_property_level(property_name: str) -> int:
    """根据房产名称获取等级"""
    for i, property_info in enumerate(PROPERTY_LEVELS):
        if property_info["name"] == property_name:
            return i
    return 0  # 默认返回最低等级

def get_next_property_info(current_property: str):
    """获取下一级房产信息"""
    current_level = get_property_level(current_property)
    if current_level < len(PROPERTY_LEVELS) - 1:
        return PROPERTY_LEVELS[current_level + 1]
    return None

def get_property_info(property_name: str):
    """根据房产名称获取完整房产信息"""
    for property_info in PROPERTY_LEVELS:
        if property_info["name"] == property_name:
            return property_info
    return None

def get_property_space(property_name: str) -> int:
    """根据房产名称获取空间"""
    property_info = get_property_info(property_name)
    return property_info["space"] if property_info else 0

def get_property_sell_bonus(property_name: str) -> int:
    """根据房产名称获取售出加成百分比"""
    property_info = get_property_info(property_name)
    return property_info["sell_bonus"] if property_info else 0

def get_property_study_bonus(property_name: str) -> int:
    """根据房产名称获取学习经验加成百分比"""
    property_info = get_property_info(property_name)
    return property_info["study_bonus"] if property_info else 0

def get_property_value(property_name: str) -> int:
    """根据房产名称获取房产价值"""
    property_info = get_property_info(property_name)
    return property_info["value"] if property_info else 0

def format_property_list(current_level: int = 0) -> str:
    """格式化房产列表显示，只显示当前等级和下五级，后面显示未知"""
    property_text = "🏠【房产等级列表】🏠\n"
    
    # 显示当前等级
    if current_level < len(PROPERTY_LEVELS):
        property_info = PROPERTY_LEVELS[current_level]
        level_text = f"Lv.{current_level}"
        cost_text = f"💰{property_info['cost']}" if property_info['cost'] > 0 else "💰免费"
        space_text = f"📦{property_info['space']}空间"
        sell_bonus_text = f"📈+{property_info['sell_bonus']}%售出" if property_info['sell_bonus'] > 0 else ""
        study_bonus_text = f"📚+{property_info['study_bonus']}%学习" if property_info['study_bonus'] > 0 else ""
        
        # 构建加成信息
        bonus_info = []
        if sell_bonus_text:
            bonus_info.append(sell_bonus_text)
        if study_bonus_text:
            bonus_info.append(study_bonus_text)
        
        bonus_display = ", ".join(bonus_info) if bonus_info else ""
        extra_info = f" ({space_text}" + (f", {bonus_display}" if bonus_display else "") + ")"
        property_text += f"{level_text} {property_info['name']} - {cost_text}{extra_info} 👈当前\n"
    
    # 显示下五级房产
    for i in range(current_level + 1, min(current_level + 6, len(PROPERTY_LEVELS))):
        property_info = PROPERTY_LEVELS[i]
        level_text = f"Lv.{i}"
        cost_text = f"💰{property_info['cost']}" if property_info['cost'] > 0 else "💰免费"
        space_text = f"📦{property_info['space']}空间"
        sell_bonus_text = f"📈+{property_info['sell_bonus']}%售出" if property_info['sell_bonus'] > 0 else ""
        study_bonus_text = f"📚+{property_info['study_bonus']}%学习" if property_info['study_bonus'] > 0 else ""
        
        # 构建加成信息
        bonus_info = []
        if sell_bonus_text:
            bonus_info.append(sell_bonus_text)
        if study_bonus_text:
            bonus_info.append(study_bonus_text)
        
        bonus_display = ", ".join(bonus_info) if bonus_info else ""
        extra_info = f" ({space_text}" + (f", {bonus_display}" if bonus_display else "") + ")"
        property_text += f"{level_text} {property_info['name']} - {cost_text}{extra_info}\n"
    
    # 如果还有更高级的房产，显示未知
    if current_level + 6 < len(PROPERTY_LEVELS):
        remaining_count = len(PROPERTY_LEVELS) - (current_level + 6)
        property_text += f"...\n❓ 还有{remaining_count}级更高等级房产，继续升级解锁更多信息"

    return property_text

