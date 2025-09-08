"""物品查询处理器"""
import re
from astrbot.api.all import *
from ..core.data_manager import ITEMS_DATA
from ..config.costume_config import get_costume_by_name, COSTUME_LIST

class ItemQueryHandler:
    def __init__(self):
        pass

    async def query_item(self, event: AstrMessageEvent):
        """查询物品详情功能"""
        try:
            group_id = event.message_obj.group_id
            if not group_id:
                yield event.plain_result('该功能仅支持群聊，请在群聊中使用。')
                return

            message = event.message_str.strip()
            
            # 解析查询命令
            if not message.startswith("查询物品"):
                yield event.plain_result('请使用格式：查询物品 物品名')
                return
            
            item_name = message[4:].strip()  # 去掉"查询物品"
            if not item_name:
                yield event.plain_result('请指定要查询的物品名称！')
                return
            
            # 首先检查是否是服装
            costume_info = self.query_costume_info(item_name)
            if costume_info:
                yield event.plain_result(costume_info)
                return
            
            # 然后检查是否是普通物品
            item_info = self.query_normal_item_info(item_name)
            if item_info:
                yield event.plain_result(item_info)
                return
            
            # 都没找到
            yield event.plain_result(f'未找到物品"{item_name}"！\n请检查物品名称是否正确。')
                
        except Exception as e:
            print(f"[Item Query] query_item函数发生异常: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f'查询物品功能出现错误: {str(e)}')

    def query_costume_info(self, item_name):
        """查询服装信息"""
        costume = get_costume_by_name(item_name)
        if not costume:
            return None
        
        info_text = f"🛍️【服装信息】🛍️\n"
        info_text += f"📦 名称：{costume['name']}\n"
        info_text += f"🎯 部位：{costume['slot']}\n"
        info_text += f"💰 价格：{costume['price']:,}金币\n"
        
        # 显示效果
        if costume.get('effects'):
            effects_desc = self.format_costume_effects(costume['effects'])
            info_text += f"✨ 效果：{effects_desc}\n"
        else:
            info_text += f"✨ 效果：无特殊效果\n"
        
        info_text += f"📝 描述：{costume['description']}\n"
        
        # 检查是否属于套装
        set_info = self.check_costume_set(item_name)
        if set_info:
            info_text += f"\n🌟 套装信息：{set_info}"
        
        info_text += f"\n💡 购买方式：服装商店"
        info_text += f"\n💡 使用方式：换衣 {item_name}"
        
        return info_text
    
    def query_normal_item_info(self, item_name):
        """查询普通物品信息"""
        if item_name not in ITEMS_DATA:
            return None
        
        item = ITEMS_DATA[item_name]
        
        info_text = f"📦【物品信息】📦\n"
        info_text += f"📝 名称：{item['name']}\n"
        info_text += f"🏷️ 分类：{item.get('category', '未分类')}\n"
        info_text += f"💰 售价：{item.get('sell_price', 0)}金币\n"
        
        # 显示购买价格（如果有的话）
        if item.get('buy_price'):
            info_text += f"💸 购买价格：{item['buy_price']}金币\n"
        
        # 显示效果描述
        if item.get('description'):
            info_text += f"📄 描述：{item['description']}\n"
        
        # 显示赠送效果
        if item.get('affection_value', 0) > 0 or any([
            item.get('hunger_effect', 0),
            item.get('mood_effect', 0),
            item.get('cleanliness_effect', 0),
            item.get('health_effect', 0)
        ]):
            info_text += f"\n💝 赠送效果：\n"
            if item.get('affection_value', 0) > 0:
                info_text += f"  • 好感度：+{item['affection_value']}\n"
            if item.get('hunger_effect', 0) != 0:
                info_text += f"  • 饥饿值：{item['hunger_effect']:+}\n"
            if item.get('mood_effect', 0) != 0:
                info_text += f"  • 心情：{item['mood_effect']:+}\n"
            if item.get('cleanliness_effect', 0) != 0:
                info_text += f"  • 清洁度：{item['cleanliness_effect']:+}\n"
            if item.get('health_effect', 0) != 0:
                info_text += f"  • 健康值：{item['health_effect']:+}\n"
        
        return info_text
    
    def format_costume_effects(self, effects):
        """格式化服装效果描述"""
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
    
    def check_costume_set(self, costume_name):
        """检查服装是否属于套装"""
        from ..config.costume_config import COSTUME_SET_BONUS
        
        for set_name, set_info in COSTUME_SET_BONUS.items():
            if costume_name in set_info["pieces"]:
                return f"{set_name} - {set_info['bonus_description']}"
        
        return None
    
    
    def get_effect_name(self, effect_key):
        """获取效果名称"""
        effect_names = {
            "affection": "好感度",
            "mood": "心情",
            "hunger": "饥饿值",
            "cleanliness": "清洁度",
            "health": "健康值",
            "level": "等级",
            "growth": "成长值",
            "moe_value": "妹抖值",
            "spoil_value": "撒娇值",
            "tsundere_value": "傲娇值",
            "dark_rate": "黑化率",
            "contrast_cute": "反差萌"
        }
        
        return effect_names.get(effect_key, effect_key)
    
