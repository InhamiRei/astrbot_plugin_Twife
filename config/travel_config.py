"""旅行系统配置文件"""

# 旅行地点列表
TRAVEL_DESTINATIONS = {
    # === 中国城市 ===
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
        "country": "中国",
        "city": "上海",
        "description": "中国最大城市，金融中心、国际化大都市",
        "journey": "清晨在外滩观看黄浦江日出，欣赏万国建筑群的壮美轮廓，上午漫步南京路步行街购物体验繁华都市，中途到豫园感受江南古典园林之美，午餐品尝生煎包、小笼包与本帮菜，下午登上环球金融中心观光厅俯瞰浦江两岸，再到新天地体验石库门里弄文化，傍晚乘坐黄浦江游轮观赏两岸灯火璀璨，夜晚在田子坊艺术街区品味咖啡和创意小店，感受东方明珠的现代魅力与历史底蕴。",
        "duration": "8h",
        "cost": 60000,
        "charm_fragments": (30, 80),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 50, "cleanliness": 50, "mood": 100, "health": 50, "growth": 100},
        "artifacts": ["近代海关大楼铜钟", "石库门雕花窗棂", "外滩万国建筑群石刻", "豫园明代园林假山石", "上海古城墙石砖"]
    },
    6: {
        "country": "中国",
        "city": "深圳",
        "description": "改革开放前沿，科技创新中心",
        "journey": "清晨登莲花山俯瞰深圳市容，感受改革开放的伟大成就，上午参观深圳博物馆了解特区发展历程，中途到世界之窗体验微缩世界奇观，午餐享用潮汕牛肉火锅与粤式茶点，下午游览大梅沙海滨公园感受南国海风，再到华强北电子市场体验科技购物乐趣，傍晚漫步深圳湾公园观赏跨海大桥夕阳，夜晚在蛇口海上世界享受海鲜大餐，感受这座年轻城市的活力与创新精神。",
        "duration": "8h",
        "cost": 60000,
        "charm_fragments": (30, 80),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 50, "cleanliness": 50, "mood": 100, "health": 50, "growth": 100},
        "artifacts": ["南海古渔村石碑", "南头古城明代城砖", "客家围屋古构件", "古代盐田晒盐石槽", "蛇口炮台清代石刻"]
    },
    7: {
        "country": "中国",
        "city": "重庆",
        "description": "山城、火锅之都，长江上游经济中心",
        "journey": "清晨在洪崖洞看嘉陵江晨雾缭绕，体验立体山城的独特魅力，上午乘坐长江索道俯瞰两江交汇壮观景象，再到磁器口古镇品尝传统小吃，午餐享用正宗重庆火锅与江湖菜，下午游览解放碑步行街购物，再到李子坝轻轨站感受穿楼而过的神奇，傍晚登南山一棵树观景台欣赏山城夜景，夜晚在朝天门码头乘船夜游两江，品尝毛血旺、口水鸡等地道美食，感受火辣重庆的热情与豪爽。",
        "duration": "10h",
        "cost": 50000,
        "charm_fragments": (50, 70),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 50, "cleanliness": 50, "mood": 100, "health": 50, "growth": 100},
        "artifacts": ["巴渝古国青铜器", "古代巴王国铜戈", "古代纤夫石刻", "朝天门古码头石阶", "山城古寨门楣"]
    },
    8: {
        "country": "中国",
        "city": "成都",
        "description": "大熊猫、宽窄巷子、九寨沟入口，美食与休闲之都",
        "journey": "清晨到成都大熊猫繁育研究基地看萌萌哒的国宝，上午漫步宽窄巷子体验老成都的悠闲生活，品尝盖碗茶和传统小吃，中途到武侯祠缅怀三国历史，午餐享用担担面、麻婆豆腐、回锅肉等川菜精华，下午游览锦里感受三国文化街区氛围，再到人民公园体验掏耳朵的巴适生活，傍晚到春熙路购物逛街，夜晚在九眼桥酒吧街感受成都夜生活，品尝串串香、兔头等地道美食，体验天府之国的休闲与美食文化。",
        "duration": "10h",
        "cost": 60000,
        "charm_fragments": (50, 80),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 50, "cleanliness": 50, "mood": 100, "health": 50, "growth": 100},
        "artifacts": ["蜀汉丞相印章", "三星堆青铜器残片", "唐代杜甫手稿", "武侯祠古碑刻", "金沙遗址太阳神鸟"]
    },
    9: {
        "country": "中国",
        "city": "拉萨",
        "description": "西藏首府，布达拉宫所在地，宗教与民族特色鲜明",
        "journey": "清晨在布达拉宫广场看第一缕阳光照亮雪域圣殿，感受藏传佛教的神圣庄严，上午参观大昭寺转经朝拜，体验虔诚信仰的力量，中途在八廓街购买藏式手工艺品，午餐品尝酥油茶、糌粑、牦牛肉等藏族美食，下午游览色拉寺观看辩经活动，再到罗布林卡感受达赖喇嘛夏宫的园林之美，傍晚到药王山观景台拍摄布达拉宫最美角度，夜晚在藏式茶馆听藏族歌舞，品尝青稞酒，感受雪域高原的神秘与纯净。",
        "duration": "10h",
        "cost": 80000,
        "charm_fragments": (50, 100),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 50, "cleanliness": 50, "mood": 100, "health": 50, "growth": 100},
        "artifacts": ["唐代文成公主佛像", "布达拉宫金顶瓦片", "吐蕃王朝印章", "大昭寺千年香炉", "藏王松赞干布佛龛"]
    },
    10: {
        "country": "中国",
        "city": "哈尔滨",
        "description": "\"冰城\"，以冰雪大世界和中俄文化交融闻名",
        "journey": "清晨漫步中央大街感受欧式建筑风情，在面包店品尝俄式列巴和红肠，上午参观圣索菲亚大教堂欣赏拜占庭式建筑之美，中途到老道外中华巴洛克街区体验中西合璧文化，午餐享用东北菜如锅包肉、杀猪菜，下午游览太阳岛雪博会或冰雪大世界（冬季），夏季则到松花江畔避暑，傍晚在防洪纪念塔观赏松花江夕阳，夜晚在中央大街品尝马迭尔冰棍，感受冰城独特的中俄文化交融魅力。",
        "duration": "10h",
        "cost": 70000,
        "charm_fragments": (50, 90),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 50, "cleanliness": 50, "mood": 100, "health": 50, "growth": 100},
        "artifacts": ["黑龙江古代渔猎铜器", "俄式建筑装饰浮雕", "清代驿站马铃", "圣索菲亚教堂钟楼铜钟", "松花江古代石刻"]
    },
    11: {
        "country": "中国",
        "city": "青岛",
        "description": "海滨城市，啤酒之都，德式建筑与海洋文化",
        "journey": "清晨在栈桥观看海上日出，感受青岛湾的清新海风，上午漫步八大关欣赏万国建筑博览，体验\"红瓦绿树、碧海蓝天\"的城市风貌，中途参观青岛啤酒博物馆了解百年啤酒文化，午餐享用海鲜大餐如爬虾、蛤蜊、海蛎子，下午登崂山感受道教名山的仙境之美，再到小鱼山公园俯瞰青岛全貌，傍晚在五四广场观赏\"五月的风\"雕塑与奥帆中心，夜晚在台东夜市品尝烧烤配青岛啤酒，感受啤酒之城的浪漫与活力。",
        "duration": "10h",
        "cost": 50000,
        "charm_fragments": (50, 70),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 50, "cleanliness": 50, "mood": 100, "health": 50, "growth": 100},
        "artifacts": ["古代即墨城石雕", "明代胶州湾海防印", "古代崂山道观钟", "古代崂山石刻", "八大关别墅铜门牌"]
    },
    12: {
        "country": "中国",
        "city": "敦煌",
        "description": "莫高窟、鸣沙山月牙泉，丝绸之路重镇",
        "journey": "清晨参观莫高窟，在专业讲解下欣赏千年佛教艺术瑰宝，感受丝绸之路的文化交融，上午游览鸣沙山，骑骆驼穿越沙漠体验古代商队生活，在月牙泉畔感受沙漠绿洲的神奇，午餐品尝胡羊焖饼、驴肉黄面等西北美食，下午参观玉门关和阳关遗址，凭吊\"春风不度玉门关\"的历史沧桑，傍晚在鸣沙山观看沙漠日落，夜晚在敦煌夜市品尝杏皮水、臊子面，观看《又见敦煌》演出，感受千年古城的历史厚重与文化魅力。",
        "duration": "10h",
        "cost": 90000,
        "charm_fragments": (50, 110),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 50, "cleanliness": 50, "mood": 100, "health": 50, "growth": 100},
        "artifacts": ["莫高窟唐代壁画残片", "丝绸之路驼铃", "古代通关文牒", "玉门关汉代烽燧砖", "敦煌遗书唐代经卷"]
    },
    
    # === 日本城市 ===
    13: {
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
    14: {
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
    15: {
        "country": "日本",
        "city": "京都",
        "description": "古都千年，神社寺庙林立，樱花与红叶名胜",
        "journey": "清晨在清水寺观看京都市景，感受古都千年的宁静祥和，上午漫步祗园花见小路寻找艺伎身影，体验传统花街文化，中途参观金阁寺欣赏金光闪闪的舍利殿倒影，午餐品尝京料理、汤豆腐、抹茶甜点等精致美食，下午游览伏见稻荷大社穿越千本鸟居，再到岚山竹林小径感受竹影婆娑，傍晚在哲学之道散步观赏樱花或红叶（季节性），夜晚在先斗町品尝怀石料理，感受千年古都的文化底蕴与季节之美。",
        "duration": "8h",
        "cost": 50000,
        "charm_fragments": (30, 70),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 100, "cleanliness": 20, "mood": 50, "health": 20, "growth": 100},
        "artifacts": ["平安时代宫廷扇子", "清水寺创建瓦片", "源氏物语手稿", "金阁寺舍利殿金箔", "祗园茶屋古门帘"]
    },
    16: {
        "country": "日本",
        "city": "宇治",
        "description": "茶之乡，平等院、宇治川风光，抹茶文化体验",
        "journey": "清晨在宇治川畔散步，感受日本茶乡的清新雅致，上午参观平等院凤凰堂，欣赏十円硬币上的国宝建筑，体验日本美学的极致，中途到宇治茶园参观采茶过程，了解日本茶道文化精髓，午餐品尝宇治抹茶荞麦面、茶泡饭等茶香料理，下午参加茶道体验课程，学习正宗日式茶道礼仪，再到表参道购买宇治抹茶伴手礼，傍晚在宇治桥观赏宇治川夕阳，夜晚在传统茶屋品尝各式抹茶甜点，感受日本茶文化的深邃与优雅。",
        "duration": "8h",
        "cost": 50000,
        "charm_fragments": (30, 70),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 100, "cleanliness": 20, "mood": 50, "health": 20, "growth": 100},
        "artifacts": ["平等院凤凰堂瓦当", "藤原氏族纹章", "茶道千利休茶具", "宇治茶园古茶臼", "源氏物语宇治十帖石碑"]
    },
    17: {
        "country": "日本",
        "city": "奈良",
        "description": "东大寺、春日大社，奈良公园梅花鹿",
        "journey": "清晨在奈良公园与可爱的梅花鹿互动，购买鹿仙贝喂食神的使者，上午参观东大寺大佛殿，仰望日本最大的青铜佛像，感受佛教文化的庄严，中途游览春日大社，穿过数千盏石灯笼的参道，午餐品尝奈良渍物、柿叶寿司等传统美食，下午漫步兴福寺五重塔周围，再到若草山登高俯瞰奈良全景，傍晚在东大寺二月堂观赏夕阳西下，夜晚在奈良町传统街区购买小鹿周边商品，感受古都奈良的历史韵味与人与自然的和谐共处。",
        "duration": "8h",
        "cost": 50000,
        "charm_fragments": (30, 70),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 100, "cleanliness": 20, "mood": 50, "health": 20, "growth": 100},
        "artifacts": ["奈良时代大佛殿瓦片", "春日大社古代灯笼", "古都平城宫瓦当", "兴福寺五重塔心柱", "奈良鹿神传说石雕"]
    },
    18: {
        "country": "日本",
        "city": "札幌",
        "description": "北海道首府，雪祭、啤酒、美食（拉面、海鲜）",
        "journey": "清晨在大通公园感受北海道的清新空气，冬季欣赏雪祭冰雕艺术，夏季观赏薰衣草花海，上午参观札幌啤酒园了解北海道啤酒历史，品尝成吉思汗烤羊肉，中途到狸小路商店街购物，午餐享用札幌拉面、海鲜丼、哈密瓜等北海道特产，下午游览藻岩山或羊之丘展望台俯瞰札幌市景，再到白色恋人公园体验甜品制作，傍晚在薄野繁华街感受北国夜生活，夜晚品尝帝王蟹、海胆、扇贝等新鲜海味，感受北海道的纯净自然与美食天堂。",
        "duration": "10h",
        "cost": 120000,
        "charm_fragments": (50, 140),
        "blackening_fragments": (0, 0),
        "special_reward": "历史文物",
        "effects": {"hunger": 100, "cleanliness": 20, "mood": 50, "health": 20, "growth": 100},
        "artifacts": ["阿伊努族传统工艺品", "北海道开拓使印章", "明治时代啤酒窖铜牌", "札幌农学校古钟", "屯田兵屯所遗物"]
    },
    19: {
        "country": "日本",
        "city": "广岛",
        "description": "世界和平纪念地，宫岛（严岛神社）",
        "journey": "清晨乘船前往宫岛，看严岛神社的朱红色大鸟居在海中矗立，感受日本三景之一的绝美风光，上午参观严岛神社体验潮起潮落的神奇变化，登弥山俯瞰濑户内海，中途品尝宫岛名物红叶馒头、广岛烧，午餐享用牡蛎料理等濑户内海鲜，下午返回广岛参观和平纪念公园和原爆圆顶馆，了解战争历史与和平意义，傍晚在本通商店街购物，夜晚在广岛城天守阁欣赏夜景，感受这座在废墟上重建的和平之城的坚韧与希望。",
        "duration": "10h",
        "cost": 80000,
        "charm_fragments": (0, 0),
        "blackening_fragments": (50, 80),
        "special_reward": "历史文物",
        "effects": {"hunger": 100, "cleanliness": 20, "mood": 50, "health": 20, "growth": 100},
        "artifacts": ["严岛神社平安时代鸟居残片", "毛利家家纹瓦当", "古代神乐面具", "广岛城天守阁鯱瓦", "平清盛奉纳经筒"]
    },
    
    # === 其他国家 ===
    20: {
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
        "artifacts": ["瑞光大金塔金叶", "昂山市场翡翠", "茵雅湖古玉", "古代蒲甘王朝银币", "缅甸佛像残片"]
    },
    21: {
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
    22: {
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
    
    # === 传说类 ===
    23: {
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
    ],
    
    # 上海纪念品
    "上海": [
        {"name": "五香豆礼盒", "effects": {"hunger": 80, "mood": 100}, "description": "城隍庙传统小食，老上海味道"},
        {"name": "海派旗袍", "effects": {"mood": 180, "cleanliness": 80}, "description": "精致海派旗袍，东方女性魅力"},
        {"name": "外滩建筑明信片", "effects": {"mood": 120, "health": 50}, "description": "万国建筑群风景明信片"},
        {"name": "石库门文创胸针", "effects": {"mood": 100, "cleanliness": 60}, "description": "老上海石库门造型胸针"},
        {"name": "豫园九曲桥模型", "effects": {"mood": 140, "health": 70}, "description": "江南园林经典，寓意吉祥"},
        {"name": "沪语方言手册", "effects": {"mood": 90, "health": 60}, "description": "学说上海话，体验海派文化"},
        {"name": "黄浦江夜景拼图", "effects": {"mood": 110, "health": 80}, "description": "东方明珠璀璨夜景"},
        {"name": "南翔小笼包调料", "effects": {"hunger": 120, "mood": 80}, "description": "正宗南翔小笼包秘制调料"},
    ],
    
    # 深圳纪念品
    "深圳": [
        {"name": "电子产品盲盒", "effects": {"mood": 160, "health": 100}, "description": "华强北特色，科技感满满"},
        {"name": "改革开放纪念币", "effects": {"mood": 200, "health": 80}, "description": "特区精神象征，意义非凡"},
        {"name": "潮汕牛肉丸", "effects": {"hunger": 140, "mood": 100}, "description": "Q弹爽滑，深圳人最爱"},
        {"name": "蛇口炮台模型", "effects": {"mood": 120, "health": 90}, "description": "历史见证，开放精神"},
        {"name": "客家围屋积木", "effects": {"mood": 110, "health": 100}, "description": "传统建筑，寓教于乐"},
        {"name": "深圳湾大桥模型", "effects": {"mood": 150, "health": 70}, "description": "现代工程奇迹"},
        {"name": "荔枝蜜礼盒", "effects": {"hunger": 100, "mood": 120}, "description": "南国荔枝香甜如蜜"},
        {"name": "科技创新徽章", "effects": {"mood": 130, "health": 90}, "description": "创新之城标志"},
    ],
    
    # 重庆纪念品
    "重庆": [
        {"name": "重庆火锅底料", "effects": {"hunger": 150, "mood": 120}, "description": "正宗老火锅，麻辣鲜香"},
        {"name": "洪崖洞夜景灯", "effects": {"mood": 180, "health": 60}, "description": "千与千寻既视感，梦幻山城"},
        {"name": "长江索道模型", "effects": {"mood": 140, "health": 80}, "description": "山城特色交通工具"},
        {"name": "磁器口麻花", "effects": {"hunger": 120, "mood": 100}, "description": "传统手工麻花，香脆可口"},
        {"name": "轻轨穿楼模型", "effects": {"mood": 160, "health": 90}, "description": "8D魔幻城市奇观"},
        {"name": "巴渝文化扇子", "effects": {"mood": 100, "cleanliness": 70}, "description": "古老巴渝文化传承"},
        {"name": "山城夜景拼图", "effects": {"mood": 120, "health": 100}, "description": "不夜城璀璨灯火"},
        {"name": "毛血旺调料包", "effects": {"hunger": 140, "mood": 90}, "description": "经典江湖菜调料"},
    ],
    
    # 成都纪念品
    "成都": [
        {"name": "熊猫公仔套装", "effects": {"mood": 220, "health": 100}, "description": "萌萌哒国宝，治愈系首选"},
        {"name": "川剧变脸面具", "effects": {"mood": 180, "health": 80}, "description": "传统川剧艺术，神秘变脸"},
        {"name": "蜀锦丝巾", "effects": {"mood": 160, "cleanliness": 100}, "description": "蜀地织锦工艺，华美精致"},
        {"name": "担担面调料包", "effects": {"hunger": 130, "mood": 110}, "description": "成都街头经典，麻辣过瘾"},
        {"name": "三国主题茶具", "effects": {"mood": 140, "health": 120}, "description": "三国文化传承，品茶论英雄"},
        {"name": "宽窄巷子门牌", "effects": {"mood": 120, "health": 90}, "description": "老成都记忆，慢生活印记"},
        {"name": "金沙太阳神鸟", "effects": {"mood": 200, "health": 100}, "description": "古蜀文明象征，神秘金沙"},
        {"name": "青城山道茶", "effects": {"mood": 100, "health": 150}, "description": "道教名山清茶，养生佳品"},
    ],
    
    # 拉萨纪念品
    "拉萨": [
        {"name": "藏式转经筒", "effects": {"mood": 150, "health": 120}, "description": "虔诚信仰象征，内心宁静"},
        {"name": "哈达祝福围巾", "effects": {"mood": 180, "cleanliness": 80}, "description": "藏族传统哈达，吉祥如意"},
        {"name": "牦牛肉干", "effects": {"hunger": 160, "mood": 100}, "description": "高原特产，营养丰富"},
        {"name": "藏银手镯", "effects": {"mood": 170, "cleanliness": 90}, "description": "藏族传统银饰，民族风情"},
        {"name": "布达拉宫模型", "effects": {"mood": 200, "health": 80}, "description": "雪域圣殿，信仰之光"},
        {"name": "青稞酒礼盒", "effects": {"hunger": 80, "mood": 140}, "description": "高原青稞酿制，醇香甘甜"},
        {"name": "唐卡艺术画", "effects": {"mood": 220, "health": 100}, "description": "藏传佛教艺术瑰宝"},
        {"name": "天珠护身符", "effects": {"mood": 120, "health": 180}, "description": "神秘天珠，护佑平安"},
    ],
    
    # 哈尔滨纪念品
    "哈尔滨": [
        {"name": "俄式套娃", "effects": {"mood": 160, "health": 80}, "description": "俄罗斯传统工艺品"},
        {"name": "马迭尔冰棍礼盒", "effects": {"hunger": 100, "mood": 140}, "description": "百年冰棍品牌，童年回忆"},
        {"name": "中央大街欧式建筑模型", "effects": {"mood": 180, "health": 90}, "description": "欧式风情，异国情调"},
        {"name": "东北大花布", "effects": {"mood": 120, "cleanliness": 100}, "description": "东北传统花布，喜庆热闹"},
        {"name": "红肠礼盒", "effects": {"hunger": 140, "mood": 100}, "description": "哈尔滨特色，俄式风味"},
        {"name": "圣索菲亚教堂音乐盒", "effects": {"mood": 200, "health": 80}, "description": "拜占庭建筑，神圣音乐"},
        {"name": "松花江石头画", "effects": {"mood": 130, "health": 100}, "description": "自然艺术，江边奇石"},
        {"name": "冰雪节纪念品", "effects": {"mood": 150, "cleanliness": 80}, "description": "冰城特色，雪花晶莹"},
    ],
    
    # 青岛纪念品
    "青岛": [
        {"name": "青岛啤酒礼盒", "effects": {"hunger": 80, "mood": 160}, "description": "百年啤酒品牌，醇香回甘"},
        {"name": "八大关建筑明信片", "effects": {"mood": 120, "health": 70}, "description": "万国建筑博览，浪漫青岛"},
        {"name": "崂山绿茶", "effects": {"mood": 100, "health": 140}, "description": "道教名山清茶，海边茶香"},
        {"name": "德式建筑模型", "effects": {"mood": 150, "health": 80}, "description": "德租时期建筑，异国风情"},
        {"name": "海洋贝壳工艺品", "effects": {"mood": 130, "cleanliness": 90}, "description": "海洋文化，自然之美"},
        {"name": "栈桥风景画", "effects": {"mood": 140, "health": 90}, "description": "青岛地标，碧海蓝天"},
        {"name": "蛤蜊海鲜干", "effects": {"hunger": 120, "mood": 100}, "description": "海鲜特产，鲜美可口"},
        {"name": "五四广场纪念品", "effects": {"mood": 160, "health": 80}, "description": "五月的风，青春活力"},
    ],
    
    # 敦煌纪念品
    "敦煌": [
        {"name": "飞天丝巾", "effects": {"mood": 200, "cleanliness": 100}, "description": "莫高窟飞天图案，飘逸优雅"},
        {"name": "驼铃风铃", "effects": {"mood": 150, "health": 80}, "description": "丝绸之路驼铃声，悠远空灵"},
        {"name": "莫高窟壁画复制品", "effects": {"mood": 220, "health": 100}, "description": "千年佛教艺术瑰宝"},
        {"name": "月牙泉沙画", "effects": {"mood": 180, "cleanliness": 80}, "description": "沙漠绿洲奇观，自然艺术"},
        {"name": "胡杨木雕", "effects": {"mood": 160, "health": 120}, "description": "千年不死胡杨，生命赞歌"},
        {"name": "夜光杯酒具", "effects": {"mood": 170, "health": 90}, "description": "葡萄美酒夜光杯，诗意人生"},
        {"name": "敦煌遗书复制品", "effects": {"mood": 200, "health": 100}, "description": "古代文献珍宝，文化传承"},
        {"name": "鸣沙山沙子瓶", "effects": {"mood": 120, "cleanliness": 90}, "description": "沙漠记忆，自然收藏"},
    ],
    
    # 京都纪念品
    "京都": [
        {"name": "和风扇子", "effects": {"mood": 140, "cleanliness": 80}, "description": "传统和风扇子，优雅别致"},
        {"name": "艺伎玩偶", "effects": {"mood": 180, "health": 70}, "description": "祗园艺伎文化，神秘典雅"},
        {"name": "金阁寺御守", "effects": {"mood": 120, "health": 100}, "description": "金阁寺祈福御守，保佑平安"},
        {"name": "京料理调味料", "effects": {"hunger": 110, "mood": 120}, "description": "精致京料理，味觉艺术"},
        {"name": "千本鸟居模型", "effects": {"mood": 200, "health": 80}, "description": "伏见稻荷神社，朱红色浪漫"},
        {"name": "竹制茶道具", "effects": {"mood": 130, "health": 120}, "description": "茶道文化，禅意生活"},
        {"name": "樱花书签", "effects": {"mood": 100, "health": 90}, "description": "樱花季节，粉色浪漫"},
        {"name": "清水寺陶瓷", "effects": {"mood": 150, "cleanliness": 100}, "description": "清水烧陶瓷，京都工艺"},
    ],
    
    # 宇治纪念品
    "宇治": [
        {"name": "宇治抹茶粉", "effects": {"hunger": 80, "mood": 140}, "description": "正宗宇治抹茶，茶香浓郁"},
        {"name": "平等院凤凰堂模型", "effects": {"mood": 200, "health": 80}, "description": "十円硬币国宝建筑"},
        {"name": "茶道具套装", "effects": {"mood": 160, "health": 120}, "description": "日式茶道，优雅文化"},
        {"name": "抹茶巧克力", "effects": {"hunger": 90, "mood": 120}, "description": "抹茶与巧克力的完美融合"},
        {"name": "宇治川风景画", "effects": {"mood": 130, "health": 90}, "description": "宇治川美景，诗意山水"},
        {"name": "源氏物语书签", "effects": {"mood": 110, "health": 100}, "description": "古典文学，文化传承"},
        {"name": "茶园竹篮", "effects": {"mood": 120, "cleanliness": 90}, "description": "采茶竹篮，田园风情"},
        {"name": "抹茶年轮蛋糕", "effects": {"hunger": 100, "mood": 130}, "description": "层次丰富，抹茶香甜"},
    ],
    
    # 奈良纪念品
    "奈良": [
        {"name": "小鹿饼干", "effects": {"hunger": 80, "mood": 160}, "description": "奈良小鹿造型，可爱治愈"},
        {"name": "东大寺御守", "effects": {"mood": 130, "health": 120}, "description": "大佛殿祈福，庇佑平安"},
        {"name": "鹿角工艺品", "effects": {"mood": 140, "health": 80}, "description": "天然鹿角制作，自然之美"},
        {"name": "春日大社灯笼", "effects": {"mood": 180, "health": 90}, "description": "千盏灯笼，神秘光影"},
        {"name": "柿叶寿司", "effects": {"hunger": 120, "mood": 100}, "description": "奈良传统美食，清香可口"},
        {"name": "奈良渍物", "effects": {"hunger": 90, "mood": 110}, "description": "传统腌菜，健康美味"},
        {"name": "五重塔模型", "effects": {"mood": 160, "health": 100}, "description": "兴福寺五重塔，古都象征"},
        {"name": "鹿仙贝", "effects": {"hunger": 60, "mood": 140}, "description": "喂鹿专用，人鹿和谐"},
    ],
    
    # 札幌纪念品
    "札幌": [
        {"name": "白色恋人巧克力", "effects": {"hunger": 100, "mood": 180}, "description": "北海道经典，甜蜜恋人"},
        {"name": "札幌拉面调料", "effects": {"hunger": 140, "mood": 120}, "description": "正宗札幌味噌拉面"},
        {"name": "薰衣草香囊", "effects": {"mood": 150, "cleanliness": 120}, "description": "富良野薰衣草，芬芳怡人"},
        {"name": "成吉思汗烤肉调料", "effects": {"hunger": 160, "mood": 100}, "description": "北海道特色烤羊肉"},
        {"name": "雪祭纪念品", "effects": {"mood": 170, "health": 80}, "description": "札幌雪祭，冰雕艺术"},
        {"name": "帝王蟹罐头", "effects": {"hunger": 180, "mood": 140}, "description": "北海道海鲜之王"},
        {"name": "哈密瓜糖", "effects": {"hunger": 80, "mood": 130}, "description": "夕张哈密瓜，香甜如蜜"},
        {"name": "阿伊努族工艺品", "effects": {"mood": 160, "health": 100}, "description": "原住民文化，传统技艺"},
    ],
    
    # 广岛纪念品
    "广岛": [
        {"name": "千纸鹤折纸", "effects": {"mood": 140, "health": 100}, "description": "和平祈愿，千纸鹤寄托"},
        {"name": "红叶馒头", "effects": {"hunger": 100, "mood": 130}, "description": "宫岛名物，枫叶造型"},
        {"name": "广岛烧调料", "effects": {"hunger": 150, "mood": 110}, "description": "广岛特色料理，层次丰富"},
        {"name": "严岛神社鸟居模型", "effects": {"mood": 200, "health": 80}, "description": "海中鸟居，日本三景"},
        {"name": "和平纪念品", "effects": {"mood": 120, "health": 120}, "description": "和平象征，铭记历史"},
        {"name": "牡蛎调料包", "effects": {"hunger": 130, "mood": 100}, "description": "濑户内海牡蛎，鲜美肥美"},
        {"name": "神乐面具", "effects": {"mood": 160, "health": 90}, "description": "传统神乐舞，神秘面具"},
        {"name": "弥山登山纪念品", "effects": {"mood": 130, "health": 110}, "description": "宫岛弥山，濑户内海美景"},
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
            "兵马俑陶片", "华清池唐代瓦当", "大雁塔经文拓片", "西安城墙古砖", "唐朝宫廷金钗",
            # 上海文物
            "近代海关大楼铜钟", "石库门雕花窗棂", "外滩万国建筑群石刻", "豫园明代园林假山石", "上海古城墙石砖",
            # 深圳文物
            "南海古渔村石碑", "南头古城明代城砖", "客家围屋古构件", "古代盐田晒盐石槽", "蛇口炮台清代石刻",
            # 重庆文物
            "巴渝古国青铜器", "古代巴王国铜戈", "古代纤夫石刻", "朝天门古码头石阶", "山城古寨门楣",
            # 成都文物
            "蜀汉丞相印章", "三星堆青铜器残片", "唐代杜甫手稿", "武侯祠古碑刻", "金沙遗址太阳神鸟",
            # 拉萨文物
            "唐代文成公主佛像", "布达拉宫金顶瓦片", "吐蕃王朝印章", "大昭寺千年香炉", "藏王松赞干布佛龛",
            # 哈尔滨文物
            "黑龙江古代渔猎铜器", "俄式建筑装饰浮雕", "清代驿站马铃", "圣索菲亚教堂钟楼铜钟", "松花江古代石刻",
            # 青岛文物
            "古代即墨城石雕", "明代胶州湾海防印", "古代崂山道观钟", "古代崂山石刻", "八大关别墅铜门牌",
            # 敦煌文物
            "莫高窟唐代壁画残片", "丝绸之路驼铃", "古代通关文牒", "玉门关汉代烽燧砖", "敦煌遗书唐代经卷"
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
            "浅草寺江户古钟", "江户城石垣残片", "明治银座煤油灯", "德川家康印章复制品", "上野宽永寺古瓦",
            # 京都文物
            "平安时代宫廷扇子", "清水寺创建瓦片", "源氏物语手稿", "金阁寺舍利殿金箔", "祗园茶屋古门帘",
            # 宇治文物
            "平等院凤凰堂瓦当", "藤原氏族纹章", "茶道千利休茶具", "宇治茶园古茶臼", "源氏物语宇治十帖石碑",
            # 奈良文物
            "奈良时代大佛殿瓦片", "春日大社古代灯笼", "古都平城宫瓦当", "兴福寺五重塔心柱", "奈良鹿神传说石雕",
            # 札幌文物
            "阿伊努族传统工艺品", "北海道开拓使印章", "明治时代啤酒窖铜牌", "札幌农学校古钟", "屯田兵屯所遗物",
            # 广岛文物
            "严岛神社平安时代鸟居残片", "毛利家家纹瓦当", "古代神乐面具", "广岛城天守阁鯱瓦", "平清盛奉纳经筒"
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
            "瑞光大金塔金叶", "昂山市场翡翠", "茵雅湖古玉", "古代蒲甘王朝银币", "缅甸佛像残片"
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
