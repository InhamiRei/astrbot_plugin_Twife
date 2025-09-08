"""基本设置和常量配置"""
import os

# 插件基本信息
PLUGIN_NAME = "群老婆插件"
PLUGIN_VERSION = "v1.4"
PLUGIN_AUTHOR = "Hey、小怪兽"

# 文件路径配置
# 获取当前插件目录（已经在 data/plugins/astrbot_plugin_aw/ 下）
PLUGIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取插件根目录
CONFIG_DIR = os.path.join(PLUGIN_DIR, 'config')  # Python配置文件目录
DATA_DIR = os.path.join(PLUGIN_DIR, 'data')     # JSON数据文件目录
IMG_DIR = os.path.join(PLUGIN_DIR, 'static', 'wife')

# 修复：确保使用绝对路径
PLUGIN_DIR = os.path.abspath(PLUGIN_DIR)
CONFIG_DIR = os.path.abspath(CONFIG_DIR)
DATA_DIR = os.path.abspath(DATA_DIR)
IMG_DIR = os.path.abspath(IMG_DIR)

# 确保目录存在
os.makedirs(CONFIG_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)

# 调试路径信息
print(f"[Debug Settings] 当前文件路径: {__file__}")
print(f"[Debug Settings] 插件根目录: {PLUGIN_DIR}")
print(f"[Debug Settings] 数据目录: {DATA_DIR}")
print(f"[Debug Settings] 全局老婆数据文件: {os.path.join(DATA_DIR, 'global_wife_data.json')}")

# JSON数据文件路径（长期存储）
GLOBAL_WIFE_DATA_FILE = os.path.join(DATA_DIR, 'global_wife_data.json')
USER_DATA_FILE = os.path.join(DATA_DIR, 'user_data.json')
DAILY_LIMITS_FILE = os.path.join(DATA_DIR, 'daily_limits.json')
STUDY_STATUS_FILE = os.path.join(DATA_DIR, 'study_status.json')
WORK_STATUS_FILE = os.path.join(DATA_DIR, 'work_status.json')
DUNGEON_DATA_FILE = os.path.join(DATA_DIR, 'dungeon_data.json')
NO_AT_USERS_FILE = os.path.join(DATA_DIR, 'no_at_users.json')

# 网络配置
IMAGE_BASE_URL = 'http://save.my996.top/?/img/'

# 游戏规则配置
NTR_MAX_DAILY = 3  # 每日最大牛老婆次数
NTR_SUCCESS_RATE = 0.20  # 牛老婆成功率
GO_OUT_MAX_DAILY = 3  # 每日最大出门转转次数

# 提示消息
NTR_MAX_NOTICE = f'为防止牛头人泛滥，一天最多可牛{NTR_MAX_DAILY}次，请明天再来吧~'
GO_OUT_MAX_NOTICE = f'为了保持探索的新鲜感，每天最多只能出门转转{GO_OUT_MAX_DAILY}次，请明天再来吧~'

# 超市商品列表（只显示日用品和滑稽物品，避免刷屏）
SUPERMARKET_ITEMS = [
    "香皂",              # 清洁用品
    "面包",              # 食物
    "巧克力",            # 食物
    "牙刷",              # 清洁用品
    "毛巾",              # 清洁用品
    "创口贴",            # 药物
    "群主的女装照",      # 滑稽
    "管理的绿帽子",      # 滑稽
    "暴雪帝国编年史",    # 滑稽
    "单身狗粮"           # 滑稽
]

# 快餐店商品列表（高饥饿值恢复食物）
FASTFOOD_ITEMS = [
    "薯条",              # 小食
    "蛋挞",              # 小食
    "吮指原味鸡",        # 小食
    "新奥尔良烤鸡腿堡",  # 中等
    "双层吉士汉堡",      # 中等
    "上校鸡块",          # 中等
    "奥尔良烤鸡翅",      # 中等
    "全家桶",            # 大套餐
    "麦旋风",            # 大套餐
    "儿童套餐",          # 大套餐
    "vivo50餐",          # 滑稽物品（放最后）
]

# 苍蝇馆子商品列表（地方特色菜，价格高但效果显著）
CANGYINGGUANZI_ITEMS = [
    "正宗兰州拉面",      # 西北菜
    "重庆小面",          # 川渝菜
    "广式肠粉",          # 粤菜
    "上海生煎包",        # 沪菜
    "北京炸酱面",        # 京菜
    "西安肉夹馍",        # 陕菜
    "东北锅包肉",        # 东北菜
    "湖南臭豆腐",        # 湘菜
    "云南过桥米线",      # 滇菜
    "新疆大盘鸡",        # 新疆菜
    "四川麻婆豆腐",      # 川菜
    "山东煎饼果子",      # 鲁菜
    "福建沙茶面",        # 闽菜
    "河南胡辣汤",        # 豫菜
    "贵州酸汤鱼"         # 黔菜
]
