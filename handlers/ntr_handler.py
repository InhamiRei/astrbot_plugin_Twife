"""NTR相关命令处理器"""
import random
import re
from astrbot.api.all import *
from ..core.data_manager import *
from ..core.ntr_system import *
from ..config.settings import *
from ..config.messages import *

class NTRHandler:
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
        if msg.startswith("牛老婆"):
            target_name = msg[len(msg.split()[0]):].strip()
            if target_name:
                # 遍历全局老婆数据查找匹配的昵称
                for user_id, user_data in global_wife_data.items():
                    try:
                        if len(user_data) > 2:
                            nick_name = user_data[2]
                            if re.search(re.escape(target_name), nick_name, re.IGNORECASE):
                                return user_id
                    except Exception as e:
                        print(f'解析目标用户时出错: {e}')
        return None

    async def ntr_wife(self, event: AstrMessageEvent):
        """牛老婆功能"""
        # 临时禁用牛老婆功能
        yield event.plain_result("纯爱战神一刀一个牛头人，现阶段无法牛老婆")
        return
        
        group_id = event.message_obj.group_id
        if not group_id:
            yield event.plain_result('该功能仅支持群聊，请在群聊中使用。')
            return

        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 确保用户数据初始化
        get_user_data(user_id)

        # 检查每日牛老婆次数限制
        current_ntr_count = get_daily_limit_data(user_id, 'ntr')
        if current_ntr_count >= NTR_MAX_DAILY:
            yield event.plain_result(f': {nickname}，{NTR_MAX_NOTICE}')
            return

        target_id = self.parse_target(event)
        if not target_id:
            yield event.plain_result(f': {nickname}，请指定一个要下手的目标')
            return

        if user_id == target_id:
            yield event.plain_result(f': {nickname}，不可以自己牛自己')
            return

        # 检查目标用户是否有老婆
        target_wife_data = get_user_wife_data(target_id)
        if not target_wife_data:
            yield event.plain_result('需要对方有老婆才能牛')
            return

        # 检查目标用户是否开启了纯爱无敌状态
        if target_wife_data[3]:  # purelove状态
            target_nickname = target_wife_data[2]
            yield event.plain_result(f': {nickname}，{target_nickname}处于纯爱无敌状态，他们的爱情坚不可摧！')
            return

        # 增加牛老婆次数
        update_daily_limit_data(user_id, 'ntr', current_ntr_count + 1)

        # 检查NTR成功率
        if check_ntr_success(user_id, group_id):
            target_wife = target_wife_data[0]
            target_nickname = target_wife_data[2]
            
            # 清除被牛者的工作和学习状态
            clear_user_work_study_status(target_id)
            # 清除牛者自己的工作和学习状态
            clear_user_work_study_status(user_id)
            
            # 删除被牛者的记录
            delete_user_wife_data(target_id)
            # 删除牛者自己的记录（如果有）
            delete_user_wife_data(user_id)
            # 写入新配置
            set_user_wife_data(user_id, target_wife, nickname, False, 0)
            
            # 记录刚牛来老婆的时间
            record_newly_acquired_wife(user_id)
            
            yield event.plain_result(f': {nickname}，你的阴谋已成功！成功牛走了{target_nickname}的老婆！')
        else:
            # 获取更新后的次数
            updated_ntr_count = get_daily_limit_data(user_id, 'ntr')
            remaining_times = NTR_MAX_DAILY - updated_ntr_count
            yield event.plain_result(f': {nickname}，{get_random_ntr_fail_event()}你还有{remaining_times}次机会')

    async def ntr_feast(self, event: AstrMessageEvent):
        """牛头人盛宴功能"""
        group_id = event.message_obj.group_id
        if not group_id:
            yield event.plain_result('该功能仅支持群聊，请在群聊中使用。')
            return

        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 确保用户数据初始化
        get_user_data(user_id)

        # 检查该群组是否已激活牛头人盛宴
        is_active, minutes, seconds = check_ntr_feast_active(group_id)
        if is_active:
            yield event.plain_result(f': {nickname}，牛头人盛宴已经开启！还剩余{minutes}分{seconds}秒。在此期间牛老婆概率大幅提升！')
            return

        # 有50%概率开启牛头人盛宴
        if random.random() < 0.5:
            activate_ntr_feast(group_id, 5)
            yield event.plain_result(f'牛头人盛宴开启成功！接下来的5分钟内，所有人牛老婆的成功率提升到50%，牛头人之王的成功率提升到80%！')
        else:
            # 失败事件
            ntr_feast_fail_events = [
                f': {nickname}的牛头人盛宴刚准备开始，结果食材全被纯爱大厨换成了心形巧克力！',
                f': {nickname}请来的牛头人乐队，半路被纯爱歌姬拐走去唱情歌了！',
                f': {nickname}刚布置好宴会场地，就被纯爱装修队粉刷成了粉红爱心小屋！',
                f': {nickname}的牛头人盛宴开幕式烟花一响，居然炸出了一行字："纯爱无敌"！',
                f': {nickname}的牛头人盛宴大门口，突然竖起了纯爱协会的"禁止通行"路牌！'
            ]
            yield event.plain_result(random.choice(ntr_feast_fail_events))

    async def ntr_invincible(self, event: AstrMessageEvent):
        """牛头人无可匹敌功能"""
        group_id = event.message_obj.group_id
        if not group_id:
            yield event.plain_result('该功能仅支持群聊，请在群聊中使用。')
            return

        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 确保用户数据初始化
        get_user_data(user_id)

        # 有40%的几率失败
        if random.random() < 0.4:
            yield event.plain_result(f': {nickname}，{get_random_ntr_fail_event()}')
            return

        # 给予NTR奖励
        is_king = (user_id == "2675588467")
        bonus_times, title, remaining_times = give_ntr_bonus(user_id, is_king)
        yield event.plain_result(f': {nickname}，{title}的力量觉醒！你获得了{bonus_times}次额外的牛老婆机会！当前剩余次数：{remaining_times}次')

    async def pure_love_invincible(self, event: AstrMessageEvent):
        """纯爱无敌功能"""
        group_id = event.message_obj.group_id
        if not group_id:
            yield event.plain_result('该功能仅支持群聊，请在群聊中使用。')
            return

        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 确保用户数据初始化
        get_user_data(user_id)

        # 检查用户是否有老婆
        wife_data = get_user_wife_data(user_id)
        if not wife_data:
            yield event.plain_result(f': {nickname}，你还没有老婆，请先使用"抽老婆"命令获取一个老婆再开启纯爱无敌状态！')
            return

        # 检查用户是否已经开启纯爱无敌状态
        if wife_data[3]:  # purelove状态
            yield event.plain_result(f': {nickname}，你已经处于纯爱无敌状态，你们的爱情坚不可摧！')
            return
            
        # 检查用户是否在冷却期内
        cooldown_ok, minutes, seconds = check_purelove_cooldown(user_id, 5)
        if not cooldown_ok:
            yield event.plain_result(f': {nickname}，你们的真爱需要经受考验，需要等待{minutes}分{seconds}秒才能永结良缘！')
            return

        # 有80%概率开启纯爱无敌状态成功
        if random.random() < 0.8:
            # 更新用户的纯爱无敌状态
            update_user_wife_data(user_id, purelove=True)
            
            # 清除冷却时间记录
            clear_purelove_cooldown(user_id)
                
            yield event.plain_result(f': {nickname}，纯爱无敌状态已开启！你的老婆将受到永久的纯爱保护，任何牛头人都无法撼动你们的爱情！')
        else:
            yield event.plain_result(f': {nickname}，你尝试开启纯爱无敌状态，但失败了。也许需要更强大的纯爱之心！')

    async def pure_love_shatter(self, event: AstrMessageEvent):
        """纯爱破碎功能"""
        group_id = event.message_obj.group_id
        if not group_id:
            yield event.plain_result('该功能仅支持群聊，请在群聊中使用。')
            return

        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 确保用户数据初始化
        get_user_data(user_id)

        # 检查用户是否有老婆
        wife_data = get_user_wife_data(user_id)
        if not wife_data:
            yield event.plain_result(f': {nickname}，你还没有老婆，无法进行纯爱破碎！')
            return

        # 检查用户是否开启了纯爱无敌状态
        if not wife_data[3]:  # purelove状态
            yield event.plain_result(f': {nickname}，你当前没有纯爱无敌状态，无需破碎！')
            return

        # 有10%概率破碎失败
        if random.random() < 0.1:
            yield event.plain_result(f': {nickname}，{random.choice(PURE_LOVE_SHATTER_FAIL_EVENTS)}')
            return

        # 破碎成功
        update_user_wife_data(user_id, purelove=False)
        
        wife_name = wife_data[0]
        wife_display_name = wife_name.split('.')[0]
        
        success_text = random.choice(PURE_LOVE_SHATTER_SUCCESS_EVENTS).format(wife_name=wife_display_name)
        yield event.plain_result(f': {nickname}，{success_text}')
