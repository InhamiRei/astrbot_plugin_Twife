"""旅行系统配置文件"""

# 旅行地点列表
TRAVEL_DESTINATIONS = {
    1: {
        "country": "中国",
        "city": "北京", 
        "description": "中国首都，政治与文化中心",
        "journey": "清晨到天安门广场观看升旗仪式，早餐来一碗热豆汁配焦圈感受老北京味道，随后进入故宫参观午门、太和殿和珍宝馆，欣赏皇家建筑的宏伟与典藏的珍宝，午餐在王府井全聚德品尝正宗烤鸭，下午骑自行车穿梭胡同参观四合院，再到什刹海乘船，湖面波光粼粼，远处还能听见票友唱京剧，傍晚登景山公园俯瞰故宫金瓦在余晖中熠熠生辉，晚上簋街大快朵颐小龙虾、爆肚与烤串，体验热闹的夜北京。",
        "duration": "10h",
        "cost": 60000,
        "charm_fragments": (50, 70),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 50, "cleanliness": 50, "mood": 100, "health": 50, "growth": 100},
        "artifacts": ["故宫龙凤金簪", "天安门城砖", "景山万春亭瓦当", "什刹海古玉佩", "胡同门环铜饰"]
    },
    2: {
        "country": "中国",
        "city": "杭州",
        "description": "\"人间天堂\"，以西湖闻名",
        "journey": "清晨在西湖边晨跑或散步，雾气弥漫的湖面映衬着断桥残雪的美景，随后乘画舫游览西湖，沿途经过三潭印月和雷峰塔，上岸后前往灵隐寺烧香祈福，午餐到楼外楼品尝龙井虾仁、西湖醋鱼和东坡肉，下午在苏堤春晓漫步或骑行环湖，再到龙井村体验采茶与品茶，傍晚去九溪烟树走走感受溪水潺潺和满山绿意，夜晚则前往河坊街品尝定胜糕、梅菜扣肉等小吃，并顺手买丝绸或龙井茶作为伴手礼。",
        "duration": "8h",
        "cost": 30000,
        "charm_fragments": (30, 50),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 50, "cleanliness": 50, "mood": 100, "health": 50, "growth": 100},
        "artifacts": ["宋代龙井茶具", "雷峰塔古砖", "灵隐寺唐代佛珠", "苏堤宋代石碑", "南宋官窑瓷片"]
    },
    3: {
        "country": "中国",
        "city": "云南",
        "description": "多民族聚居，四季如春",
        "journey": "清晨在丽江古城的青石板路上漫步，看纳西小院木雕窗棂，吃一碗热腾腾的米线，上午出发前往玉龙雪山，乘索道登上冰川公园，感受高原雪域的壮丽风光，午餐在白沙古镇品尝腊排骨火锅，下午前往大理洱海，骑行环湖拍照，远处苍山如黛，湖水碧波荡漾，傍晚在洱海边的小酒馆里一边听民谣一边看落日余晖洒在水面，晚上返回丽江参加纳西古乐演出或篝火晚会，与少数民族载歌载舞共度热闹时光。",
        "duration": "8h",
        "cost": 40000,
        "charm_fragments": (30, 60),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 50, "cleanliness": 50, "mood": 100, "health": 50, "growth": 100},
        "artifacts": ["纳西东巴古经卷", "明代玉龙雪山石碑", "大理国古钱币", "南诏国白族银器", "丽江木府古木雕"]
    },
    4: {
        "country": "中国",
        "city": "西安",
        "description": "古都十三朝遗址，历史文化底蕴深厚",
        "journey": "早晨出发前往临潼参观兵马俑，数千兵马俑整齐列阵气势恢宏，随后游览华清池感受唐玄宗与杨贵妃的凄美故事，午餐在回民街大快朵颐羊肉泡馍、肉夹馍与冰峰汽水，下午登上古城墙骑单车一圈，俯瞰古城街景，傍晚前往大雁塔北广场观看壮观的音乐喷泉，夜晚则到德福巷酒吧街听live或者再来一碗辣香四溢的biangbiang面结束美好的一天。",
        "duration": "8h",
        "cost": 40000,
        "charm_fragments": (30, 60),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 50, "cleanliness": 50, "mood": 100, "health": 50, "growth": 100},
        "artifacts": ["兵马俑陶片", "华清池唐代瓦当", "大雁塔经文拓片", "西安城墙古砖", "唐朝宫廷金钗"]
    },
    5: {
        "country": "日本",
        "city": "大阪",
        "description": "商业繁华，美食之都",
        "journey": "清晨到大阪城公园拍摄天守阁，登高远眺城市景色，上午去黑门市场大快朵颐，品尝新鲜生蚝、寿司、和牛串与章鱼小丸子，午餐在心斋桥附近拉面店享用地道豚骨拉面，下午到环球影城畅玩哈利波特园区和过山车，傍晚回到道顿堀，看著名的格力高广告牌灯光亮起，夜晚一边乘坐河上游船欣赏水上夜景，一边边走边吃大阪烧和串炸，感受城市的繁华与美味。",
        "duration": "8h",
        "cost": 50000,
        "charm_fragments": (30, 70),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 100, "cleanliness": 20, "mood": 50, "health": 20, "growth": 100},
        "artifacts": ["大阪城天守阁瓦片", "道顿堀江户时代商标", "黑门市场明治铜秤", "心斋桥古石灯笼", "丰臣家纹章瓦当"]
    },
    6: {
        "country": "日本",
        "city": "东京",
        "description": "日本首都，国际大都市",
        "journey": "早晨到浅草雷门拍照，在浅草寺求签并在仲见世街尝人形烧，上午前往上野公园散步参观博物馆或动物园，再去秋叶原购物街体验二次元文化和扭蛋机，午餐品尝拉面或回转寿司，下午去银座逛百货公司然后到涩谷忠犬八公像前合影并穿越世界最繁忙的十字路口，傍晚登涩谷Sky观景台俯瞰夕阳下的东京塔和远处的富士山，夜晚前往新宿歌舞伎町体验夜生活，在居酒屋享用烤鸡串配冰镇啤酒，最后在便利店买草莓牛奶和甜点带回酒店。",
        "duration": "10h",
        "cost": 60000,
        "charm_fragments": (50, 80),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 100, "cleanliness": 20, "mood": 50, "health": 20, "growth": 100},
        "artifacts": ["浅草寺江户古钟", "江户城石垣残片", "明治银座煤油灯", "德川家康印章复制品", "上野宽永寺古瓦"]
    },
    7: {
        "country": "缅甸",
        "city": "仰光",
        "description": "最大城市，有著名的瑞光大金塔",
        "journey": "清晨到瑞光大金塔朝拜祈福，阳光照耀下的佛塔金光灿烂，上午前往仰光殖民风格的老城区参观百年邮局和旧英式建筑，中途停在茶馆喝一杯缅甸奶茶，午餐享用咖喱饭和发酵茶叶沙拉，下午逛昂山市场挑选玉石和手工艺品，傍晚到茵雅湖畔散步看日落倒映湖面，夜晚去夜市吃烤鱼、炒米粉和各种地道小吃，感受仰光的市井烟火与独特氛围。",
        "duration": "5h",
        "cost": 1000,
        "charm_fragments": (0, 0),
        "blackening_fragments": (20, 50),
        "special_reward": "历史文物",
        "effects": {"hunger": 20, "cleanliness": 20, "mood": 20, "health": 20, "growth": 100},
        "artifacts": ["瑞光大金塔金叶", "昂山市场翡翠", "茵雅湖古玉", "殖民地邮票", "缅甸佛像残片"]
    },
    8: {
        "country": "埃及",
        "city": "开罗",
        "description": "世界古文明，金字塔之城",
        "journey": "清晨前往吉萨金字塔群观看日出照射在胡夫金字塔上的壮观景象，与神秘的狮身人面像合影留念，上午参观埃及博物馆欣赏图坦卡蒙法老的黄金面具和无数古埃及文物，午餐品尝传统埃及料理如烤羊肉和扁豆汤，下午漫步老开罗的科普特区参观悬空教堂和本-埃兹拉犹太会堂，傍晚登上萨拉丁城堡俯瞰开罗全景和远处的尼罗河，夜晚在尼罗河上乘坐传统帆船观赏两岸灯火，品尝阿拉伯水烟和甜茶，感受千年古都的神秘魅力。",
        "duration": "10h",
        "cost": 60000,
        "charm_fragments": (50, 80),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 100, "cleanliness": 20, "mood": 100, "health": 20, "growth": 150},
        "artifacts": ["法老陵墓莎草纸", "古埃及圣甲虫护符", "古埃及象形文字石板", "尼罗河神庙雕像", "图坦卡蒙复制品"]
    },
    9: {
        "country": "阿联酋",
        "city": "迪拜",
        "description": "中东金融中心，奢华与摩天大楼之城",
        "journey": "清晨登上世界最高建筑哈利法塔148层观景台俯瞰迪拜全貌和波斯湾日出美景，上午前往迪拜购物中心逛世界最大的购物天堂并观赏室内瀑布，中午在Armani酒店享受奢华午餐，下午前往棕榈岛亚特兰蒂斯酒店体验水上乐园和与海豚互动，傍晚乘坐豪华游艇出海游览迪拜海岸线和帆船酒店，夜晚在迪拜喷泉观赏震撼的音乐喷泉表演，最后前往黄金街购买珠宝首饰或在香料街感受传统阿拉伯风情，体验沙漠与现代化的完美融合。",
        "duration": "10h",
        "cost": 100000,
        "charm_fragments": (50, 120),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 100, "cleanliness": 20, "mood": 100, "health": 20, "growth": 150},
        "artifacts": ["古代阿拉伯商路印章", "古代阿拉伯书法手稿", "贝都因部落银币", "香料之路古地图", "古代阿拉伯星盘"]
    },
    10: {
        "country": "传说",
        "city": "亚特兰蒂斯",
        "description": "沉没的海底文明，水晶科技与神秘并存",
        "journey": "清晨穿上深海潜水装备，在神秘的传送门中下潜至万米海底，眼前浮现出金碧辉煌的亚特兰蒂斯城市废墟，水晶塔在深海中发出柔和的蓝光，上午探索海神波塞冬的神殿，观赏古老的水晶科技装置仍在缓缓运转，午餐享用海洋精灵制作的深海珍馐，品尝从未见过的奇异海草和发光贝类，下午在失落的图书馆中研读古老的亚特兰蒂斯文明记录，傍晚乘坐水晶潜艇游览整座海底城市，夜晚参加海族的盛大庆典，与美人鱼一同在水晶宫殿中舞蹈，感受这个传说文明的神奇魅力与无尽智慧。",
        "duration": "10h",
        "cost": 500000,
        "charm_fragments": (200, 600),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 999, "cleanliness": 999, "mood": 999, "health": 999, "growth": 200},
        "artifacts": ["亚特兰蒂斯水晶核心", "海神波塞冬三叉戟碎片", "深海智慧石板", "远古水晶能量球", "亚特兰蒂斯王冠残片"]
    }
}

# 纪念品伴手礼配置（按城市分类）
SOUVENIRS = {
    # 北京纪念品
    "北京": [
        {"name": "北京烤鸭真空装", "effects": {"hunger": 180, "mood": 120}, "description": "正宗北京烤鸭，回味无穷"},
        {"name": "故宫文创胶带", "effects": {"mood": 100, "health": 5}, "description": "故宫联名文创，颜值超高"},
        {"name": "景泰蓝花瓶", "effects": {"mood": 200, "cleanliness": 10}, "description": "精美的景泰蓝工艺品，可大幅提升心情"},
        {"name": "熊猫玩偶", "effects": {"mood": 220, "health": 15}, "description": "可爱的熊猫公仔，心情大好"},
        {"name": "中国结挂饰", "effects": {"mood": 120, "health": 8}, "description": "传统手工编织，寓意吉祥"},
        {"name": "麻将钥匙扣", "effects": {"mood": 130, "health": 10}, "description": "迷你麻将，手气加成"},
        {"name": "文房四宝套装", "effects": {"mood": 100, "health": 15}, "description": "笔墨纸砚，书香气质"},
        {"name": "藏式转经筒", "effects": {"mood": 120, "health": 20}, "description": "佛教法器，内心平静"},
    ],
    
    # 杭州纪念品
    "杭州": [
        {"name": "龙井茶叶礼盒", "effects": {"health": 100, "mood": 100}, "description": "正宗西湖龙井，有益身心健康"},
        {"name": "西湖龙井护手霜", "effects": {"cleanliness": 90, "mood": 80}, "description": "茶香护肌，温润如玉"},
        {"name": "杭州丝绸眼罩", "effects": {"health": 150, "cleanliness": 80}, "description": "真丝眼罩，助眠神器"},
        {"name": "丝绸围巾", "effects": {"mood": 150, "cleanliness": 80}, "description": "柔滑的真丝围巾，增加魅力"},
        {"name": "青花瓷茶具", "effects": {"mood": 180, "health": 60}, "description": "典雅的青花瓷，提升气质"},
        {"name": "古典扇子", "effects": {"mood": 100, "cleanliness": 80}, "description": "精致折扇，古典美人必备"},
        {"name": "苏州刺绣手帕", "effects": {"cleanliness": 120, "mood": 70}, "description": "精美刺绣，工艺精湛"},
        {"name": "竹制茶杯", "effects": {"health": 80, "mood": 100}, "description": "竹香淡雅，禅意生活"},
    ],
    
    # 云南纪念品
    "云南": [
        {"name": "云南鲜花饼", "effects": {"hunger": 100, "mood": 140}, "description": "玫瑰花香，甜蜜浪漫"},
        {"name": "普洱茶饼", "effects": {"health": 150, "mood": 90}, "description": "陈年普洱，越品越香"},
        {"name": "岭南荔枝干", "effects": {"hunger": 90, "mood": 120}, "description": "甜蜜荔枝，南国风情"},
        {"name": "民族风银饰", "effects": {"mood": 140, "cleanliness": 100}, "description": "云南银饰，民族风情"},
        {"name": "玉龙雪山水晶", "effects": {"health": 120, "mood": 100}, "description": "雪山水晶，纯净透明"},
        {"name": "大理扎染围巾", "effects": {"mood": 110, "cleanliness": 90}, "description": "传统扎染，艺术气息"},
        {"name": "丽江古城木雕", "effects": {"mood": 130, "health": 100}, "description": "纳西木雕，古城记忆"},
        {"name": "云南过桥米线调料", "effects": {"hunger": 160, "mood": 80}, "description": "正宗调料，家的味道"},
    ],
    
    # 西安纪念品
    "西安": [
        {"name": "兵马俑巧克力", "effects": {"hunger": 120, "mood": 150}, "description": "创意巧克力，萌翻了"},
        {"name": "陕西肉夹馍调料包", "effects": {"hunger": 160, "mood": 110}, "description": "正宗调料，家乡味道"},
        {"name": "唐装旗袍", "effects": {"mood": 120, "cleanliness": 80}, "description": "传统服饰，优雅迷人"},
        {"name": "大雁塔香囊", "effects": {"mood": 140, "health": 100}, "description": "佛塔香囊，宁神静气"},
        {"name": "西安城墙砖茶", "effects": {"health": 120, "mood": 90}, "description": "古城茶砖，厚重历史"},
        {"name": "大雁塔模型", "effects": {"mood": 180, "health": 80}, "description": "古塔模型，智慧之光"},
        {"name": "陕西剪纸艺术", "effects": {"mood": 120, "cleanliness": 100}, "description": "民间剪纸，传统技艺"},
        {"name": "凉皮调料包", "effects": {"hunger": 140, "mood": 90}, "description": "西安凉皮，清爽解腻"},
    ],
    
    # 大阪纪念品
    "大阪": [
        {"name": "章鱼小丸子模型", "effects": {"mood": 180, "health": 100}, "description": "大阪特色，超萌章鱼烧"},
        {"name": "大阪烧调料包", "effects": {"hunger": 160, "mood": 120}, "description": "正宗大阪烧，家庭制作"},
        {"name": "心斋桥购物袋", "effects": {"mood": 120, "cleanliness": 100}, "description": "时尚购物袋，潮流标志"},
        {"name": "道顿堀霓虹灯模型", "effects": {"mood": 140, "health": 110}, "description": "繁华夜景，霓虹闪烁"},
        {"name": "大阪城钥匙扣", "effects": {"mood": 100, "health": 90}, "description": "古城记忆，历史传承"},
        {"name": "和牛肉干", "effects": {"hunger": 150, "health": 120}, "description": "顶级和牛，入口即化"},
        {"name": "关西腔学习手册", "effects": {"mood": 140, "health": 100}, "description": "关西方言，幽默风趣"},
        {"name": "大阪环球影城纪念品", "effects": {"mood": 200, "health": 150}, "description": "影城特色，刺激回忆"},
    ],
    
    # 东京纪念品
    "东京": [
        {"name": "哆啦A梦手办", "effects": {"mood": 220, "health": 100}, "description": "蓝胖子手办，童心满满"},
        {"name": "浅草寺御守", "effects": {"mood": 120, "health": 100}, "description": "祈福御守，神明庇佑"},
        {"name": "秋叶原扭蛋", "effects": {"mood": 160, "health": 100}, "description": "限定扭蛋，开盲盒的快乐"},
        {"name": "东京香蕉糕点", "effects": {"hunger": 110, "mood": 130}, "description": "东京特产，香甜可口"},
        {"name": "高达模型", "effects": {"mood": 180, "health": 80}, "description": "机甲模型，男人的浪漫"},
        {"name": "柴犬玩偶", "effects": {"mood": 200, "health": 100}, "description": "柴犬玩偶，忠诚可爱"},
        {"name": "动漫周边徽章", "effects": {"mood": 150, "health": 120}, "description": "动漫徽章，二次元之魂"},
        {"name": "涩谷十字路口模型", "effects": {"mood": 140, "health": 110}, "description": "繁忙十字路口，都市印象"},
    ],
    
    # 仰光纪念品
    "仰光": [
        {"name": "翡翠手镯", "effects": {"mood": 150, "health": 80}, "description": "缅甸翡翠，温润如玉"},
        {"name": "瑞光大金塔纪念品", "effects": {"mood": 150, "health": 120}, "description": "圣地纪念品，灵性满满"},
        {"name": "缅甸红宝石", "effects": {"mood": 200, "health": 100}, "description": "珍贵红宝石，价值连城"},
        {"name": "佛像挂件", "effects": {"mood": 100, "health": 120}, "description": "佛教护身符，内心安宁"},
        {"name": "茵雅湖珍珠", "effects": {"cleanliness": 140, "mood": 100}, "description": "淡水珍珠，温润光泽"},
        {"name": "缅甸特色面条", "effects": {"hunger": 160, "mood": 80}, "description": "椰奶面条，异国美味"},
        {"name": "传统龙基服饰", "effects": {"mood": 120, "cleanliness": 90}, "description": "缅甸传统服装，异域风情"},
        {"name": "仰光街头小食", "effects": {"hunger": 140, "mood": 80}, "description": "街头美食，冒险味蕾"},
    ],
    
    # 开罗纪念品
    "开罗": [
        {"name": "法老黄金项链", "effects": {"mood": 180, "cleanliness": 50}, "description": "古埃及风格，尊贵典雅"},
        {"name": "金字塔水晶球", "effects": {"mood": 160, "health": 80}, "description": "神秘水晶，蕴含古老智慧"},
        {"name": "尼罗河莎草纸画", "effects": {"mood": 140, "health": 60}, "description": "手工绘制，记录古代传说"},
        {"name": "埃及艳后化妆盒", "effects": {"cleanliness": 150, "mood": 120}, "description": "精美化妆盒，重现古典美丽"},
        {"name": "圣甲虫护身符", "effects": {"health": 100, "mood": 90}, "description": "古埃及护符，带来好运"},
        {"name": "法老面具复制品", "effects": {"mood": 200, "cleanliness": 40}, "description": "图坦卡蒙面具，威严神圣"},
        {"name": "阿拉伯香料盒", "effects": {"mood": 100, "health": 120}, "description": "传统香料，异域芬芳"},
        {"name": "沙漠玫瑰水", "effects": {"cleanliness": 120, "mood": 110}, "description": "沙漠之花，清香怡人"},
    ],
    
    # 迪拜纪念品
    "迪拜": [
        {"name": "黄金手镯", "effects": {"mood": 220, "cleanliness": 60}, "description": "纯金制品，奢华尊贵"},
        {"name": "哈利法塔模型", "effects": {"mood": 180, "health": 80}, "description": "世界最高塔，摩天奇迹"},
        {"name": "阿拉伯香水", "effects": {"cleanliness": 180, "mood": 140}, "description": "中东香氛，神秘诱人"},
        {"name": "骆驼毛围巾", "effects": {"cleanliness": 100, "mood": 120}, "description": "沙漠之舟，温暖柔软"},
        {"name": "波斯地毯", "effects": {"mood": 200, "health": 100}, "description": "手工编织，艺术珍品"},
        {"name": "椰枣礼盒", "effects": {"hunger": 150, "mood": 100}, "description": "沙漠甘露，营养丰富"},
        {"name": "帆船酒店纪念品", "effects": {"mood": 190, "health": 90}, "description": "七星奢华，传奇酒店"},
        {"name": "沙画瓶", "effects": {"mood": 130, "cleanliness": 80}, "description": "彩色沙画，沙漠艺术"},
    ],
    
    # 亚特兰蒂斯纪念品
    "亚特兰蒂斯": [
        {"name": "水晶项链", "effects": {"mood": 300, "cleanliness": 150}, "description": "深海水晶制成，散发神秘蓝光"},
        {"name": "海神护身符", "effects": {"health": 200, "mood": 180}, "description": "海神波塞冬的祝福，庇护航海平安"},
        {"name": "深海珍珠", "effects": {"cleanliness": 200, "mood": 150}, "description": "万年深海孕育，价值连城"},
        {"name": "亚特兰蒂斯音乐盒", "effects": {"mood": 250, "health": 120}, "description": "播放远古海族乐曲，令人心旷神怡"},
        {"name": "智慧之书", "effects": {"mood": 200, "health": 180}, "description": "记录失落文明的智慧，开启心灵"},
        {"name": "能量水晶", "effects": {"health": 250, "mood": 100}, "description": "蕴含古老能量，滋养身心"},
        {"name": "海洋精华", "effects": {"cleanliness": 180, "health": 150}, "description": "纯净的海洋精华，美容养颜"},
        {"name": "神话雕像", "effects": {"mood": 280, "health": 100}, "description": "海神与美人鱼的传说雕像"},
    ]
}

# 博物馆配置
MUSEUMS = {
    "中国": {
        "name": "中华文明博物馆",
        "description": "收藏中华五千年文明瑰宝的殿堂",
        "artifacts_accepted": [
            "故宫龙凤金簪", "天安门城砖", "景山万春亭瓦当", "什刹海古玉佩", "胡同门环铜饰",
            "宋代龙井茶具", "雷峰塔古砖", "灵隐寺唐代佛珠", "苏堤宋代石碑", "南宋官窑瓷片",
            "纳西东巴古经卷", "明代玉龙雪山石碑", "大理国古钱币", "南诏国白族银器", "丽江木府古木雕",
            "兵马俑陶片", "华清池唐代瓦当", "大雁塔经文拓片", "西安城墙古砖", "唐朝宫廷金钗"
        ],
        "donation_rewards": {
            "coins": 10000,
            "experience": 2000
        }
    },
    "日本": {
        "name": "日本国立历史博物馆",
        "description": "展示日本从古代到现代历史文化的博物馆",
        "artifacts_accepted": [
            "大阪城天守阁瓦片", "道顿堀江户时代商标", "黑门市场明治铜秤", "心斋桥古石灯笼", "丰臣家纹章瓦当",
            "浅草寺江户古钟", "江户城石垣残片", "明治银座煤油灯", "德川家康印章复制品", "上野宽永寺古瓦"
        ],
        "donation_rewards": {
            "coins": 10000,
            "experience": 2000
        }
    },
    "缅甸": {
        "name": "缅甸国家博物馆",
        "description": "保存缅甸古代文明和佛教文化的圣地",
        "artifacts_accepted": [
            "瑞光大金塔金叶", "昂山市场翡翠", "茵雅湖古玉", "殖民地邮票", "缅甸佛像残片"
        ],
        "donation_rewards": {
            "coins": 10000,
            "experience": 2000
        }
    },
    "埃及": {
        "name": "开罗埃及博物馆",
        "description": "收藏世界最丰富的古埃及文明珍宝",
        "artifacts_accepted": [
            "法老陵墓莎草纸", "古埃及圣甲虫护符", "古埃及象形文字石板", "尼罗河神庙雕像", "图坦卡蒙复制品"
        ],
        "donation_rewards": {
            "coins": 10000,
            "experience": 2000
        }
    },
    "阿联酋": {
        "name": "迪拜未来博物馆",
        "description": "展示阿拉伯传统文化与现代科技融合的博物馆",
        "artifacts_accepted": [
            "古代阿拉伯商路印章", "古代阿拉伯书法手稿", "贝都因部落银币", "香料之路古地图", "古代阿拉伯星盘"
        ],
        "donation_rewards": {
            "coins": 10000,
            "experience": 2000
        }
    },
    "传说": {
        "name": "神话传说博物馆",
        "description": "收藏失落文明与神话传说文物的神秘殿堂",
        "artifacts_accepted": [
            "亚特兰蒂斯水晶核心", "海神波塞冬三叉戟碎片", "深海智慧石板", "远古水晶能量球", "亚特兰蒂斯王冠残片"
        ],
        "donation_rewards": {
            "coins": 50000,
            "experience": 10000
        }
    }
}

# 碎片转换配置
FRAGMENT_CONVERSION = {
    "charm_fragments": {
        "name": "反差萌碎片",
        "required_amount": 100,
        "effect": {"charm_contrast": 1},
        "description": "集齐100个反差萌碎片可增加1点反差萌属性"
    },
    "blackening_fragments": {
        "name": "黑化率碎片", 
        "required_amount": 100,
        "effect": {"blackening": 1},
        "description": "集齐100个黑化率碎片可增加1点黑化率属性"
    }
}
