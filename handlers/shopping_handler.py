"""购物相关命令处理器"""
import random
from astrbot.api.all import *
from ..core.data_manager import *
from ..config.settings import SUPERMARKET_ITEMS, FASTFOOD_ITEMS, CANGYINGGUANZI_ITEMS
from ..config.events import GO_OUT_COIN_EVENTS
from ..config.messages import get_affection_status
from ..config.travel_config import FRAGMENT_CONVERSION, SOUVENIRS
from ..utils.formatters import format_backpack, format_artifacts
from .fragment_handler import fragment_handler

class ShoppingHandler:
    def __init__(self):
        pass

    async def check_assets(self, event: AstrMessageEvent):
        """资产查询功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 确保用户数据初始化
        user_data_obj = get_user_data(user_id)
        coins = user_data_obj["coins"]
        backpack_str = format_backpack(user_data_obj["backpack"])
        trophies_str = format_backpack(user_data_obj["trophies"])  # 使用相同的格式化函数
        property_name = user_data_obj["property"]
        furniture_inventory = user_data_obj["furniture"]
        wardrobe = user_data_obj.get("wardrobe", {})
        artifacts = user_data_obj.get("artifacts", {})
        artifacts_str = format_artifacts(artifacts)
        
        # 获取房产信息
        from ..config.properties import get_property_value, get_property_space, get_property_sell_bonus, PROPERTY_LEVELS
        from ..config.furniture import calculate_furniture_total_value, calculate_furniture_total_space, format_furniture_inventory
        
        property_value = get_property_value(property_name)
        property_space = get_property_space(property_name)
        sell_bonus = get_property_sell_bonus(property_name)
        
        property_description = ""
        for property_info in PROPERTY_LEVELS:
            if property_info["name"] == property_name:
                property_description = property_info["description"]
                break
        
        # 计算家具相关数据
        furniture_value = calculate_furniture_total_value(furniture_inventory)
        used_space = calculate_furniture_total_space(furniture_inventory)
        available_space = property_space - used_space
        furniture_str = format_furniture_inventory(furniture_inventory)

        # 计算总身价
        total_worth = property_value + furniture_value


        # 构建资产信息
        assets_message = f": {nickname}的资产信息\n"
        assets_message += f"💎 总身价：{total_worth}\n"
        assets_message += f"💰 金币：{coins}\n"
        # assets_message += f"🐕 宠物：暂无宠物\n"
        assets_message += f"🏠 房产：{property_name} 📦 空间：{used_space}/{property_space} (剩余：{available_space})\n"
        if property_description:
            assets_message += f"{property_description}\n"
        assets_message += f"🪑 家具：{furniture_str}\n"
        assets_message += f"🚢 奢侈资产：暂无\n"
        # assets_message += f"🎩 服务型资产：👷管家x0,🎀女佣x0,🪓保镖x0,🚖司机x0,🩺私人医生x0\n"
        # assets_message += f"📈 股票/基金：暂无\n"
        # assets_message += f"🏭 公司/商铺/矿产/地皮/岛屿：暂无\n"
        assets_message += f"🎒 背包：{backpack_str}\n"
        assets_message += f"🏆 战利品：{trophies_str}\n"
        assets_message += f"👗 衣柜：{self.format_wardrobe(wardrobe)}\n"
        assets_message += f"🏛️ 历史文物：{artifacts_str}"
        if user_data_obj["trophies"]:  # 如果有战利品，提示可以一键出售
            assets_message += f"\n💡 提示：使用\"一键出售战利品\"命令可快速出售所有战利品"

        yield event.plain_result(assets_message)

    async def sell_all_trophies(self, event: AstrMessageEvent):
        """一键出售所有战利品"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 获取用户数据
        user_data_obj = get_user_data(user_id)
        trophies = user_data_obj["trophies"].copy()
        
        if not trophies:
            yield event.plain_result(f': {nickname}，你目前没有任何战利品可以出售。')
            return
        
        # 获取房产售出加成
        property_name = user_data_obj["property"]
        from ..config.properties import get_property_sell_bonus
        sell_bonus = get_property_sell_bonus(property_name)
        
        # 计算战利品总价值
        base_total_value = 0
        total_bonus = 0
        final_total_value = 0
        trophy_details = []
        
        # 世界Boss奖励物品价格配置
        world_boss_items_price = {
            # 可可萝阶段奖励
            "可可萝的围裙": 1500,
            "温暖的料理": 2500,
            "美食食谱": 3000,
            "可可萝的笑容": 4000,
            "公主之心": 10000,
            "可可萝的发夹": 4500,
            "厨师的骄傲": 5000,
            # 大芋头王阶段奖励
            "芋头片": 1200,
            "烤芋头": 2000,
            "芋头泥": 2800,
            "金芋头": 3500,
            "芋头王冠": 8000,
            "芋头圣杯": 4200,
            "芋头权杖": 4800,
            # 基础攻击奖励 - 通用
            "小血瓶": 50,
            "能量药水": 80,
            "经验药水": 100,
            "金币袋": 120,
            "勇气徽章": 150,
            # 基础攻击奖励 - 可可萝专属
            "可可萝的祝福": 200,
            "公主护身符": 180,
            "料理残渣": 60,
            # 基础攻击奖励 - 大芋头王专属
            "芋头渣": 40,
            "芋头种子": 90,
            "香甜精华": 160
        }
        
        # 从地下城配置中获取物品价格
        from ..config.dungeon_config import DUNGEON_LIST
        
        for item_name, count in trophies.items():
            item_price = 0
            
            # 首先检查是否为世界Boss奖励物品
            if item_name in world_boss_items_price:
                item_price = world_boss_items_price[item_name]
            else:
                # 在所有地下城的掉落列表中查找该物品的价格
                for dungeon in DUNGEON_LIST:
                    if 'monsters' in dungeon:
                        for monster in dungeon['monsters']:
                            if 'drops' in monster:
                                for drop in monster['drops']:
                                    if drop['item'] == item_name:
                                        item_price = drop['price']
                                        break
                                if item_price > 0:
                                    break
                        if item_price > 0:
                            break
            
            if item_price > 0:
                # 计算基础价值
                base_item_total = item_price * count
                # 计算房产加成
                bonus_amount = int(base_item_total * sell_bonus / 100)
                # 计算最终价值
                final_item_total = base_item_total + bonus_amount
                
                base_total_value += base_item_total
                total_bonus += bonus_amount
                final_total_value += final_item_total
                
                if sell_bonus > 0:
                    trophy_details.append(f"{item_name} x{count} = {base_item_total}(+{bonus_amount})金币")
                else:
                    trophy_details.append(f"{item_name} x{count} = {final_item_total}金币")
        
        if final_total_value == 0:
            yield event.plain_result(f': {nickname}，你的战利品都没有价值，无法出售。')
            return
        
        # 更新用户数据：增加金币，清空战利品
        user_data_obj["coins"] += final_total_value
        user_data_obj["trophies"] = {}
        update_user_data(user_id, coins=user_data_obj["coins"], trophies=user_data_obj["trophies"])
        
        # 构建结果消息
        result_msg = f": {nickname}，一键出售战利品完成\n"
        result_msg += f"💰 基础总价：{base_total_value}金币\n"
        result_msg += f"🏠 房产加成：+{sell_bonus}% (+{total_bonus}金币)\n"
        result_msg += f"💰 总收入：{final_total_value}金币"
        result_msg += f"\n💎 实际到账：{final_total_value}金币"
        result_msg += f"\n💎 当前金币：{user_data_obj['coins']}"
        result_msg += "\n🏆 战利品列表："
        result_msg += "，".join(trophy_details)

        
        yield event.plain_result(result_msg)

    async def go_out(self, event: AstrMessageEvent):
        """出门转转功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 确保用户数据初始化
        user_data_obj = get_user_data(user_id)
        
        # 检查每日出门转转次数限制
        from ..config.settings import GO_OUT_MAX_DAILY, GO_OUT_MAX_NOTICE
        current_go_out_count = get_daily_limit_data(user_id, 'go_out')
        if current_go_out_count >= GO_OUT_MAX_DAILY:
            yield event.plain_result(f': {nickname}，{GO_OUT_MAX_NOTICE}')
            return
        
        current_coins = user_data_obj["coins"]
        backpack = user_data_obj["backpack"].copy()
        
        # 设置概率：70%获得物品，30%触发金币事件
        if random.random() < 0.7:
            # 获得物品事件
            items = get_items_for_go_out()
            if not items:
                yield event.plain_result(f': {nickname}，物品配置未加载，请联系管理员检查配置文件。')
                return
                
            weights = [item[1] for item in items]  # 获取权重
            
            # 基于权重随机选择物品
            chosen_item = random.choices(items, weights=weights, k=1)[0]
            item_name = chosen_item[0]
            min_count = chosen_item[2]
            max_count = chosen_item[3]
            item_desc = chosen_item[4]
            
            # 随机数量
            item_count = random.randint(min_count, max_count)
            
            # 更新背包
            if item_name in backpack:
                backpack[item_name] += item_count
            else:
                backpack[item_name] = item_count
            
            # 保存数据
            update_user_data(user_id, backpack=backpack)
            
            # 构建回复消息
            if item_count == 1:
                result_message = f': {nickname}出门转转，获得了{item_name}！\n{item_desc}'
            else:
                result_message = f': {nickname}出门转转，获得了{item_name} x{item_count}！\n{item_desc}'
                
        else:
            # 金币事件
            chosen_event = random.choice(GO_OUT_COIN_EVENTS)
            event_desc = chosen_event[0]
            min_coin_change = chosen_event[1]
            max_coin_change = chosen_event[2]
            
            # 随机金币变化
            coin_change = random.randint(min_coin_change, max_coin_change)
            new_coins = max(0, current_coins + coin_change)  # 确保金币不为负数
            
            # 如果金币会变成负数，调整实际损失
            if current_coins + coin_change < 0:
                actual_loss = current_coins
                coin_change = -actual_loss
                new_coins = 0
            
            # 保存数据
            update_user_data(user_id, coins=new_coins)
            
            # 构建回复消息
            if coin_change > 0:
                result_message = f': {nickname}出门转转，{event_desc}\n💰 获得了{coin_change}金币！\n💰 当前金币：{new_coins}'
            else:
                result_message = f': {nickname}出门转转，{event_desc}\n💸 损失了{abs(coin_change)}金币...\n💰 当前金币：{new_coins}'
        
        # 增加使用次数
        update_daily_limit_data(user_id, 'go_out', current_go_out_count + 1)
        remaining_times = GO_OUT_MAX_DAILY - (current_go_out_count + 1)
        
        # 添加剩余次数提示
        if remaining_times > 0:
            result_message += f'\n🔄 今日剩余次数：{remaining_times}次'
        else:
            result_message += f'\n⏰ 今日出门转转次数已用完，请明天再来！'
        
        yield event.plain_result(result_message)

    async def give_gift(self, event: AstrMessageEvent):
        """赠送礼物功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 解析命令，获取物品名称和数量
        message_str = event.message_str.strip()
        if not message_str.startswith("赠送礼物"):
            yield event.plain_result(f': {nickname}，请使用正确的格式：赠送礼物 物品名称 数量')
            return
            
        parts = message_str[4:].strip().split()  # 去掉"赠送礼物"前缀
        if len(parts) < 1:
            yield event.plain_result(f': {nickname}，请指定要赠送的物品名称，格式：赠送礼物 物品名称 数量')
            return
        elif len(parts) == 1:
            item_name = parts[0]
            quantity = 1  # 默认数量为1
        else:
            item_name = parts[0]
            try:
                quantity = int(parts[1])
                if quantity <= 0:
                    yield event.plain_result(f': {nickname}，赠送数量必须大于0')
                    return
            except ValueError:
                yield event.plain_result(f': {nickname}，请输入有效的数量')
                return

        # 检查用户是否有老婆
        wife_data = get_user_wife_data(user_id)
        if not wife_data:
            yield event.plain_result(f': {nickname}，你还没有老婆，无法赠送礼物。请先使用"抽老婆"命令获取一个老婆！')
            return

        # 获取用户数据
        user_data_obj = get_user_data(user_id)
        backpack = user_data_obj["backpack"]
        
        # 检查背包中是否有该物品
        if item_name not in backpack or backpack[item_name] <= 0:
            yield event.plain_result(f': {nickname}，你的背包中没有{item_name}，无法赠送。')
            return
            
        # 检查背包中是否有足够的物品数量
        available_quantity = backpack[item_name]
        if available_quantity < quantity:
            yield event.plain_result(f': {nickname}，你的背包中只有{available_quantity}个{item_name}，无法赠送{quantity}个。')
            return
            
        # 检查是否为碎片类型物品
        is_fragment = False
        fragment_type = None
        for frag_type, frag_config in FRAGMENT_CONVERSION.items():
            if item_name == frag_config["name"]:
                is_fragment = True
                fragment_type = frag_type
                break
        
        # 根据物品类型设置数量限制
        if is_fragment:
            # 碎片类物品允许更高的数量限制（最多1000个）
            if quantity > 1000:
                yield event.plain_result(f': {nickname}，一次最多只能赠送1000个{item_name}')
                return
        else:
            # 普通物品保持99个的限制
            if quantity > 99:
                yield event.plain_result(f': {nickname}，一次最多只能赠送99个物品')
                return
        
        # 检查是否为纪念品伴手礼
        is_souvenir = False
        souvenir_info = None
        for country, souvenirs in SOUVENIRS.items():
            for souvenir in souvenirs:
                if item_name == souvenir["name"]:
                    is_souvenir = True
                    souvenir_info = souvenir
                    break
            if is_souvenir:
                break
        
        # 处理碎片类型物品
        if is_fragment:
            # 碎片必须满100个才能使用
            if quantity < 100:
                yield event.plain_result(f': {nickname}，{item_name}需要满100个才能赠送给老婆提升属性！当前数量：{available_quantity}')
                return
            if quantity % 100 != 0:
                yield event.plain_result(f': {nickname}，{item_name}的使用数量必须是100的倍数！')
                return
            
            # 使用碎片处理器
            success, result = fragment_handler.use_fragments(user_id, fragment_type, quantity)
            if not success:
                yield event.plain_result(f': {nickname}，使用{item_name}失败：{result}')
                return
            
            # 构建碎片使用结果消息
            wife_name = wife_data[0]
            wife_display_name = wife_name.split('.')[0]
            
            result_message = f': {nickname}，你使用了{quantity}个{item_name}为{wife_display_name}提升属性！\n'
            result_message += f'💫 {wife_display_name}：感受到了神秘力量的注入，身体发生了微妙的变化...\n'
            
            for attr_name, attr_value in result["attribute_increases"].items():
                if attr_name == "charm_contrast":
                    result_message += f'✨ 反差萌 +{attr_value}点\n'
                elif attr_name == "blackening":
                    result_message += f'🖤 黑化率 +{attr_value}点\n'
            
            result_message += f'📦 剩余{item_name}：{result["remaining_fragments"]}个'
            
            yield event.plain_result(result_message)
            return
        
        # 处理纪念品伴手礼
        elif is_souvenir:
            # 直接从背包中移除物品
            backpack[item_name] -= quantity
            if backpack[item_name] <= 0:
                del backpack[item_name]
            
            # 应用纪念品效果
            wife_name = wife_data[0]
            wife_display_name = wife_name.split('.')[0]
            current_mood = wife_data[10] if len(wife_data) > 10 else 100
            
            # 计算属性变化
            total_mood_gain = souvenir_info["effects"].get("mood", 0) * quantity
            new_mood = max(0, min(1000, current_mood + total_mood_gain))
            
            # 更新数据
            update_user_data(user_id, backpack=backpack)
            update_user_wife_data(user_id, mood=new_mood)
            
            # 构建纪念品使用结果消息
            result_message = f': {nickname}，你向{wife_display_name}赠送了{item_name} x{quantity}\n'
            result_message += f'🎁 {souvenir_info["description"]}\n'
            result_message += f'💝 {wife_display_name}：这是从旅行中带回来的珍贵纪念品呢！谢谢你！\n'
            result_message += f'😊 心情：{current_mood} → {new_mood} (+{total_mood_gain})\n'
            
            # 注释：纪念品只影响心情值，其他效果只是装饰性描述
            # 不再显示虚假的属性变化，因为老婆系统中没有这些属性
            
            yield event.plain_result(result_message)
            return
        
        # 检查物品是否在配置中（普通物品）
        if item_name not in ITEMS_DATA:
            yield event.plain_result(f': {nickname}，找不到物品{item_name}的信息，无法赠送。')
            return
            
        # 获取物品信息
        item_info = ITEMS_DATA[item_name]
        affection_value = item_info['affection_value']
        description = item_info['description']
        
        # 获取物品属性效果
        hunger_effect = item_info.get('hunger_effect', 0)
        mood_effect = item_info.get('mood_effect', 0)
        cleanliness_effect = item_info.get('cleanliness_effect', 0)
        health_effect = item_info.get('health_effect', 0)
        
        # 获取老婆名称和当前属性
        wife_name = wife_data[0]
        wife_display_name = wife_name.split('.')[0]
        current_affection = wife_data[4]
        current_hunger = wife_data[7]
        current_cleanliness = wife_data[8]
        current_health = wife_data[9]
        current_mood = wife_data[10]
        
        # 更新背包（减少指定数量的物品）
        backpack[item_name] -= quantity
        if backpack[item_name] <= 0:
            del backpack[item_name]
            
        # 批量计算属性效果（每个物品的效果叠加）
        total_affection_gain = affection_value * quantity
        total_hunger_gain = hunger_effect * quantity
        total_mood_gain = mood_effect * quantity
        total_cleanliness_gain = cleanliness_effect * quantity
        total_health_gain = health_effect * quantity
            
        # 更新好感度，四舍五入到小数点后1位
        new_affection = round(current_affection + total_affection_gain, 1)
        
        # 更新老婆属性（最高1000，最低0）
        new_hunger = max(0, min(1000, current_hunger + total_hunger_gain))
        new_cleanliness = max(0, min(1000, current_cleanliness + total_cleanliness_gain))
        new_health = max(0, min(1000, current_health + total_health_gain))
        new_mood = max(0, min(1000, current_mood + total_mood_gain))
        
        # 保存数据
        update_user_data(user_id, backpack=backpack)
        update_user_wife_data(user_id, affection=new_affection, hunger=new_hunger, 
                             cleanliness=new_cleanliness, health=new_health, mood=new_mood)
        
        # 生成随机回应（简化版）
        if quantity == 1:
            gift_responses = [
                f"{wife_display_name}接过{item_name}：谢谢你！",
                f"{wife_display_name}对{item_name}爱不释手：正是我想要的！",
                f"{wife_display_name}开心地收下了{item_name}：你真的太贴心了！",
                f"{wife_display_name}红着脸接过{item_name}：这…这太珍贵了…",
                f"{wife_display_name}惊喜地抱着{item_name}：你怎么知道我喜欢这个！"
            ]
        else:
            gift_responses = [
                f"{wife_display_name}接过{quantity}个{item_name}：哇，这么多！谢谢你！",
                f"{wife_display_name}对{quantity}个{item_name}爱不释手：这些都是我想要的！",
                f"{wife_display_name}开心地收下了{quantity}个{item_name}：你对我真的太好了！",
                f"{wife_display_name}红着脸接过{quantity}个{item_name}：这…这些都太珍贵了…",
                f"{wife_display_name}惊喜地抱着{quantity}个{item_name}：你真了解我的喜好！"
            ]
        
        if quantity == 1:
            result_message = f': {nickname}，你向{wife_display_name}赠送了{item_name}\n'
        else:
            result_message = f': {nickname}，你向{wife_display_name}赠送了{item_name} x{quantity}\n'
        result_message += f'{description}\n'
        result_message += f'{random.choice(gift_responses)}\n'
        result_message += f'💖 好感度增加了{total_affection_gain:.1f}点！({current_affection:.1f} → {new_affection:.1f})\n'
        
        # 显示属性变化
        attribute_changes = []
        if total_hunger_gain != 0:
            attribute_changes.append(f'🍽️ 饥饿：{current_hunger} → {new_hunger} ({total_hunger_gain:+d})')
        if total_mood_gain != 0:
            attribute_changes.append(f'😊 心情：{current_mood} → {new_mood} ({total_mood_gain:+d})')
        if total_cleanliness_gain != 0:
            attribute_changes.append(f'🧼 清洁：{current_cleanliness} → {new_cleanliness} ({total_cleanliness_gain:+d})')
        if total_health_gain != 0:
            attribute_changes.append(f'❤️ 健康：{current_health} → {new_health} ({total_health_gain:+d})')
        
        if attribute_changes:
            result_message += '\n'.join(attribute_changes)
        
        # 检查是否达到特殊里程碑
        milestone_levels = [1000, 2000, 3000, 4000, 5000, 10000, 50000, 100000]
        for milestone in milestone_levels:
            if new_affection >= milestone and current_affection < milestone:
                if milestone == 1000:
                    result_message += '\n🎆 恭喜！你们的好感度达到了1000！感情进入新的阶段！'
                elif milestone == 10000:
                    result_message += '\n✨ 好感度突破万点大关！你们的爱情已经超越了一般的恋人关系！'
                elif milestone == 100000:
                    result_message += '\n🌟 好感度突破十万大关！这是传说中的至高境界！'
                else:
                    result_message += f'\n💕 好感度达到了{milestone}！你们的爱情越来越深厚！'
                break
        
        affection_status = get_affection_status(new_affection)
        result_message += f'\n{affection_status}'
        
        yield event.plain_result(result_message)

    async def sell_item(self, event: AstrMessageEvent):
        """出售物品功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 解析命令，获取物品名称
        message_str = event.message_str.strip()
        if not message_str.startswith("出售物品"):
            yield event.plain_result(f': {nickname}，请使用正确的格式：出售物品 物品名称')
            return
            
        item_name = message_str[4:].strip()  # 去掉"出售物品"前缀
        if not item_name:
            yield event.plain_result(f': {nickname}，请指定要出售的物品名称，格式：出售物品 物品名称')
            return

        # 获取用户数据
        user_data_obj = get_user_data(user_id)
        backpack = user_data_obj["backpack"]
        current_coins = user_data_obj["coins"]
        
        # 检查背包中是否有该物品
        if item_name not in backpack or backpack[item_name] <= 0:
            yield event.plain_result(f': {nickname}，你的背包中没有{item_name}，无法出售。')
            return
        
        # 检查是否为历史文物（历史文物无法出售）
        from ..config.travel_config import MUSEUMS
        is_artifact = False
        for country, museum_info in MUSEUMS.items():
            if item_name in museum_info["artifacts_accepted"]:
                is_artifact = True
                break
        
        if is_artifact:
            yield event.plain_result(f': {nickname}，{item_name}是珍贵的历史文物，无法出售！你可以将其捐赠给博物馆获得更丰厚的奖励。')
            return
        
        # 检查是否为碎片（碎片也无法直接出售，只能通过赠送礼物使用）
        from ..config.travel_config import FRAGMENT_CONVERSION, SOUVENIRS
        for frag_type, frag_config in FRAGMENT_CONVERSION.items():
            if item_name == frag_config["name"]:
                yield event.plain_result(f': {nickname}，{item_name}无法直接出售！你可以通过「赠送礼物 {item_name} 100」来使用它提升老婆属性。')
                return
        
        # 检查是否为纪念品（纪念品无法出售，具有纪念价值）
        is_souvenir = False
        for city, souvenirs in SOUVENIRS.items():
            for souvenir in souvenirs:
                if item_name == souvenir["name"]:
                    is_souvenir = True
                    break
            if is_souvenir:
                break
        
        if is_souvenir:
            yield event.plain_result(f': {nickname}，{item_name}是珍贵的旅行纪念品，具有特殊的纪念价值，无法出售！你可以通过「赠送礼物」给老婆使用。')
            return
            
        # 检查物品是否在配置中
        if item_name not in ITEMS_DATA:
            yield event.plain_result(f': {nickname}，找不到物品{item_name}的信息，无法出售。')
            return
            
        # 获取物品信息
        item_info = ITEMS_DATA[item_name]
        base_sell_price = item_info['sell_price']
        description = item_info['description']
        category = item_info['category']
        
        # 获取房产售出加成
        property_name = user_data_obj["property"]
        from ..config.properties import get_property_sell_bonus
        sell_bonus = get_property_sell_bonus(property_name)
        
        # 计算最终售价（基础价格 + 房产加成）
        bonus_amount = int(base_sell_price * sell_bonus / 100)
        final_sell_price = base_sell_price + bonus_amount
        
        # 更新背包（减少1个物品）
        backpack[item_name] -= 1
        if backpack[item_name] <= 0:
            del backpack[item_name]
            
        # 更新金币
        new_coins = current_coins + final_sell_price
        
        # 保存数据
        update_user_data(user_id, coins=new_coins, backpack=backpack)
        
        # 生成商人回应（简化版）
        merchant_responses = [
            "商人看了看：这个不错，可以收下。",
            "商人点点头：这种东西我要了。",
            "商人笑道：这个在市场上还挺好卖的。"
        ]
        
        result_message = f': {nickname}，你向商人出售了{item_name}\n'
        result_message += f'{description}\n'
        result_message += f'{random.choice(merchant_responses)}\n'
        
        if sell_bonus > 0:
            result_message += f'💰 基础售价：{base_sell_price}金币\n'
            result_message += f'🏠 房产加成：+{sell_bonus}% (+{bonus_amount}金币)\n'
            result_message += f'💰 实际获得：{final_sell_price}金币！({current_coins} → {new_coins})'
        else:
            result_message += f'💰 获得了{final_sell_price}金币！({current_coins} → {new_coins})'
        
        yield event.plain_result(result_message)

    async def supermarket_list(self, event: AstrMessageEvent):
        """超市列表功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 获取用户数据
        user_data_obj = get_user_data(user_id)
        coins = user_data_obj["coins"]
        
        # 构建超市列表
        supermarket_message = f"🛒 {nickname}的超市购物\n"
        supermarket_message += f"💰 当前金币：{coins}\n\n"
        supermarket_message += "☀️ 超市列表：\n"
        
        # 显示超市商品
        for item_name in SUPERMARKET_ITEMS:
            if item_name in ITEMS_DATA:
                item_data = ITEMS_DATA[item_name]
                buy_price = item_data.get('buy_price', 0)
                description = item_data.get('description', '')
                # 提取emoji
                emoji = description.split(' ')[0] if ' ' in description else '📦'
                supermarket_message += f" - {emoji} {item_name} - 💰{buy_price}金币\n"
            else:
                supermarket_message += f" - 📦 {item_name} - 💰?金币 (配置缺失)\n"
        
        supermarket_message += "\n💡 使用「购买物品 物品名称 数量」来购买商品"
        
        yield event.plain_result(supermarket_message)

    async def fastfood_list(self, event: AstrMessageEvent):
        """快餐店列表功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 获取用户数据
        user_data_obj = get_user_data(user_id)
        coins = user_data_obj["coins"]
        
        # 构建快餐店列表
        fastfood_message = f"🍗 {nickname}的啃你🐔列表\n"
        fastfood_message += f"💰 当前金币：{coins}\n\n"

        # 显示快餐店商品
        for item_name in FASTFOOD_ITEMS:
            if item_name in ITEMS_DATA:
                item_data = ITEMS_DATA[item_name]
                buy_price = item_data.get('buy_price', 0)
                hunger_effect = item_data.get('hunger_effect', 0)
                description = item_data.get('description', '')
                # 提取emoji
                emoji = description.split(' ')[0] if ' ' in description else '🍗'
                fastfood_message += f"{emoji} {item_name} - 💰{buy_price}金币\n"
            else:
                fastfood_message += f"🍗 {item_name} - 💰?金币 (配置缺失)\n"
        
        fastfood_message += "\n💡 使用「购买物品 物品名称 数量」来购买商品"
        
        yield event.plain_result(fastfood_message)

    async def cangyingguanzi_list(self, event: AstrMessageEvent):
        """苍蝇馆子列表功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 获取用户数据
        user_data_obj = get_user_data(user_id)
        coins = user_data_obj["coins"]
        
        # 构建苍蝇馆子列表
        cangyingguanzi_message = f"🏮 {nickname}的苍蝇馆子外卖\n"
        cangyingguanzi_message += f"💰 当前金币：{coins}\n\n"
        
        # 显示苍蝇馆子商品
        for item_name in CANGYINGGUANZI_ITEMS:
            if item_name in ITEMS_DATA:
                item_data = ITEMS_DATA[item_name]
                buy_price = item_data.get('buy_price', 0)
                hunger_effect = item_data.get('hunger_effect', 0)
                mood_effect = item_data.get('mood_effect', 0)
                description = item_data.get('description', '')
                # 提取emoji
                emoji = description.split(' ')[0] if ' ' in description else '🍜'
                cangyingguanzi_message += f"{emoji} {item_name} - 💰{buy_price}金币"
                cangyingguanzi_message += "\n"
            else:
                cangyingguanzi_message += f"🍜 {item_name} - 💰?金币 (配置缺失)\n"
        
        cangyingguanzi_message += "\n💡 使用「购买物品 物品名称 数量」来购买地方菜"
        
        yield event.plain_result(cangyingguanzi_message)

    async def buy_item(self, event: AstrMessageEvent):
        """购买物品功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 解析命令，获取物品名称和数量
        message_str = event.message_str.strip()
        if not message_str.startswith("购买物品"):
            yield event.plain_result(f': {nickname}，请使用正确的格式：购买物品 物品名称 数量')
            return
            
        parts = message_str[4:].strip().split()  # 去掉"购买物品"前缀
        if len(parts) < 1:
            yield event.plain_result(f': {nickname}，请指定要购买的物品名称，格式：购买物品 物品名称 数量')
            return
        elif len(parts) == 1:
            item_name = parts[0]
            quantity = 1  # 默认数量为1
        else:
            item_name = parts[0]
            try:
                quantity = int(parts[1])
                if quantity <= 0:
                    yield event.plain_result(f': {nickname}，购买数量必须大于0')
                    return
                if quantity > 99:
                    yield event.plain_result(f': {nickname}，一次最多只能购买99个物品')
                    return
            except ValueError:
                yield event.plain_result(f': {nickname}，请输入有效的数量')
                return

        # 检查物品是否在任何商品列表中（超市、快餐店、苍蝇馆子）
        if item_name not in SUPERMARKET_ITEMS and item_name not in FASTFOOD_ITEMS and item_name not in CANGYINGGUANZI_ITEMS:
            yield event.plain_result(f': {nickname}，没有找到{item_name}这种商品，请使用「超市列表」、「快餐店列表」或「苍蝇馆子」查看可购买的商品')
            return

        # 检查物品配置是否存在
        if item_name not in ITEMS_DATA:
            yield event.plain_result(f': {nickname}，{item_name}的配置信息缺失，无法购买')
            return

        # 获取物品信息
        item_info = ITEMS_DATA[item_name]
        buy_price = item_info.get('buy_price', 0)
        description = item_info['description']
        
        # 获取用户数据
        user_data_obj = get_user_data(user_id)
        current_coins = user_data_obj["coins"]
        backpack = user_data_obj["backpack"].copy()
        
        # 计算总价
        total_cost = buy_price * quantity
        
        # 检查金币是否足够
        if current_coins < total_cost:
            yield event.plain_result(f': {nickname}，购买{quantity}个{item_name}需要{total_cost}金币，你当前只有{current_coins}金币，金币不足！')
            return
        
        # 购买成功处理
        new_coins = current_coins - total_cost
        
        # 更新背包
        if item_name in backpack:
            backpack[item_name] += quantity
        else:
            backpack[item_name] = quantity
            
        # 保存数据
        update_user_data(user_id, coins=new_coins, backpack=backpack)
        
        # 确定购买地点并生成相应的回应
        if item_name in SUPERMARKET_ITEMS:
            store_name = "超市"
            purchase_responses = [
                "✨ 收银员笑着说：欢迎光临，祝您购物愉快！",
                "✨ 收银员热情地包装好商品：谢谢惠顾！",
                "✨ 收银员点头：这是个不错的选择！"
            ]
        elif item_name in FASTFOOD_ITEMS:
            store_name = "快餐店"
            purchase_responses = [
                "🍔 店员微笑着说：欢迎光临快餐店，请慢用！",
                "🍗 店员热情地递过来：新鲜出炉的美味！",
                "🍟 店员点头：您选择的是我们的招牌美食！"
            ]
        else:  # item_name in CANGYINGGUANZI_ITEMS
            store_name = "苍蝇馆子"
            purchase_responses = [
                "🏮 老板笑呵呵地说：这是我们的招牌菜，保证正宗！",
                "🥢 老板娘热情地打包：地道口味，绝对满意！",
                "🍜 掌勺师傅点头：这道菜我做了三十年，味道绝了！",
                "🌶️ 老板拍胸脯保证：我们用的都是家乡的配料！",
                "🏪 店老板眯着眼说：这个味道，外面可吃不到！"
            ]
        
        if quantity == 1:
            result_message = f': {nickname}，你在{store_name}购买了{item_name}！\n'
        else:
            result_message = f': {nickname}，你在{store_name}购买了{item_name} x{quantity}！\n'
            
        result_message += f'{description}\n'
        result_message += f'{random.choice(purchase_responses)}\n'
        result_message += f'💰 花费了{total_cost}金币！({current_coins} → {new_coins})\n'
        result_message += f'🎒 {item_name}已放入背包！'
        
        yield event.plain_result(result_message)

    def format_wardrobe(self, wardrobe):
        """格式化衣柜显示"""
        if not wardrobe:
            return "暂无服装"
        
        # 按部位分组
        slots_group = {}
        for costume_name, costume_info in wardrobe.items():
            slot = costume_info.get("slot", "其他")
            if slot not in slots_group:
                slots_group[slot] = []
            slots_group[slot].append(costume_name)
        
        wardrobe_parts = []
        for slot, costumes in slots_group.items():
            costumes_str = "、".join(costumes)
            wardrobe_parts.append(f"{costumes_str}（{slot}）")
        
        return "，".join(wardrobe_parts)
