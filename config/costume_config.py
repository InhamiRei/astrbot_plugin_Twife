"""服装配置文件"""

# 装备部位定义
EQUIPMENT_SLOTS = {
    "头部": "head",
    "身体": "body", 
    "手部": "hands",
    "腿部": "legs",
    "脚部": "feet",
    "手持": "held",
    "饰品": "accessory"
}

# 兔女郎套装配置
COSTUME_LIST = [
    # 头部装备
    {
        "name": "兔女郎·黑兔耳发箍",
        "slot": "头部",
        "price": 100000,
        "effects": {
            "moe_value": 15,  # 增加妹抖值15%
        },
        "description": "可爱的黑色兔耳发箍，散发着神秘魅力"
    },
    {
        "name": "兔女郎·白蕾丝兔耳",
        "slot": "头部", 
        "price": 100000,
        "effects": {
            "spoil_value": 15,  # 增加撒娇值15%
        },
        "description": "精致的白色蕾丝兔耳，纯真可爱"
    },
    
    # 身体装备
    {
        "name": "兔女郎·亮黑紧身衣",
        "slot": "身体",
        "price": 150000,
        "effects": {
            "dark_rate": 10,  # 增加黑化率10%
            "contrast_cute": 20,  # 增加反差萌20%
        },
        "description": "紧身的黑色兔女郎装，展现完美身材"
    },
    {
        "name": "兔女郎·白兔女郎装",
        "slot": "身体",
        "price": 150000, 
        "effects": {
            "moe_value": 10,  # 增加妹抖值10%
            "spoil_value": 15,  # 增加撒娇值15%
        },
        "description": "纯白色的兔女郎装，清纯可人"
    },
    
    # 手部装备
    {
        "name": "兔女郎·黑蕾丝手套",
        "slot": "手部",
        "price": 80000,
        "effects": {
            "tsundere_value": 12,  # 增加傲娇值12%
        },
        "description": "黑色蕾丝手套，增添一丝神秘感"
    },
    {
        "name": "兔女郎·白绒毛手套", 
        "slot": "手部",
        "price": 80000,
        "effects": {
            "moe_value": 12,  # 增加妹抖值12%
        },
        "description": "柔软的白色绒毛手套，温暖可爱"
    },
    
    # 腿部装备
    {
        "name": "兔女郎·黑丝袜",
        "slot": "腿部",
        "price": 120000,
        "effects": {
            "dark_rate": 15,  # 增加黑化率15%
            "tsundere_value": 8,  # 增加傲娇值8%
        },
        "description": "性感的黑色丝袜，魅力十足"
    },
    {
        "name": "兔女郎·白丝袜",
        "slot": "腿部", 
        "price": 120000,
        "effects": {
            "moe_value": 18,  # 增加妹抖值18%
        },
        "description": "纯白的丝袜，清纯可爱"
    },
    
    # 脚部装备
    {
        "name": "兔女郎·黑高跟鞋",
        "slot": "脚部",
        "price": 110000,
        "effects": {
            "tsundere_value": 15,  # 增加傲娇值15%
            "contrast_cute": 10,  # 增加反差萌10%
        },
        "description": "优雅的黑色高跟鞋，增添女王气质"
    },
    {
        "name": "兔女郎·白高跟鞋",
        "slot": "脚部",
        "price": 110000,
        "effects": {
            "spoil_value": 20,  # 增加撒娇值20%
        },
        "description": "纯白色高跟鞋，优雅迷人"
    },
    
    # 手持装备
    {
        "name": "兔女郎·胡萝卜",
        "slot": "手持",
        "price": 90000,
        "effects": {
            "moe_value": 25,  # 增加妹抖值25%
        },
        "description": "可爱的胡萝卜道具，兔子的最爱"
    },
    {
        "name": "兔女郎·银色托盘",
        "slot": "手持",
        "price": 90000,
        "effects": {
            "spoil_value": 18,  # 增加撒娇值18%
        },
        "description": "精致的银色托盘，专业服务员的象征"
    },
    {
        "name": "兔女郎·魔术手杖",
        "slot": "手持",
        "price": 90000,
        "effects": {
            "contrast_cute": 30,  # 增加反差萌30%
        },
        "description": "神秘的魔术手杖，充满魔力"
    },
    
    # 饰品装备
    {
        "name": "兔女郎·毛茸兔尾巴",
        "slot": "饰品",
        "price": 85000,
        "effects": {
            "moe_value": 20,  # 增加妹抖值20%
            "contrast_cute": 15,  # 增加反差萌15%
        },
        "description": "毛茸茸的兔尾巴，可爱到犯规"
    },
    {
        "name": "兔女郎·爱心贴纸",
        "slot": "饰品",
        "price": 85000,
        "effects": {
            "spoil_value": 25,  # 增加撒娇值25%
        },
        "description": "粉色的爱心贴纸，增添甜美气息"
    },

    # === 女仆套装 ===
    # 头部装备
    {
        "name": "女仆·白褶皱发箍",
        "slot": "头部",
        "price": 95000,
        "effects": {
            "moe_value": 18,  # 增加妹抖值18%
            "spoil_value": 12,  # 增加撒娇值12%
        },
        "description": "精致的白色褶皱发箍，女仆的经典装扮"
    },
    
    # 身体装备
    {
        "name": "女仆·黑白女仆装",
        "slot": "身体",
        "price": 145000,
        "effects": {
            "moe_value": 25,  # 增加妹抖值25%
            "spoil_value": 20,  # 增加撒娇值20%
        },
        "description": "经典的黑白女仆装，优雅而可爱"
    },
    
    # 手部装备
    {
        "name": "女仆·花边手套",
        "slot": "手部",
        "price": 78000,
        "effects": {
            "spoil_value": 16,  # 增加撒娇值16%
            "contrast_cute": 8,  # 增加反差萌8%
        },
        "description": "带有精美花边的白色手套，展现女仆的细致"
    },
    
    # 腿部装备
    {
        "name": "女仆·白丝袜",
        "slot": "腿部",
        "price": 115000,
        "effects": {
            "moe_value": 22,  # 增加妹抖值22%
            "spoil_value": 10,  # 增加撒娇值10%
        },
        "description": "纯白色的丝袜，突显女仆的纯真可爱"
    },
    
    # 脚部装备
    {
        "name": "女仆·玛丽珍高跟鞋",
        "slot": "脚部",
        "price": 105000,
        "effects": {
            "moe_value": 15,  # 增加妹抖值15%
            "spoil_value": 18,  # 增加撒娇值18%
        },
        "description": "经典的玛丽珍高跟鞋，女仆专用款式"
    },
    
    # 手持装备
    {
        "name": "女仆·银色茶点托盘",
        "slot": "手持",
        "price": 88000,
        "effects": {
            "spoil_value": 20,  # 增加撒娇值20%
            "contrast_cute": 12,  # 增加反差萌12%
        },
        "description": "精致的银色托盘，专业女仆的必备工具"
    },
    
    # 饰品装备
    {
        "name": "女仆·萌萌啾饰品",
        "slot": "饰品",
        "price": 82000,
        "effects": {
            "moe_value": 28,  # 增加妹抖值28%
        },
        "description": "超级可爱的小饰品，萌化人心"
    },

    # === 巫女套装 ===
    # 头部装备
    {
        "name": "巫女·流苏丝带发带",
        "slot": "头部",
        "price": 115000,
        "effects": {
            "tsundere_value": 18,  # 增加傲娇值18%
            "contrast_cute": 15,  # 增加反差萌15%
        },
        "description": "飘逸的红白流苏发带，神圣而优雅"
    },
    
    # 身体装备
    {
        "name": "巫女·红白祈福长袍",
        "slot": "身体",
        "price": 180000,
        "effects": {
            "tsundere_value": 20,  # 增加傲娇值20%
            "contrast_cute": 25,  # 增加反差萌25%
            "dark_rate": 8,  # 增加黑化率8%
        },
        "description": "神圣的红白祈福长袍，蕴含神秘力量"
    },
    
    # 手部装备
    {
        "name": "巫女·宽袖流光手套",
        "slot": "手部",
        "price": 95000,
        "effects": {
            "contrast_cute": 20,  # 增加反差萌20%
            "tsundere_value": 10,  # 增加傲娇值10%
        },
        "description": "宽大的流光手套，散发着神秘光芒"
    },
    
    # 腿部装备
    {
        "name": "巫女·甘神红绯袴",
        "slot": "腿部",
        "price": 140000,
        "effects": {
            "tsundere_value": 25,  # 增加傲娇值25%
            "contrast_cute": 12,  # 增加反差萌12%
        },
        "description": "传统的红色绯袴，庄重而神秘"
    },
    
    # 脚部装备
    {
        "name": "巫女·神佑木屐",
        "slot": "脚部",
        "price": 130000,
        "effects": {
            "contrast_cute": 22,  # 增加反差萌22%
            "dark_rate": 10,  # 增加黑化率10%
        },
        "description": "受神明庇佑的传统木屐，每一步都蕴含神力"
    },
    
    # 手持装备
    {
        "name": "巫女·御幣祈福法器",
        "slot": "手持",
        "price": 108000,
        "effects": {
            "contrast_cute": 35,  # 增加反差萌35%
            "tsundere_value": 8,  # 增加傲娇值8%
        },
        "description": "神圣的御幣法器，能够净化邪恶"
    },
    
    # 饰品装备
    {
        "name": "巫女·铃铛小符饰",
        "slot": "饰品",
        "price": 102000,
        "effects": {
            "contrast_cute": 18,  # 增加反差萌18%
            "dark_rate": 15,  # 增加黑化率15%
        },
        "description": "带有神秘符咒的小铃铛，清脆悦耳"
    },

    # === 魔法少女套装 ===
    # 头部装备
    {
        "name": "魔法少女·星光缎带发饰",
        "slot": "头部",
        "price": 105000,
        "effects": {
            "moe_value": 20,  # 增加妹抖值20%
            "contrast_cute": 18,  # 增加反差萌18%
        },
        "description": "闪耀着星光的缎带发饰，魔法少女的标志"
    },
    
    # 身体装备
    {
        "name": "魔法少女·梦幻蓬蓬连衣裙",
        "slot": "身体",
        "price": 135000,
        "effects": {
            "moe_value": 30,  # 增加妹抖值30%
            "spoil_value": 15,  # 增加撒娇值15%
            "contrast_cute": 20,  # 增加反差萌20%
        },
        "description": "梦幻般的蓬蓬连衣裙，充满魔法气息"
    },
    
    # 手部装备
    {
        "name": "魔法少女·闪光蕾丝手套",
        "slot": "手部",
        "price": 85000,
        "effects": {
            "moe_value": 15,  # 增加妹抖值15%
            "contrast_cute": 12,  # 增加反差萌12%
        },
        "description": "散发着魔法光芒的蕾丝手套，优雅而神秘"
    },
    
    # 腿部装备
    {
        "name": "魔法少女·彩虹渐变长袜",
        "slot": "腿部",
        "price": 115000,
        "effects": {
            "moe_value": 25,  # 增加妹抖值25%
            "spoil_value": 8,  # 增加撒娇值8%
        },
        "description": "彩虹色渐变的长袜，每一步都闪耀着梦幻色彩"
    },
    
    # 脚部装备
    {
        "name": "魔法少女·魔力水晶高跟鞋",
        "slot": "脚部",
        "price": 110000,
        "effects": {
            "contrast_cute": 25,  # 增加反差萌25%
            "spoil_value": 12,  # 增加撒娇值12%
        },
        "description": "嵌有魔力水晶的高跟鞋，每一步都释放魔法能量"
    },
    
    # 手持装备
    {
        "name": "魔法少女·星尘魔法权杖",
        "slot": "手持",
        "price": 88000,
        "effects": {
            "moe_value": 18,  # 增加妹抖值18%
            "contrast_cute": 30,  # 增加反差萌30%
        },
        "description": "由星尘凝聚而成的魔法权杖，蕴含无穷魔力"
    },
    
    # 饰品装备
    {
        "name": "魔法少女·流光星尘胸饰",
        "slot": "饰品",
        "price": 86000,
        "effects": {
            "moe_value": 22,  # 增加妹抖值22%
            "contrast_cute": 16,  # 增加反差萌16%
        },
        "description": "流淌着星尘光芒的胸饰，魔法少女的力量源泉"
    },

    # === 小恶魔套装 ===
    # 头部装备
    {
        "name": "小恶魔·红黑角发箍",
        "slot": "头部",
        "price": 108000,
        "effects": {
            "dark_rate": 20,  # 增加黑化率20%
            "tsundere_value": 15,  # 增加傲娇值15%
        },
        "description": "红黑相间的小恶魔角发箍，散发着诱人的邪恶气息"
    },
    
    # 身体装备
    {
        "name": "小恶魔·俏皮紧身连衣裙",
        "slot": "身体",
        "price": 142000,
        "effects": {
            "dark_rate": 25,  # 增加黑化率25%
            "tsundere_value": 20,  # 增加傲娇值20%
            "contrast_cute": 15,  # 增加反差萌15%
        },
        "description": "紧贴身形的连衣裙，展现小恶魔的诱惑魅力"
    },
    
    # 手部装备
    {
        "name": "小恶魔·镶边指套手套",
        "slot": "手部",
        "price": 82000,
        "effects": {
            "dark_rate": 18,  # 增加黑化率18%
            "contrast_cute": 10,  # 增加反差萌10%
        },
        "description": "精致的镶边指套手套，增添神秘的诱惑力"
    },
    
    # 腿部装备
    {
        "name": "小恶魔·破洞网状长袜",
        "slot": "腿部",
        "price": 118000,
        "effects": {
            "dark_rate": 22,  # 增加黑化率22%
            "tsundere_value": 12,  # 增加傲娇值12%
        },
        "description": "带有破洞的网状长袜，性感中透露着叛逆"
    },
    
    # 脚部装备
    {
        "name": "小恶魔·亮漆高跟鞋",
        "slot": "脚部",
        "price": 112000,
        "effects": {
            "dark_rate": 16,  # 增加黑化率16%
            "tsundere_value": 18,  # 增加傲娇值18%
        },
        "description": "闪亮的漆皮高跟鞋，每一步都充满诱惑"
    },
    
    # 手持装备（多选项）
    {
        "name": "小恶魔·火焰小叉",
        "slot": "手持",
        "price": 85000,
        "effects": {
            "dark_rate": 30,  # 增加黑化率30%
            "tsundere_value": 8,  # 增加傲娇值8%
        },
        "description": "燃烧着邪恶火焰的小叉子，小恶魔的经典武器"
    },
    {
        "name": "小恶魔·幽火滴蜡",
        "slot": "手持",
        "price": 87000,
        "effects": {
            "dark_rate": 25,  # 增加黑化率25%
            "contrast_cute": 20,  # 增加反差萌20%
        },
        "description": "燃烧着幽蓝火焰的蜡烛，散发着神秘诱惑"
    },
    {
        "name": "小恶魔·男仆口球",
        "slot": "手持",
        "price": 89000,
        "effects": {
            "dark_rate": 35,  # 增加黑化率35%
            "contrast_cute": 15,  # 增加反差萌15%
        },
        "description": "小恶魔的特殊道具，充满禁忌的诱惑"
    },
    
    # 饰品装备
    {
        "name": "小恶魔·尾巴小铃铛",
        "slot": "饰品",
        "price": 84000,
        "effects": {
            "dark_rate": 20,  # 增加黑化率20%
            "tsundere_value": 16,  # 增加傲娇值16%
            "contrast_cute": 12,  # 增加反差萌12%
        },
        "description": "小恶魔尾巴上的铃铛，每次摆动都发出诱人铃声"
    },

    # === 修女套装 ===
    # 头部装备
    {
        "name": "修女·圣洁白纱头巾",
        "slot": "头部",
        "price": 100000,
        "effects": {
            "moe_value": 5,  # 增加妹抖值5%
            "spoil_value": 5,  # 增加撒娇值5%
            "tsundere_value": 5,  # 增加傲娇值5%
            "dark_rate": 5,  # 增加黑化率5%
            "contrast_cute": 8,  # 增加反差萌8%
        },
        "description": "圣洁的白色纱质头巾，散发着神圣的光辉"
    },
    
    # 身体装备
    {
        "name": "修女·黑白修女长袍",
        "slot": "身体",
        "price": 155000,
        "effects": {
            "moe_value": 8,  # 增加妹抖值8%
            "spoil_value": 8,  # 增加撒娇值8%
            "tsundere_value": 8,  # 增加傲娇值8%
            "dark_rate": 8,  # 增加黑化率8%
            "contrast_cute": 12,  # 增加反差萌12%
        },
        "description": "庄重的黑白修女长袍，体现神圣与纯洁"
    },
    
    # 手部装备
    {
        "name": "修女·纯白丝绸手套",
        "slot": "手部",
        "price": 85000,
        "effects": {
            "moe_value": 6,  # 增加妹抖值6%
            "spoil_value": 6,  # 增加撒娇值6%
            "tsundere_value": 6,  # 增加傲娇值6%
            "dark_rate": 6,  # 增加黑化率6%
            "contrast_cute": 8,  # 增加反差萌8%
        },
        "description": "纯白的丝绸手套，柔软而神圣"
    },
    
    # 腿部装备
    {
        "name": "修女·神启长袜",
        "slot": "腿部",
        "price": 125000,
        "effects": {
            "moe_value": 7,  # 增加妹抖值7%
            "spoil_value": 7,  # 增加撒娇值7%
            "tsundere_value": 7,  # 增加傲娇值7%
            "dark_rate": 7,  # 增加黑化率7%
            "contrast_cute": 10,  # 增加反差萌10%
        },
        "description": "受神明祝福的长袜，蕴含着神启的力量"
    },
    
    # 脚部装备
    {
        "name": "修女·纯白软底鞋",
        "slot": "脚部",
        "price": 115000,
        "effects": {
            "moe_value": 6,  # 增加妹抖值6%
            "spoil_value": 6,  # 增加撒娇值6%
            "tsundere_value": 6,  # 增加傲娇值6%
            "dark_rate": 6,  # 增加黑化率6%
            "contrast_cute": 9,  # 增加反差萌9%
        },
        "description": "纯白色的软底鞋，每一步都踏着神圣的光辉"
    },
    
    # 手持装备
    {
        "name": "修女·十字圣典",
        "slot": "手持",
        "price": 95000,
        "effects": {
            "moe_value": 5,  # 增加妹抖值5%
            "spoil_value": 5,  # 增加撒娇值5%
            "tsundere_value": 5,  # 增加傲娇值5%
            "dark_rate": 5,  # 增加黑化率5%
            "contrast_cute": 15,  # 增加反差萌15%
        },
        "description": "神圣的十字圣典，记载着神的教诲与爱"
    },
    
    # 饰品装备
    {
        "name": "修女·圣光吊坠",
        "slot": "饰品",
        "price": 90000,
        "effects": {
            "moe_value": 6,  # 增加妹抖值6%
            "spoil_value": 6,  # 增加撒娇值6%
            "tsundere_value": 6,  # 增加傲娇值6%
            "dark_rate": 6,  # 增加黑化率6%
            "contrast_cute": 12,  # 增加反差萌12%
        },
        "description": "散发着圣光的十字吊坠，守护纯洁的心灵"
    }
]

# 套装效果配置
COSTUME_SET_BONUS = {
    "兔女郎套装": {
        "pieces": [
            "兔女郎·黑兔耳发箍", "兔女郎·白蕾丝兔耳",  # 头部任选其一
            "兔女郎·亮黑紧身衣", "兔女郎·白兔女郎装",  # 身体任选其一
            "兔女郎·黑蕾丝手套", "兔女郎·白绒毛手套",  # 手部任选其一
            "兔女郎·黑丝袜", "兔女郎·白丝袜",  # 腿部任选其一
            "兔女郎·黑高跟鞋", "兔女郎·白高跟鞋",  # 脚部任选其一
            "兔女郎·胡萝卜", "兔女郎·银色托盘", "兔女郎·魔术手杖",  # 手持任选其一
            "兔女郎·毛茸兔尾巴", "兔女郎·爱心贴纸"  # 饰品任选其一
        ],
        "required_slots": ["头部", "身体", "手部", "腿部", "脚部", "手持", "饰品"],
        "bonus_effects": {
            "moe_value": 50,  # 套装额外增加50%妹抖值
            "spoil_value": 50,  # 套装额外增加50%撒娇值
            "tsundere_value": 30,  # 套装额外增加30%傲娇值
            "dark_rate": 20,  # 套装额外增加20%黑化率
            "contrast_cute": 80,  # 套装额外增加80%反差萌
        },
        "bonus_description": "兔女郎套装效果：全属性大幅提升，魅力爆表！"
    },
    
    "女仆套装": {
        "pieces": [
            "女仆·白褶皱发箍",  # 头部
            "女仆·黑白女仆装",  # 身体
            "女仆·花边手套",  # 手部
            "女仆·白丝袜",  # 腿部
            "女仆·玛丽珍高跟鞋",  # 脚部
            "女仆·银色茶点托盘",  # 手持
            "女仆·萌萌啾饰品"  # 饰品
        ],
        "required_slots": ["头部", "身体", "手部", "腿部", "脚部", "手持", "饰品"],
        "bonus_effects": {
            "moe_value": 60,  # 套装额外增加60%妹抖值
            "spoil_value": 70,  # 套装额外增加70%撒娇值
            "tsundere_value": 20,  # 套装额外增加20%傲娇值
            "dark_rate": 10,  # 套装额外增加10%黑化率
            "contrast_cute": 50,  # 套装额外增加50%反差萌
        },
        "bonus_description": "女仆套装效果：妹抖值与撒娇值大幅提升，可爱到犯规！"
    },
    
    "巫女套装": {
        "pieces": [
            "巫女·流苏丝带发带",  # 头部
            "巫女·红白祈福长袍",  # 身体
            "巫女·宽袖流光手套",  # 手部
            "巫女·甘神红绯袴",  # 腿部
            "巫女·神佑木屐",  # 脚部
            "巫女·御幣祈福法器",  # 手持
            "巫女·铃铛小符饰"  # 饰品
        ],
        "required_slots": ["头部", "身体", "手部", "腿部", "脚部", "手持", "饰品"],
        "bonus_effects": {
            "moe_value": 30,  # 套装额外增加30%妹抖值
            "spoil_value": 20,  # 套装额外增加20%撒娇值
            "tsundere_value": 80,  # 套装额外增加80%傲娇值
            "dark_rate": 60,  # 套装额外增加60%黑化率
            "contrast_cute": 100,  # 套装额外增加100%反差萌
        },
        "bonus_description": "巫女套装效果：傲娇值与反差萌极大提升，神秘魅力无人能敌！"
    },
    
    "魔法少女套装": {
        "pieces": [
            "魔法少女·星光缎带发饰",  # 头部
            "魔法少女·梦幻蓬蓬连衣裙",  # 身体
            "魔法少女·闪光蕾丝手套",  # 手部
            "魔法少女·彩虹渐变长袜",  # 腿部
            "魔法少女·魔力水晶高跟鞋",  # 脚部
            "魔法少女·星尘魔法权杖",  # 手持
            "魔法少女·流光星尘胸饰"  # 饰品
        ],
        "required_slots": ["头部", "身体", "手部", "腿部", "脚部", "手持", "饰品"],
        "bonus_effects": {
            "moe_value": 80,  # 套装额外增加80%妹抖值
            "spoil_value": 40,  # 套装额外增加40%撒娇值
            "tsundere_value": 30,  # 套装额外增加30%傲娇值
            "dark_rate": 15,  # 套装额外增加15%黑化率
            "contrast_cute": 120,  # 套装额外增加120%反差萌
        },
        "bonus_description": "魔法少女套装效果：妹抖值与反差萌爆表提升，梦幻魅力征服一切！"
    },
    
    "小恶魔套装": {
        "pieces": [
            "小恶魔·红黑角发箍",  # 头部
            "小恶魔·俏皮紧身连衣裙",  # 身体
            "小恶魔·镶边指套手套",  # 手部
            "小恶魔·破洞网状长袜",  # 腿部
            "小恶魔·亮漆高跟鞋",  # 脚部
            "小恶魔·火焰小叉", "小恶魔·幽火滴蜡", "小恶魔·男仆口球",  # 手持任选其一
            "小恶魔·尾巴小铃铛"  # 饰品
        ],
        "required_slots": ["头部", "身体", "手部", "腿部", "脚部", "手持", "饰品"],
        "bonus_effects": {
            "moe_value": 20,  # 套装额外增加20%妹抖值
            "spoil_value": 30,  # 套装额外增加30%撒娇值
            "tsundere_value": 70,  # 套装额外增加70%傲娇值
            "dark_rate": 100,  # 套装额外增加100%黑化率
            "contrast_cute": 90,  # 套装额外增加90%反差萌
        },
        "bonus_description": "小恶魔套装效果：黑化率与傲娇值极致提升，诱惑魅力无法抗拒！"
    },
    
    "修女套装": {
        "pieces": [
            "修女·圣洁白纱头巾",  # 头部
            "修女·黑白修女长袍",  # 身体
            "修女·纯白丝绸手套",  # 手部
            "修女·神启长袜",  # 腿部
            "修女·纯白软底鞋",  # 脚部
            "修女·十字圣典",  # 手持
            "修女·圣光吊坠"  # 饰品
        ],
        "required_slots": ["头部", "身体", "手部", "腿部", "脚部", "手持", "饰品"],
        "bonus_effects": {
            "moe_value": 25,  # 套装额外增加25%妹抖值
            "spoil_value": 25,  # 套装额外增加25%撒娇值
            "tsundere_value": 25,  # 套装额外增加25%傲娇值
            "dark_rate": 25,  # 套装额外增加25%黑化率
            "contrast_cute": 35,  # 套装额外增加35%反差萌
        },
        "bonus_description": "修女套装效果：神圣与纯洁的完美平衡，全属性均衡提升！"
    }
}

def get_costume_by_name(costume_name):
    """根据名称获取服装信息"""
    for costume in COSTUME_LIST:
        if costume["name"] == costume_name:
            return costume
    return None

def get_costumes_by_slot(slot):
    """根据部位获取服装列表"""
    return [costume for costume in COSTUME_LIST if costume["slot"] == slot]

def calculate_equipment_effects(equipped_items):
    """计算装备的属性效果"""
    total_effects = {
        "moe_value": 0,
        "spoil_value": 0,
        "tsundere_value": 0,
        "dark_rate": 0,
        "contrast_cute": 0
    }
    
    # 计算单个装备的效果
    for slot, item_name in equipped_items.items():
        if item_name:
            costume = get_costume_by_name(item_name)
            if costume and "effects" in costume:
                for effect, value in costume["effects"].items():
                    total_effects[effect] += value
    
    # 检查套装效果
    set_bonus = check_set_bonus(equipped_items)
    if set_bonus:
        for effect, value in set_bonus["bonus_effects"].items():
            total_effects[effect] += value
    
    return total_effects, set_bonus

def check_set_bonus(equipped_items):
    """检查是否穿齐套装"""
    for set_name, set_info in COSTUME_SET_BONUS.items():
        required_slots = set_info["required_slots"]
        pieces = set_info["pieces"]
        
        # 检查是否所有必需部位都有装备
        equipped_slots = []
        equipped_pieces = []
        
        for slot, item_name in equipped_items.items():
            if item_name and slot in required_slots:
                equipped_slots.append(slot)
                equipped_pieces.append(item_name)
        
        # 检查是否穿齐了所有必需的部位
        if set(equipped_slots) == set(required_slots):
            # 检查装备的物品是否都属于这个套装
            valid_pieces = [piece for piece in equipped_pieces if piece in pieces]
            if len(valid_pieces) == len(required_slots):
                return set_info
    
    return None
