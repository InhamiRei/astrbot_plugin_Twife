"""换衣处理器"""
import re
from astrbot.api.all import *
from ..core.data_manager import *
from ..config.costume_config import get_costume_by_name

class DressUpHandler:
    def __init__(self):
        pass

    async def dress_up(self, event: AstrMessageEvent):
        """换衣功能"""
        try:
            group_id = event.message_obj.group_id
            if not group_id:
                yield event.plain_result('该功能仅支持群聊，请在群聊中使用。')
                return

            user_id = str(event.get_sender_id())
            message = event.message_str.strip()
            
            # 检查是否有老婆
            wife_data = get_user_wife_data(user_id)
            if not wife_data:
                yield event.plain_result('你还没有老婆呢！请先使用"抽老婆"命令。')
                return
            
            # 解析换衣命令
            if not message.startswith("换衣"):
                yield event.plain_result('请使用格式：换衣 服装名')
                return
            
            costume_name = message[2:].strip()  # 去掉"换衣"
            if not costume_name:
                yield event.plain_result('请指定要穿的服装名称！\n使用"资产查询"查看衣柜中的服装。')
                return
            
            # 获取用户数据
            user_data_obj = get_user_data(user_id)
            wardrobe = user_data_obj.get("wardrobe", {})
            equipment = user_data_obj.get("equipment", {})
            
            # 检查衣柜中是否有该服装
            if costume_name not in wardrobe:
                yield event.plain_result(f'衣柜中没有"{costume_name}"！\n使用"服装商店"购买或"资产查询"查看已有服装。')
                return
            
            costume_info = wardrobe[costume_name]
            slot = costume_info["slot"]
            
            # 检查该部位是否已有装备
            current_equipment = equipment.get(slot)
            if current_equipment:
                # 将当前装备放回衣柜
                current_costume = get_costume_by_name(current_equipment)
                if current_costume:
                    wardrobe[current_equipment] = {
                        "name": current_equipment,
                        "slot": current_costume["slot"],
                        "effects": current_costume["effects"],
                        "description": current_costume["description"]
                    }
            
            # 装备新服装
            equipment[slot] = costume_name
            
            # 从衣柜中移除已装备的服装
            del wardrobe[costume_name]
            
            # 保存数据
            update_user_data(user_id, wardrobe=wardrobe, equipment=equipment)
            
            wife_name = wife_data[0].split('.')[0]
            result_text = f'成功为{wife_name}换上了"{costume_name}"！'
            
            if current_equipment:
                result_text += f'\n原来的"{current_equipment}"已放回衣柜。'
            
            # 显示装备效果
            costume = get_costume_by_name(costume_name)
            if costume and "effects" in costume:
                effects_desc = self.format_effects_description(costume["effects"])
                result_text += f'\n✨ 装备效果：{effects_desc}'
            
            yield event.plain_result(result_text)
                
        except Exception as e:
            print(f"[Dress Up] dress_up函数发生异常: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f'换衣功能出现错误: {str(e)}')

    async def undress(self, event: AstrMessageEvent):
        """脱下装备功能"""
        try:
            group_id = event.message_obj.group_id
            if not group_id:
                yield event.plain_result('该功能仅支持群聊，请在群聊中使用。')
                return

            user_id = str(event.get_sender_id())
            message = event.message_str.strip()
            
            # 检查是否有老婆
            wife_data = get_user_wife_data(user_id)
            if not wife_data:
                yield event.plain_result('你还没有老婆呢！请先使用"抽老婆"命令。')
                return
            
            # 解析脱下命令
            if not message.startswith("脱下"):
                yield event.plain_result('请使用格式：脱下 服装名 或 脱下 部位')
                return
            
            target = message[2:].strip()  # 去掉"脱下"
            if not target:
                yield event.plain_result('请指定要脱下的服装名称或部位！')
                return
            
            # 获取用户数据
            user_data_obj = get_user_data(user_id)
            wardrobe = user_data_obj.get("wardrobe", {})
            equipment = user_data_obj.get("equipment", {})
            
            # 确定要脱下的服装
            costume_name = None
            slot = None
            
            # 检查是否是直接指定服装名
            for eq_slot, eq_name in equipment.items():
                if eq_name and eq_name == target:
                    costume_name = eq_name
                    slot = eq_slot
                    break
            
            # 如果没找到，检查是否是指定部位
            if not costume_name:
                if target in equipment:
                    slot = target
                    costume_name = equipment.get(slot)
                else:
                    yield event.plain_result(f'未找到"{target}"！请检查服装名或部位是否正确。')
                    return
            
            # 检查该部位是否有装备
            if not costume_name:
                yield event.plain_result(f'{slot}部位没有装备任何服装！')
                return
            
            # 脱下装备，放回衣柜
            equipment[slot] = None
            costume = get_costume_by_name(costume_name)
            if costume:
                wardrobe[costume_name] = {
                    "name": costume_name,
                    "slot": costume["slot"],
                    "effects": costume["effects"],
                    "description": costume["description"]
                }
            
            # 保存数据
            update_user_data(user_id, wardrobe=wardrobe, equipment=equipment)
            
            wife_name = wife_data[0].split('.')[0]
            yield event.plain_result(f'成功为{wife_name}脱下了"{costume_name}"！\n服装已放回衣柜。')
                
        except Exception as e:
            print(f"[Dress Up] undress函数发生异常: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f'脱下装备功能出现错误: {str(e)}')

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
