"""地下城配置文件"""

# 地下城列表
DUNGEON_LIST = [
    {
        "id": 1,
        "name": "哥布林巢穴",
        "description": "充满危险的哥布林巢穴，里面有各种强弱不同的哥布林（普通哥布林，哥布林战士，哥布林斥候，狼骑哥布林，哥布林女巫，战车哥布林，哥布林狂战士，哥布林萨满，哥布林祭司，哥布林王）",
        "min_level": 1,  # 最低等级要求
        "base_experience": 50,  # 该地下城的基础经验奖励
        "monsters": [
            {
                "name": "普通哥布林",
                "difficulty": 1,
                "weight": 40,  # 出现权重
                "experience": 10,  # 击杀经验
                "drops": [
                    {"item": "普通哥布林结晶", "price": 25, "weight": 50},
                    {"item": "哥布林碎铁刀", "price": 20, "weight": 25},
                    {"item": "破损的哥布林兽皮片", "price": 12, "weight": 20},
                    {"item": "哥布林草药包", "price": 30, "weight": 5}
                ],
                "description": "最常见的哥布林，实力较弱"
            },
            {
                "name": "哥布林战士",
                "difficulty": 5,
                "weight": 25,
                "experience": 15,  # 击杀经验
                "drops": [
                    {"item": "哥布林战士结晶", "price": 60, "weight": 40},
                    {"item": "哥布林铁刃", "price": 75, "weight": 25},
                    {"item": "哥布林护腕", "price": 50, "weight": 20},
                    {"item": "哥布林部落战士徽记", "price": 85, "weight": 10},
                    {"item": "哥布林调配药", "price": 65, "weight": 5}
                ],
                "description": "拥有基础战斗技能的哥布林"
            },
            {
                "name": "哥布林斥候",
                "difficulty": 10,
                "weight": 20,
                "experience": 50,  # 击杀经验
                "drops": [
                    {"item": "哥布林斥候结晶", "price": 75, "weight": 40},
                    {"item": "哥布林短弓", "price": 90, "weight": 25},
                    {"item": "迅捷哥布林靴", "price": 65, "weight": 20},
                    {"item": "哥布林侦查卷轴", "price": 100, "weight": 10},
                    {"item": "敏捷药水·哥布林调制", "price": 75, "weight": 5}
                ],
                "description": "速度很快的哥布林侦察兵"
            },
            {
                "name": "狼骑哥布林",
                "difficulty": 12,
                "weight": 8,
                "experience": 100,  # 击杀经验
                "drops": [
                    {"item": "狼骑哥布林结晶", "price": 120, "weight": 35},
                    {"item": "狼牙哥布林项链", "price": 150, "weight": 25},
                    {"item": "哥布林骑兵长矛", "price": 140, "weight": 20},
                    {"item": "哥布林野狼皮斗篷", "price": 110, "weight": 15},
                    {"item": "野性哥布林药剂", "price": 100, "weight": 5}
                ],
                "description": "骑着狼的哥布林，机动性极强"
            },
            {
                "name": "哥布林女巫",
                "difficulty": 15,
                "weight": 5,
                "experience": 200,  # 击杀经验
                "drops": [
                    {"item": "哥布林女巫结晶", "price": 150, "weight": 35},
                    {"item": "黑雾哥布林法杖", "price": 180, "weight": 25},
                    {"item": "哥布林诅咒骨符", "price": 160, "weight": 20},
                    {"item": "哥布林巫袍", "price": 130, "weight": 15},
                    {"item": "哥布林魔力药水", "price": 100, "weight": 5}
                ],
                "description": "会使用黑暗魔法的哥布林"
            },
            {
                "name": "战车哥布林",
                "difficulty": 20,
                "weight": 3,
                "experience": 500,  # 击杀经验
                "drops": [
                    {"item": "战车哥布林结晶", "price": 200, "weight": 35},
                    {"item": "哥布林重锤", "price": 240, "weight": 25},
                    {"item": "哥布林钢甲", "price": 220, "weight": 20},
                    {"item": "战车残骸零件", "price": 180, "weight": 15},
                    {"item": "哥布林血怒药剂", "price": 120, "weight": 5}
                ],
                "description": "驾驶战车的精英哥布林"
            },
            {
                "name": "哥布林狂战士",
                "difficulty": 25,
                "weight": 2,
                "experience": 1000,  # 击杀经验
                "drops": [
                    {"item": "哥布林狂战士结晶", "price": 250, "weight": 35},
                    {"item": "狂暴哥布林巨斧", "price": 300, "weight": 25},
                    {"item": "狂战护甲·哥布林制", "price": 280, "weight": 20},
                    {"item": "哥布林怒吼面具", "price": 240, "weight": 15},
                    {"item": "狂暴哥布林药水", "price": 150, "weight": 5}
                ],
                "description": "失去理智的强大哥布林战士"
            },
            {
                "name": "哥布林萨满",
                "difficulty": 30,
                "weight": 1,
                "experience": 1500,  # 击杀经验
                "drops": [
                    {"item": "哥布林萨满结晶", "price": 300, "weight": 30},
                    {"item": "哥布林萨满萨满部落图腾", "price": 360, "weight": 25},
                    {"item": "哥布林灵能法杖", "price": 340, "weight": 20},
                    {"item": "哥布林萨满羽冠", "price": 310, "weight": 15},
                    {"item": "哥布林萨满自然之息药剂", "price": 200, "weight": 10}
                ],
                "description": "掌握强大魔法的哥布林长老"
            },
            {
                "name": "哥布林祭司",
                "difficulty": 40,
                "weight": 1,
                "experience": 2000,  # 击杀经验
                "drops": [
                    {"item": "哥布林祭司结晶", "price": 375, "weight": 30},
                    {"item": "神圣哥布林权杖", "price": 450, "weight": 25},
                    {"item": "哥布林祭司羽织", "price": 400, "weight": 20},
                    {"item": "哥布林圣光骨符", "price": 350, "weight": 15},
                    {"item": "哥布林圣泉药液", "price": 250, "weight": 10}
                ],
                "description": "神圣力量的哥布林祭司"
            },
            {
                "name": "哥布林王",
                "difficulty": 50,
                "weight": 0.5,
                "experience": 5000,  # 击杀经验
                "drops": [
                    {"item": "哥布林王结晶", "price": 1200, "weight": 25},
                    {"item": "哥布林王的传奇战刀", "price": 1500, "weight": 20},
                    {"item": "哥布林王之冠", "price": 1350, "weight": 20},
                    {"item": "哥布林王的王者血铸护甲", "price": 1250, "weight": 15},
                    {"item": "哥布林王的统御骨杖", "price": 1200, "weight": 10},
                    {"item": "传说哥布林药剂", "price": 800, "weight": 10}
                ],
                "description": "哥布林巢穴的绝对统治者"
            }
        ]
    },
    {
        "id": 2,
        "name": "鬼灭无限城",
        "description": "鬼舞辻无惨的无限城，充满了各种强大的鬼类（普通鬼，手鬼，响凯，矢琶羽，朱沙丸，鸣女，鬼舞辻无惨（伪））",
        "min_level": 20,  # 最低等级要求
        "base_experience": 1000,  # 该地下城的基础经验奖励
        "monsters": [
            {
                "name": "普通鬼",
                "difficulty": 40,
                "weight": 30,  # 出现权重
                "experience": 2000,  # 击杀经验
                "drops": [
                    {"item": "鬼之血", "price": 520, "weight": 50},
                    {"item": "破损的鬼爪", "price": 555, "weight": 25},
                    {"item": "鬼之鳞片", "price": 560, "weight": 20},
                    {"item": "暗夜精华", "price": 650, "weight": 5}
                ],
                "description": "最普通的鬼，实力不强但比人类强很多"
            },
            {
                "name": "手鬼",
                "difficulty": 45,
                "weight": 20,
                "experience": 2500,
                "drops": [
                    {"item": "手鬼结晶", "price": 800, "weight": 40},
                    {"item": "巨大鬼手", "price": 820, "weight": 25},
                    {"item": "手鬼之牙", "price": 900, "weight": 20},
                    {"item": "怨念碎片", "price": 1100, "weight": 10},
                    {"item": "鬼力药剂", "price": 1200, "weight": 5}
                ],
                "description": "拥有众多手臂的恐怖之鬼"
            },
            {
                "name": "响凯",
                "difficulty": 50,
                "weight": 15,
                "experience": 4000,
                "drops": [
                    {"item": "响凯的鼓", "price": 1500, "weight": 35},
                    {"item": "空间操控符", "price": 1600, "weight": 25},
                    {"item": "鼓声共鸣石", "price": 1800, "weight": 20},
                    {"item": "空间碎片", "price": 1600, "weight": 15},
                    {"item": "鼓之血清", "price": 2200, "weight": 5}
                ],
                "description": "能操控空间的鼓鬼"
            },
            {
                "name": "矢琶羽",
                "difficulty": 55,
                "weight": 12,
                "experience": 6000,
                "drops": [
                    {"item": "矢琶羽之眼", "price": 2200, "weight": 35},
                    {"item": "红血操术符", "price": 2300, "weight": 25},
                    {"item": "血液操控石", "price": 2400, "weight": 20},
                    {"item": "视线追踪器", "price": 2500, "weight": 15},
                    {"item": "血鬼术精华", "price": 3200, "weight": 5}
                ],
                "description": "能操控血液的可怕之鬼"
            },
            {
                "name": "朱沙丸",
                "difficulty": 60,
                "weight": 12,
                "experience": 8000,
                "drops": [
                    {"item": "朱沙丸的手球", "price": 5000, "weight": 35},
                    {"item": "重力操控珠", "price": 6000, "weight": 25},
                    {"item": "朱沙手鞠", "price": 7000, "weight": 20},
                    {"item": "重力核心", "price": 8000, "weight": 15},
                    {"item": "手鞠药剂", "price": 10000, "weight": 5}
                ],
                "description": "操控重力和手鞠的女鬼"
            },
            {
                "name": "鸣女",
                "difficulty": 65,
                "weight": 1.5,
                "experience": 10000,
                "drops": [
                    {"item": "鸣女的琵琶", "price": 10000, "weight": 20},
                    {"item": "上弦肆证明", "price": 12000, "weight": 25},
                    {"item": "空间操控琵琶", "price": 14000, "weight": 20},
                    {"item": "无限城核心", "price": 16000, "weight": 15},
                    {"item": "音律血清", "price": 20000, "weight": 20}
                ],
                "description": "操控无限城的琵琶女鬼"
            },
            {
                "name": "鬼舞辻无惨（伪）",
                "difficulty": 80,
                "weight": 0.2,
                "experience": 50000,
                "drops": [
                    {"item": "无惨的血", "price": 50000, "weight": 10},
                    {"item": "鬼王证明", "price": 60000, "weight": 15},
                    {"item": "完美生物细胞", "price": 70000, "weight": 15},
                    {"item": "鬼之始祖核心", "price": 80000, "weight": 20},
                    {"item": "万鬼之王权杖", "price": 90000, "weight": 15},
                    {"item": "不死不灭血清", "price": 100000, "weight": 25}
                ],
                "description": "鬼之始祖，万鬼之王，无限城的绝对主宰"
            }
        ]
    }
]

# 地下城战斗奖励配置
DUNGEON_REWARDS = {
    "attribute_gain_min": 1,  # 属性增长最小值
    "attribute_gain_max": 3,  # 属性增长最大值
    "stat_penalty": {
        "hunger": -20,     # 饥饿度减少
        "cleanliness": -15, # 清洁度减少
        "health": -10,     # 健康度减少
        "mood": -15        # 心情减少
    }
}

# 地下城冷却时间配置（小时）
DUNGEON_COOLDOWN_HOURS = 4
