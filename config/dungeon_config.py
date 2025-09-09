"""地下城配置文件"""

# 地下城列表
DUNGEON_LIST = [
    # =============哥布林系列地下城=============
    {
        "id": 1,
        "name": "哥布林巢穴",
        "description": "充满弱小哥布林的巢穴，适合新手冒险者磨练技巧（普通哥布林，哥布林战士，哥布林斥候）",
        "min_level": 1,  # 最低等级要求
        "base_experience": 50,  # 该地下城的基础经验奖励
        "monsters": [
            {
                "name": "普通哥布林",
                "difficulty": 1,
                "weight": 50,  # 出现权重
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
                "weight": 35,
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
                "difficulty": 8,
                "weight": 15,
                "experience": 25,  # 击杀经验
                "drops": [
                    {"item": "哥布林斥候结晶", "price": 75, "weight": 40},
                    {"item": "哥布林短弓", "price": 90, "weight": 25},
                    {"item": "迅捷哥布林靴", "price": 65, "weight": 20},
                    {"item": "哥布林侦查卷轴", "price": 100, "weight": 10},
                    {"item": "敏捷药水·哥布林调制", "price": 75, "weight": 5}
                ],
                "description": "速度很快的哥布林侦察兵"
            }
        ]
    },
    {
        "id": 2,
        "name": "哥布林要塞",
        "description": "哥布林的军事要塞，有更强的哥布林战士和骑兵部队（狼骑哥布林，哥布林女巫，哥布林重装战士，蜘蛛骑士哥布林，巨鼠骑士哥布林，战车哥布林）",
        "min_level": 10,  # 最低等级要求
        "base_experience": 150,  # 该地下城的基础经验奖励
        "monsters": [
            {
                "name": "狼骑哥布林",
                "difficulty": 12,
                "weight": 25,
                "experience": 80,  # 击杀经验
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
                "weight": 20,
                "experience": 120,  # 击杀经验
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
                "name": "哥布林重装战士",
                "difficulty": 18,
                "weight": 20,
                "experience": 150,  # 击杀经验
                "drops": [
                    {"item": "哥布林重装结晶", "price": 180, "weight": 35},
                    {"item": "哥布林重型盾牌", "price": 220, "weight": 25},
                    {"item": "哥布林板甲", "price": 200, "weight": 20},
                    {"item": "哥布林守护符", "price": 160, "weight": 15},
                    {"item": "重装哥布林药剂", "price": 120, "weight": 5}
                ],
                "description": "身穿重甲的哥布林精英战士"
            },
            {
                "name": "蜘蛛骑士哥布林",
                "difficulty": 20,
                "weight": 10,
                "experience": 200,  # 击杀经验
                "drops": [
                    {"item": "蜘蛛骑士结晶", "price": 250, "weight": 35},
                    {"item": "哥布林蛛丝战甲", "price": 300, "weight": 25},
                    {"item": "毒牙哥布林匕首", "price": 280, "weight": 20},
                    {"item": "蜘蛛卵囊", "price": 200, "weight": 15},
                    {"item": "毒性哥布林药剂", "price": 150, "weight": 5}
                ],
                "description": "骑着巨型蜘蛛的哥布林，可以释放毒液"
            },
            {
                "name": "巨鼠骑士哥布林",
                "difficulty": 22,
                "weight": 5,
                "experience": 250,  # 击杀经验
                "drops": [
                    {"item": "巨鼠骑士结晶", "price": 280, "weight": 35},
                    {"item": "哥布林鼠牙长枪", "price": 320, "weight": 25},
                    {"item": "巨鼠皮护甲", "price": 300, "weight": 20},
                    {"item": "鼠王徽章", "price": 250, "weight": 15},
                    {"item": "敏捷巨鼠药剂", "price": 180, "weight": 5}
                ],
                "description": "骑着巨大老鼠的哥布林，速度惊人"
            },
            {
                "name": "战车哥布林",
                "difficulty": 20,
                "weight": 3,
                "experience": 300,  # 击杀经验
                "drops": [
                    {"item": "战车哥布林结晶", "price": 200, "weight": 35},
                    {"item": "哥布林重锤", "price": 240, "weight": 25},
                    {"item": "哥布林钢甲", "price": 220, "weight": 20},
                    {"item": "战车残骸零件", "price": 180, "weight": 15},
                    {"item": "哥布林血怒药剂", "price": 120, "weight": 5}
                ],
                "description": "驾驶战车的精英哥布林"
            }
        ]
    },
    {
        "id": 3,
        "name": "哥布林王国",
        "description": "哥布林文明的最高成就，拥有强大的精英部队和传奇英雄（哥布林幻术师，野猪骑士哥布林，哥布林先知，哥布林狂战士，哥布林萨满，哥布林祭司，哥布林英雄，哥布林酋长，哥布林巨人，哥布林王）",
        "min_level": 15,  # 最低等级要求
        "base_experience": 300,  # 该地下城的基础经验奖励
        "monsters": [
            {
                "name": "哥布林幻术师",
                "difficulty": 25,
                "weight": 20,
                "experience": 300,  # 击杀经验
                "drops": [
                    {"item": "哥布林幻术师结晶", "price": 350, "weight": 35},
                    {"item": "幻象哥布林法珠", "price": 400, "weight": 25},
                    {"item": "哥布林幻术手套", "price": 380, "weight": 20},
                    {"item": "幻术符文石", "price": 320, "weight": 15},
                    {"item": "幻象哥布林药剂", "price": 250, "weight": 5}
                ],
                "description": "精通幻术的哥布林法师，能创造假象迷惑敌人"
            },
            {
                "name": "野猪骑士哥布林",
                "difficulty": 28,
                "weight": 15,
                "experience": 400,  # 击杀经验
                "drops": [
                    {"item": "野猪骑士结晶", "price": 400, "weight": 35},
                    {"item": "哥布林野猪战锤", "price": 480, "weight": 25},
                    {"item": "野猪皮重甲", "price": 450, "weight": 20},
                    {"item": "野猪獠牙项链", "price": 380, "weight": 15},
                    {"item": "狂怒野猪药剂", "price": 300, "weight": 5}
                ],
                "description": "骑着巨型野猪的哥布林重骑兵，冲撞力惊人"
            },
            {
                "name": "哥布林先知",
                "difficulty": 30,
                "weight": 10,
                "experience": 500,  # 击杀经验
                "drops": [
                    {"item": "哥布林先知结晶", "price": 500, "weight": 30},
                    {"item": "预言哥布林水晶球", "price": 600, "weight": 25},
                    {"item": "哥布林先知长袍", "price": 550, "weight": 20},
                    {"item": "命运符文石", "price": 480, "weight": 15},
                    {"item": "预知哥布林药剂", "price": 400, "weight": 10}
                ],
                "description": "能预知未来的哥布林智者，掌握时间魔法"
            },
            {
                "name": "哥布林狂战士",
                "difficulty": 25,
                "weight": 8,
                "experience": 600,  # 击杀经验
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
                "weight": 5,
                "experience": 800,  # 击杀经验
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
                "name": "哥布林英雄",
                "difficulty": 35,
                "weight": 8,
                "experience": 800,  # 击杀经验
                "drops": [
                    {"item": "哥布林英雄结晶", "price": 700, "weight": 30},
                    {"item": "英雄哥布林圣剑", "price": 850, "weight": 25},
                    {"item": "哥布林英雄铠甲", "price": 800, "weight": 20},
                    {"item": "英雄徽章", "price": 650, "weight": 15},
                    {"item": "英雄哥布林药剂", "price": 500, "weight": 10}
                ],
                "description": "哥布林族中的传奇英雄，实力强大"
            },
            {
                "name": "哥布林祭司",
                "difficulty": 40,
                "weight": 3,
                "experience": 1000,  # 击杀经验
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
                "name": "哥布林酋长",
                "difficulty": 40,
                "weight": 5,
                "experience": 1200,  # 击杀经验
                "drops": [
                    {"item": "哥布林酋长结晶", "price": 900, "weight": 30},
                    {"item": "酋长哥布林战斧", "price": 1100, "weight": 25},
                    {"item": "哥布林酋长王冠", "price": 1000, "weight": 20},
                    {"item": "部族统领令牌", "price": 850, "weight": 15},
                    {"item": "统领哥布林药剂", "price": 650, "weight": 10}
                ],
                "description": "哥布林部族的最高统治者"
            },
            {
                "name": "哥布林巨人",
                "difficulty": 45,
                "weight": 2,
                "experience": 1800,  # 击杀经验
                "drops": [
                    {"item": "哥布林巨人结晶", "price": 1200, "weight": 25},
                    {"item": "巨人哥布林大棒", "price": 1400, "weight": 25},
                    {"item": "哥布林巨人之拳", "price": 1350, "weight": 20},
                    {"item": "巨人之力药剂", "price": 1000, "weight": 15},
                    {"item": "巨人血液", "price": 800, "weight": 15}
                ],
                "description": "变异的巨型哥布林，力量恐怖"
            },
            {
                "name": "哥布林王",
                "difficulty": 50,
                "weight": 1,
                "experience": 3000,  # 击杀经验
                "drops": [
                    {"item": "哥布林王结晶", "price": 1800, "weight": 20},
                    {"item": "哥布林王的传奇战刀", "price": 2200, "weight": 20},
                    {"item": "哥布林王之冠", "price": 2000, "weight": 20},
                    {"item": "哥布林王的王者血铸护甲", "price": 1900, "weight": 15},
                    {"item": "哥布林王的统御骨杖", "price": 1800, "weight": 15},
                    {"item": "传说哥布林药剂", "price": 1200, "weight": 10}
                ],
                "description": "哥布林王国的绝对统治者，传奇般的存在"
            }
        ]
    },
    
    # =============鬼灭系列地下城=============
    {
        "id": 4,
        "name": "鬼灭入门城",
        "description": "充满普通鬼类的废弃城镇，是猎鬼人的试炼之地（普通鬼，手鬼，响凯）",
        "min_level": 20,  # 最低等级要求
        "base_experience": 500,  # 该地下城的基础经验奖励
        "monsters": [
            {
                "name": "普通鬼",
                "difficulty": 35,
                "weight": 50,  # 出现权重
                "experience": 800,  # 击杀经验
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
                "difficulty": 40,
                "weight": 30,
                "experience": 1200,
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
                "difficulty": 45,
                "weight": 20,
                "experience": 2000,
                "drops": [
                    {"item": "响凯的鼓", "price": 1500, "weight": 35},
                    {"item": "空间操控符", "price": 1600, "weight": 25},
                    {"item": "鼓声共鸣石", "price": 1800, "weight": 20},
                    {"item": "空间碎片", "price": 1600, "weight": 15},
                    {"item": "鼓之血清", "price": 2200, "weight": 5}
                ],
                "description": "能操控空间的鼓鬼"
            }
        ]
    },
    {
        "id": 5,
        "name": "鬼灭试炼城",
        "description": "下弦鬼盘踞的恐怖之地，实力强大的鬼类聚集地（下弦陆·蜘蛛鬼累，下弦伍·鵺，下弦肆·钰壶）",
        "min_level": 25,  # 最低等级要求
        "base_experience": 1000,  # 该地下城的基础经验奖励
        "monsters": [
            {
                "name": "下弦陆·蜘蛛鬼累",
                "difficulty": 55,
                "weight": 40,
                "experience": 3500,
                "drops": [
                    {"item": "下弦陆证明", "price": 3000, "weight": 30},
                    {"item": "蜘蛛丝血鬼术符", "price": 3500, "weight": 25},
                    {"item": "累的蜘蛛茧", "price": 4000, "weight": 20},
                    {"item": "血鬼术·蜘蛛之书", "price": 4500, "weight": 15},
                    {"item": "下弦之血", "price": 5000, "weight": 10}
                ],
                "description": "下弦陆，蜘蛛血鬼术的使用者，操控蜘蛛丝"
            },
            {
                "name": "下弦伍·鵺",
                "difficulty": 58,
                "weight": 35,
                "experience": 4000,
                "drops": [
                    {"item": "下弦伍证明", "price": 3500, "weight": 30},
                    {"item": "鵺的羽翼", "price": 4000, "weight": 25},
                    {"item": "暗影血鬼术符", "price": 4500, "weight": 20},
                    {"item": "血鬼术·影之书", "price": 5000, "weight": 15},
                    {"item": "鵺之血", "price": 5500, "weight": 10}
                ],
                "description": "下弦伍，能操控暗影的飞行之鬼"
            },
            {
                "name": "下弦肆·钰壶",
                "difficulty": 60,
                "weight": 25,
                "experience": 5000,
                "drops": [
                    {"item": "下弦肆证明", "price": 4000, "weight": 30},
                    {"item": "钰壶的壶", "price": 4500, "weight": 25},
                    {"item": "陶艺血鬼术符", "price": 5000, "weight": 20},
                    {"item": "血鬼术·陶艺之书", "price": 5500, "weight": 15},
                    {"item": "钰壶之血", "price": 6000, "weight": 10}
                ],
                "description": "下弦肆，精通陶艺血鬼术的艺术家之鬼"
            }
        ]
    },
    {
        "id": 6,
        "name": "鬼灭无限城",
        "description": "鬼舞辻无惨的无限城，上弦鬼和鬼王的领域（上弦陆·妓夫太郎与堕姬，上弦伍·玉壶，上弦肆·半天狗，上弦叁·猗窝座，上弦贰·童磨，上弦壹·黑死牟，鸣女，鬼舞辻无惨）",
        "min_level": 30,  # 最低等级要求
        "base_experience": 2000,  # 该地下城的基础经验奖励
        "monsters": [
            {
                "name": "上弦陆·妓夫太郎与堕姬",
                "difficulty": 65,
                "weight": 25,
                "experience": 8000,
                "drops": [
                    {"item": "上弦陆证明", "price": 8000, "weight": 25},
                    {"item": "妓夫太郎的镰刀", "price": 10000, "weight": 20},
                    {"item": "堕姬的腰带", "price": 9000, "weight": 20},
                    {"item": "毒血血鬼术符", "price": 12000, "weight": 15},
                    {"item": "兄妹合体血清", "price": 15000, "weight": 20}
                ],
                "description": "上弦陆，兄妹合体的双子鬼"
            },
            {
                "name": "上弦伍·玉壶",
                "difficulty": 68,
                "weight": 20,
                "experience": 10000,
                "drops": [
                    {"item": "上弦伍证明", "price": 10000, "weight": 25},
                    {"item": "玉壶的千本针", "price": 12000, "weight": 20},
                    {"item": "血鬼术壶", "price": 14000, "weight": 20},
                    {"item": "水獄血鬼术符", "price": 16000, "weight": 15},
                    {"item": "玉壶精华", "price": 18000, "weight": 20}
                ],
                "description": "上弦伍，壶中之鬼，水獄血鬼术"
            },
            {
                "name": "上弦肆·半天狗",
                "difficulty": 70,
                "weight": 15,
                "experience": 12000,
                "drops": [
                    {"item": "上弦肆证明", "price": 12000, "weight": 25},
                    {"item": "半天狗的分身符", "price": 15000, "weight": 20},
                    {"item": "情感血鬼术符", "price": 18000, "weight": 20},
                    {"item": "恨之结晶", "price": 20000, "weight": 15},
                    {"item": "分身血清", "price": 25000, "weight": 20}
                ],
                "description": "上弦肆，能分裂出不同情感分身的鬼"
            },
            {
                "name": "上弦叁·猗窝座",
                "difficulty": 72,
                "weight": 15,
                "experience": 15000,
                "drops": [
                    {"item": "上弦叁证明", "price": 15000, "weight": 25},
                    {"item": "猗窝座的拳套", "price": 18000, "weight": 20},
                    {"item": "破坏杀血鬼术符", "price": 22000, "weight": 20},
                    {"item": "术式展开核心", "price": 25000, "weight": 15},
                    {"item": "武神血清", "price": 30000, "weight": 20}
                ],
                "description": "上弦叁，精通武术的格斗之鬼"
            },
            {
                "name": "上弦贰·童磨",
                "difficulty": 75,
                "weight": 10,
                "experience": 20000,
                "drops": [
                    {"item": "上弦贰证明", "price": 20000, "weight": 25},
                    {"item": "童磨的铁扇", "price": 25000, "weight": 20},
                    {"item": "冰血鬼术符", "price": 30000, "weight": 20},
                    {"item": "极乐教教主令", "price": 35000, "weight": 15},
                    {"item": "冰晶血清", "price": 40000, "weight": 20}
                ],
                "description": "上弦贰，冰血鬼术的教主之鬼"
            },
            {
                "name": "上弦壹·黑死牟",
                "difficulty": 78,
                "weight": 8,
                "experience": 25000,
                "drops": [
                    {"item": "上弦壹证明", "price": 25000, "weight": 25},
                    {"item": "黑死牟的日轮刀", "price": 35000, "weight": 20},
                    {"item": "月之呼吸血鬼术符", "price": 40000, "weight": 20},
                    {"item": "剑鬼之心", "price": 45000, "weight": 15},
                    {"item": "月影血清", "price": 50000, "weight": 20}
                ],
                "description": "上弦壹，最强的剑士之鬼"
            },
            {
                "name": "鸣女",
                "difficulty": 65,
                "weight": 5,
                "experience": 18000,
                "drops": [
                    {"item": "鸣女的琵琶", "price": 18000, "weight": 20},
                    {"item": "新上弦肆证明", "price": 20000, "weight": 25},
                    {"item": "空间操控琵琶", "price": 25000, "weight": 20},
                    {"item": "无限城核心", "price": 30000, "weight": 15},
                    {"item": "音律血清", "price": 35000, "weight": 20}
                ],
                "description": "操控无限城的琵琶女鬼"
            },
            {
                "name": "鬼舞辻无惨",
                "difficulty": 85,
                "weight": 0.5,
                "experience": 100000,
                "drops": [
                    {"item": "无惨的完美血", "price": 100000, "weight": 10},
                    {"item": "鬼王至尊证明", "price": 120000, "weight": 15},
                    {"item": "完美生物细胞", "price": 150000, "weight": 15},
                    {"item": "鬼之始祖核心", "price": 180000, "weight": 20},
                    {"item": "万鬼之王权杖", "price": 200000, "weight": 15},
                    {"item": "不死不灭血清", "price": 250000, "weight": 25}
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
