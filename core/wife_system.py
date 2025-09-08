"""老婆系统核心模块"""
import random
import requests
import os
from datetime import datetime, timedelta
from ..config.settings import *
from ..config.messages import ANIMEWIFE_FAIL_EVENTS, DIVORCE_FAIL_EVENTS
from .data_manager import *

def get_taken_wives():
    """获取已经被占用的老婆文件名列表"""
    import json
    from ..config.settings import GLOBAL_WIFE_DATA_FILE
    
    taken_wives = []
    
    # 直接读取文件，避免模块级变量作用域问题
    try:
        if os.path.exists(GLOBAL_WIFE_DATA_FILE):
            with open(GLOBAL_WIFE_DATA_FILE, 'r', encoding='utf-8') as f:
                wife_data_dict = json.load(f)
            
            print(f"[Debug] 直接从文件读取，老婆数据数量: {len(wife_data_dict)}")
            print(f"[Debug] 用户列表: {list(wife_data_dict.keys())[:5]}")
            
            for user_id, wife_data in wife_data_dict.items():
                if wife_data and len(wife_data) > 0:
                    wife_filename = wife_data[0]  # 老婆文件名在索引0
                    taken_wives.append(wife_filename)
                    # print(f"[Debug] 用户 {user_id} 拥有老婆: {wife_filename}")
            
            print(f"[Debug] 已占用老婆总数: {len(taken_wives)}")
        else:
            print(f"[Debug] 老婆数据文件不存在: {GLOBAL_WIFE_DATA_FILE}")
            
    except Exception as e:
        print(f"[Debug] 读取老婆数据文件时出错: {e}")
        import traceback
        traceback.print_exc()
    
    return taken_wives

def is_wife_available(wife_filename: str):
    """检查指定的老婆是否可用（未被占用）"""
    taken_wives = get_taken_wives()
    return wife_filename not in taken_wives

def get_available_wives():
    """获取可用老婆列表（过滤掉已被占用的老婆）"""
    try:
        all_wives = []
        
        # 尝试从本地文件夹获取图片列表
        if os.path.exists(IMG_DIR):
            local_images = os.listdir(IMG_DIR)
            if local_images:
                all_wives = local_images.copy()
        
        # 如果本地没有图片，从网址获取
        if not all_wives:
            response = requests.get(IMAGE_BASE_URL)
            if response.status_code == 200:
                all_wives = response.text.splitlines()
        
        if not all_wives:
            return []
        
        # 获取已被占用的老婆列表
        taken_wives = get_taken_wives()
        print(f'所有老婆图片数量: {len(all_wives)}')
        print(f'已被占用的老婆数量: {len(taken_wives)}')
        
        # 过滤掉已被占用的老婆
        available_wives = [wife for wife in all_wives if wife not in taken_wives]
        print(f'可用老婆数量: {len(available_wives)}')
        
        # 显示一些示例
        if taken_wives:
            print(f'已占用的老婆示例: {taken_wives[:3]}')
        if available_wives:
            print(f'可用老婆示例: {available_wives[:3]}')
        
        return available_wives
        
    except Exception as e:
        print(f'获取老婆列表时发生错误: {str(e)}')
        import traceback
        traceback.print_exc()
        return []

def select_candidate_wives(available_wives: list, count: int = 10):
    """从可用老婆中选择候选者"""
    if len(available_wives) < count:
        return available_wives.copy()
    else:
        return random.sample(available_wives, count)

def has_random_fail_event(fail_rate: float = 0.10):
    """判断是否触发随机失败事件"""
    return random.random() < fail_rate

def get_random_fail_event():
    """获取随机失败事件"""
    return random.choice(ANIMEWIFE_FAIL_EVENTS)

def get_random_divorce_fail_event():
    """获取随机离婚失败事件"""
    return random.choice(DIVORCE_FAIL_EVENTS)

def check_animewife_cooldown(user_id: str, cooldown_minutes: int = 1):
    """检查抽老婆冷却时间"""
    current_time = datetime.now()
    if user_id in animewife_cooldown:
        last_animewife_time = animewife_cooldown[user_id]
        cooldown_period = timedelta(minutes=cooldown_minutes)
        if current_time < last_animewife_time + cooldown_period:
            remaining = last_animewife_time + cooldown_period - current_time
            seconds = int(remaining.total_seconds())
            return False, seconds
    return True, 0

def update_animewife_cooldown(user_id: str):
    """更新抽老婆冷却时间"""
    animewife_cooldown[user_id] = datetime.now()

def store_candidate_wives(user_id: str, candidates: list):
    """存储候选老婆列表"""
    candidate_wives[user_id] = candidates

def get_candidate_wives(user_id: str):
    """获取候选老婆列表"""
    return candidate_wives.get(user_id, [])

def clear_candidate_wives(user_id: str):
    """清除候选老婆列表"""
    if user_id in candidate_wives:
        del candidate_wives[user_id]

def find_wife_in_candidates(user_id: str, wife_name_input: str):
    """在候选列表中查找匹配的老婆，并检查是否可用"""
    candidates = get_candidate_wives(user_id)
    for wife_file in candidates:
        wife_display_name = wife_file.split('.')[0]
        if wife_display_name.lower() == wife_name_input.lower() or wife_name_input.lower() in wife_display_name.lower():
            # 在返回之前检查该老婆是否仍然可用
            if is_wife_available(wife_file):
                return wife_file
            else:
                print(f'老婆 {wife_display_name} 已经被其他用户占用，无法确认')
                return "TAKEN"  # 返回特殊值表示已被占用
    return None

def get_wife_image_path(wife_name: str):
    """获取老婆图片路径"""
    local_path = os.path.join(IMG_DIR, wife_name)
    if os.path.exists(local_path):
        return local_path, True  # 本地图片
    else:
        return IMAGE_BASE_URL + wife_name, False  # 网络图片
