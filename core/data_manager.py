"""数据管理模块 - 处理所有数据的加载、保存和操作"""
import json
import os
from datetime import datetime, timedelta
from ..config.settings import *

# 全局数据存储
global_wife_data = {}
user_data = {}
daily_limits = {}
study_status = {}
work_status = {}
ITEMS_DATA = {}
WORK_LIST = []
dungeon_data = {}  # 存储用户地下城数据
no_at_users = []  # 不希望被@艾特的用户列表

# 缓存变量
offline_completed_studies = {}
offline_completed_works = {}
candidate_wives = {}
animewife_cooldown = {}
ntr_feast_active = {}
newly_acquired_wives = {}

# 插件实例引用，用于访问调度器
wife_plugin_instance = None

def get_today():
    """获取上海时区当日日期"""
    utc_now = datetime.utcnow()
    shanghai_time = utc_now + timedelta(hours=8)
    return shanghai_time.date().isoformat()

# === 全局老婆数据管理 ===
def load_global_wife_data():
    """载入全局老婆数据"""
    global global_wife_data
    print(f"[Debug] 尝试加载全局老婆数据文件: {GLOBAL_WIFE_DATA_FILE}")
    print(f"[Debug] 文件是否存在: {os.path.exists(GLOBAL_WIFE_DATA_FILE)}")
    
    if not os.path.exists(GLOBAL_WIFE_DATA_FILE):
        print(f"[Debug] 文件不存在，创建空文件")
        with open(GLOBAL_WIFE_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=4)
        global_wife_data = {}
    else:
        print(f"[Debug] 正在读取文件...")
        with open(GLOBAL_WIFE_DATA_FILE, 'r', encoding='utf-8') as f:
            global_wife_data = json.load(f)
        print(f"[Debug] 成功加载 {len(global_wife_data)} 条老婆数据")
        print(f"[Debug] 用户列表: {list(global_wife_data.keys())[:5]}")  # 只显示前5个
        
        # 检查配置文件是否为旧格式，为缺失的参数添加默认值
        for user_id, user_data_item in global_wife_data.items():
            if len(user_data_item) < 3:
                user_data_item.append(user_id)
            if len(user_data_item) < 4:
                user_data_item.append(False)
            if len(user_data_item) < 5:
                user_data_item.append(0)
            if len(user_data_item) < 6:
                user_data_item.append(1)
            if len(user_data_item) < 7:
                user_data_item.append(0)
            if len(user_data_item) < 8:
                user_data_item.append(1000)
            if len(user_data_item) < 9:
                user_data_item.append(1000)
            if len(user_data_item) < 10:
                user_data_item.append(1000)
            if len(user_data_item) < 11:
                user_data_item.append(1000)
            if len(user_data_item) < 12:
                user_data_item.append("正常")
            if len(user_data_item) < 13:
                user_data_item.append("幼儿园")
            if len(user_data_item) < 14:
                user_data_item.append(0)
            # 添加新的老婆特殊属性字段
            if len(user_data_item) < 15:
                user_data_item.append(0)  # 妹抖值 (14)
            if len(user_data_item) < 16:
                user_data_item.append(0)  # 撒娇值 (15)
            if len(user_data_item) < 17:
                user_data_item.append(0)  # 傲娇值 (16)
            if len(user_data_item) < 18:
                user_data_item.append(0)  # 黑化率 (17)
            if len(user_data_item) < 19:
                user_data_item.append(0)  # 反差萌 (18)

def save_global_wife_data():
    """保存全局老婆数据"""
    with open(GLOBAL_WIFE_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(global_wife_data, f, ensure_ascii=False, indent=4)

def get_user_wife_data(user_id: str):
    """获取用户老婆数据，如果不存在则返回None"""
    if not global_wife_data:
        load_global_wife_data()
    return global_wife_data.get(str(user_id))

def set_user_wife_data(user_id: str, wife_name: str, nickname: str, purelove=False, affection=0, level=1, growth=0, hunger=1000, cleanliness=1000, health=1000, mood=1000, status="正常", education_level="幼儿园", knowledge=0, moe_value=0, spoil_value=0, tsundere_value=0, dark_rate=0, contrast_cute=0):
    """设置用户老婆数据"""
    if not global_wife_data:
        load_global_wife_data()
    
    global_wife_data[str(user_id)] = [wife_name, "permanent", nickname, purelove, affection, level, growth, hunger, cleanliness, health, mood, status, education_level, knowledge, moe_value, spoil_value, tsundere_value, dark_rate, contrast_cute]
    save_global_wife_data()

def update_user_wife_data(user_id: str, **kwargs):
    """更新用户老婆数据的特定字段"""
    user_data_item = get_user_wife_data(user_id)
    if not user_data_item:
        return False
    
    # 映射参数到对应的索引
    field_mapping = {
        'wife_name': 0,
        'nickname': 2,
        'purelove': 3,
        'affection': 4,
        'level': 5,
        'growth': 6,
        'hunger': 7,
        'cleanliness': 8,
        'health': 9,
        'mood': 10,
        'status': 11,
        'education_level': 12,
        'knowledge': 13,
        'moe_value': 14,
        'spoil_value': 15,
        'tsundere_value': 16,
        'dark_rate': 17,
        'contrast_cute': 18
    }
    
    for field, value in kwargs.items():
        if field in field_mapping:
            user_data_item[field_mapping[field]] = value
    
    save_global_wife_data()
    return True

def delete_user_wife_data(user_id: str):
    """删除用户老婆数据"""
    if str(user_id) in global_wife_data:
        del global_wife_data[str(user_id)]
        save_global_wife_data()
        return True
    return False

# === 用户永久数据管理 ===
def load_user_data():
    """载入用户永久数据（金币、背包、房产）"""
    global user_data
    if not os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=4)
        user_data = {}
    else:
        with open(USER_DATA_FILE, 'r', encoding='utf-8') as f:
            user_data = json.load(f)

def save_user_data():
    """保存用户永久数据"""
    with open(USER_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(user_data, f, ensure_ascii=False, indent=4)

def get_user_data(user_id: str):
    """获取用户数据，如果不存在则创建默认数据"""
    if not user_data:
        load_user_data()
    
    if user_id not in user_data:
        user_data[user_id] = {
            "coins": 100,  # 默认100金币
            "backpack": {},  # 空背包
            "property": "桥洞下的破旧帐篷",  # 默认房产
            "furniture": {},  # 家具库存
            "trophies": {},  # 战利品（地下城掉落）
            "wardrobe": {},  # 衣柜（存放服装）
            "equipment": {  # 当前装备
                "头部": None,
                "身体": None,
                "手部": None,
                "腿部": None,
                "脚部": None,
                "手持": None,
                "饰品": None
            }
        }
        save_user_data()
    
    # 确保现有用户也有所有字段
    if "furniture" not in user_data[user_id]:
        user_data[user_id]["furniture"] = {}
        save_user_data()
    
    if "trophies" not in user_data[user_id]:
        user_data[user_id]["trophies"] = {}
        save_user_data()
        
    if "wardrobe" not in user_data[user_id]:
        user_data[user_id]["wardrobe"] = {}
        save_user_data()
        
    if "equipment" not in user_data[user_id]:
        user_data[user_id]["equipment"] = {
            "头部": None,
            "身体": None,
            "手部": None,
            "腿部": None,
            "脚部": None,
            "手持": None,
            "饰品": None
        }
        save_user_data()
    
    return user_data[user_id]

def update_user_data(user_id: str, coins=None, backpack=None, property=None, furniture=None, trophies=None, wardrobe=None, equipment=None):
    """更新用户数据"""
    user_data_obj = get_user_data(user_id)
    if coins is not None:
        user_data_obj["coins"] = coins
    if backpack is not None:
        user_data_obj["backpack"] = backpack
    if property is not None:
        user_data_obj["property"] = property
    if furniture is not None:
        user_data_obj["furniture"] = furniture
    if trophies is not None:
        user_data_obj["trophies"] = trophies
    if wardrobe is not None:
        user_data_obj["wardrobe"] = wardrobe
    if equipment is not None:
        user_data_obj["equipment"] = equipment
    save_user_data()

# === 每日限制数据管理 ===
def load_daily_limits():
    """载入每日限制数据"""
    global daily_limits
    if not os.path.exists(DAILY_LIMITS_FILE):
        with open(DAILY_LIMITS_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=4)
        daily_limits = {}
    else:
        with open(DAILY_LIMITS_FILE, 'r', encoding='utf-8') as f:
            daily_limits = json.load(f)

def save_daily_limits():
    """保存每日限制数据"""
    with open(DAILY_LIMITS_FILE, 'w', encoding='utf-8') as f:
        json.dump(daily_limits, f, ensure_ascii=False, indent=4)

def get_daily_limit_data(user_id: str, limit_type: str):
    """获取用户每日限制数据，如果不存在或者是新的一天则重置"""
    if not daily_limits:
        load_daily_limits()
    
    today = get_today()
    
    if user_id not in daily_limits:
        daily_limits[user_id] = {}
    
    user_limits = daily_limits[user_id]
    
    # 检查是否是新的一天或者该限制类型不存在
    if limit_type not in user_limits or user_limits[limit_type].get('date') != today:
        # 重置该限制类型的数据
        user_limits[limit_type] = {
            'date': today,
            'count': 0
        }
        save_daily_limits()
    
    return user_limits[limit_type]['count']

def update_daily_limit_data(user_id: str, limit_type: str, count: int):
    """更新用户每日限制数据"""
    if not daily_limits:
        load_daily_limits()
    
    today = get_today()
    
    if user_id not in daily_limits:
        daily_limits[user_id] = {}
    
    user_limits = daily_limits[user_id]
    
    # 更新数据
    user_limits[limit_type] = {
        'date': today,
        'count': count
    }
    save_daily_limits()

# === 学习状态数据管理 ===
def load_study_status():
    """载入学习状态数据"""
    global study_status
    print(f"加载学习状态文件: {STUDY_STATUS_FILE}")
    if not os.path.exists(STUDY_STATUS_FILE):
        print("学习状态文件不存在，创建空文件")
        with open(STUDY_STATUS_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=4)
        study_status = {}
    else:
        print("学习状态文件存在，开始读取")
        with open(STUDY_STATUS_FILE, 'r', encoding='utf-8') as f:
            study_status = json.load(f)
        print(f"成功加载学习状态，数量: {len(study_status)}")
        print(f"学习状态内容: {study_status}")

def save_study_status():
    """保存学习状态数据"""
    global study_status  # 声明全局变量  
    print(f"[数据管理] 准备保存学习状态到文件: {STUDY_STATUS_FILE}")
    print(f"[数据管理] 要保存的学习状态: {study_status}")
    try:
        with open(STUDY_STATUS_FILE, 'w', encoding='utf-8') as f:
            json.dump(study_status, f, ensure_ascii=False, indent=4)
        print(f"[数据管理] 学习状态保存成功")
        
        # 验证保存结果
        with open(STUDY_STATUS_FILE, 'r', encoding='utf-8') as f:
            saved_data = json.load(f)
        print(f"[数据管理] 验证保存结果，文件中的数据: {saved_data}")
    except Exception as e:
        print(f"[数据管理] 保存学习状态失败: {e}")
        import traceback
        traceback.print_exc()

# === 打工状态数据管理 ===
def load_work_status():
    """载入打工状态数据"""
    global work_status
    print(f"加载打工状态文件: {WORK_STATUS_FILE}")
    if not os.path.exists(WORK_STATUS_FILE):
        print("打工状态文件不存在，创建空文件")
        with open(WORK_STATUS_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=4)
        work_status = {}
    else:
        print("打工状态文件存在，开始读取")
        with open(WORK_STATUS_FILE, 'r', encoding='utf-8') as f:
            work_status = json.load(f)
        print(f"成功加载打工状态，数量: {len(work_status)}")
        print(f"打工状态内容: {work_status}")

def save_work_status():
    """保存打工状态数据"""
    with open(WORK_STATUS_FILE, 'w', encoding='utf-8') as f:
        json.dump(work_status, f, ensure_ascii=False, indent=4)

# === 配置数据管理 ===
def load_items_config():
    """从Python配置加载物品数据"""
    global ITEMS_DATA
    try:
        # 导入Python配置中的物品列表
        from ..config.items_config import ITEMS_LIST
        # 确保正确更新全局变量
        new_items_data = {item['name']: item for item in ITEMS_LIST}
        ITEMS_DATA.clear()  # 先清空
        ITEMS_DATA.update(new_items_data)  # 然后更新
        print(f"成功加载物品配置，数量: {len(ITEMS_DATA)}")
        print(f"ITEMS_DATA 示例: {list(ITEMS_DATA.keys())[:5]}")
    except Exception as e:
        print(f"加载物品配置失败: {e}")
        import traceback
        traceback.print_exc()
        ITEMS_DATA.clear()

def load_work_config():
    """从Python配置加载打工数据"""
    global WORK_LIST
    try:
        # 导入Python配置中的工作列表
        from ..config.work_config import WORK_LIST as WORK_CONFIG_LIST
        WORK_LIST = WORK_CONFIG_LIST
        print(f"成功加载工作配置，数量: {len(WORK_LIST)}")
    except Exception as e:
        print(f"加载工作配置失败: {e}")
        WORK_LIST = []

def get_items_for_go_out():
    """获取用于出门转转的物品列表（兼容原格式）"""
    items_list = []
    for item_name, item_data in ITEMS_DATA.items():
        items_list.append((
            item_name,
            item_data['weight'],
            item_data['min_count'],
            item_data['max_count'],
            item_data['description']
        ))
    return items_list

def clear_user_work_study_status(user_id: str):
    """清除用户的工作和学习状态（当老婆归属发生变化时调用）"""
    global work_status, study_status
    
    # 清除学习状态
    if user_id in study_status:
        print(f"清除用户 {user_id} 的学习状态")
        del study_status[user_id]
        save_study_status()
    
    # 清除工作状态
    if user_id in work_status:
        print(f"清除用户 {user_id} 的工作状态")
        del work_status[user_id]
        save_work_status()

# === 地下城数据管理 ===
def load_dungeon_data():
    """载入地下城数据"""
    global dungeon_data
    print(f"加载地下城数据文件: {DUNGEON_DATA_FILE}")
    if not os.path.exists(DUNGEON_DATA_FILE):
        print("地下城数据文件不存在，创建空文件")
        with open(DUNGEON_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=4)
        dungeon_data = {}
    else:
        print("地下城数据文件存在，开始读取")
        with open(DUNGEON_DATA_FILE, 'r', encoding='utf-8') as f:
            dungeon_data = json.load(f)
        print(f"成功加载地下城数据，数量: {len(dungeon_data)}")

def load_no_at_users():
    """载入不艾特用户列表"""
    global no_at_users
    print(f"加载不艾特用户配置文件: {NO_AT_USERS_FILE}")
    if not os.path.exists(NO_AT_USERS_FILE):
        print("不艾特用户配置文件不存在，创建默认文件")
        default_config = {
            "description": "不希望被@艾特的用户列表",
            "no_at_users": [],
            "last_modified": datetime.now().strftime("%Y-%m-%d")
        }
        with open(NO_AT_USERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, ensure_ascii=False, indent=4)
        no_at_users = []
    else:
        print("不艾特用户配置文件存在，开始读取")
        with open(NO_AT_USERS_FILE, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
            no_at_users = config_data.get('no_at_users', [])
        print(f"成功加载不艾特用户配置，用户数量: {len(no_at_users)}")

def save_no_at_users():
    """保存不艾特用户列表"""
    try:
        config_data = {
            "description": "不希望被@艾特的用户列表",
            "no_at_users": no_at_users,
            "last_modified": datetime.now().strftime("%Y-%m-%d")
        }
        with open(NO_AT_USERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(config_data, f, ensure_ascii=False, indent=4)
        print("不艾特用户配置保存成功")
    except Exception as e:
        print(f"保存不艾特用户配置失败: {e}")

def save_dungeon_data():
    """保存地下城数据"""
    with open(DUNGEON_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(dungeon_data, f, ensure_ascii=False, indent=4)

def get_user_dungeon_data(user_id: str):
    """获取用户地下城数据，如果不存在则创建默认数据"""
    if not dungeon_data:
        load_dungeon_data()
    
    if user_id not in dungeon_data:
        dungeon_data[user_id] = {
            "last_dungeon_time": None,  # 最后一次进入地下城的时间
            "kill_stats": {},  # 杀怪统计 {"怪物名": 数量}
            "total_dungeons": 0  # 总共进入地下城次数
        }
        save_dungeon_data()
    
    return dungeon_data[user_id]

def update_user_dungeon_data(user_id: str, **kwargs):
    """更新用户地下城数据"""
    user_dungeon = get_user_dungeon_data(user_id)
    
    for field, value in kwargs.items():
        if field in user_dungeon:
            user_dungeon[field] = value
    
    save_dungeon_data()

def add_kill_stats(user_id: str, monster_name: str, count: int):
    """添加杀怪统计"""
    user_dungeon = get_user_dungeon_data(user_id)
    
    if monster_name not in user_dungeon["kill_stats"]:
        user_dungeon["kill_stats"][monster_name] = 0
    
    user_dungeon["kill_stats"][monster_name] += count
    save_dungeon_data()

def get_kill_stats_display(user_id: str):
    """获取杀怪统计的显示文本"""
    user_dungeon = get_user_dungeon_data(user_id)
    kill_stats = user_dungeon["kill_stats"]
    
    if not kill_stats:
        return "暂无击杀记录"
    
    # 获取怪物难度映射
    from ..config.dungeon_config import DUNGEON_LIST
    monster_difficulty_map = {}
    for dungeon in DUNGEON_LIST:
        for monster in dungeon['monsters']:
            monster_difficulty_map[monster['name']] = monster['difficulty']
    
    # 按怪物难度从低到高排序
    sorted_stats = sorted(kill_stats.items(), key=lambda x: monster_difficulty_map.get(x[0], 999))
    
    stats_text = []
    for monster_name, count in sorted_stats:
        stats_text.append(f"{monster_name}x{count}")
    
    return "，".join(stats_text)

# 初始化所有数据
def initialize_all_data():
    """初始化所有数据"""
    load_global_wife_data()
    load_user_data()
    load_items_config()
    load_work_config()
    load_daily_limits()
    load_study_status()
    load_work_status()
    load_dungeon_data()
    load_no_at_users()
    print("所有数据初始化完成")
