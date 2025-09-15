"""老婆详情处理器"""
import re
from astrbot.api.all import *
from ..core.data_manager import *
from ..config.costume_config import calculate_equipment_effects, get_costume_by_name

class WifeDetailsHandler:
    def __init__(self):
        pass

    def parse_at_target(self, event):
        """解析@目标"""
        for comp in event.message_obj.message:
            if isinstance(comp, At):
                return str(comp.qq)
        return None

    def parse_target(self, event):
        """解析@目标或用户名"""
        target_id = self.parse_at_target(event)
        if target_id:
            return target_id
        msg = event.message_str.strip()
        if msg.startswith("老婆详情"):
            target_name = msg[len("老婆详情"):].strip()
            if target_name:
                # 遍历全局老婆数据查找匹配的昵称
                for user_id, user_data in global_wife_data.items():
                    try:
                        # 检查存储的昵称是否匹配
                        if len(user_data) > 2:
                            nick_name = user_data[2]  # 昵称存储在索引2
                            if re.search(re.escape(target_name), nick_name, re.IGNORECASE):
                                return user_id
                    except Exception as e:
                        print(f'解析目标用户时出错: {e}')
        return None

    async def query_wife_details(self, event: AstrMessageEvent):
        """查询老婆详情功能"""
        try:
            group_id = event.message_obj.group_id
            if not group_id:
                yield event.plain_result('该功能仅支持群聊，请在群聊中使用。')
                return

            target_id = self.parse_target(event)

            try:
                user_id = str(event.get_sender_id())
                nickname = event.get_sender_name()
            except AttributeError as e:
                yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
                return

            target_id = target_id or user_id
            
            # 确保用户数据初始化
            get_user_data(user_id)
            if target_id != user_id:
                get_user_data(target_id)

            # 获取目标用户的老婆数据
            wife_data = get_user_wife_data(target_id)
            if not wife_data:
                yield event.plain_result('未找到老婆信息！请先使用"抽老婆"命令抽取一位老婆吧~')
                return

            # 确保老婆数据包含所有属性
            if len(wife_data) < 19:
                # 为旧数据补充默认属性（从0开始）
                while len(wife_data) < 19:
                    wife_data.append(0)  # 所有特殊属性都从0开始
                save_global_wife_data()  # 保存更新后的数据

            wife_name = wife_data[0]
            name = wife_name.split('.')[0]
            target_nickname = wife_data[2]
            moe_value = wife_data[14]
            spoil_value = wife_data[15]
            tsundere_value = wife_data[16]
            dark_rate = wife_data[17]
            contrast_cute = wife_data[18]
            
            # 获取用户装备信息
            user_data_obj = get_user_data(target_id)
            equipped_items = user_data_obj.get("equipment", {})
            
            # 计算装备加成效果
            equipment_effects, set_bonus = calculate_equipment_effects(equipped_items)
            
            # 计算最终属性（基础属性 + 装备加成的百分比）
            final_moe = int(moe_value * (1 + equipment_effects["moe_value"] / 100))
            final_spoil = int(spoil_value * (1 + equipment_effects["spoil_value"] / 100))
            final_tsundere = int(tsundere_value * (1 + equipment_effects["tsundere_value"] / 100))
            final_dark_rate = int(dark_rate * (1 + equipment_effects["dark_rate"] / 100))
            final_contrast_cute = int(contrast_cute * (1 + equipment_effects["contrast_cute"] / 100))
            
            # 格式化属性显示
            attributes_text = self.format_attributes_display(
                moe_value, spoil_value, tsundere_value, dark_rate, contrast_cute,
                final_moe, final_spoil, final_tsundere, final_dark_rate, final_contrast_cute,
                equipment_effects
            )
            
            # 格式化装备显示
            equipment_text = self.format_equipment_display(equipped_items, set_bonus)
            
            # 判断是否为本人查询
            if target_id == user_id:
                text_message = f': {target_nickname}的老婆{name}的详细信息：\n{attributes_text}\n\n{equipment_text}'
            else:
                text_message = f': {target_nickname}的老婆{name}的详细信息：\n{attributes_text}\n\n{equipment_text}'

            # 直接发送文本消息，不带图片
            yield event.plain_result(text_message)
                
        except Exception as e:
            print(f"[Wife Plugin] query_wife_details函数发生异常: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f'查询老婆详情功能出现错误: {str(e)}')

    def format_attributes_display(self, base_moe, base_spoil, base_tsundere, base_dark_rate, base_contrast_cute,
                                 final_moe, final_spoil, final_tsundere, final_dark_rate, final_contrast_cute, equipment_effects):
        """格式化属性显示"""
        
        attributes_text = "【特殊属性】\n"
        
        # 如果有装备加成，显示基础值+加成值=最终值的格式
        if any(effect > 0 for effect in equipment_effects.values()):
            # 直接使用装备提供的真实加成百分比，而不是反推计算
            actual_moe_increase = int(equipment_effects['moe_value'])
            actual_spoil_increase = int(equipment_effects['spoil_value'])
            actual_tsundere_increase = int(equipment_effects['tsundere_value'])
            actual_dark_increase = int(equipment_effects['dark_rate'])
            actual_contrast_increase = int(equipment_effects['contrast_cute'])

            attributes_text += f"💕 妹抖值：{base_moe} (+{actual_moe_increase}%) = {final_moe}\n"
            attributes_text += f"🎀 撒娇值：{base_spoil} (+{actual_spoil_increase}%) = {final_spoil}\n"
            attributes_text += f"😤 傲娇值：{base_tsundere} (+{actual_tsundere_increase}%) = {final_tsundere}\n"
            attributes_text += f"🖤 黑化率：{base_dark_rate} (+{actual_dark_increase}%) = {final_dark_rate}\n"
            attributes_text += f"✨ 反差萌：{base_contrast_cute} (+{actual_contrast_increase}%) = {final_contrast_cute}"
        else:
            # 没有装备加成时，只显示基础值
            attributes_text += f"💕 妹抖值：{base_moe}\n"
            attributes_text += f"🎀 撒娇值：{base_spoil}\n"
            attributes_text += f"😤 傲娇值：{base_tsundere}\n"
            attributes_text += f"🖤 黑化率：{base_dark_rate}\n"
            attributes_text += f"✨ 反差萌：{base_contrast_cute}"
        
        return attributes_text
        
    def format_equipment_display(self, equipped_items, set_bonus):
        """格式化装备显示"""
        
        equipment_text = "【当前装备】\n"
        
        slot_names = {
            "头部": "👑 头部",
            "身体": "👗 身体",
            "手部": "🧤 手部", 
            "腿部": "👖 腿部",
            "脚部": "👠 脚部",
            "手持": "🎪 手持",
            "饰品": "💎 饰品"
        }
        
        has_equipment = False
        for slot, item_name in equipped_items.items():
            if item_name:
                has_equipment = True
                equipment_text += f"{slot_names.get(slot, slot)}：{item_name}\n"
            else:
                equipment_text += f"{slot_names.get(slot, slot)}：无\n"
        
        if not has_equipment:
            equipment_text += "暂无任何装备\n"
        
        # 显示套装效果
        if set_bonus:
            equipment_text += f"\n🌟 套装效果：{set_bonus['bonus_description']}"
            
        return equipment_text.rstrip()

