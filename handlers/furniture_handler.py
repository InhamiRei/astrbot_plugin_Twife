"""家具中心相关命令处理器"""
import random
from astrbot.api.all import *
from ..core.data_manager import *
from ..config.furniture import *
from ..config.properties import *

class FurnitureHandler:
    def __init__(self):
        pass

    async def furniture_center(self, event: AstrMessageEvent):
        """家具中心功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 获取用户数据
        user_data_obj = get_user_data(user_id)
        coins = user_data_obj["coins"]
        property_name = user_data_obj["property"]
        furniture_inventory = user_data_obj["furniture"]
        
        # 获取房产信息
        property_space = get_property_space(property_name)
        used_space = calculate_furniture_total_space(furniture_inventory)
        available_space = property_space - used_space
        
        # 构建家具中心信息
        furniture_info = f"🪑 {nickname}的家具中心\n"
        furniture_info += f"💰 当前金币：{coins}\n"
        furniture_info += f"🏠 当前房产：{property_name}\n"
        furniture_info += f"📦 房产空间：{used_space}/{property_space} (剩余:{available_space})\n\n"
        furniture_info += format_furniture_list()
        
        yield event.plain_result(furniture_info)

    async def buy_furniture(self, event: AstrMessageEvent):
        """购买家具功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 解析命令，获取家具名称
        message_str = event.message_str.strip()
        if not message_str.startswith("购买家具"):
            yield event.plain_result(f': {nickname}，请使用正确的格式：购买家具 家具名称')
            return
            
        furniture_name = message_str[4:].strip()  # 去掉"购买家具"前缀
        if not furniture_name:
            yield event.plain_result(f': {nickname}，请指定要购买的家具名称，格式：购买家具 家具名称')
            return

        # 检查家具是否存在
        furniture_info = get_furniture_by_name(furniture_name)
        if not furniture_info:
            yield event.plain_result(f': {nickname}，没有找到名为"{furniture_name}"的家具，请使用「家具中心」查看可购买的家具')
            return

        # 获取用户数据
        user_data_obj = get_user_data(user_id)
        current_coins = user_data_obj["coins"]
        property_name = user_data_obj["property"]
        furniture_inventory = user_data_obj["furniture"].copy()
        
        # 检查金币是否足够
        buy_price = furniture_info["buy_price"]
        if current_coins < buy_price:
            yield event.plain_result(f': {nickname}，购买{furniture_name}需要{buy_price}金币，你当前只有{current_coins}金币，金币不足！')
            return
        
        # 检查空间是否足够
        property_space = get_property_space(property_name)
        used_space = calculate_furniture_total_space(furniture_inventory)
        furniture_space = furniture_info["space"]
        
        if used_space + furniture_space > property_space:
            available_space = property_space - used_space
            yield event.plain_result(f': {nickname}，{furniture_name}需要{furniture_space}空间，但你的房产只剩{available_space}空间！请升级房产或出售一些家具。')
            return
        
        # 购买成功处理
        new_coins = current_coins - buy_price
        
        # 更新家具库存
        if furniture_name in furniture_inventory:
            furniture_inventory[furniture_name] += 1
        else:
            furniture_inventory[furniture_name] = 1
            
        # 保存数据
        update_user_data(user_id, coins=new_coins, furniture=furniture_inventory)
        
        # 生成购买回应
        purchase_responses = [
            "✨ 家具店老板笑着说：这是个明智的选择！",
            "✨ 家具店老板热情地安排送货：很快就能送到您家！",
            "✨ 家具店老板点头：您的品味真不错！"
        ]
        
        new_used_space = used_space + furniture_space
        
        result_message = f': {nickname}，你在家具中心购买了{furniture_name}！\n'
        result_message += f'{furniture_info["description"]}\n'
        result_message += f'{random.choice(purchase_responses)}\n'
        result_message += f'💰 花费了{buy_price}金币！({current_coins} → {new_coins})\n'
        result_message += f'📦 占用空间：{furniture_space} ({used_space}/{property_space} → {new_used_space}/{property_space})\n'
        result_message += f'🪑 {furniture_name}已安装到你的房产中！'
        
        yield event.plain_result(result_message)

    async def sell_furniture(self, event: AstrMessageEvent):
        """出售家具功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 解析命令，获取家具名称
        message_str = event.message_str.strip()
        if not message_str.startswith("出售家具"):
            yield event.plain_result(f': {nickname}，请使用正确的格式：出售家具 家具名称')
            return
            
        furniture_name = message_str[4:].strip()  # 去掉"出售家具"前缀
        if not furniture_name:
            yield event.plain_result(f': {nickname}，请指定要出售的家具名称，格式：出售家具 家具名称')
            return

        # 获取用户数据
        user_data_obj = get_user_data(user_id)
        furniture_inventory = user_data_obj["furniture"]
        current_coins = user_data_obj["coins"]
        
        # 检查是否拥有该家具
        if furniture_name not in furniture_inventory or furniture_inventory[furniture_name] <= 0:
            yield event.plain_result(f': {nickname}，你没有{furniture_name}，无法出售。')
            return
            
        # 检查家具信息
        furniture_info = get_furniture_by_name(furniture_name)
        if not furniture_info:
            yield event.plain_result(f': {nickname}，找不到{furniture_name}的信息，无法出售。')
            return
            
        # 获取售价
        sell_price = furniture_info["sell_price"]
        furniture_space = furniture_info["space"]
        description = furniture_info["description"]
        
        # 更新家具库存
        furniture_inventory = furniture_inventory.copy()
        furniture_inventory[furniture_name] -= 1
        if furniture_inventory[furniture_name] <= 0:
            del furniture_inventory[furniture_name]
            
        # 更新金币
        new_coins = current_coins + sell_price
        
        # 保存数据
        update_user_data(user_id, coins=new_coins, furniture=furniture_inventory)
        
        # 生成回应
        merchant_responses = [
            "家具回收商看了看：这个还不错，我收了。",
            "家具回收商点点头：质量还可以，给你个好价钱。",
            "家具回收商笑道：这种家具我们很需要。"
        ]
        
        result_message = f': {nickname}，你向家具回收商出售了{furniture_name}\n'
        result_message += f'{description}\n'
        result_message += f'{random.choice(merchant_responses)}\n'
        result_message += f'💰 获得了{sell_price}金币！({current_coins} → {new_coins})\n'
        result_message += f'📦 释放了{furniture_space}空间！'
        
        yield event.plain_result(result_message)
