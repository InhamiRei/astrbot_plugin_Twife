"""房产相关命令处理器"""
import random
from astrbot.api.all import *
from ..core.data_manager import *
from ..config.properties import *

class PropertyHandler:
    def __init__(self):
        pass

    async def property_center(self, event: AstrMessageEvent):
        """房产中心功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 确保用户数据初始化
        user_data_obj = get_user_data(user_id)
        current_property = user_data_obj["property"]
        coins = user_data_obj["coins"]
        current_level = get_property_level(current_property)
        
        # 构建房产中心信息
        property_info = f": {nickname}的房产中心\n"
        property_info += f"💰 当前金币：{coins}\n"
        property_info += f"🏠 当前房产：Lv.{current_level} {current_property}\n"
        
        # 显示下一级房产信息
        next_property = get_next_property_info(current_property)
        if next_property:
            property_info += f"⬆️ 下一级：{next_property['name']} (💰{next_property['cost']})\n"
            property_info += "💡 使用「升级房产」升级\n"
        else:
            property_info += "🎉 已拥有最高级房产！\n"
        
        property_info += "\n📋 房产等级列表：\n"
        property_info += format_property_list(current_level)
        
        yield event.plain_result(property_info)

    async def upgrade_property(self, event: AstrMessageEvent):
        """升级房产功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 确保用户数据初始化
        user_data_obj = get_user_data(user_id)
        current_property = user_data_obj["property"]
        coins = user_data_obj["coins"]
        
        # 获取下一级房产信息
        next_property = get_next_property_info(current_property)
        if not next_property:
            yield event.plain_result(f': {nickname}，你已经拥有最高级的房产了，无法继续升级！')
            return
        
        # 检查金币是否足够
        upgrade_cost = next_property["cost"]
        if coins < upgrade_cost:
            yield event.plain_result(f': {nickname}，升级到{next_property["name"]}需要{upgrade_cost}金币，你当前只有{coins}金币，金币不足！')
            return
        
        # 10%的概率遇到特殊事件（升级失败但不扣金币）
        if random.random() < 0.1:
            fail_events = [
                f': {nickname}，装修工人罢工了！他们要求涨工资，升级暂时搁置...',
                f': {nickname}，建筑材料被台风吹走了！需要重新采购，升级失败...',
                f': {nickname}，设计师临时跑路了！带走了所有的设计图纸...',
                f': {nickname}，施工时发现地基有问题！需要重新勘探，升级失败...',
                f': {nickname}，邻居投诉你们施工太吵！被城管叫停了...',
                f': {nickname}，装修公司被发现是黑心企业！工程被迫终止...',
                f': {nickname}，升级过程中发现房产证有问题！需要重新办理手续...',
                f': {nickname}，装修材料在运输途中被盗！保险公司正在调查...',
                f': {nickname}，设计方案被发现抄袭！需要重新设计，升级失败...',
                f': {nickname}，施工队伍食物中毒了！全部进医院，工程暂停...'
            ]
            yield event.plain_result(random.choice(fail_events))
            return
        
        # 正常升级流程
        new_coins = coins - upgrade_cost
        update_user_data(user_id, coins=new_coins, property=next_property["name"])
        
        current_level = get_property_level(current_property)
        new_level = get_property_level(next_property["name"])
        
        success_message = f': 🎉 恭喜{nickname}！\n'
        success_message += f'房产升级成功！\n\n'
        success_message += f'🏠 Lv.{current_level} {current_property}\n'
        success_message += f'    ⬇️\n'
        success_message += f'🏠 Lv.{new_level} {next_property["name"]}\n'
        success_message += f'    {next_property["description"]}\n\n'
        success_message += f'💰 消耗金币：{upgrade_cost}\n'
        success_message += f'💰 剩余金币：{new_coins}'
        
        yield event.plain_result(success_message)