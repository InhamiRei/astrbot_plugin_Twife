"""服装商店处理器"""
import re
from astrbot.api.all import *
from ..core.data_manager import *
from ..config.costume_config import COSTUME_LIST, get_costume_by_name

class CostumeShopHandler:
    def __init__(self):
        pass

    async def costume_shop(self, event: AstrMessageEvent):
        """服装商店功能"""
        try:
            group_id = event.message_obj.group_id
            if not group_id:
                yield event.plain_result('该功能仅支持群聊，请在群聊中使用。')
                return

            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
            
            # 确保用户数据初始化
            get_user_data(user_id)
            
            # 构建服装商店信息（和家具中心相同的方式）
            shop_info = f"🛍️ {nickname}的服装商店\n"
            shop_info += "💡 使用「购买服装 服装名」来购买心仪的服装吧~\n"
            
            # 按部位分组显示
            slots = ["头部", "身体", "手部", "腿部", "脚部", "手持", "饰品"]
            slot_icons = {
                "头部": "👑",
                "身体": "👗",
                "手部": "🧤",
                "腿部": "👖",
                "脚部": "👠",
                "手持": "🎪",
                "饰品": "💎"
            }
            
            for slot in slots:
                slot_costumes = [costume for costume in COSTUME_LIST if costume["slot"] == slot]
                if slot_costumes:
                    shop_info += f"{slot_icons.get(slot, '📦')} 【{slot}】\n"
                    
                    for costume in slot_costumes:
                        # 格式化效果描述
                        effects_desc = self.format_effects_description(costume["effects"])
                        shop_info += f"⭐️ {costume['name']} - 💰{costume['price']:,}金币 (✨{effects_desc})\n"
                    
                    shop_info += "\n"
            shop_info += "🌟 套装提示：集齐任意整套装备可获得额外属性加成！\n"
            shop_info += "🎭 五大系列：兔女郎、女仆、巫女、魔法少女、小恶魔套装"
            
            yield event.plain_result(shop_info)
                
        except Exception as e:
            print(f"[Costume Shop] costume_shop函数发生异常: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f'服装商店功能出现错误: {str(e)}')

    async def buy_costume(self, event: AstrMessageEvent):
        """购买服装功能"""
        try:
            group_id = event.message_obj.group_id
            if not group_id:
                yield event.plain_result('该功能仅支持群聊，请在群聊中使用。')
                return

            user_id = str(event.get_sender_id())
            message = event.message_str.strip()
            
            # 解析购买命令
            if not message.startswith("购买服装"):
                yield event.plain_result('请使用格式：购买服装 服装名')
                return
            
            costume_name = message[4:].strip()  # 去掉"购买服装"
            if not costume_name:
                yield event.plain_result('请指定要购买的服装名称！\n使用"服装商店"查看可购买的服装。')
                return
            
            # 检查服装是否存在
            costume = get_costume_by_name(costume_name)
            if not costume:
                yield event.plain_result(f'服装"{costume_name}"不存在！\n使用"服装商店"查看可购买的服装。')
                return
            
            # 获取用户数据
            user_data_obj = get_user_data(user_id)
            current_coins = user_data_obj.get("coins", 0)
            wardrobe = user_data_obj.get("wardrobe", {})
            
            # 检查金币是否足够
            if current_coins < costume["price"]:
                yield event.plain_result(f'金币不足！需要{costume["price"]:,}金币，你现在有{current_coins:,}金币。')
                return
            
            # 检查是否已经拥有该服装
            if costume_name in wardrobe:
                yield event.plain_result(f'你已经拥有"{costume_name}"了！')
                return
            
            # 扣除金币并添加服装到衣柜
            new_coins = current_coins - costume["price"]
            wardrobe[costume_name] = {
                "name": costume_name,
                "slot": costume["slot"],
                "effects": costume["effects"],
                "description": costume["description"]
            }
            
            update_user_data(user_id, coins=new_coins, wardrobe=wardrobe)
            
            yield event.plain_result(f'成功购买"{costume_name}"！\n'
                                   f'花费{costume["price"]:,}金币，剩余{new_coins:,}金币。\n'
                                   f'服装已放入衣柜，使用"换衣 {costume_name}"来装备。')
                
        except Exception as e:
            print(f"[Costume Shop] buy_costume函数发生异常: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f'购买服装功能出现错误: {str(e)}')

    def format_shop_display(self):
        """格式化服装商店显示（用于文本回退模式）"""

        shop_text = "🛍️【服装商店】🛍️\n"

        # 按部位分组显示
        slots = ["头部", "身体", "手部", "腿部", "脚部", "手持", "饰品"]
        slot_icons = {
            "头部": "👑",
            "身体": "👗",
            "手部": "🧤",
            "腿部": "👖",
            "脚部": "👠",
            "手持": "🎪",
            "饰品": "💎"
        }

        for slot in slots:
            shop_text += f"\n{slot_icons.get(slot, '📦')} 【{slot}】\n"

            slot_costumes = [costume for costume in COSTUME_LIST if costume["slot"] == slot]
            for costume in slot_costumes:
                # 格式化效果描述
                effects_desc = self.format_effects_description(costume["effects"])
                shop_text += f"⭐️ {costume['name']}\n✨ 价格：{costume['price']:,}金币 ✨ 效果：{effects_desc}\n\n"
        
        shop_text += "🌟 套装提示：集齐任意整套装备可获得额外属性加成！\n"
        shop_text += "🎭 五大系列：兔女郎、女仆、巫女、魔法少女、小恶魔套装\n"
        shop_text += "💡 使用方法：购买服装 [服装名]"
        
        return shop_text
    
    def format_effects_description(self, effects):
        """格式化效果描述"""
        if not effects:
            return "无特殊效果"
        
        effect_names = {
            "moe_value": "妹抖值",
            "spoil_value": "撒娇值", 
            "tsundere_value": "傲娇值",
            "dark_rate": "黑化率",
            "contrast_cute": "反差萌"
        }
        
        effects_list = []
        for effect, value in effects.items():
            effect_name = effect_names.get(effect, effect)
            effects_list.append(f"{effect_name}+{value}%")
        
        return "、".join(effects_list)

