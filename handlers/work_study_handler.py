"""工作学习相关命令处理器"""
import random
from datetime import datetime, timedelta
from astrbot.api.all import *
from ..core import data_manager
from ..core.education_system import *
from ..config.education import get_education_index, EDUCATION_LEVELS

class WorkStudyHandler:
    def __init__(self):
        pass

    async def go_study(self, event: AstrMessageEvent):
        """出门学习功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
            print(f"[工作学习处理器] 收到学习请求 - 用户ID: {user_id}, 昵称: {nickname}")
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 解析命令，获取学习小时数
        message_str = event.message_str.strip()
        if not message_str.startswith("出门学习"):
            yield event.plain_result(f': {nickname}，请使用正确的格式：出门学习 小时数')
            return
            
        try:
            hours_str = message_str[4:].strip()  # 去掉"出门学习"前缀
            if not hours_str:
                yield event.plain_result(f': {nickname}，请指定学习小时数，格式：出门学习 小时数（1-12小时）')
                return
                
            hours = int(hours_str)
            if hours < 1 or hours > 12:
                yield event.plain_result(f': {nickname}，学习时间必须在1-12小时之间')
                return
        except ValueError:
            yield event.plain_result(f': {nickname}，请输入有效的小时数（1-12）')
            return

        # 检查学习要求
        requirements_ok, requirements_message = check_study_requirements(user_id)
        if not requirements_ok:
            yield event.plain_result(f': {nickname}，{requirements_message}')
            return

        # 检查冲突
        conflict_exists, conflict_message = check_study_conflict(user_id)
        if conflict_exists:
            yield event.plain_result(f': {nickname}，{conflict_message}')
            return
        
        # 检查是否正在旅行中
        travel_conflict_exists, travel_conflict_message = self._check_travel_conflict(user_id)
        if travel_conflict_exists:
            yield event.plain_result(f': {nickname}，{travel_conflict_message}')
            return

        # 开始学习
        group_id = str(event.message_obj.group_id) if hasattr(event.message_obj, 'group_id') else None
        end_time = start_study(user_id, hours, nickname, group_id)
        
        # 获取老婆名称和学历
        wife_data = data_manager.get_user_wife_data(user_id)
        wife_name = wife_data[0]
        wife_display_name = wife_name.split('.')[0]
        education_level = wife_data[12]
        
        # 随机学习事件描述
        study_events = get_study_events()
        study_event = f"{wife_display_name}{random.choice(study_events)}"
        
        result_message = f': {nickname}，{study_event}\n'
        result_message += f'📚 当前学历：{education_level}\n'
        result_message += f'⏰ 学习时长：{hours}小时\n'
        result_message += f'🕐 预计完成时间：{end_time.strftime("%H:%M")}\n'
        result_message += f'💡 学习完成后她会获得学识和经验，但可能会有点饿哦~'
        
        yield event.plain_result(result_message)

    async def work_list(self, event: AstrMessageEvent):
        """打工列表功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 检查工作配置是否加载
        if not data_manager.WORK_LIST:
            yield event.plain_result(f': {nickname}，打工系统暂未配置，请联系管理员添加工作配置文件。')
            return

        # 检查用户是否有老婆
        wife_data = data_manager.get_user_wife_data(user_id)
        if not wife_data:
            yield event.plain_result(f': {nickname}，你还没有老婆，无法查看打工列表。请先使用"抽老婆"命令获取一个老婆！')
            return

        # 获取用户老婆的等级和学历
        user_level = wife_data[5]  # 等级
        user_education = wife_data[12]  # 学历
        user_education_index = get_education_index(user_education)

        work_list_message = f": {nickname}的打工列表 💼\n"
        work_list_message += f"👤 当前等级：Lv.{user_level} | 📚 当前学历：{user_education}\n\n"

        available_works = []
        unavailable_works = []

        for work in data_manager.WORK_LIST:
            work_id = work["id"]
            name = work["name"]
            pay = work["pay"]
            duration = work["duration"]
            level_required = work["level_required"]
            education_required = work["education_required"]
            education_required_name = EDUCATION_LEVELS[education_required]["name"]

            if user_level >= level_required and user_education_index >= education_required:
                # 可以做的工作
                available_works.append(f"{work_id:2d}. {name} 💰{pay}金币 ⏰{duration}h")
            else:
                # 不能做的工作
                unavailable_works.append(f"{work_id:2d}. {name} (需要Lv.{level_required}, {education_required_name})")

        if available_works:
            work_list_message += "✅ 可接受的工作：\n"
            work_list_message += "\n".join(available_works)
        else:
            work_list_message += "❌ 暂无可接受的工作"

        if unavailable_works:
            work_list_message += "\n🔒 暂时无法接受的工作：\n"
            work_list_message += "\n".join(unavailable_works[:5])  # 只显示前5个避免刷屏
            if len(unavailable_works) > 5:
                work_list_message += f"\n...还有{len(unavailable_works)-5}个工作需要更高等级"

        work_list_message += "\n\n💡 使用「出门打工 序号」开始打工"

        yield event.plain_result(work_list_message)

    async def go_work(self, event: AstrMessageEvent):
        """出门打工功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法通过 event.get_sender_id() 获取用户 ID，请检查消息事件对象。')
            return

        # 检查工作配置是否加载
        if not data_manager.WORK_LIST:
            yield event.plain_result(f': {nickname}，打工系统暂未配置，请联系管理员添加工作配置文件。')
            return

        # 解析命令，获取工作序号
        message_str = event.message_str.strip()
        if not message_str.startswith("出门打工"):
            yield event.plain_result(f': {nickname}，请使用正确的格式：出门打工 序号')
            return
            
        try:
            work_id_str = message_str[4:].strip()  # 去掉"出门打工"前缀
            if not work_id_str:
                yield event.plain_result(f': {nickname}，请指定工作序号，格式：出门打工 序号')
                return
                
            work_id = int(work_id_str)
            
            # 查找对应的工作
            selected_work = None
            for work in data_manager.WORK_LIST:
                if work["id"] == work_id:
                    selected_work = work
                    break
            
            if not selected_work:
                yield event.plain_result(f': {nickname}，找不到序号为{work_id}的工作，请使用「打工列表」查看可用工作')
                return
                
        except ValueError:
            yield event.plain_result(f': {nickname}，请输入有效的工作序号')
            return

        # 检查用户是否有老婆
        wife_data = data_manager.get_user_wife_data(user_id)
        if not wife_data:
            yield event.plain_result(f': {nickname}，你还没有老婆，无法让她出门打工。请先使用"抽老婆"命令获取一个老婆！')
            return

        # 检查老婆状态是否满足打工要求
        from ..utils.validators import check_wife_status_for_activity
        status_ok, status_message = check_wife_status_for_activity(wife_data)
        if not status_ok:
            wife_name = wife_data[0]
            wife_display_name = wife_name.split('.')[0]
            yield event.plain_result(f': {nickname}，{wife_display_name}{status_message[3:]}！建议先使用礼物改善她的状态~')
            return

        # 检查等级和学历要求
        user_level = wife_data[5]  # 等级
        user_education = wife_data[12]  # 学历
        user_education_index = get_education_index(user_education)
        
        level_required = selected_work["level_required"]
        education_required = selected_work["education_required"]
        education_required_name = EDUCATION_LEVELS[education_required]["name"]
        
        if user_level < level_required:
            yield event.plain_result(f': {nickname}，{selected_work["name"]}需要等级Lv.{level_required}，你的老婆当前等级Lv.{user_level}，等级不足！')
            return
            
        if user_education_index < education_required:
            yield event.plain_result(f': {nickname}，{selected_work["name"]}需要学历{education_required_name}，你的老婆当前学历{user_education}，学历不足！')
            return

        # 检查是否已经在学习中
        if user_id in data_manager.study_status and data_manager.study_status[user_id].get('is_studying', False):
            end_time_str = data_manager.study_status[user_id]['end_time']
            end_time = datetime.fromisoformat(end_time_str)
            current_time = datetime.now()
            remaining = end_time - current_time
            if remaining.total_seconds() > 0:
                hours_left = int(remaining.total_seconds() // 3600)
                minutes_left = int((remaining.total_seconds() % 3600) // 60)
                yield event.plain_result(f': {nickname}，你的老婆正在学习中，还需要{hours_left}小时{minutes_left}分钟才能完成！不能同时进行打工。')
                return
            else:
                # 学习已过期，清除状态
                del data_manager.study_status[user_id]
                data_manager.save_study_status()

        # 检查是否正在旅行中
        travel_conflict_exists, travel_conflict_message = self._check_travel_conflict(user_id)
        if travel_conflict_exists:
            yield event.plain_result(f': {nickname}，{travel_conflict_message}')
            return

        # 检查是否已经在打工中
        if user_id in data_manager.work_status and data_manager.work_status[user_id].get('is_working', False):
            end_time_str = data_manager.work_status[user_id]['end_time']
            end_time = datetime.fromisoformat(end_time_str)
            current_time = datetime.now()
            remaining = end_time - current_time
            if remaining.total_seconds() > 0:
                hours_left = int(remaining.total_seconds() // 3600)
                minutes_left = int((remaining.total_seconds() % 3600) // 60)
                yield event.plain_result(f': {nickname}，你的老婆正在打工中，还需要{hours_left}小时{minutes_left}分钟才能完成！')
                return
            else:
                # 打工已过期，清除状态
                del data_manager.work_status[user_id]
                data_manager.save_work_status()

        # 开始打工
        duration = selected_work["duration"]
        start_time = datetime.now()
        end_time = start_time + timedelta(hours=duration)
        
        # 获取群组ID用于后续通知
        group_id = str(event.message_obj.group_id) if hasattr(event.message_obj, 'group_id') else None
        
        # 保存打工状态
        data_manager.work_status[user_id] = {
            'is_working': True,
            'start_time': start_time.isoformat(),
            'end_time': end_time.isoformat(),
            'work_id': work_id,
            'group_id': group_id,
            'nickname': nickname
        }
        data_manager.save_work_status()
        
        # 安排主动通知
        if data_manager.wife_plugin_instance:
            try:
                data_manager.wife_plugin_instance.schedule_task_completion(user_id, "work", end_time)
                print(f"[打工系统] 已安排主动通知，结束时间: {end_time}")
            except Exception as e:
                print(f"[打工系统] 安排主动通知失败: {e}")
        else:
            print(f"[打工系统] 警告：插件实例未找到，无法安排主动通知")
        
        # 获取老婆名称
        wife_name = wife_data[0]
        wife_display_name = wife_name.split('.')[0]
        
        # 随机打工事件描述
        work_events = [
            f"{wife_display_name}穿好工作服出门了，准备认真工作！",
            f"{wife_display_name}带着满满的干劲去上班了！",
            f"{wife_display_name}说要努力赚钱，然后就出门工作了！",
            f"{wife_display_name}背着小包包去打工，看起来很有责任心！",
            f"{wife_display_name}为了改善生活条件，决定去打工！",
            f"{wife_display_name}今天很有动力，要去工作赚钱！",
            f"{wife_display_name}说要体验社会生活，开心地出门了！",
            f"{wife_display_name}带着学习的心态去工作了！",
            f"{wife_display_name}为了变得更独立而去打工！",
            f"{wife_display_name}说要为你们的未来努力赚钱！"
        ]
        
        work_event = random.choice(work_events)
        
        result_message = f': {nickname}，{work_event}\n'
        result_message += f'💼 工作内容：{selected_work["name"]}\n'
        result_message += f'📝 工作描述：{selected_work["description"]}\n'
        result_message += f'⏰ 工作时长：{duration}小时\n'
        result_message += f'💰 预期收入：{selected_work["pay"]}金币\n'
        result_message += f'🕐 预计完成时间：{end_time.strftime("%H:%M")}\n'
        
        yield event.plain_result(result_message)
    
    def _check_travel_conflict(self, user_id: str):
        """检查是否与旅行冲突"""
        # 确保数据已经加载（防止重启后数据未加载的问题）
        if not data_manager.travel_status:
            print(f"[工作学习系统] 检查旅行冲突时发现数据未加载，重新初始化")
            # 重新加载旅行状态数据
            data_manager.load_travel_status()
        
        print(f"[工作学习系统] 检查旅行冲突 - 用户ID: {user_id}")
        
        # 检查是否正在旅行中
        if user_id in data_manager.travel_status and data_manager.travel_status[user_id].get('is_traveling', False):
            travel_data = data_manager.travel_status[user_id]
            end_time_str = travel_data['end_time']
            end_time = datetime.fromisoformat(end_time_str)
            current_time = datetime.now()
            remaining = end_time - current_time
            
            if remaining.total_seconds() > 0:
                hours_left = int(remaining.total_seconds() // 3600)
                minutes_left = int((remaining.total_seconds() % 3600) // 60)
                
                # 获取旅行目的地信息
                from ..config.travel_config import TRAVEL_DESTINATIONS
                destination_index = travel_data['destination_index']
                if destination_index in TRAVEL_DESTINATIONS:
                    destination = TRAVEL_DESTINATIONS[destination_index]
                    location = f"{destination['country']}·{destination['city']}"
                else:
                    location = "未知地点"
                
                return True, f"老婆正在{location}旅行中，还需要{hours_left}小时{minutes_left}分钟才能返回！不能同时进行学习或打工。"
            else:
                # 旅行已过期，清除状态
                print(f"[工作学习系统] 用户 {user_id} 的旅行已过期，清除状态")
                del data_manager.travel_status[user_id]
                data_manager.save_travel_status()
        
        print(f"[工作学习系统] 无旅行冲突")
        return False, ""
