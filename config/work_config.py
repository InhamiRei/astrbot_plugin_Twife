"""工作配置文件 - 所有可用工作的定义

工作配置字段说明：
- id: 工作编号，用于命令中选择工作
- name: 工作名称，显示给用户看的
- pay: 工作报酬，完成工作后获得的金币数量
- duration: 工作时长，单位为小时
- description: 工作描述，详细介绍工作内容
- hunger_cost: 饥饿值消耗，工作会减少老婆的饥饿值
- cleanliness_cost: 清洁值消耗，工作会减少老婆的清洁值
- mood_cost: 心情值消耗，正数表示减少心情，负数表示增加心情
- health_cost: 健康值消耗，工作会减少老婆的健康值
- growth_reward: 成长值奖励，完成工作后老婆获得的成长值
- level_required: 等级要求，老婆需要达到的最低等级
- education_required: 学历要求，对应学历等级：0=无要求，1=小学，2=初中，3=高中，4=大学，5=研究生，6=博士
"""

# 工作列表配置
WORK_LIST = [
    {
        "id": 1,
        "name": "捡废品",
        "pay": 200,
        "duration": 2,
        "description": "在街道上寻找可回收的废品，虽然脏累但是入门工作",
        "hunger_cost": 15,
        "cleanliness_cost": 25,
        "mood_cost": 10,
        "health_cost": 5,
        "growth_reward": 50,
        "level_required": 1,
        "education_required": 0
    },
    {
        "id": 2,
        "name": "群里搬屎",
        "pay": 100,
        "duration": 1,
        "description": "在各种群里搬运表情包和沙雕内容，虽然轻松但略显无聊",
        "hunger_cost": 5,
        "cleanliness_cost": 5,
        "mood_cost": 15,
        "health_cost": 0,
        "growth_reward": 100,
        "level_required": 1,
        "education_required": 0
    },
    {
        "id": 3,
        "name": "发传单",
        "pay": 500,
        "duration": 3,
        "description": "在商业街发放广告传单，需要一定的沟通能力",
        "hunger_cost": 20,
        "cleanliness_cost": 15,
        "mood_cost": 5,
        "health_cost": 8,
        "growth_reward": 150,
        "level_required": 2,
        "education_required": 1
    },
    {
        "id": 4,
        "name": "便利店营业员",
        "pay": 1200,
        "duration": 8,
        "description": "在便利店做收银和理货工作，需要基本算数能力",
        "hunger_cost": 25,
        "cleanliness_cost": 10,
        "mood_cost": 8,
        "health_cost": 10,
        "growth_reward": 200,
        "level_required": 2,
        "education_required": 1
    },
    {
        "id": 5,
        "name": "群里当男娘",
        "pay": 3200,
        "duration": 8,
        "description": "在群里扮演可爱男娘角色，需要一定的表演天赋和脸皮厚度",
        "hunger_cost": 10,
        "cleanliness_cost": 5,
        "mood_cost": 5,
        "health_cost": 0,
        "growth_reward": 250,
        "level_required": 3,
        "education_required": 1
    },
    {
        "id": 6,
        "name": "餐厅服务员",
        "pay": 4000,
        "duration": 8,
        "description": "在餐厅为客人点餐和送餐，需要良好的服务意识",
        "hunger_cost": 30,
        "cleanliness_cost": 20,
        "mood_cost": 12,
        "health_cost": 15,
        "growth_reward": 300,
        "level_required": 3,
        "education_required": 2
    },
    {
        "id": 7,
        "name": "快递配送员",
        "pay": 4500,
        "duration": 8,
        "description": "骑车或步行配送快递包裹，需要体力和路线规划能力",
        "hunger_cost": 40,
        "cleanliness_cost": 25,
        "mood_cost": 10,
        "health_cost": 20,
        "growth_reward": 350,
        "level_required": 4,
        "education_required": 2
    },
    {
        "id": 8,
        "name": "宠物店助理",
        "pay": 5000,
        "duration": 8,
        "description": "帮助照顾宠物店的小动物，需要爱心和耐心",
        "hunger_cost": 20,
        "cleanliness_cost": 20,
        "mood_cost": -5,
        "health_cost": 8,
        "growth_reward": 400,
        "level_required": 5,
        "education_required": 2
    },
    {
        "id": 9,
        "name": "游戏账号代练",
        "pay": 5500,
        "duration": 8,
        "description": "帮土豪玩家刷等级，手速和肝要够硬",
        "hunger_cost": 20,
        "cleanliness_cost": 5,
        "mood_cost": -8,
        "health_cost": 5,
        "growth_reward": 450,
        "level_required": 5,
        "education_required": 3
    },
    {
        "id": 10,
        "name": "女仆咖啡厅服务员",
        "pay": 8888,
        "duration": 8,
        "description": "在女仆咖啡厅为客人服务，需要较高的颜值和服务技巧",
        "hunger_cost": 25,
        "cleanliness_cost": 15,
        "mood_cost": 5,
        "health_cost": 10,
        "growth_reward": 500,
        "level_required": 6,
        "education_required": 3
    },
    {
        "id": 11,
        "name": "弹幕审核官",
        "pay": 9000,
        "duration": 8,
        "description": "日常工作就是在屏幕前刷‘2333’，需要强大心理承受力",
        "hunger_cost": 15,
        "cleanliness_cost": 5,
        "mood_cost": -12,
        "health_cost": 5,
        "growth_reward": 1000,
        "level_required": 7,
        "education_required": 4
    },
    {
        "id": 12,
        "name": "鉴黄师",
        "pay": 12000,
        "duration": 8,
        "description": "传说中的神秘职业，看片看到怀疑人生，需要极强的心理素质",
        "hunger_cost": 20,
        "cleanliness_cost": 5,
        "mood_cost": -8,
        "health_cost": 8,
        "growth_reward": 1500,
        "level_required": 8,
        "education_required": 5
    },
    {
        "id": 13,
        "name": "网红吃播助理",
        "pay": 12500,
        "duration": 8,
        "description": "负责给吃播补菜、擦嘴和打光，比吃的人还累",
        "hunger_cost": 30,
        "cleanliness_cost": 12,
        "mood_cost": -3,
        "health_cost": 15,
        "growth_reward": 2000,
        "level_required": 10,
        "education_required": 5
    },
    {
        "id": 14,
        "name": "梦话记录员",
        "pay": 13000,
        "duration": 8,
        "description": "每天负责监听别人梦话，整理成日报，需要极强的忍笑能力",
        "hunger_cost": 20,
        "cleanliness_cost": 8,
        "mood_cost": 5,
        "health_cost": 10,
        "growth_reward": 3000,
        "level_required": 15,
        "education_required": 6
    },
    {
        "id": 15,
        "name": "尸体化妆师",
        "pay": 20000,
        "duration": 12,
        "description": "让死去的人也能像生前一样好看，胆量和技术都要过硬",
        "hunger_cost": 25,
        "cleanliness_cost": 5,
        "mood_cost": -10,
        "health_cost": 15,
        "growth_reward": 5000,
        "level_required": 20,
        "education_required": 6
    },
    {
        "id": 16,
        "name": "暴雪帝国史官",
        "pay": 50000,
        "duration": 8,
        "description": "记录暴雪帝国的编年史，是个神圣的职业",
        "hunger_cost": 100,
        "cleanliness_cost": 50,
        "mood_cost": -50,
        "health_cost": 50,
        "growth_reward": 10000,
        "level_required": 30,
        "education_required": 7
    }
]
