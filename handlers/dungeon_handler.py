"""地下城处理器"""
import random
import re
from datetime import datetime, timedelta
from astrbot.api.all import *
from ..core.data_manager import *
from ..config.dungeon_config import DUNGEON_LIST, DUNGEON_REWARDS, DUNGEON_COOLDOWN_HOURS
from ..utils.experience_utils import process_experience_gain

class DungeonHandler:
    def __init__(self):
        pass

    def parse_dungeon_id(self, message_str):
        """解析地下城序号"""
        # 提取 "前往地下城 1" 中的数字
        match = re.search(r'前往地下城\s*(\d+)', message_str)
        if match:
            return int(match.group(1))
        return None

    async def dungeon_list(self, event: AstrMessageEvent):
        """显示地下城列表"""
        try:
            group_id = event.message_obj.group_id
            if not group_id:
                yield event.plain_result('该功能仅支持群聊，请在群聊中使用。')
                return

            # 构建地下城列表文本
            dungeon_text = "🗡️ 地下城列表 🗡️\n"

            for dungeon in DUNGEON_LIST:
                dungeon_text += f"{dungeon['id']}. {dungeon['name']}：{dungeon['description']}\n"
            dungeon_text += "☁️ 发送 '前往地下城 序号' 进入地下城冒险"
            dungeon_text += f"，冷却时间：{DUNGEON_COOLDOWN_HOURS}小时"

            yield event.plain_result(dungeon_text)

        except Exception as e:
            print(f"[Dungeon Handler] dungeon_list函数发生异常: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f'显示地下城列表时出现错误: {str(e)}')

    async def enter_dungeon(self, event: AstrMessageEvent):
        """进入地下城"""
        try:
            group_id = event.message_obj.group_id
            if not group_id:
                yield event.plain_result('该功能仅支持群聊，请在群聊中使用。')
                return

            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()

            # 检查是否有老婆
            wife_data = get_user_wife_data(user_id)
            if not wife_data:
                yield event.plain_result('你还没有老婆！请先使用"抽老婆"命令抽取一位老婆吧~')
                return

            # 解析地下城序号
            dungeon_id = self.parse_dungeon_id(event.message_str)
            if dungeon_id is None:
                yield event.plain_result('请指定地下城序号！例如：前往地下城 1')
                return

            # 查找对应的地下城
            target_dungeon = None
            for dungeon in DUNGEON_LIST:
                if dungeon['id'] == dungeon_id:
                    target_dungeon = dungeon
                    break

            if not target_dungeon:
                yield event.plain_result(f'地下城序号 {dungeon_id} 不存在！请使用"地下城列表"查看可用的地下城。')
                return

            # 检查等级要求
            wife_level = wife_data[5]  # 老婆等级在索引5
            if wife_level < target_dungeon['min_level']:
                yield event.plain_result(f'老婆等级不足！{target_dungeon["name"]}要求等级{target_dungeon["min_level"]}，你的老婆目前等级{wife_level}。')
                return

            # 检查冷却时间
            user_dungeon_data = get_user_dungeon_data(user_id)
            if user_dungeon_data['last_dungeon_time']:
                last_time = datetime.fromisoformat(user_dungeon_data['last_dungeon_time'])
                cooldown_end = last_time + timedelta(hours=DUNGEON_COOLDOWN_HOURS)
                current_time = datetime.now()
                
                if current_time < cooldown_end:
                    remaining = cooldown_end - current_time
                    hours = int(remaining.total_seconds() // 3600)
                    minutes = int((remaining.total_seconds() % 3600) // 60)
                    yield event.plain_result(f'地下城冷却中！还需等待 {hours}小时{minutes}分钟 才能再次进入地下城。')
                    return

            # 检查老婆状态（饥饿、清洁、健康、心情都需要大于30才能进入地下城）
            hunger = wife_data[7]      # 饥饿度
            cleanliness = wife_data[8]  # 清洁度
            health = wife_data[9]      # 健康度
            mood = wife_data[10]       # 心情

            if hunger < 30 or cleanliness < 30 or health < 30 or mood < 30:
                yield event.plain_result('老婆状态不佳！饥饿度、清洁度、健康度、心情都需要大于30才能进入地下城。请先照顾好老婆！')
                return

            # 开始地下城冒险
            result = self.process_dungeon_battle(user_id, target_dungeon, wife_data)

            # 更新最后进入地下城时间
            update_user_dungeon_data(user_id, 
                                   last_dungeon_time=datetime.now().isoformat(),
                                   total_dungeons=user_dungeon_data['total_dungeons'] + 1)

            yield event.plain_result(result)

        except Exception as e:
            print(f"[Dungeon Handler] enter_dungeon函数发生异常: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f'进入地下城时出现错误: {str(e)}')

    def process_dungeon_battle(self, user_id: str, dungeon: dict, wife_data: list):
        """处理地下城战斗逻辑"""
        try:
            wife_name = wife_data[0].split('.')[0]
            wife_level = wife_data[5]
            
            # 保存原始属性值，防止在更新数据时被修改
            original_hunger = wife_data[7]
            original_cleanliness = wife_data[8]
            original_health = wife_data[9]
            original_mood = wife_data[10]
            
            # 获取老婆的特殊属性（基础值）
            base_moe_value = wife_data[14]      # 妹抖值（武力）
            base_spoil_value = wife_data[15]    # 撒娇值（智力）
            base_tsundere_value = wife_data[16] # 傲娇值（敏捷）
            base_dark_rate = wife_data[17]      # 黑化率（暴击率）
            base_contrast_cute = wife_data[18]  # 反差萌（暴击伤害）
            
            # 获取装备加成效果
            user_data_obj = get_user_data(user_id)
            equipped_items = user_data_obj.get("equipment", {})
            
            from ..config.costume_config import calculate_equipment_effects
            equipment_effects, set_bonus = calculate_equipment_effects(equipped_items)
            
            # 计算最终属性（基础属性 + 装备加成）
            moe_value = int(base_moe_value * (1 + equipment_effects["moe_value"] / 100))
            spoil_value = int(base_spoil_value * (1 + equipment_effects["spoil_value"] / 100))
            tsundere_value = int(base_tsundere_value * (1 + equipment_effects["tsundere_value"] / 100))
            dark_rate = int(base_dark_rate * (1 + equipment_effects["dark_rate"] / 100))
            contrast_cute = int(base_contrast_cute * (1 + equipment_effects["contrast_cute"] / 100))

            # 计算战斗力（重新平衡）
            base_power = wife_level * 5  # 降低等级权重
            attribute_power = moe_value * 1.0 + spoil_value * 0.8 + tsundere_value * 0.9  # 大幅降低属性权重
            total_power = base_power + attribute_power

            # 计算暴击率和暴击伤害
            crit_rate = min(dark_rate * 0.01, 0.3)  # 暴击率最高30%
            crit_damage = 1.2 + contrast_cute * 0.005  # 降低暴击伤害加成

            # 根据战斗力计算可击杀的怪物数量
            kill_results = {}
            total_kills = 0
            total_experience = dungeon['base_experience']  # 使用地下城特定的基础经验
            total_drops = {}  # 改为更准确的名称

            # 创建加权怪物列表
            weighted_monsters = []
            for monster in dungeon['monsters']:
                for _ in range(int(monster['weight'] * 10)):  # 乘以10增加精度
                    weighted_monsters.append(monster)

            # 计算战斗次数：基础50次，最多附加50次
            base_battles = 50  # 基础战斗次数
            # 每10战斗力增加1次额外战斗，最多增加50次
            extra_battles = min(int(total_power / 10), 50)
            max_kills = base_battles + extra_battles

            for _ in range(max_kills):
                if not weighted_monsters:
                    break
                
                # 随机选择怪物
                monster = random.choice(weighted_monsters)
                
                # 重新设计击败几率计算，更加严格的平衡
                monster_difficulty = monster['difficulty']
                
                # 难度差距惩罚（如果怪物难度高于等级，大幅降低成功率）
                level_diff = wife_level - monster_difficulty
                if level_diff >= 0:
                    # 等级相当或更高
                    base_success = 0.6 + (level_diff * 0.15)  # 基础60%，等级优势每级+15%
                else:
                    # 怪物难度更高，大幅惩罚
                    penalty = abs(level_diff) * 0.2
                    base_success = max(0.05, 0.4 - penalty)  # 最低5%，每级差距-20%
                
                # 战斗力加成（大幅降低）
                import math
                power_ratio = total_power / (monster_difficulty * 8)  # 怪物难度作为基准
                power_bonus = min(0.3, math.log(power_ratio + 1) / 5)  # 最多30%加成
                
                # 最终成功率
                success_rate = max(0.01, min(0.85, base_success + power_bonus))  # 最低1%，最高85%
                
                # 暴击判定（降低影响）
                is_crit = random.random() < crit_rate
                if is_crit:
                    success_rate = min(0.9, success_rate * crit_damage)  # 暴击最高90%

                if random.random() < success_rate:
                    # 击杀成功
                    monster_name = monster['name']
                    if monster_name not in kill_results:
                        kill_results[monster_name] = 0
                    kill_results[monster_name] += 1
                    total_kills += 1

                    # 添加到杀怪统计
                    add_kill_stats(user_id, monster_name, 1)

                    # 获得经验
                    total_experience += monster['experience']  # 使用怪物特定的经验值

                    # 处理掉落物品
                    if 'drops' in monster:
                        for drop in monster['drops']:
                            # 根据权重决定是否掉落
                            drop_chance = drop['weight'] / 100.0  # 权重转换为概率
                            if random.random() < drop_chance:
                                item_name = drop['item']
                                if item_name not in total_drops:
                                    total_drops[item_name] = 0
                                total_drops[item_name] += 1

            # 更新用户战利品（添加掉落物品）
            user_data_obj = get_user_data(user_id)
            for item_name, count in total_drops.items():
                if item_name not in user_data_obj['trophies']:
                    user_data_obj['trophies'][item_name] = 0
                user_data_obj['trophies'][item_name] += count

            # 计算金币奖励（基于掉落物品价值）
            total_gold = 0
            for item_name, count in total_drops.items():
                # 在所有怪物的掉落列表中查找该物品的价格
                item_price = 0
                for monster in dungeon['monsters']:
                    if 'drops' in monster:
                        for drop in monster['drops']:
                            if drop['item'] == item_name:
                                item_price = drop['price']
                                break
                        if item_price > 0:
                            break
                total_gold += item_price * count * 0.1  # 获得物品价值10%的金币

            user_data_obj['coins'] += int(total_gold)
            update_user_data(user_id, coins=user_data_obj['coins'], trophies=user_data_obj['trophies'])

            # 更新老婆属性（降低基础属性，提升特殊属性和经验）
            # 计算属性变化
            new_hunger = max(0, original_hunger + DUNGEON_REWARDS['stat_penalty']['hunger'])
            new_cleanliness = max(0, original_cleanliness + DUNGEON_REWARDS['stat_penalty']['cleanliness'])
            new_health = max(0, original_health + DUNGEON_REWARDS['stat_penalty']['health'])
            new_mood = max(0, original_mood + DUNGEON_REWARDS['stat_penalty']['mood'])

            # 增加特殊属性（有概率增加，不是必然的）
            # 注意：这里应该基于基础属性值进行增长，而不是装备加成后的值
            new_moe = base_moe_value
            new_spoil = base_spoil_value  
            new_tsundere = base_tsundere_value

            # 妹抖值（武力）增加 - 70%概率
            if random.random() < 0.7:
                attr_gain = random.randint(DUNGEON_REWARDS['attribute_gain_min'], DUNGEON_REWARDS['attribute_gain_max'])
                new_moe = base_moe_value + attr_gain

            # 撒娇值（智力）增加 - 60%概率
            if random.random() < 0.6:
                new_spoil = base_spoil_value + random.randint(1, 2)

            # 傲娇值（敏捷）增加 - 60%概率
            if random.random() < 0.6:
                new_tsundere = base_tsundere_value + random.randint(1, 2)

            new_dark = dark_rate        # 黑化率（暴击率）保持不变
            new_contrast = contrast_cute # 反差萌（暴击伤害）保持不变

            # 使用新的经验系统处理升级
            current_level = wife_data[5]
            current_growth = wife_data[6]
            
            exp_result = process_experience_gain(current_level, current_growth, total_experience)
            new_level = exp_result["new_level"]
            new_growth = exp_result["new_growth"]
            
            # 生成升级消息
            level_up_msg = ""
            if exp_result["level_up_messages"]:
                level_up_msg = "\n" + "\n".join([msg.replace("升级了！", f"{wife_name}升级了！") for msg in exp_result["level_up_messages"]])

            # 更新老婆数据
            update_user_wife_data(user_id,
                                hunger=new_hunger,
                                cleanliness=new_cleanliness,
                                health=new_health,
                                mood=new_mood,
                                level=new_level,
                                growth=new_growth,
                                moe_value=new_moe,
                                spoil_value=new_spoil,
                                tsundere_value=new_tsundere,
                                dark_rate=new_dark,
                                contrast_cute=new_contrast)

            # 构建结果消息  
            equipment_info = ""
            if any(item for item in equipped_items.values() if item):
                equipment_info = "⚔️ (装备加成已生效) "
            result_msg = f"⚔️ {wife_name}在{dungeon['name']}中的冒险结果 {equipment_info}⚔️\n"
            # result_msg += f"🎯 本次战斗：进行了{max_kills}次战斗（基础{base_battles}次 + 额外{extra_battles}次）\n\n"

            result_msg += f"💰 获得金币：{int(total_gold)}\n"
            result_msg += f"✨ 获得经验：{total_experience}\n"

            result_msg += f"❤️ 老婆变化："
            
            # 构建属性变化信息，只显示有变化的
            attribute_changes = []
            
            # 特殊属性变化（显示基础属性的变化）
            if new_moe != base_moe_value:
                attribute_changes.append(f"妹抖值：{base_moe_value} → {new_moe} (+{new_moe - base_moe_value})")
            else:
                attribute_changes.append(f"妹抖值：{base_moe_value}（无变化）")
                
            if new_spoil != base_spoil_value:
                attribute_changes.append(f"撒娇值：{base_spoil_value} → {new_spoil} (+{new_spoil - base_spoil_value})")
            else:
                attribute_changes.append(f"撒娇值：{base_spoil_value}（无变化）")
                
            if new_tsundere != base_tsundere_value:
                attribute_changes.append(f"傲娇值：{base_tsundere_value} → {new_tsundere} (+{new_tsundere - base_tsundere_value})")
            else:
                attribute_changes.append(f"傲娇值：{base_tsundere_value}（无变化）")
            
            # 基础属性变化（这些总是会变化）
            attribute_changes.append(f"饥饿度：{original_hunger} → {new_hunger}")
            attribute_changes.append(f"清洁度：{original_cleanliness} → {new_cleanliness}")
            attribute_changes.append(f"健康度：{original_health} → {new_health}")
            attribute_changes.append(f"心情：{original_mood} → {new_mood}")
            
            result_msg += "，".join(attribute_changes) + "\n"

            if kill_results:
                result_msg += "💀 击败的敌人："
                
                # 按怪物难度从低到高排序
                monster_difficulty_map = {}
                for monster in dungeon['monsters']:
                    monster_difficulty_map[monster['name']] = monster['difficulty']
                
                # 对击败的敌人按难度排序
                sorted_kills = sorted(kill_results.items(), key=lambda x: monster_difficulty_map.get(x[0], 999))
                
                kill_list = []
                for monster_name, count in sorted_kills:
                    kill_list.append(f"{monster_name} x{count}")
                result_msg += "，".join(kill_list) + "\n"
            else:
                result_msg += "😅 很遗憾，这次冒险没有击败任何敌人...\n"

            if total_drops:
                result_msg += "🏆 获得的战利品："
                drop_list = []
                for item_name, count in total_drops.items():
                    drop_list.append(f"{item_name} x{count}")
                result_msg += "，".join(drop_list) + "\n"

            if level_up_msg:
                result_msg += level_up_msg

            return result_msg

        except Exception as e:
            print(f"处理地下城战斗时发生错误: {e}")
            import traceback
            traceback.print_exc()
            return f"地下城战斗处理时出现错误: {str(e)}"
