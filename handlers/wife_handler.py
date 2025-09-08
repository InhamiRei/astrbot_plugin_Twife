"""老婆相关命令处理器"""
import random
import re
from astrbot.api.all import *
from astrbot.api.message_components import Node, Nodes
from ..core.wife_system import *
from ..core.ntr_system import *
from ..core.data_manager import *
from ..config.settings import *
from ..config.messages import *
from ..utils.formatters import *
from ..utils.time_utils import *

class WifeHandler:
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
        if msg.startswith("牛老婆") or msg.startswith("查老婆"):
            target_name = msg[len(msg.split()[0]):].strip()
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

    async def animewife(self, event: AstrMessageEvent):
        """抽老婆功能"""
        group_id = event.message_obj.group_id
        if not group_id:
            return  # 在私聊中不提示信息，直接返回

        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 确保用户数据初始化
        get_user_data(user_id)

        # 检查抽老婆冷却时间（1分钟）
        cooldown_ok, remaining_seconds = check_animewife_cooldown(user_id, 1)
        if not cooldown_ok:
            yield event.plain_result(f': {nickname}，抽老婆冷却中，还需要等待{remaining_seconds}秒才能再次抽取~')
            return

        # 检查用户是否已经有老婆
        wife_data = get_user_wife_data(user_id)
        if wife_data:
            wife_name = wife_data[0]
            name = wife_name.split('.')[0]
            yield event.plain_result(f': {nickname}，你已经有老婆了（{name}）！如果想要新老婆，请先使用"净身出户"离婚。')
            return

        # 添加随机事件触发，有10%的概率触发特殊事件
        if has_random_fail_event(0.10):
            event_result = f": {nickname}，{get_random_fail_event()}"
            yield event.plain_result(event_result)
            return

        # 正常流程，抽取10个候选老婆
        available_wives = get_available_wives()
        if not available_wives:
            yield event.plain_result(f': {nickname}，目前所有的二次元老婆都已经名花有主了！请等待其他用户离婚后再来尝试吧~')
            return

        candidates = select_candidate_wives(available_wives, 10)
        
        # 存储候选老婆列表
        store_candidate_wives(user_id, candidates)

        # 更新抽老婆冷却时间
        update_animewife_cooldown(user_id)

        # 获取机器人自身信息
        try:
            bot_uin = event.get_self_id()
        except:
            bot_uin = "10001"  # 默认机器人QQ号
        
        bot_name = "小芋头"  # 默认机器人名称
        
        # 创建合并转发消息节点列表
        nodes = []
        
        # 添加标题节点
        title_node = Node(
            content=[Plain(f"💖 {nickname} 的候选老婆列表 💖\n\n请使用「确认老婆 名字」来选择你心仪的老婆吧~")],
            name=bot_name,
            uin=bot_uin
        )
        nodes.append(title_node)

        # 为所有候选老婆创建节点
        for i, wife_file in enumerate(candidates, 1):
            wife_name = wife_file.split('.')[0]
            
            # 创建消息内容
            content = [Plain(f"{i}. {wife_name}")]
            
            # 添加图片
            try:
                image_path, is_local = get_wife_image_path(wife_file)
                if is_local:
                    content.append(Image.fromFileSystem(image_path))
                else:
                    content.append(Image.fromURL(image_path))
            except Exception as e:
                print(f'加载老婆图片失败 {wife_file}: {e}')
                content.append(Plain("\n(图片加载失败)"))
            
            # 创建节点
            wife_node = Node(
                content=content,
                name=bot_name,
                uin=bot_uin
            )
            nodes.append(wife_node)
        
        # 尝试发送合并转发消息
        try:
            forward_message = Nodes(nodes)
            print(f'正在发送合并转发消息，包含{len(nodes)}个节点')
            yield event.chain_result([forward_message])
                
        except Exception as e:
            error_msg = str(e)
            print(f'发送合并转发消息失败: {error_msg}')
            
            # 检查是否是因为消息过大导致的错误
            if "retcode=9000" in error_msg or "ActionFailed" in error_msg:
                print(f'检测到消息内容过大错误(retcode=9000)，回退到文本模式发送')
                await self._send_candidates_as_text(event, nickname, candidates)
                return
            elif "status='failed'" in error_msg:
                print(f'合并转发发送失败，尝试文本模式发送')
                await self._send_candidates_as_text(event, nickname, candidates)
                return
            else:
                print(f'未知错误类型: {type(e).__name__}: {error_msg}')
                raise e

    async def _send_candidates_as_text(self, event: AstrMessageEvent, nickname: str, candidates: list):
        """回退方案：以文本方式发送候选老婆列表"""
        candidate_list = "、".join([name.split('.')[0] for name in candidates])
        
        result_message = f': {nickname}\n'
        result_message += f'❤️ 为你准备了10位候选老婆: \n'
        result_message += f'💖 {candidate_list}\n'
        result_message += f'💘 请使用"确认老婆 名字"来选择你心仪的老婆吧~'

        yield event.plain_result(result_message)

    async def confirm_wife(self, event: AstrMessageEvent):
        """确认老婆功能"""
        group_id = event.message_obj.group_id
        if not group_id:
            return

        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 检查用户是否已经有老婆
        wife_data = get_user_wife_data(user_id)
        if wife_data:
            wife_name = wife_data[0]
            name = wife_name.split('.')[0]
            yield event.plain_result(f': {nickname}，你已经有老婆了（{name}）！如果想要新老婆，请先使用"净身出户"离婚。')
            return

        # 检查用户是否有候选老婆列表
        candidates = get_candidate_wives(user_id)
        if not candidates:
            yield event.plain_result(f': {nickname}，你还没有候选老婆列表，请先使用"抽老婆"命令抽取候选老婆。')
            return

        # 解析命令，获取老婆名字
        message_str = event.message_str.strip()
        if not message_str.startswith("确认老婆"):
            yield event.plain_result(f': {nickname}，请使用正确的格式：确认老婆 名字')
            return
            
        wife_name_input = message_str[4:].strip()  # 去掉"确认老婆"前缀
        if not wife_name_input:
            candidate_list = "、".join([name.split('.')[0] for name in candidates])
            yield event.plain_result(f': {nickname}，请指定要确认的老婆名字：\n{candidate_list}\n\n格式：确认老婆 名字')
            return

        # 在候选列表中查找匹配的老婆
        selected_wife = find_wife_in_candidates(user_id, wife_name_input)
        if not selected_wife:
            candidate_list = "、".join([name.split('.')[0] for name in candidates])
            yield event.plain_result(f': {nickname}，没有找到名为"{wife_name_input}"的候选老婆。\n你的候选列表：\n{candidate_list}')
            return
        elif selected_wife == "TAKEN":
            yield event.plain_result(f': {nickname}，很遗憾，名为"{wife_name_input}"的老婆已经被其他人抢先选择了！请从剩余的候选老婆中选择一位吧~')
            return

        # 确认成功，设置老婆
        name = selected_wife.split('.')[0]
        text_message = f': {nickname}，恭喜你！你的二次元老婆是{name}哒~'

        # 尝试发送图片
        try:
            image_path, is_local = get_wife_image_path(selected_wife)
            if is_local:
                chain = [
                    Plain(text_message),
                    Image.fromFileSystem(image_path)
                ]
            else:
                chain = [
                    Plain(text_message),
                    Image.fromURL(image_path)
                ]
            yield event.chain_result(chain)
        except Exception as e:
            print(f'发送老婆图片时发生错误{type(e)}')
            yield event.plain_result(text_message)

        # 设置老婆数据，特殊属性从0开始
        set_user_wife_data(user_id, selected_wife, nickname, False, 0)
        
        # 清除候选老婆列表
        clear_candidate_wives(user_id)

    async def search_wife(self, event: AstrMessageEvent):
        """查老婆功能"""
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
                yield event.plain_result('未找到老婆信息！')
                return

            wife_name = wife_data[0]
            name = wife_name.split('.')[0]
            target_nickname = wife_data[2]
            affection = wife_data[4]
            purelove_status = wife_data[3]
            level = wife_data[5]
            growth = wife_data[6]
            hunger = wife_data[7]
            cleanliness = wife_data[8]
            health = wife_data[9]
            mood = wife_data[10]
            status = wife_data[11]
            education_level = wife_data[12]
            knowledge = wife_data[13]
            
            # 格式化老婆状态
            wife_status_str = format_wife_status(level, growth, hunger, cleanliness, health, mood, status)
            
            # 格式化学历和学识信息
            from ..config.education import format_education_display
            education_str = format_education_display(education_level, knowledge)
            
            # 获取当前活动状态
            from ..core import data_manager
            activity_type, activity_desc, remaining_time = get_user_activity_status(target_id, data_manager.study_status, data_manager.work_status, data_manager.WORK_LIST)
            if remaining_time:
                activity_status_str = f"🎯 当前状态：{activity_desc}（还剩{remaining_time}）"
            else:
                activity_status_str = f"🎯 当前状态：{activity_desc}"
            
            # 获取杀怪统计
            kill_stats_display = get_kill_stats_display(target_id)
            kill_stats_str = f"⚔️ 已击败：{kill_stats_display}"
            
            # 判断是否为本人查询
            if target_id == user_id:
                # 本人查询
                affection_status = get_affection_status(affection)
                if purelove_status:
                    purelove_text = "🛡️ 纯爱无敌状态：已开启，爱情固若金汤！"
                else:
                    purelove_text = "⚠️ 纯爱无敌状态：未开启，小心牛头人攻击！"
                text_message = f': {target_nickname}的二次元老婆是{name}哒~\n\n{wife_status_str}\n\n{activity_status_str}\n\n📚 {education_str}\n💖 好感度：{affection:.1f}\n{affection_status}\n{purelove_text}\n\n{kill_stats_str}'
            else:
                # 他人查询
                if purelove_status:
                    purelove_text = "🛡️ 纯爱无敌状态：已开启"
                else:
                    purelove_text = "⚠️ 纯爱无敌状态：未开启"
                text_message = f': {target_nickname}的二次元老婆是{name}哒~\n\n{wife_status_str}\n\n{activity_status_str}\n\n📚 {education_str}\n💖 他们的好感度：{affection:.1f}\n{purelove_text}\n{kill_stats_str}'

            # 尝试发送带图片的消息
            try:
                image_path, is_local = get_wife_image_path(wife_name)
                
                if is_local:
                    chain = [
                        Plain(text_message),
                        Image.fromFileSystem(image_path)
                    ]
                else:
                    chain = [
                        Plain(text_message),
                        Image.fromURL(image_path)
                    ]
                yield event.chain_result(chain)
            except Exception as e:
                print(f'[Wife Plugin] 发送老婆图片时发生错误: {e}')
                yield event.plain_result(text_message)
                
        except Exception as e:
            print(f"[Wife Plugin] search_wife函数发生异常: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f'查老婆功能出现错误: {str(e)}')

    async def divorce(self, event: AstrMessageEvent):
        """净身出户功能"""
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

        # 获取用户老婆数据
        wife_data = get_user_wife_data(user_id)
        if not wife_data:
            yield event.plain_result(f': {nickname}，你目前没有老婆，无法净身出户。')
            return

        wife_name = wife_data[0]
        wife_name_display = wife_name.split('.')[0]

        # 添加10%的失败概率
        if random.random() < 0.1:
            fail_text = f': {nickname}，{wife_name_display}{random.choice(DIVORCE_FAIL_EVENTS)}'
            yield event.plain_result(fail_text)
            return

        # 离婚成功，删除用户的老婆记录
        delete_user_wife_data(user_id)
        
        # 清除工作和学习状态
        clear_user_work_study_status(user_id)
        
        # 清除冷却时间记录
        clear_purelove_cooldown(user_id)

        yield event.plain_result(f': {nickname}，你已经和{wife_name_display}离婚了，净身出户成功！')
