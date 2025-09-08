"""老婆特殊属性处理器"""
import re
from astrbot.api.all import *
from ..core.data_manager import *

class SpecialAttributesHandler:
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
        if msg.startswith("老婆属性"):
            target_name = msg[len("老婆属性"):].strip()
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

    async def query_wife_attributes(self, event: AstrMessageEvent):
        """查询老婆特殊属性功能"""
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
            
            # 格式化属性显示
            attributes_text = self.format_attributes_display(
                moe_value, spoil_value, tsundere_value, dark_rate, contrast_cute
            )
            
            # 判断是否为本人查询
            if target_id == user_id:
                text_message = f': {target_nickname}的老婆{name}的特殊属性：\n{attributes_text}'
            else:
                text_message = f': {target_nickname}的老婆{name}的特殊属性：\n{attributes_text}'

            # 直接发送文本消息，不带图片
            yield event.plain_result(text_message)
                
        except Exception as e:
            print(f"[Wife Plugin] query_wife_attributes函数发生异常: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f'查询老婆属性功能出现错误: {str(e)}')

    def format_attributes_display(self, moe_value, spoil_value, tsundere_value, dark_rate, contrast_cute):
        """格式化属性显示"""
        
        attributes_text = f"""💕 妹抖值：{moe_value}
🎀 撒娇值：{spoil_value}
😤 傲娇值：{tsundere_value}
🖤 黑化率：{dark_rate}
✨ 反差萌：{contrast_cute}"""
        
        return attributes_text

