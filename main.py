"""抽老婆插件 - 重构版本"""
from astrbot.api.all import *
from astrbot.api.event import MessageEventResult
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
import os
import re
import json

# 导入配置模块
from .config.settings import *
from .config.properties import *
from .config.education import *
from .config.events import *
from .config.messages import *
from .config.work_config import WORK_LIST
from .config.items_config import ITEMS_LIST

# 导入核心模块
from .core.data_manager import *
from .core.wife_system import *
from .core.ntr_system import *
from .core.education_system import *
from .core.work_system import *

# 导入工具模块
from .utils.formatters import *
from .utils.validators import *
from .utils.time_utils import *

# 导入处理器
from .handlers.wife_handler import WifeHandler
from .handlers.ntr_handler import NTRHandler
from .handlers.property_handler import PropertyHandler
from .handlers.shopping_handler import ShoppingHandler
from .handlers.work_study_handler import WorkStudyHandler
from .handlers.furniture_handler import FurnitureHandler
from .handlers.special_attributes_handler import WifeDetailsHandler
from .handlers.dungeon_handler import DungeonHandler
from .handlers.costume_shop_handler import CostumeShopHandler
from .handlers.dress_up_handler import DressUpHandler
from .handlers.item_query_handler import ItemQueryHandler
from .handlers.world_boss_handler import WorldBossHandler
from .handlers.scratch_card_handler import ScratchCardHandler

@register(
    "astrbot_plugin_aw",
    "Hey、小怪兽",
    "群老婆插件",
    "v1.4",
    ""
)
class WifePlugin(Star):
    """群老婆插件 - 重构版本
    
    支持抽老婆、查老婆、牛老婆等各种功能
    完全模块化架构，包含21个命令功能
    """
    
    def __init__(self, context: Context):
        super().__init__(context)
        print("="*50)
        print("[老婆插件] 开始初始化...")
        print("="*50)
        
        try:
            # 初始化调度器用于主动通知
            self.scheduler = AsyncIOScheduler()
            self.scheduler.start()
            
            # 初始化所有处理器
            self.wife_handler = WifeHandler()
            self.ntr_handler = NTRHandler()
            self.property_handler = PropertyHandler()
            self.shopping_handler = ShoppingHandler()
            self.work_study_handler = WorkStudyHandler()
            self.furniture_handler = FurnitureHandler()
            self.wife_details_handler = WifeDetailsHandler()
            self.dungeon_handler = DungeonHandler()
            self.costume_shop_handler = CostumeShopHandler()
            self.dress_up_handler = DressUpHandler()
            self.item_query_handler = ItemQueryHandler()
            self.world_boss_handler = WorldBossHandler()
            self.scratch_card_handler = ScratchCardHandler()

            # 初始化所有数据
            initialize_all_data()
            
            # 初始化世界Boss数据
            from .core.world_boss_system import initialize_world_boss_data
            initialize_world_boss_data()
            
            # 设置每日Boss刷新任务
            self.setup_daily_boss_refresh()
            
            
            # 设置全局插件实例引用，让其他模块可以访问调度器
            from .core import data_manager
            data_manager.wife_plugin_instance = self

            # 恢复重启前未完成的定时任务（包括过期任务的主动通知）
            print("[插件初始化] 开始恢复任务...")
            self.restore_pending_tasks()
            print("[插件初始化] 任务恢复完成")
            
            # 注意：不再调用 check_and_process_expired_tasks() 
            # 过期任务由 restore_pending_tasks() 统一处理，确保主动通知正常工作

            # 设置命令映射
            self.commands = {
            # 老婆相关命令
            "抽老婆": self.wife_handler.animewife,
            "确认老婆": self.wife_handler.confirm_wife,
            "查老婆": self.wife_handler.search_wife,
            "净身出户": self.wife_handler.divorce,

            # NTR和纯爱相关命令
            "牛老婆": self.ntr_handler.ntr_wife,
            "牛头人盛宴": self.ntr_handler.ntr_feast,
            "牛头人无可匹敌": self.ntr_handler.ntr_invincible,
            "纯爱无敌": self.ntr_handler.pure_love_invincible,
            "纯爱破碎": self.ntr_handler.pure_love_shatter,

            # 房产相关命令
            "房产中心": self.property_handler.property_center,
            "升级房产": self.property_handler.upgrade_property,

            # 购物和资产相关命令
            "出门转转": self.shopping_handler.go_out,
            "资产查询": self.shopping_handler.check_assets,
            "赠送礼物": self.shopping_handler.give_gift,
            "出售物品": self.shopping_handler.sell_item,
            "超市列表": self.shopping_handler.supermarket_list,
            "快餐店列表": self.shopping_handler.fastfood_list,
            "苍蝇馆子": self.shopping_handler.cangyingguanzi_list,
            "购买物品": self.shopping_handler.buy_item,
            "一键出售战利品": self.shopping_handler.sell_all_trophies,

            # 工作学习相关命令
            "出门学习": self.work_study_handler.go_study,
            "打工列表": self.work_study_handler.work_list,
            "出门打工": self.work_study_handler.go_work,

            # 家具相关命令
            "家具中心": self.furniture_handler.furniture_center,
            "家具中心-图片": self.furniture_menu,
            "购买家具": self.furniture_handler.buy_furniture,
            "出售家具": self.furniture_handler.sell_furniture,

            # 系统命令
            "抽老婆菜单": self.wife_menu,
            
            # 特殊属性查询命令
            "老婆详情": self.wife_details_handler.query_wife_details,
            
            # 地下城命令
            "地下城列表": self.dungeon_handler.dungeon_list,
            "前往地下城": self.dungeon_handler.enter_dungeon,
            
            # 服装系统命令
            "服装商店": self.costume_shop_handler.costume_shop,
            "购买服装": self.costume_shop_handler.buy_costume,
            "换衣": self.dress_up_handler.dress_up,
            "脱下": self.dress_up_handler.undress,
            "查询物品": self.item_query_handler.query_item,
            
            # 世界Boss命令
            "世界boss": self.world_boss_handler.world_boss_status,
            "攻击boss": self.world_boss_handler.attack_boss,
            
            # 咕咕嘎嘎命令（注意：长命令要放在短命令前面，避免匹配冲突）
            "咕咕嘎嘎池": self.scratch_card_handler.prize_pool_query,
            "咕咕嘎嘎": self.scratch_card_handler.scratch_card,
            
            # 管理员命令
            "刷新boss": self.admin_refresh_boss,
            "全体赔偿": self.admin_global_compensation,
            }

            self.admins = self.load_admins()
        except Exception as e:
            print(f"[老婆插件] 初始化时发生错误: {e}")
            import traceback
            traceback.print_exc()
            # 设置空命令字典以防止后续错误
            self.commands = {}
            self.admins = []
            # 确保scheduler被正确初始化
            if not hasattr(self, 'scheduler'):
                print("[老婆插件] 创建备用调度器...")
                self.scheduler = AsyncIOScheduler()
                self.scheduler.start()

    def load_admins(self):
        """加载管理员列表"""
        try:
            with open(os.path.join('data', 'cmd_config.json'), 'r', encoding='utf-8-sig') as f:
                config = json.load(f)
                return config.get('admins_id', [])
        except Exception as e:
            print(f"加载管理员列表失败: {str(e)}")
            return []

    def check_and_process_expired_tasks(self):
        """检查并处理重启后已过期的任务"""
        try:
            # 检查过期的学习任务
            check_and_process_completed_studies()

            # 检查过期的打工任务
            check_and_process_expired_works()
        except Exception as e:
            print(f"检查过期任务时出错: {e}")

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

    @event_message_type(EventMessageType.ALL)
    async def on_all_messages(self, event: AstrMessageEvent):
        try:
            # 检查是否为群聊消息
            if not hasattr(event.message_obj, "group_id"):
                return

            # 注意：现在使用主动通知机制，不再需要被动检查任务完成状态
            # 但仍保留离线通知检查作为兜底机制
            
            # 发送离线完成的学习通知（兜底机制）
            if offline_completed_studies:
                current_group_id = str(event.message_obj.group_id)
                user_id = str(event.get_sender_id())
                
                if user_id in offline_completed_studies:
                    offline_study = offline_completed_studies[user_id]
                    if offline_study['group_id'] == current_group_id:
                        yield event.plain_result(offline_study['message'])
                        del offline_completed_studies[user_id]

            # 发送离线完成的打工通知（兜底机制）
            if offline_completed_works:
                current_group_id = str(event.message_obj.group_id)
                user_id = str(event.get_sender_id())

                if user_id in offline_completed_works:
                    offline_work = offline_completed_works[user_id]
                    if offline_work['group_id'] == current_group_id:
                        yield event.plain_result(offline_work['message'])
                        del offline_completed_works[user_id]

            group_id = event.message_obj.group_id
            message_str = event.message_str.strip()

            for command, func in self.commands.items():
                # 精准匹配：消息必须完全等于命令，或者是带参数的命令
                match_condition = message_str == command or (command in ["确认老婆", "牛老婆", "查老婆", "老婆详情", "赠送礼物", "出售物品", "购买物品", "出门学习", "出门打工", "购买家具", "出售家具", "家具中心-图片", "前往地下城", "一键出售战利品", "购买服装", "换衣", "脱下", "查询物品", "世界boss", "攻击boss", "咕咕嘎嘎", "咕咕嘎嘎池", "刷新boss", "全体赔偿"] and message_str.startswith(command))

                if match_condition:
                    # 正式群
                    official_group_id = "1029319414"
                    # 自测群
                    test_group_id = "680018081"
                    if str(group_id) not in {official_group_id, test_group_id}:
                        yield event.plain_result(
                            f"为了避免刷屏，请前往 {official_group_id} 群玩抽老婆~"
                        )
                        break

                    try:
                        async for result in func(event):
                            yield result
                    except Exception as e:
                        import traceback
                        traceback.print_exc()
                        yield event.plain_result(f"执行命令时出现错误: {str(e)}")
                    break

        except Exception as e:
            import traceback
            traceback.print_exc()

    async def wife_menu(self, event: AstrMessageEvent):
        """抽老婆菜单指令，发送菜单图片"""
        # 获取menu.png的路径（与main.py同级）
        menu_image_path = os.path.join(os.path.dirname(__file__), 'static', 'pic', 'menu.png')

        # 检查图片文件是否存在
        if os.path.exists(menu_image_path):
            # 发送图片
            try:
                chain = [Image.fromFileSystem(menu_image_path)]
                yield event.chain_result(chain)
                return
            except Exception as e:
                print(f'发送菜单图片时发生错误: {e}')
        
        # 图片不存在或发送失败时的回退方案，发送文本菜单
        menu = ":\n"
        menu += "【抽老婆系统】指令菜单\n"
        menu += "1. 抽老婆 - 抽取10位候选老婆供选择\n"
        menu += "2. 确认老婆 名字 - 从候选列表中选择心仪的老婆\n"
        menu += "3. 查老婆 - 查看自己或他人的老婆（包含老婆属性信息）\n"
        menu += "4. 牛老婆 - 尝试NTR别人的老婆（需要@对方）\n"
        menu += "5. 净身出户 - 和当前老婆离婚\n"
        menu += "6. 纯爱无敌 - 获得永久保护，完全防止被NTR\n"
        menu += "7. 纯爱破碎 - 取消纯爱无敌保护状态\n"
        menu += "8. 牛头人无可匹敌 - 获得额外的牛老婆机会\n"
        menu += "9. 牛头人盛宴 - 尝试开启盛宴，提高牛老婆成功率\n"
        menu += "10. 房产中心 - 查看房产信息和升级列表\n"
        menu += "11. 升级房产 - 使用金币升级房产\n"
        menu += "12. 出门转转 - 外出探险，随机获得物品或金币变化\n"
        menu += "13. 资产查询 - 查看个人资产（金币、背包、房产）\n"
        menu += "14. 赠送礼物 物品名 数量 - 给老婆送礼物增加好感度和属性(数量可选，默认1)\n"
        menu += "15. 出售物品 物品名 - 将物品出售换取金币\n"
        menu += "16. 超市列表 - 查看超市中所有可购买的商品\n"
        menu += "17. 快餐店列表 - 查看快餐店菜单(高饥饿值恢复)\n"
        menu += "18. 苍蝇馆子 - 查看地方特色菜(价格昂贵但效果拔群)\n"
        menu += "19. 购买物品 物品名 数量 - 购买指定物品(超市/快餐店/苍蝇馆子)\n"
        menu += "20. 出门学习 小时数 - 让老婆出门学习(1-12小时)\n"
        menu += "21. 打工列表 - 查看所有可用的打工工作\n"
        menu += "22. 出门打工 序号 - 让老婆去指定工作打工\n"
        menu += "23. 家具中心 - 查看家具商店，购买各种家具装饰房产\n"
        menu += "24. 家具中心-图片 - 查看精美的家具目录图片\n"
        menu += "25. 购买家具 家具名 - 购买指定家具装饰房产\n"
        menu += "26. 出售家具 家具名 - 出售不需要的家具换取金币\n"
        menu += "27. 老婆详情 - 查询老婆的妹抖值、撒娇值、傲娇值、黑化率、反差萌及装备信息\n"
        menu += "28. 地下城列表 - 查看可进入的地下城列表\n"
        menu += "29. 前往地下城 序号 - 进入指定地下城进行冒险战斗\n"
        menu += "30. 一键出售战利品 - 快速出售所有战利品（地下城+世界Boss奖励）\n"
        menu += "31. 抽老婆菜单 - 显示本菜单\n"
        menu += "32. 服装商店 - 购买精品服装（兔女郎、女仆、巫女、魔法少女、小恶魔套装）\n"
        menu += "33. 购买服装 服装名 - 购买指定服装\n"
        menu += "34. 换衣 服装名 - 为老婆穿上指定服装\n"
        menu += "35. 脱下 服装名/部位 - 脱下指定服装或部位的装备\n"
        menu += "36. 查询物品 物品名 - 查看物品详情和效果\n"
        menu += "37. 世界boss - 查看当前世界Boss状态和伤害排行榜\n"
        menu += "38. 攻击boss - 攻击世界Boss，造成伤害（消耗30健康值）\n"
        menu += "39. 咕咕嘎嘎 [数量] - 花费100金币试试运气，有机会获得咕咕嘎嘎池大奖（概率极低），可批量（如：咕咕嘎嘎 10）\n"
        menu += "40. 咕咕嘎嘎池 - 查看当前咕咕嘎嘎池状态和奖励说明\n"
        menu += "41. 刷新boss [Boss名称] - 【管理员专用】刷新世界Boss和排行榜（可指定可可萝或大芋头王）\n"
        menu += "42. 全体赔偿 金币数量 - 【管理员专用】给所有用户赔偿指定数量的金币\n"
        menu += "\n【系统特色】\n"
        menu += "🎮 完全重构的模块化架构\n"
        menu += "📊 老婆属性系统：等级、成长值、饥饿、清洁、健康、心情\n"
        menu += "⚔️ 特殊属性系统：妹抖值、撒娇值、傲娇值、黑化率、反差萌（从0开始，等待培养）\n"
        menu += "🏫 学历系统：从幼儿园到全知全能的12个等级\n"
        menu += "🏠 房产系统：14个等级的房产升级，空间限制，售出加成\n"
        menu += "🪑 家具系统：65种精美家具，11个分类，装饰房产提升身价\n"
        menu += "💰 经济系统：金币、背包、超市购物、身价计算\n"
        menu += "🍗 快餐系统：快餐店高饥饿值食物，大幅满足老婆食欲\n"
        menu += "🏮 苍蝇馆子系统：15种地方特色菜，价格昂贵但效果拔群\n"
        menu += "📚 学习系统：出门学习增加学识和经验\n"
        menu += "💼 打工系统：多种工作选择，等级学历要求\n"
        menu += "💕 情感系统：好感度、纯爱保护\n"
        menu += "⚔️ NTR系统：牛头人盛宴、无敌状态\n"
        menu += "🗡️ 地下城系统：冒险战斗、杀怪统计、结晶收集\n"
        menu += "👗 服装系统：五大精品套装、装备属性加成、套装效果\n"
        menu += "🐉 世界Boss系统：挑战黑化可可萝、获得珍贵料理道具、全服协作排行榜\n"
        menu += "🎫 咕咕嘎嘎系统：咕咕嘎嘎池模式运气游戏，支持批量操作（咕咕嘎嘎 数量），每次100金币进入咕咕嘎嘎池，三等奖(20%)、二等奖(50%)、一等奖(100%)等你来拿\n"

        yield event.plain_result(menu)

    async def furniture_menu(self, event: AstrMessageEvent):
        """家具中心-图片指令，发送家具目录图片"""
        # 获取furniture.png的路径（与main.py同级）
        furniture_image_path = os.path.join(os.path.dirname(__file__), 'static', 'pic', 'furniture.png')

        # 检查图片文件是否存在
        if os.path.exists(furniture_image_path):
            # 发送图片
            try:
                chain = [Image.fromFileSystem(furniture_image_path)]
                yield event.chain_result(chain)
                return
            except Exception as e:
                print(f'发送家具图片时发生错误: {e}')
        
        # 图片不存在或发送失败时的回退方案，调用家具中心文本功能
        async for result in self.furniture_handler.furniture_center(event):
            yield result

    async def admin_refresh_boss(self, event: AstrMessageEvent):
        """管理员刷新Boss指令"""
        try:
            user_id = str(event.get_sender_id())
            admin_qq = "1620592237"
            
            # 检查是否为管理员
            if user_id != admin_qq:
                yield event.plain_result("❌ 权限不足喵~")
                return
            
            # 解析命令参数
            message_str = event.message_str.strip()
            parts = message_str.split()
            
            boss_name = None
            if len(parts) > 1:
                # 如果指定了Boss名称
                boss_param = " ".join(parts[1:])
                if "可可萝" in boss_param or "kkr" in boss_param.lower():
                    boss_name = "可可萝（黑化）"
                elif "芋头" in boss_param or "taro" in boss_param.lower():
                    boss_name = "大芋头王"
                else:
                    yield event.plain_result("❌ 无效的Boss名称！支持：可可萝、大芋头王")
                    return
            
            # 执行Boss刷新
            from .core.world_boss_system import reset_world_boss, get_daily_boss_name
            
            if boss_name:
                # 刷新为指定Boss
                actual_boss_name = reset_world_boss(boss_name)
                result_msg = f"✅ 管理员手动刷新Boss成功！\n"
                result_msg += f"🐉 新Boss：{actual_boss_name}\n"
                result_msg += f"📊 所有战斗记录和排行榜已重置\n"
                result_msg += f"🔄 所有玩家每日攻击次数已重置\n"
                result_msg += f"⚔️ 快来挑战新的世界Boss吧！"
            else:
                # 刷新为今日Boss
                today_boss = get_daily_boss_name()
                actual_boss_name = reset_world_boss(today_boss)
                result_msg = f"✅ 管理员刷新今日Boss成功！\n"
                result_msg += f"🐉 今日Boss：{actual_boss_name}\n"
                result_msg += f"📊 所有战斗记录和排行榜已重置\n"
                result_msg += f"🔄 所有玩家每日攻击次数已重置\n"
                result_msg += f"⚔️ 快来挑战新的世界Boss吧！"
            
            yield event.plain_result(result_msg)
            
        except Exception as e:
            print(f"[管理员刷新Boss] 执行失败: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f"❌ 刷新Boss时发生错误: {str(e)}")

    async def admin_global_compensation(self, event: AstrMessageEvent):
        """管理员全体赔偿指令"""
        try:
            user_id = str(event.get_sender_id())
            admin_qq = "1620592237"
            
            # 检查是否为管理员
            if user_id != admin_qq:
                yield event.plain_result("❌ 权限不足喵~")
                return
            
            # 解析命令参数
            message_str = event.message_str.strip()
            parts = message_str.split()
            
            if len(parts) < 2:
                yield event.plain_result("❌ 参数不足！正确格式：全体赔偿 金币数量")
                return
            
            try:
                compensation_amount = int(parts[1])
                if compensation_amount <= 0:
                    yield event.plain_result("❌ 赔偿金币数量必须大于0！")
                    return
            except ValueError:
                yield event.plain_result("❌ 无效的金币数量！请输入正整数。")
                return
            
            # 导入数据管理模块
            from .core import data_manager
            
            # 确保数据已加载
            if not data_manager.user_data:
                data_manager.load_user_data()
            
            # 获取所有用户数据
            user_list = []
            total_users = 0
            total_compensated = 0
            
            # 遍历所有有老婆的用户进行赔偿
            for user_id_key in data_manager.global_wife_data.keys():
                # 获取用户当前数据（如果不存在会自动创建）
                user_data_obj = data_manager.get_user_data(user_id_key)
                old_coins = user_data_obj["coins"]
                new_coins = old_coins + compensation_amount
                
                # 更新用户金币
                data_manager.update_user_data(user_id_key, coins=new_coins)
                
                # 获取用户昵称
                wife_data = data_manager.get_user_wife_data(user_id_key)
                nickname = wife_data[2] if wife_data and len(wife_data) > 2 else user_id_key
                
                user_list.append(f"{nickname}: {old_coins} + {compensation_amount} = {new_coins}")
                total_users += 1
                total_compensated += compensation_amount
            
            if total_users == 0:
                yield event.plain_result("❌ 没有找到任何用户进行赔偿！")
                return
            
            # 构建结果消息
            result_msg = f"✅ 管理员全体赔偿执行完成！\n"
            result_msg += f"💰 赔偿金额：{compensation_amount} 金币/人\n"
            result_msg += f"👥 受益用户：{total_users} 人\n"
            result_msg += f"💎 总计赔偿：{total_compensated} 金币\n\n"
            result_msg += "【赔偿详情】\n"
            
            # 分页显示用户列表（避免消息过长）
            max_users_per_page = 20
            if len(user_list) <= max_users_per_page:
                result_msg += "\n".join(user_list)
                yield event.plain_result(result_msg)
            else:
                # 分页发送
                for i in range(0, len(user_list), max_users_per_page):
                    page_users = user_list[i:i + max_users_per_page]
                    page_num = i // max_users_per_page + 1
                    total_pages = (len(user_list) + max_users_per_page - 1) // max_users_per_page
                    
                    if i == 0:
                        # 第一页包含头部信息
                        page_msg = result_msg + f"【第{page_num}/{total_pages}页】\n" + "\n".join(page_users)
                    else:
                        # 后续页面只显示用户列表
                        page_msg = f"【全体赔偿详情 - 第{page_num}/{total_pages}页】\n" + "\n".join(page_users)
                    
                    yield event.plain_result(page_msg)
            
        except Exception as e:
            print(f"[管理员全体赔偿] 执行失败: {e}")
            import traceback
            traceback.print_exc()
            yield event.plain_result(f"❌ 执行全体赔偿时发生错误: {str(e)}")


    def restore_pending_tasks(self):
        """恢复重启前未完成的定时任务"""
        try:
            current_time = datetime.now()
            print(f"[任务恢复] 启动任务恢复, 当前时间: {current_time}")
            
            # 确保数据已加载
            from .core import data_manager
            print(f"[任务恢复] 学习状态数据: {len(data_manager.study_status)} 个")
            print(f"[任务恢复] 打工状态数据: {len(data_manager.work_status)} 个")
            
            # 恢复学习任务
            expired_studies = []
            for user_id, study_data in data_manager.study_status.items():
                if study_data.get('is_studying', False):
                    try:
                        end_time = datetime.fromisoformat(study_data['end_time'])
                        print(f"[任务恢复] 学习任务 用户{user_id}: 结束时间 {end_time}")
                        
                        if current_time < end_time:
                            # 任务还未完成，重新安排通知
                            job_id = f"study_{user_id}"
                            self.scheduler.add_job(
                                self._task_completion_callback,
                                "date",
                                id=job_id,
                                args=[user_id, "study"],
                                run_date=end_time,
                                misfire_grace_time=60,
                            )
                            print(f"[任务恢复] 恢复学习任务通知: 用户{user_id}, 完成时间: {end_time}")
                        else:
                            # 任务已过期，标记为需要立即处理
                            expired_studies.append(user_id)
                            print(f"[任务恢复] 学习任务已过期: 用户{user_id}, 过期时间: {end_time}")
                            
                    except Exception as e:
                        print(f"[任务恢复] 恢复学习任务失败 用户{user_id}: {e}")
            
            # 恢复打工任务
            expired_works = []
            for user_id, work_data in data_manager.work_status.items():
                if work_data.get('is_working', False):
                    try:
                        end_time = datetime.fromisoformat(work_data['end_time'])
                        print(f"[任务恢复] 打工任务 用户{user_id}: 结束时间 {end_time}")
                        
                        if current_time < end_time:
                            # 任务还未完成，重新安排通知
                            job_id = f"work_{user_id}"
                            self.scheduler.add_job(
                                self._task_completion_callback,
                                "date",
                                id=job_id,
                                args=[user_id, "work"],
                                run_date=end_time,
                                misfire_grace_time=60,
                            )
                            print(f"[任务恢复] 恢复打工任务通知: 用户{user_id}, 完成时间: {end_time}")
                        else:
                            # 任务已过期，标记为需要立即处理
                            expired_works.append(user_id)
                            print(f"[任务恢复] 打工任务已过期: 用户{user_id}, 过期时间: {end_time}")
                            
                    except Exception as e:
                        print(f"[任务恢复] 恢复打工任务失败 用户{user_id}: {e}")
            
            # 立即处理过期的任务
            if expired_studies:
                print(f"[任务恢复] 立即处理 {len(expired_studies)} 个过期学习任务")
                for user_id in expired_studies:
                    # 安排在5秒后执行，避免启动时立即执行导致的问题
                    self.scheduler.add_job(
                        self._task_completion_callback,
                        "date",
                        args=[user_id, "study"],
                        run_date=current_time + timedelta(seconds=5),
                        misfire_grace_time=60,
                    )
                    
            if expired_works:
                print(f"[任务恢复] 立即处理 {len(expired_works)} 个过期打工任务")
                for user_id in expired_works:
                    # 安排在5秒后执行，避免启动时立即执行导致的问题
                    self.scheduler.add_job(
                        self._task_completion_callback,
                        "date",
                        args=[user_id, "work"],
                        run_date=current_time + timedelta(seconds=5),
                        misfire_grace_time=60,
                    )
                        
        except Exception as e:
            print(f"[任务恢复] 恢复任务时出错: {e}")

    def schedule_task_completion(self, user_id: str, task_type: str, end_time: datetime):
        """安排任务完成的通知"""
        try:
            job_id = f"{task_type}_{user_id}"
            # 先删除可能存在的旧任务
            try:
                self.scheduler.remove_job(job_id)
            except:
                pass
                
            # 添加新的定时任务
            self.scheduler.add_job(
                self._task_completion_callback,
                "date",
                id=job_id,
                args=[user_id, task_type],
                run_date=end_time,
                misfire_grace_time=60,
            )
            print(f"已安排{task_type}任务完成通知: 用户{user_id}, 时间: {end_time}")
        except Exception as e:
            print(f"安排任务完成通知失败: {e}")

    async def _task_completion_callback(self, user_id: str, task_type: str):
        """任务完成的回调函数"""
        try:
            print(f"[回调函数] 任务完成回调触发: 用户{user_id}, 类型{task_type}")
            
            if task_type == "study":
                # 处理学习完成
                result = self._process_study_completion_with_message(user_id)
                print(f"[回调函数] 学习完成处理结果: {result is not None}")
            elif task_type == "work":
                # 处理打工完成
                result = self._process_work_completion_with_message(user_id)
                print(f"[回调函数] 打工完成处理结果: {result is not None}")
            else:
                print(f"[回调函数] 未知任务类型: {task_type}")
                return
                
            if result and result.get('group_id') and result.get('message'):
                group_id = result['group_id']
                print(f"[回调函数] 准备发送消息到群组: {group_id}")
                
                # 使用正确的 unified_msg_origin 格式: platform_name:message_type:session_id
                possible_origins = [
                    f"aiocqhttp:GroupMessage:{group_id}",  # 正确格式
                    f"aiocqhttp:group:{group_id}",  # 备用格式1
                    f"aiocqhttp_group_{group_id}",  # 备用格式2
                    group_id  # 直接使用群组ID作为最后备选
                ]
                
                success = False
                for unified_msg_origin in possible_origins:
                    try:
                        print(f"[回调函数] 尝试发送到: {unified_msg_origin}")
                        # 构建包含@功能的消息
                        # result['message'] 格式类似 ": Hey 、小怪兽，..."
                        if result['message'].startswith(': '):
                            # 检查用户是否在不艾特列表中
                            if user_id in data_manager.no_at_users:
                                # 不艾特该用户，直接发送消息内容
                                print(f"[回调函数] 用户{user_id}在不艾特列表中，跳过@功能")
                                message_result = MessageEventResult().message(result['message'][2:])  # 去掉开头的": "
                            else:
                                # 构建@消息
                                if task_type == "study":
                                    user_info = data_manager.study_status.get(user_id, {})
                                else:  # task_type == "work"
                                    user_info = data_manager.work_status.get(user_id, {})
                                user_nickname = user_info.get('nickname', user_id)
                                message_result = MessageEventResult().at(name=user_nickname, qq=user_id).message(" " + result['message'][2:])  # 去掉开头的": "并添加空格
                        else:
                            message_result = MessageEventResult().message(result['message'])
                        
                        await self.context.send_message(unified_msg_origin, message_result)
                        print(f"[回调函数] 成功发送{task_type}完成通知到群组{group_id} (格式: {unified_msg_origin})")
                        success = True
                        break
                    except Exception as send_error:
                        print(f"[回调函数] 发送失败 (格式: {unified_msg_origin}): {send_error}")
                        continue
                
                if not success:
                    print(f"[回调函数] 所有格式都发送失败，群组ID: {group_id}")
                    
            else:
                print(f"[回调函数] 结果无效: result={result is not None}, group_id={result.get('group_id') if result else None}")
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(f"[回调函数] 任务完成回调出错: {e}")

    def _process_study_completion_with_message(self, user_id: str):
        """处理学习完成并返回消息"""
        from .core.education_system import process_study_completion
        return process_study_completion(user_id)

    def _process_work_completion_with_message(self, user_id: str):
        """处理打工完成并返回消息"""  
        from .core.work_system import process_work_completion
        return process_work_completion(user_id)


    def setup_daily_boss_refresh(self):
        """设置每日Boss刷新任务"""
        try:
            # 每天凌晨0:01刷新Boss
            self.scheduler.add_job(
                self._daily_boss_refresh_callback,
                "cron",
                id="daily_boss_refresh",
                hour=0,
                minute=1,
                misfire_grace_time=3600,  # 1小时的宽限时间
            )
            print("[世界Boss] 已设置每日Boss刷新任务（每天0:01执行）")
        except Exception as e:
            print(f"[世界Boss] 设置每日刷新任务失败: {e}")

    async def _daily_boss_refresh_callback(self):
        """每日Boss刷新回调函数"""
        try:
            print("[世界Boss] 开始执行每日Boss刷新...")
            
            from .core.world_boss_system import reset_world_boss, get_daily_boss_name
            
            # 获取今日Boss并刷新
            today_boss = get_daily_boss_name()
            reset_world_boss(today_boss)
            
            print(f"[世界Boss] 每日刷新完成，今日Boss: {today_boss}")
            
            # 可以在这里添加通知逻辑，比如向群组发送Boss刷新消息
            # 但需要知道具体的群组ID
            
        except Exception as e:
            print(f"[世界Boss] 每日刷新回调执行失败: {e}")
            import traceback
            traceback.print_exc()


    async def terminate(self):
        """插件终止时的清理工作"""
        try:
            if hasattr(self, 'scheduler') and self.scheduler:
                self.scheduler.shutdown()
                print("任务调度器已关闭")
        except Exception as e:
            print(f"关闭调度器时出错: {e}")
