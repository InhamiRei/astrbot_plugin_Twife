"""世界boss系统核心模块"""
import random
import math
import json
import os
import re
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
from .data_manager import *

# 世界Boss配置
WORLD_BOSS_CONFIG = {
    "可可萝（黑化）": {
        "name": "可可萝（黑化）",
        "description": "被黑暗力量侵蚀的公主，散发着危险的气息",
        "shield": 15,  # 护盾值15%，公主的神圣防护
        "phases": [
            {"phase": 1, "max_hp": 10000, "name": "小小引导者"},
            {"phase": 2, "max_hp": 30000, "name": "极光绽放"},
            {"phase": 3, "max_hp": 50000, "name": "精灵的启示"}
        ],
        "rewards": {
            1: {"coins": [10000, 12000], "items": ["可可萝的围裙", "温暖的料理", "美食食谱"]},
            2: {"coins": [15000, 20000], "items": ["可可萝的围裙", "温暖的料理", "美食食谱", "可可萝的笑容", "公主之心"]},
            3: {"coins": [20000, 30000], "items": ["可可萝的围裙", "温暖的料理", "美食食谱", "可可萝的笑容", "公主之心", "可可萝的发夹", "厨师的骄傲"]}
        },
        "voice_dir": "kkr"
    },
    "大芋头王": {
        "name": "大芋头王",
        "description": "巨大的芋头成精，散发着香甜诱人的气息",
        "shield": 25,  # 护盾值25%，芋头的厚实外皮
        "phases": [
            {"phase": 1, "max_hp": 15000, "name": "香甜表皮"},
            {"phase": 2, "max_hp": 35000, "name": "软糯内心"},
            {"phase": 3, "max_hp": 120000, "name": "芋头之王"}
        ],
        "rewards": {
            1: {"coins": [10000, 15000], "items": ["芋头片", "烤芋头", "芋头泥"]},
            2: {"coins": [20000, 30000], "items": ["芋头片", "烤芋头", "芋头泥", "金芋头", "芋头王冠"]},
            3: {"coins": [30000, 50000], "items": ["芋头片", "烤芋头", "芋头泥", "金芋头", "芋头王冠", "芋头圣杯", "芋头权杖"]}
        },
        "voice_dir": "taro"
    },
    "圆头耄耋": {
        "name": "圆头耄耋",
        "description": "我这个级别的基米，可以哈任何人！！！",
        "shield": 20,  # 护盾值20%，基米的天然抗性
        "phases": [
            {"phase": 1, "max_hp": 18000, "name": "圆头凝视"},
            {"phase": 2, "max_hp": 40000, "name": "哈气震场"},
            {"phase": 3, "max_hp": 150000, "name": "猫界霸主"}
        ],
        "rewards": {
            1: {"coins": [12000, 18000], "items": ["哈基米毛发", "耄耋碎片", "哈气表情包"]},
            2: {"coins": [25000, 35000], "items": ["哈基米毛发", "耄耋碎片", "哈气表情包", "哈基米徽章", "哈气尖牙"]},
            3: {"coins": [40000, 60000], "items": ["哈基米毛发", "耄耋碎片", "哈气表情包", "哈基米徽章", "哈气尖牙", "耄耋王冠", "南北绿豆"]}
        },
        "voice_dir": "hjm"
    }
}

# 全局Boss状态数据
world_boss_data = {}
world_boss_damage_records = {}  # 记录每个用户对boss造成的伤害
daily_attack_counts = {}  # 记录每个用户每日攻击次数

def clean_nickname(nickname: str) -> str:
    """清理昵称，去除图片文件后缀"""
    if not nickname:
        return nickname
    
    # 常见的图片文件扩展名
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.ico']
    
    # 使用正则表达式匹配并去除图片后缀（不区分大小写）
    pattern = r'(' + '|'.join(re.escape(ext) for ext in image_extensions) + r')$'
    cleaned_nickname = re.sub(pattern, '', nickname, flags=re.IGNORECASE)
    
    return cleaned_nickname.strip()

def load_world_boss_data():
    """加载世界Boss数据"""
    global world_boss_data, world_boss_damage_records, daily_attack_counts

    # 使用正确的数据目录路径
    from ..config.settings import DATA_DIR
    boss_data_file = os.path.join(DATA_DIR, 'world_boss_data.json')
    damage_records_file = os.path.join(DATA_DIR, 'world_boss_damage_records.json')
    daily_attacks_file = os.path.join(DATA_DIR, 'daily_attack_counts.json')
    
    # 加载Boss状态数据
    if not os.path.exists(boss_data_file):
        # 初始化第一个Boss
        world_boss_data = initialize_new_boss("可可萝（黑化）")
        save_world_boss_data()
    else:
        with open(boss_data_file, 'r', encoding='utf-8') as f:
            world_boss_data = json.load(f)
        
        # 数据兼容性检查 - 确保包含所有必需字段
        required_fields = ["name", "description", "current_phase", "current_hp", "max_hp", "phase_name", "is_defeated"]
        if not world_boss_data or not all(field in world_boss_data for field in required_fields):
            print("[世界Boss] 检测到数据格式不兼容，重新初始化Boss数据...")
            world_boss_data = initialize_new_boss("可可萝（黑化）")
            save_world_boss_data()
    
    # 加载伤害记录
    if not os.path.exists(damage_records_file):
        world_boss_damage_records = {}
        save_world_boss_damage_records()
    else:
        with open(damage_records_file, 'r', encoding='utf-8') as f:
            world_boss_damage_records = json.load(f)
    
    # 加载每日攻击次数
    if not os.path.exists(daily_attacks_file):
        daily_attack_counts = {}
        save_daily_attack_counts()
    else:
        with open(daily_attacks_file, 'r', encoding='utf-8') as f:
            daily_attack_counts = json.load(f)
        
        # 检查是否需要重置每日攻击次数（新的一天）
        today = datetime.now().strftime("%Y-%m-%d")
        if daily_attack_counts.get("last_reset_date") != today:
            print(f"[世界Boss] 检测到新的一天，重置每日攻击次数")
            daily_attack_counts = {
                "last_reset_date": today,
                "counts": {}
            }
            save_daily_attack_counts()

def save_world_boss_data():
    """保存世界Boss数据"""
    from ..config.settings import DATA_DIR
    boss_data_file = os.path.join(DATA_DIR, 'world_boss_data.json')
    with open(boss_data_file, 'w', encoding='utf-8') as f:
        json.dump(world_boss_data, f, ensure_ascii=False, indent=4)

def save_world_boss_damage_records():
    """保存伤害记录"""
    from ..config.settings import DATA_DIR
    damage_records_file = os.path.join(DATA_DIR, 'world_boss_damage_records.json')
    with open(damage_records_file, 'w', encoding='utf-8') as f:
        json.dump(world_boss_damage_records, f, ensure_ascii=False, indent=4)

def save_daily_attack_counts():
    """保存每日攻击次数"""
    from ..config.settings import DATA_DIR
    daily_attacks_file = os.path.join(DATA_DIR, 'daily_attack_counts.json')
    with open(daily_attacks_file, 'w', encoding='utf-8') as f:
        json.dump(daily_attack_counts, f, ensure_ascii=False, indent=4)

def reset_phase_attack_counts():
    """重置阶段出刀次数（保留排名数据）"""
    global daily_attack_counts
    print("[世界Boss] 阶段切换，重置出刀次数但保留排名数据")
    
    # 保留日期但清空出刀次数
    today = datetime.now().strftime("%Y-%m-%d")
    daily_attack_counts = {
        "last_reset_date": today,
        "counts": {}
    }
    save_daily_attack_counts()
    print("[世界Boss] 阶段出刀次数重置完成，所有玩家可以重新攻击")

def initialize_new_boss(boss_name: str) -> dict:
    """初始化新的世界Boss"""
    if boss_name not in WORLD_BOSS_CONFIG:
        return {}
    
    config = WORLD_BOSS_CONFIG[boss_name]
    return {
        "name": boss_name,
        "description": config["description"],
        "current_phase": 1,
        "current_hp": config["phases"][0]["max_hp"],
        "max_hp": config["phases"][0]["max_hp"],
        "phase_name": config["phases"][0]["name"],
        "is_defeated": False,
        "created_at": datetime.now().isoformat(),
        "last_attack_time": None
    }

def calculate_damage(user_id: str, boss_name: str = "可可萝（黑化）") -> Tuple[int, str]:
    """计算用户对Boss造成的伤害
    
    Args:
        user_id: 用户ID
        boss_name: Boss名称，用于计算特定属性加成
    
    Returns:
        Tuple[int, str]: (伤害值, 详细计算信息)
    """
    # 获取老婆数据
    wife_data = get_user_wife_data(user_id)
    if not wife_data:
        return 0, "你还没有老婆，无法参与战斗！"
    
    user_data_obj = get_user_data(user_id)
    
    # 基础属性
    level = wife_data[5]  # 等级
    base_moe_value = wife_data[14]  # 妹抖值
    base_spoil_value = wife_data[15]  # 撒娇值  
    base_tsundere_value = wife_data[16]  # 傲娇值
    base_dark_rate = wife_data[17]  # 黑化率
    base_contrast_cute = wife_data[18]  # 反差萌
    
    # 装备加成计算 - 使用统一的服装系统
    equipment = user_data_obj.get("equipment", {})
    
    # 使用统一的服装装备效果计算
    from ..config.costume_config import calculate_equipment_effects, get_costume_by_name
    equipment_effects, set_bonus = calculate_equipment_effects(equipment)
    
    # 计算加成后的最终属性值
    final_moe_value = base_moe_value * (1 + equipment_effects["moe_value"] / 100)
    final_spoil_value = base_spoil_value * (1 + equipment_effects["spoil_value"] / 100)
    final_tsundere_value = base_tsundere_value * (1 + equipment_effects["tsundere_value"] / 100)
    final_dark_rate = base_dark_rate * (1 + equipment_effects["dark_rate"] / 100)
    final_contrast_cute = base_contrast_cute * (1 + equipment_effects["contrast_cute"] / 100)
    
    # 构建装备信息显示
    equipment_info = []
    for slot, item_name in equipment.items():
        if item_name:
            costume = get_costume_by_name(item_name)
            if costume and "effects" in costume:
                item_bonuses = []
                effects = costume["effects"]
                
                if effects.get("moe_value", 0) > 0:
                    item_bonuses.append(f"妹抖+{effects['moe_value']}%")
                if effects.get("spoil_value", 0) > 0:
                    item_bonuses.append(f"撒娇+{effects['spoil_value']}%")
                if effects.get("tsundere_value", 0) > 0:
                    item_bonuses.append(f"傲娇+{effects['tsundere_value']}%")
                if effects.get("dark_rate", 0) > 0:
                    item_bonuses.append(f"黑化+{effects['dark_rate']}%")
                if effects.get("contrast_cute", 0) > 0:
                    item_bonuses.append(f"反差萌+{effects['contrast_cute']}%")
                
                if item_bonuses:
                    equipment_info.append(f"{item_name}({','.join(item_bonuses)})")
    
    # 添加套装效果信息
    if set_bonus:
        equipment_info.append(f"套装效果({set_bonus['bonus_description']})")
    
    # 基础伤害计算
    # 等级影响 (1-100级，基础倍数0.5-5.0)
    level_multiplier = min(0.5 + (level * 0.045), 5.0)
    
    # 特殊属性影响 - 使用加成后的属性值，考虑Boss免疫
    special_multiplier = 1.0
    
    # 妹抖值 - 可可萝免疫
    if "可可萝" not in boss_name:
        special_multiplier += final_moe_value * 0.013  # 妹抖值每点+1.3%
    
    # 撒娇值 - 圆头耄耋免疫
    if "圆头耄耋" not in boss_name:
        special_multiplier += final_spoil_value * 0.014  # 撒娇值每点+1.4%
    
    # 傲娇值 - 大芋头王免疫
    if "芋头" not in boss_name:
        special_multiplier += final_tsundere_value * 0.013  # 傲娇值每点+1.3%
    
    # 黑化率和反差萌不被免疫
    special_multiplier += final_dark_rate * 0.03  # 黑化率每点+3%
    special_multiplier += final_contrast_cute * 0.02  # 反差萌每点+2%
    
    # 随机波动 (80%-120%)
    random_multiplier = random.uniform(0.8, 1.2)
    
    # 最终伤害计算 (去掉了好感度影响)
    base_damage = 100  # 基础伤害
    raw_damage = int(base_damage * level_multiplier * special_multiplier * random_multiplier)
    
    # 应用Boss护盾减伤
    shield_percentage = 0
    if boss_name in WORLD_BOSS_CONFIG:
        shield_percentage = WORLD_BOSS_CONFIG[boss_name].get("shield", 0)
    
    # 计算护盾减伤后的最终伤害
    shield_reduction = raw_damage * (shield_percentage / 100)
    final_damage = int(raw_damage - shield_reduction)
    
    # 确保最小伤害
    final_damage = max(final_damage, 10)
    
    # 构建详细信息
    detail_info = f"等级x{level_multiplier:.2f} + 特殊属性x{special_multiplier:.2f} + 随机x{random_multiplier:.2f}"
    if equipment_info:
        detail_info += f" + 装备[{','.join(equipment_info)}]"
    
    # 添加护盾减伤信息
    if shield_percentage > 0:
        detail_info += f" - 护盾减伤{shield_percentage}%({int(shield_reduction)})"
    
    # 打印详细的伤害计算日志
    wife_name = clean_nickname(wife_data[0]) if wife_data else "未知"
    print(f"[世界Boss] ===== 伤害计算详情 =====")
    print(f"[世界Boss] 用户ID: {user_id}")
    print(f"[世界Boss] 老婆: {wife_name} | 等级: {level}")
    print(f"[世界Boss] 基础属性: 妹抖{base_moe_value} 撒娇{base_spoil_value} 傲娇{base_tsundere_value} 黑化{base_dark_rate} 反差萌{base_contrast_cute}")
    
    if equipment_info:
        print(f"[世界Boss] 装备加成: {' | '.join(equipment_info)}")
        print(f"[世界Boss] 最终属性: 妹抖{final_moe_value:.1f} 撒娇{final_spoil_value:.1f} 傲娇{final_tsundere_value:.1f} 黑化{final_dark_rate:.1f} 反差萌{final_contrast_cute:.1f}")
    else:
        print(f"[世界Boss] 装备: 无装备加成")
    
    # 显示护盾信息
    if shield_percentage > 0:
        print(f"[世界Boss] Boss护盾: {shield_percentage}% 减伤")
        print(f"[世界Boss] 计算过程: 基础{base_damage} × 等级{level_multiplier:.2f} × 特殊属性{special_multiplier:.2f} × 随机{random_multiplier:.2f} = {raw_damage} (原始伤害)")
        print(f"[世界Boss] 护盾减伤: {raw_damage} - {int(shield_reduction)} = {final_damage} (最终伤害)")
    else:
        print(f"[世界Boss] 计算过程: 基础{base_damage} × 等级{level_multiplier:.2f} × 特殊属性{special_multiplier:.2f} × 随机{random_multiplier:.2f} = {final_damage}")
    
    print(f"[世界Boss] 最终伤害: {final_damage}")
    print(f"[世界Boss] ========================")
    
    return final_damage, detail_info

def attack_world_boss(user_id: str, nickname: str, group_id: str) -> dict:
    """攻击世界Boss
    
    Returns:
        dict: 攻击结果，包含伤害、Boss状态变化等信息
    """
    global world_boss_data, world_boss_damage_records, daily_attack_counts
    
    # 检查是否在Boss刷新时间段内 (23:55-00:05)
    current_time = datetime.now()
    current_hour = current_time.hour
    current_minute = current_time.minute
    
    # 23:55-23:59 或 00:00-00:05 这些时间不能攻击
    if (current_hour == 23 and current_minute >= 55) or (current_hour == 0 and current_minute <= 5):
        return {"success": False, "message": "Boss刷新时间段(23:55-00:05)，暂时无法攻击！请稍后再试。"}
    
    # 检查Boss是否存在并且数据完整
    if not world_boss_data or world_boss_data.get("is_defeated", True):
        return {"success": False, "message": "当前没有可攻击的世界Boss！"}
    
    # 额外安全检查 - 确保必需字段存在
    required_fields = ["current_phase", "current_hp", "max_hp", "name"]
    if not all(field in world_boss_data for field in required_fields):
        print("[世界Boss] 数据字段不完整，尝试重新初始化...")
        # 重新加载数据
        load_world_boss_data()
        if not world_boss_data or not all(field in world_boss_data for field in required_fields):
            return {"success": False, "message": "世界Boss数据异常，请联系管理员！"}
    
    # 检查每日攻击次数限制
    today = datetime.now().strftime("%Y-%m-%d")
    if daily_attack_counts.get("last_reset_date") != today:
        # 如果是新的一天，重置攻击次数
        daily_attack_counts = {
            "last_reset_date": today,
            "counts": {}
        }
        save_daily_attack_counts()
    
    user_attack_count = daily_attack_counts.get("counts", {}).get(user_id, 0)
    if user_attack_count >= 5:
        return {"success": False, "message": f"你此阶段已经攻击了{user_attack_count}次Boss，每天最多只能攻击5次！请明天再来！"}
    
    # 检查老婆是否存在
    wife_data = get_user_wife_data(user_id)
    if not wife_data:
        return {"success": False, "message": "你还没有老婆，无法参与战斗！"}
    
    # 检查健康值是否足够
    current_health = wife_data[9]  # 健康值在索引9
    if current_health < 30:
        return {"success": False, "message": f"老婆健康值不足(当前{current_health})，需要至少30点健康值才能参战！"}
    
    # 计算伤害
    boss_name = world_boss_data["name"]
    damage, damage_detail = calculate_damage(user_id, boss_name)
    
    # 检查阶段伤害阈值
    current_phase = world_boss_data["current_phase"]
    
    # # 2阶段需要至少1000伤害才能破防
    # if current_phase == 2 and damage < 1000:
    #     if "可可萝" in boss_name:
    #         message = f"你的攻击只造成了{damage}点伤害！\n可可萝的【极光护盾】闪闪发光，完全挡住了你的攻击！\n( ´∀｀)σ"
    #     elif "芋头" in boss_name:
    #         message = f"你的攻击只造成了{damage}点伤害！\n大芋头王的【软糯护壁】弹性十足，吸收了你的攻击！\n(๑´ڡ`๑)"
    #     else:
    #         message = f"你的攻击只造成了{damage}点伤害！\nBoss的防护完全挡住了你的攻击！"
        
    #     return {
    #         "success": False,
    #         "message": message
    #     }
    
    # # 3阶段需要至少3000伤害才能破防  
    # if current_phase == 3 and damage < 3000:
    #     if "可可萝" in boss_name:
    #         message = f"你的攻击只造成了{damage}点伤害！\n【精灵启示】的神圣光芒包围着可可萝，你的攻击被完全无效化了！\n(｡◕∀◕｡) ~"
    #     elif "芋头" in boss_name:
    #         message = f"你的攻击只造成了{damage}点伤害！\n【芋头之王】的威严不可侵犯，香甜的气息化解了你的攻击！\n(◕‿◕)♡"
    #     else:
    #         message = f"你的攻击只造成了{damage}点伤害！\nBoss的最终防护完全无效化了你的攻击！"
        
    #     return {
    #         "success": False,
    #         "message": message
    #     }
    
    # 攻击成功，扣除健康值
    update_user_wife_data(user_id, health=current_health - 30)
    
    # 更新每日攻击次数
    if "counts" not in daily_attack_counts:
        daily_attack_counts["counts"] = {}
    daily_attack_counts["counts"][user_id] = daily_attack_counts["counts"].get(user_id, 0) + 1
    
    # 记录伤害
    clean_nick = clean_nickname(nickname)  # 清理昵称
    clean_wife_name = clean_nickname(wife_data[0])  # 清理老婆名字，去除图片后缀
    if user_id not in world_boss_damage_records:
        world_boss_damage_records[user_id] = {
            "total_damage": 0,
            "attack_count": 0,
            "nickname": clean_nick,
            "wife_name": clean_wife_name,
            "group_id": group_id
        }
    
    world_boss_damage_records[user_id]["total_damage"] += damage
    world_boss_damage_records[user_id]["attack_count"] += 1
    world_boss_damage_records[user_id]["nickname"] = clean_nick  # 更新昵称
    world_boss_damage_records[user_id]["wife_name"] = clean_wife_name  # 更新老婆名字，确保去除图片后缀
    
    # 对Boss造成伤害
    world_boss_data["current_hp"] -= damage
    world_boss_data["last_attack_time"] = datetime.now().isoformat()
    
    # 给予每次攻击的基础奖励 - 根据Boss类型确定奖励物品
    base_reward_coins = random.randint(200, 500)  # 200-500金币
    boss_name = world_boss_data["name"]
    
    if "可可萝" in boss_name:
        # 可可萝相关的基础奖励
        base_reward_items = ["小血瓶", "能量药水", "可可萝的祝福", "公主护身符", "料理残渣"]
    elif "芋头" in boss_name:
        # 大芋头王相关的基础奖励
        base_reward_items = ["小血瓶", "能量药水", "芋头渣", "芋头种子", "香甜精华"]
    elif "圆头耄耋" in boss_name:
        # 圆头耄耋相关的基础奖励
        base_reward_items = ["小血瓶", "能量药水", "哈基米胡须", "圆头护符", "哈气精华"]
    else:
        # 默认奖励
        base_reward_items = ["小血瓶", "能量药水", "经验药水", "金币袋", "勇气徽章"]
    
    selected_item = random.choice(base_reward_items)
    
    # 发放基础奖励
    user_data_obj = get_user_data(user_id)
    user_data_obj["coins"] += base_reward_coins
    
    # 发放基础战利品
    if selected_item not in user_data_obj["trophies"]:
        user_data_obj["trophies"][selected_item] = 0
    user_data_obj["trophies"][selected_item] += 1
    
    save_user_data()  # 保存用户数据
    
    result = {
        "success": True,
        "damage": damage,
        "damage_detail": damage_detail,
        "boss_current_hp": world_boss_data["current_hp"],
        "boss_max_hp": world_boss_data["max_hp"],
        "boss_name": world_boss_data["name"],  # 添加Boss名称，确保语音播放正确
        "phase_defeated": False,
        "boss_defeated": False,
        "phase_rewards": None,
        "final_rewards": None,
        "base_reward_coins": base_reward_coins,
        "base_reward_item": selected_item
    }
    
    # 检查是否击败当前阶段
    if world_boss_data["current_hp"] <= 0:
        current_phase = world_boss_data["current_phase"]
        boss_name = world_boss_data["name"]
        
        # 发放阶段奖励
        phase_rewards = distribute_phase_rewards(current_phase, boss_name)
        result["phase_rewards"] = phase_rewards
        result["phase_defeated"] = True
        result["defeated_phase"] = current_phase
        
        # 检查是否还有下一阶段
        boss_config = WORLD_BOSS_CONFIG[boss_name]
        if current_phase < len(boss_config["phases"]):
            # 进入下一阶段
            next_phase = current_phase + 1
            next_phase_config = boss_config["phases"][next_phase - 1]
            
            world_boss_data["current_phase"] = next_phase
            world_boss_data["current_hp"] = next_phase_config["max_hp"]
            world_boss_data["max_hp"] = next_phase_config["max_hp"]
            world_boss_data["phase_name"] = next_phase_config["name"]
            
            # 重置出刀次数但保留排名（伤害记录不重置，累加排名）
            reset_phase_attack_counts()
            
            result["next_phase"] = next_phase
            result["next_phase_name"] = next_phase_config["name"]
            result["next_phase_hp"] = next_phase_config["max_hp"]
        else:
            # Boss完全被击败
            world_boss_data["is_defeated"] = True
            final_rewards = generate_final_ranking()
            result["boss_defeated"] = True
            result["final_rewards"] = final_rewards
    
    # 保存数据
    save_world_boss_data()
    save_world_boss_damage_records()
    save_daily_attack_counts()
    
    return result

def distribute_phase_rewards(phase: int, boss_name: str) -> dict:
    """分发阶段奖励"""
    if boss_name not in WORLD_BOSS_CONFIG:
        return {}
    
    rewards_config = WORLD_BOSS_CONFIG[boss_name]["rewards"][phase]
    rewards_distributed = {}
    
    print(f"[世界Boss] 开始发放第{phase}阶段奖励给{len(world_boss_damage_records)}名参与者")
    
    # 按伤害排序生成排行榜
    damage_ranking = sorted(world_boss_damage_records.items(), 
                           key=lambda x: x[1]["total_damage"], 
                           reverse=True)
    
    # 排名奖励配置
    ranking_rewards = {
        1: 3000,  # 第一名3000金币
        2: 2000,  # 第二名2000金币
        3: 1000   # 第三名1000金币
    }
    
    for rank, (user_id, damage_data) in enumerate(damage_ranking, 1):
        if damage_data["total_damage"] > 0:
            # 计算基础金币奖励
            coin_min, coin_max = rewards_config["coins"]
            coins_reward = random.randint(coin_min, coin_max)
            
            # 添加排名奖励
            ranking_bonus = ranking_rewards.get(rank, 0)
            total_coins = coins_reward + ranking_bonus
            
            # 随机选择1-3个物品奖励
            items_reward = random.sample(rewards_config["items"], min(random.randint(1, 3), len(rewards_config["items"])))
            
            print(f"[世界Boss] 给用户{user_id}({damage_data['nickname']})发放奖励: 基础{coins_reward}金币 + 排名奖励{ranking_bonus}金币 = 总计{total_coins}金币, {items_reward}")
            
            # 发放奖励 - 获取用户数据
            user_data_obj = get_user_data(user_id)
            old_coins = user_data_obj["coins"]
            
            # 发放金币
            user_data_obj["coins"] += total_coins
            
            # 发放物品到战利品（不是背包！）
            for item in items_reward:
                if item not in user_data_obj["trophies"]:
                    user_data_obj["trophies"][item] = 0
                user_data_obj["trophies"][item] += 1
                print(f"[世界Boss] 添加物品 {item} 到用户 {user_id} 战利品, 当前数量: {user_data_obj['trophies'][item]}")
            
            # 立即保存用户数据
            save_user_data()
            
            # 验证数据是否保存成功
            verify_data = get_user_data(user_id)
            print(f"[世界Boss] 验证保存结果 - 用户{user_id}:")
            print(f"  金币: {old_coins} -> {verify_data['coins']} (应该是{old_coins + total_coins})")
            for item in items_reward:
                print(f"  战利品 {item}: {verify_data['trophies'].get(item, 0)} (应该>=1)")
            
            print(f"[世界Boss] 用户{user_id}战利品当前状态: {dict(list(verify_data['trophies'].items())[-5:])}")
            
            rewards_distributed[user_id] = {
                "nickname": clean_nickname(damage_data["nickname"]),  # 确保昵称干净
                "coins": coins_reward,
                "ranking_bonus": ranking_bonus,
                "total_coins": total_coins,
                "items": items_reward,
                "total_damage": damage_data["total_damage"],
                "rank": rank
            }
    
    print(f"[世界Boss] 第{phase}阶段奖励发放完成，共{len(rewards_distributed)}名勇士获得奖励")
    return rewards_distributed

def generate_final_ranking() -> dict:
    """生成最终排行榜"""
    # 按伤害排序
    ranking = sorted(world_boss_damage_records.items(), 
                    key=lambda x: x[1]["total_damage"], 
                    reverse=True)
    
    ranking_data = {
        "ranking": [],
        "total_participants": len(ranking),
        "total_damage": sum(data["total_damage"] for _, data in ranking)
    }
    
    for i, (user_id, damage_data) in enumerate(ranking, 1):
        ranking_data["ranking"].append({
            "rank": i,
            "user_id": user_id,
            "nickname": clean_nickname(damage_data["nickname"]),  # 确保昵称干净
            "wife_name": damage_data["wife_name"],
            "total_damage": damage_data["total_damage"],
            "attack_count": damage_data["attack_count"]
        })
    
    return ranking_data

def get_world_boss_status() -> dict:
    """获取世界Boss状态"""
    if not world_boss_data:
        return {"exists": False}
    
    # 检查数据完整性
    required_fields = ["name", "description", "current_phase", "phase_name", "current_hp", "max_hp", "is_defeated"]
    if not all(field in world_boss_data for field in required_fields):
        print("[世界Boss] get_world_boss_status: 数据字段不完整，尝试重新初始化...")
        load_world_boss_data()
        if not world_boss_data or not all(field in world_boss_data for field in required_fields):
            return {"exists": False}
    
    # 获取伤害排行榜（前10名）
    damage_ranking = sorted(world_boss_damage_records.items(), 
                           key=lambda x: x[1]["total_damage"], 
                           reverse=True)[:10]
    
    ranking_display = []
    for i, (user_id, damage_data) in enumerate(damage_ranking, 1):
        ranking_display.append({
            "rank": i,
            "nickname": clean_nickname(damage_data["nickname"]),  # 确保昵称干净
            "wife_name": damage_data["wife_name"],
            "total_damage": damage_data["total_damage"],
            "attack_count": damage_data["attack_count"]
        })
    
    # 获取Boss护盾信息
    boss_name = world_boss_data["name"]
    shield_percentage = 0
    if boss_name in WORLD_BOSS_CONFIG:
        shield_percentage = WORLD_BOSS_CONFIG[boss_name].get("shield", 0)
    
    return {
        "exists": True,
        "name": world_boss_data["name"],
        "description": world_boss_data["description"],
        "current_phase": world_boss_data["current_phase"],
        "phase_name": world_boss_data["phase_name"],
        "current_hp": world_boss_data["current_hp"],
        "max_hp": world_boss_data["max_hp"],
        "shield": shield_percentage,
        "is_defeated": world_boss_data.get("is_defeated", False),
        "total_participants": len(world_boss_damage_records),
        "total_damage_dealt": sum(data["total_damage"] for data in world_boss_damage_records.values()),
        "ranking": ranking_display
    }

def get_daily_boss_name():
    """根据当前日期确定今天的Boss"""
    import hashlib
    
    # 获取今天的日期
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 使用日期的哈希值来决定Boss，这样每天的Boss是固定的但看起来随机
    hash_value = int(hashlib.md5(today.encode()).hexdigest(), 16)
    
    boss_list = ["可可萝（黑化）", "大芋头王", "圆头耄耋"]
    boss_index = hash_value % len(boss_list)
    
    return boss_list[boss_index]

def reset_world_boss(boss_name=None):
    """重置世界Boss（每天自动调用或管理员指定）"""
    global world_boss_data, world_boss_damage_records, daily_attack_counts
    
    # 如果没有指定Boss名称，则使用今日Boss
    if boss_name is None:
        boss_name = get_daily_boss_name()
    
    # 清空伤害记录
    world_boss_damage_records = {}
    
    # 重置每日攻击次数
    today = datetime.now().strftime("%Y-%m-%d")
    daily_attack_counts = {
        "last_reset_date": today,
        "counts": {}
    }
    
    # 初始化指定的Boss
    world_boss_data = initialize_new_boss(boss_name)
    
    save_world_boss_data()
    save_world_boss_damage_records()
    save_daily_attack_counts()
    
    print(f"[世界Boss] 已重置为新Boss: {boss_name}")
    return boss_name

def check_and_refresh_daily_boss():
    """检查并刷新每日Boss"""
    try:
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # 检查Boss是否需要刷新
        if not world_boss_data:
            # 没有Boss数据，初始化今日Boss
            boss_name = reset_world_boss()
            return boss_name
        
        # 检查Boss创建日期
        boss_created_date = world_boss_data.get("created_at", "")
        if boss_created_date:
            try:
                created_datetime = datetime.fromisoformat(boss_created_date)
                created_date = created_datetime.strftime("%Y-%m-%d")
                
                if created_date != current_date:
                    # Boss需要刷新
                    boss_name = reset_world_boss()
                    print(f"[世界Boss] 检测到新的一天，自动刷新Boss为: {boss_name}")
                    return boss_name
            except Exception as e:
                print(f"[世界Boss] 解析Boss创建时间失败: {e}")
                # 如果解析失败，重新创建Boss
                boss_name = reset_world_boss()
                return boss_name
        
        # Boss不需要刷新，返回当前Boss名称
        return world_boss_data.get("name", "可可萝（黑化）")
        
    except Exception as e:
        print(f"[世界Boss] 检查Boss刷新时出错: {e}")
        # 出错时初始化一个新Boss
        return reset_world_boss()

# 初始化数据
def initialize_world_boss_data():
    """初始化世界Boss数据"""
    try:
        load_world_boss_data()
        
        # 检查并刷新每日Boss
        current_boss_name = check_and_refresh_daily_boss()
        
        boss_name = world_boss_data.get('name', '无')
        current_phase = world_boss_data.get('current_phase', '未知')
        current_hp = world_boss_data.get('current_hp', '未知')
        print(f"世界Boss系统初始化完成，当前Boss: {boss_name}, 阶段: {current_phase}, 血量: {current_hp}")
        print(f"世界Boss数据字段: {list(world_boss_data.keys()) if world_boss_data else '空'}")
        
        return current_boss_name
    except Exception as e:
        print(f"世界Boss系统初始化失败: {e}")
        import traceback
        traceback.print_exc()
        return None
