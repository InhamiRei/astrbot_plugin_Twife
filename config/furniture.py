"""家具配置"""

# 家具列表
FURNITURE_LIST = [
    {
        "name": "崭新的木椅",
        "category": "座椅",
        "buy_price": 500,
        "sell_price": 250,
        "space": 5,
        "value": 500,
        "description": "🪑 简单朴素的木制椅子，坐起来还算舒适",
        "rarity": "普通"
    },
    {
        "name": "高贵的羊皮沙发",
        "category": "座椅",
        "buy_price": 15000,
        "sell_price": 7500,
        "space": 20,
        "value": 15000,
        "description": "🛋️ 奢华的真皮沙发，坐上去就不想起来",
        "rarity": "稀有"
    },
    {
        "name": "简约茶几",
        "category": "桌子",
        "buy_price": 800,
        "sell_price": 400,
        "space": 8,
        "value": 800,
        "description": "☕ 简洁的白色茶几，放几本书很有格调",
        "rarity": "普通"
    },
    {
        "name": "豪华实木餐桌",
        "category": "桌子",
        "buy_price": 8000,
        "sell_price": 4000,
        "space": 25,
        "value": 8000,
        "description": "🍽️ 厚重的实木餐桌，一家人围桌吃饭的温馨感",
        "rarity": "稀有"
    },
    {
        "name": "温馨单人床",
        "category": "床类",
        "buy_price": 2000,
        "sell_price": 1000,
        "space": 15,
        "value": 2000,
        "description": "🛏️ 舒适的单人床，睡眠质量有保障",
        "rarity": "普通"
    },
    {
        "name": "奢华双人大床",
        "category": "床类",
        "buy_price": 25000,
        "sell_price": 12500,
        "space": 35,
        "value": 25000,
        "description": "🛌 五星级酒店同款大床，躺下就是享受",
        "rarity": "史诗"
    },
    {
        "name": "小巧书架",
        "category": "储物",
        "buy_price": 1200,
        "sell_price": 600,
        "space": 10,
        "value": 1200,
        "description": "📚 简单的三层书架，放满书显得很有文化",
        "rarity": "普通"
    },
    {
        "name": "古典衣柜",
        "category": "储物",
        "buy_price": 5000,
        "sell_price": 2500,
        "space": 30,
        "value": 5000,
        "description": "👗 雕花精美的实木衣柜，储物空间很大",
        "rarity": "稀有"
    },
    {
        "name": "时尚落地灯",
        "category": "装饰",
        "buy_price": 600,
        "sell_price": 300,
        "space": 3,
        "value": 600,
        "description": "💡 现代风格的落地灯，营造温馨氛围",
        "rarity": "普通"
    },
    {
        "name": "水晶吊灯",
        "category": "装饰",
        "buy_price": 12000,
        "sell_price": 6000,
        "space": 8,
        "value": 12000,
        "description": "💎 璀璨的水晶吊灯，瞬间提升房间档次",
        "rarity": "稀有"
    },
    {
        "name": "舒适地毯",
        "category": "装饰",
        "buy_price": 1000,
        "sell_price": 500,
        "space": 12,
        "value": 1000,
        "description": "🏺 柔软的羊毛地毯，光脚踩上去很舒服",
        "rarity": "普通"
    },
    {
        "name": "古董花瓶",
        "category": "装饰",
        "buy_price": 3000,
        "sell_price": 1500,
        "space": 2,
        "value": 3000,
        "description": "🏺 精美的青花瓷花瓶，插几支花很优雅",
        "rarity": "稀有"
    },
    {
        "name": "现代电视柜",
        "category": "家电",
        "buy_price": 2500,
        "sell_price": 1250,
        "space": 18,
        "value": 2500,
        "description": "📺 简约的电视柜，配套的储物空间刚好",
        "rarity": "普通"
    },
    {
        "name": "智能冰箱",
        "category": "家电",
        "buy_price": 18000,
        "sell_price": 9000,
        "space": 22,
        "value": 18000,
        "description": "❄️ 大容量智能冰箱，保鲜效果一流",
        "rarity": "稀有"
    },
    {
        "name": "按摩躺椅",
        "category": "座椅",
        "buy_price": 30000,
        "sell_price": 15000,
        "space": 28,
        "value": 30000,
        "description": "💆 高级按摩躺椅，疲劳一扫而光",
        "rarity": "史诗"
    },
    {
        "name": "钢琴",
        "category": "特殊",
        "buy_price": 50000,
        "sell_price": 25000,
        "space": 40,
        "value": 50000,
        "description": "🎹 优雅的三角钢琴，琴声悠扬动人",
        "rarity": "传说"
    },
    {
        "name": "红酒收藏柜",
        "category": "特殊",
        "buy_price": 20000,
        "sell_price": 10000,
        "space": 25,
        "value": 20000,
        "description": "🍷 恒温红酒柜，展示收藏的好酒",
        "rarity": "史诗"
    },
    {
        "name": "艺术雕像",
        "category": "装饰",
        "buy_price": 8000,
        "sell_price": 4000,
        "space": 6,
        "value": 8000,
        "description": "🗿 精美的大理石雕像，艺术气息浓厚",
        "rarity": "稀有"
    },
    # 更多座椅类
    {
        "name": "游戏电竞椅",
        "category": "座椅",
        "buy_price": 3500,
        "sell_price": 1750,
        "space": 12,
        "value": 3500,
        "description": "🎮 专业电竞椅，久坐不累，RGB灯效酷炫",
        "rarity": "普通"
    },
    {
        "name": "老板椅",
        "category": "座椅",
        "buy_price": 6800,
        "sell_price": 3400,
        "space": 15,
        "value": 6800,
        "description": "💼 真皮老板椅，坐上去就有成功人士的感觉",
        "rarity": "稀有"
    },
    {
        "name": "懒人沙发",
        "category": "座椅",
        "buy_price": 1200,
        "sell_price": 600,
        "space": 8,
        "value": 1200,
        "description": "🛋️ 软软的豆袋沙发，躺下就不想起来",
        "rarity": "普通"
    },
    {
        "name": "皇室宝座",
        "category": "座椅",
        "buy_price": 100000,
        "sell_price": 50000,
        "space": 45,
        "value": 100000,
        "description": "👑 镶金嵌钻的皇室宝座，彰显至尊地位",
        "rarity": "传说"
    },
    # 更多桌子类
    {
        "name": "书桌",
        "category": "桌子",
        "buy_price": 1500,
        "sell_price": 750,
        "space": 12,
        "value": 1500,
        "description": "📖 简约书桌，学习工作的好伙伴",
        "rarity": "普通"
    },
    {
        "name": "玻璃茶几",
        "category": "桌子",
        "buy_price": 2200,
        "sell_price": 1100,
        "space": 10,
        "value": 2200,
        "description": "🔮 时尚玻璃茶几，透明设计显得空间更大",
        "rarity": "普通"
    },
    {
        "name": "升降办公桌",
        "category": "桌子",
        "buy_price": 4500,
        "sell_price": 2250,
        "space": 16,
        "value": 4500,
        "description": "⬆️ 智能升降桌，站坐切换，健康办公",
        "rarity": "稀有"
    },
    {
        "name": "古董八仙桌",
        "category": "桌子",
        "buy_price": 35000,
        "sell_price": 17500,
        "space": 30,
        "value": 35000,
        "description": "🏮 清代古董八仙桌，文物级别的收藏品",
        "rarity": "史诗"
    },
    # 更多床类
    {
        "name": "上下铺",
        "category": "床类",
        "buy_price": 2800,
        "sell_price": 1400,
        "space": 18,
        "value": 2800,
        "description": "🏠 实用上下铺，节省空间的选择",
        "rarity": "普通"
    },
    {
        "name": "按摩床",
        "category": "床类",
        "buy_price": 18000,
        "sell_price": 9000,
        "space": 28,
        "value": 18000,
        "description": "💆 智能按摩床，睡觉的同时享受按摩",
        "rarity": "稀有"
    },
    {
        "name": "水床",
        "category": "床类",
        "buy_price": 12000,
        "sell_price": 6000,
        "space": 32,
        "value": 12000,
        "description": "🌊 新奇的水床体验，如在水中漂浮",
        "rarity": "稀有"
    },
    {
        "name": "悬浮床",
        "category": "床类",
        "buy_price": 200000,
        "sell_price": 100000,
        "space": 40,
        "value": 200000,
        "description": "🚀 科幻悬浮床，磁悬浮技术打造的未来睡眠体验",
        "rarity": "传说"
    },
    # 更多储物类
    {
        "name": "鞋柜",
        "category": "储物",
        "buy_price": 800,
        "sell_price": 400,
        "space": 8,
        "value": 800,
        "description": "👠 多层鞋柜，整齐收纳各种鞋子",
        "rarity": "普通"
    },
    {
        "name": "储物柜",
        "category": "储物",
        "buy_price": 1800,
        "sell_price": 900,
        "space": 15,
        "value": 1800,
        "description": "📦 万能储物柜，什么都能装",
        "rarity": "普通"
    },
    {
        "name": "保险箱",
        "category": "储物",
        "buy_price": 15000,
        "sell_price": 7500,
        "space": 12,
        "value": 15000,
        "description": "🔒 防盗保险箱，贵重物品的守护者",
        "rarity": "稀有"
    },
    {
        "name": "智能衣帽间",
        "category": "储物",
        "buy_price": 80000,
        "sell_price": 40000,
        "space": 60,
        "value": 80000,
        "description": "👔 全自动智能衣帽间，AI帮你搭配服装",
        "rarity": "史诗"
    },
    # 更多装饰类
    {
        "name": "盆栽",
        "category": "装饰",
        "buy_price": 200,
        "sell_price": 100,
        "space": 2,
        "value": 200,
        "description": "🌱 小清新绿植，净化空气美化环境",
        "rarity": "普通"
    },
    {
        "name": "挂画",
        "category": "装饰",
        "buy_price": 1500,
        "sell_price": 750,
        "space": 1,
        "value": 1500,
        "description": "🖼️ 精美装饰画，提升房间艺术气息",
        "rarity": "普通"
    },
    {
        "name": "镜子",
        "category": "装饰",
        "buy_price": 800,
        "sell_price": 400,
        "space": 3,
        "value": 800,
        "description": "🪞 大号梳妆镜，照出美丽的自己",
        "rarity": "普通"
    },
    {
        "name": "水族箱",
        "category": "装饰",
        "buy_price": 5500,
        "sell_price": 2750,
        "space": 20,
        "value": 5500,
        "description": "🐠 大型水族箱，海底世界尽在眼前",
        "rarity": "稀有"
    },
    {
        "name": "名画真迹",
        "category": "装饰",
        "buy_price": 500000,
        "sell_price": 250000,
        "space": 2,
        "value": 500000,
        "description": "🎨 梵高向日葵真迹，无价的艺术珍品",
        "rarity": "传说"
    },
    # 更多家电类
    {
        "name": "洗衣机",
        "category": "家电",
        "buy_price": 3500,
        "sell_price": 1750,
        "space": 12,
        "value": 3500,
        "description": "👕 全自动洗衣机，衣物清洁的好帮手",
        "rarity": "普通"
    },
    {
        "name": "空调",
        "category": "家电",
        "buy_price": 4200,
        "sell_price": 2100,
        "space": 8,
        "value": 4200,
        "description": "❄️ 变频空调，四季如春的舒适体验",
        "rarity": "普通"
    },
    {
        "name": "微波炉",
        "category": "家电",
        "buy_price": 800,
        "sell_price": 400,
        "space": 4,
        "value": 800,
        "description": "🔥 家用微波炉，快速加热美食",
        "rarity": "普通"
    },
    {
        "name": "智能音响",
        "category": "家电",
        "buy_price": 2200,
        "sell_price": 1100,
        "space": 3,
        "value": 2200,
        "description": "🔊 AI智能音响，声控播放你喜欢的音乐",
        "rarity": "普通"
    },
    {
        "name": "投影仪",
        "category": "家电",
        "buy_price": 6800,
        "sell_price": 3400,
        "space": 5,
        "value": 6800,
        "description": "📽️ 4K激光投影仪，家庭影院体验",
        "rarity": "稀有"
    },
    {
        "name": "智能机器人",
        "category": "家电",
        "buy_price": 50000,
        "sell_price": 25000,
        "space": 6,
        "value": 50000,
        "description": "🤖 家务机器人，全自动打理家庭生活",
        "rarity": "史诗"
    },
    # 新增运动健身类
    {
        "name": "跑步机",
        "category": "健身",
        "buy_price": 8000,
        "sell_price": 4000,
        "space": 25,
        "value": 8000,
        "description": "🏃 专业跑步机，在家就能享受跑步乐趣",
        "rarity": "稀有"
    },
    {
        "name": "哑铃架",
        "category": "健身",
        "buy_price": 2500,
        "sell_price": 1250,
        "space": 10,
        "value": 2500,
        "description": "💪 专业哑铃组合，力量训练必备",
        "rarity": "普通"
    },
    {
        "name": "瑜伽垫",
        "category": "健身",
        "buy_price": 300,
        "sell_price": 150,
        "space": 2,
        "value": 300,
        "description": "🧘 专业瑜伽垫，冥想健身两相宜",
        "rarity": "普通"
    },
    {
        "name": "家用健身房",
        "category": "健身",
        "buy_price": 120000,
        "sell_price": 60000,
        "space": 80,
        "value": 120000,
        "description": "🏋️ 全套健身设备，私人健身房体验",
        "rarity": "史诗"
    },
    # 新增厨房类
    {
        "name": "燃气灶",
        "category": "厨房",
        "buy_price": 1200,
        "sell_price": 600,
        "space": 6,
        "value": 1200,
        "description": "🔥 双眼燃气灶，烹饪美食的基础设备",
        "rarity": "普通"
    },
    {
        "name": "烤箱",
        "category": "厨房",
        "buy_price": 2800,
        "sell_price": 1400,
        "space": 8,
        "value": 2800,
        "description": "🍞 大容量烤箱，烘焙达人必备",
        "rarity": "普通"
    },
    {
        "name": "橱柜",
        "category": "厨房",
        "buy_price": 8500,
        "sell_price": 4250,
        "space": 30,
        "value": 8500,
        "description": "🍽️ 整体橱柜，厨房收纳的完美解决方案",
        "rarity": "稀有"
    },
    {
        "name": "智能厨房系统",
        "category": "厨房",
        "buy_price": 300000,
        "sell_price": 150000,
        "space": 50,
        "value": 300000,
        "description": "👨‍🍳 AI智能厨房，机器人大厨为你烹饪",
        "rarity": "传说"
    },
    # 新增娱乐类
    {
        "name": "游戏机",
        "category": "娱乐",
        "buy_price": 3000,
        "sell_price": 1500,
        "space": 4,
        "value": 3000,
        "description": "🎮 最新游戏主机，畅玩各种大作",
        "rarity": "普通"
    },
    {
        "name": "麻将桌",
        "category": "娱乐",
        "buy_price": 5000,
        "sell_price": 2500,
        "space": 20,
        "value": 5000,
        "description": "🀄 自动麻将桌，朋友聚会的好选择",
        "rarity": "稀有"
    },
    {
        "name": "台球桌",
        "category": "娱乐",
        "buy_price": 15000,
        "sell_price": 7500,
        "space": 35,
        "value": 15000,
        "description": "🎱 专业台球桌，绅士运动的优雅体现",
        "rarity": "稀有"
    },
    {
        "name": "KTV包间",
        "category": "娱乐",
        "buy_price": 80000,
        "sell_price": 40000,
        "space": 60,
        "value": 80000,
        "description": "🎤 专业KTV设备，在家就能开演唱会",
        "rarity": "史诗"
    }
]

def get_furniture_by_name(furniture_name: str):
    """根据家具名称获取家具信息"""
    for furniture in FURNITURE_LIST:
        if furniture["name"] == furniture_name:
            return furniture
    return None

def get_furniture_by_category(category: str):
    """根据分类获取家具列表"""
    return [furniture for furniture in FURNITURE_LIST if furniture["category"] == category]

def get_furniture_by_rarity(rarity: str):
    """根据稀有度获取家具列表"""
    return [furniture for furniture in FURNITURE_LIST if furniture["rarity"] == rarity]

def format_furniture_list() -> str:
    """格式化家具列表显示"""
    furniture_text = "🪑【家具中心商品目录】🪑\n\n"

    # 按分类整理
    categories = {}
    for furniture in FURNITURE_LIST:
        category = furniture["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(furniture)

    # 分类显示
    for category, items in categories.items():
        furniture_text += f"【{category}类】\n"
        for item in items:
            rarity_emoji = {
                "普通": "⚪",
                "稀有": "🔵",
                "史诗": "🟣",
                "传说": "🟡"
            }.get(item["rarity"], "⚪")

            furniture_text += f"{rarity_emoji} {item['name']} - 💰{item['buy_price']}金币 (📦{item['space']}空间)\n"
        furniture_text += "\n"

    furniture_text += "💡 使用「购买家具 家具名称」购买家具\n"
    furniture_text += "💡 使用「出售家具 家具名称」出售家具"

    return furniture_text

def calculate_furniture_total_value(furniture_inventory: dict) -> int:
    """计算家具总价值"""
    total_value = 0
    for furniture_name, quantity in furniture_inventory.items():
        furniture_info = get_furniture_by_name(furniture_name)
        if furniture_info:
            total_value += furniture_info["value"] * quantity
    return total_value

def calculate_furniture_total_space(furniture_inventory: dict) -> int:
    """计算家具总占用空间"""
    total_space = 0
    for furniture_name, quantity in furniture_inventory.items():
        furniture_info = get_furniture_by_name(furniture_name)
        if furniture_info:
            total_space += furniture_info["space"] * quantity
    return total_space

def format_furniture_inventory(furniture_inventory: dict) -> str:
    """格式化家具库存显示"""
    if not furniture_inventory:
        return "无家具"
    
    furniture_list = []
    for furniture_name, quantity in furniture_inventory.items():
        if quantity > 0:
            furniture_info = get_furniture_by_name(furniture_name)
            if furniture_info:
                # 资产查询中不显示稀有度标识，保持简洁
                furniture_list.append(f"{furniture_name} x{quantity}")
            else:
                furniture_list.append(f"❓{furniture_name} x{quantity}")
    
    return ", ".join(furniture_list) if furniture_list else "无家具"
