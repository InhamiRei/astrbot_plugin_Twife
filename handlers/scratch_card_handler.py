"""咕咕嘎嘎处理器"""
import random
from astrbot.api.all import *
from ..core.data_manager import *

class ScratchCardHandler:
    def __init__(self):
        # 定义咕咕嘎嘎的奖励配置
        self.SCRATCH_COST = 100  # 每次咕咕嘎嘎花费100金币
        
        # 普通奖励配置：(奖励金额, 权重, 描述)
        self.SCRATCH_REWARDS = [
            # 常规奖励（高概率）
            (0, 5000, "谢谢惠顾"),
            (20, 1000, "小奖"),
            (50, 800, "小赚"),
            (100, 500, "回本"),
            (200, 300, "翻倍"),
            (500, 150, "中奖"),
            (1000, 80, "好运"),
            (2000, 40, "大奖"),

            ("三等奖", 1, "三等奖"),    # 20%咕咕嘎嘎池
            ("二等奖", 0.5, "二等奖"),   # 50%咕咕嘎嘎池
            ("一等奖", 0.1, "一等奖")    # 100%咕咕嘎嘎池
        ]
        
        # 特殊效果文本
        self.EFFECT_TEXTS = {
            0: [
                "💔 很遗憾，这次没有中奖",
                "🤷‍♂️ 运气不太好呢",
                "😅 下次一定能中的",
                "🙃 再接再厉吧",
                "🍂 好运可能在下一次",
                "🕳️ 空空如也",
                "🌧️ 今天小雨点",
                "📉 没关系，生活还要继续",
                "😬 擦肩而过了",
                "🎲 幸运值还在积蓄"
            ],
            20: [
                "🎁 小奖来了",
                "💝 聊胜于无",
                "🍬 小甜头一个",
                "🌱 运气的萌芽",
                "📦 小礼物到手",
                "🧩 一点点安慰",
                "😌 至少没空手",
                "🤏 小小收获",
                "📍 稍微回血一下",
                "🌸 好运的开端"
            ],
            50: [
                "💔 亏了一半",
                "😅 至少回了点血",
                "🤏 聊胜于无吧",
                "😬 有总比没有好",
                "📉 还是亏了不少",
                "🥲 起码不是全亏",
                "😓 回了个零头",
                "🙃 聊以安慰",
                "💸 亏得不算太惨",
                "🤷‍♂️ 总有收获"
            ],
            100: [
                "✨ 刚好回本",
                "⚖️ 不亏不赚",
                "🔄 平平稳稳",
                "🙂 有来有回",
                "💸 保本就好",
                "⚪ 完美平衡",
                "🪙 运气在原地踏步",
                "🔔 稳住了",
                "🧘 心态很稳",
                "🛟 没赚没亏"
            ],
            200: [
                "💰 赚了点零花钱",
                "🎯 不错的运气",
                "🍀 好运起飞",
                "📦 收获加倍",
                "🎵 小确幸时刻",
                "🌞 小阳光洒下",
                "🧧 多拿了点",
                "✨ 一丝亮光",
                "📍 运气渐佳",
                "🚶‍♂️ 迈向幸运"
            ],
            500: [
                "🎉 中奖了",
                "🍀 运气开始转好",
                "💎 不错的回报",
                "🌟 还挺惊喜",
                "📈 上升趋势",
                "😄 开心翻倍",
                "💌 好运邮递",
                "🎀 小小惊喜",
                "🥳 值得庆祝",
                "🧲 好运磁场开启"
            ],
            1000: [
                "✨ 你是今天的幸运儿",
                "🌟 好运连连",
                "🎊 千元喜讯",
                "💎 还不错嘛",
                "🎯 命中注定",
                "🚀 运气起飞",
                "🥂 为自己干杯",
                "🎵 喜上眉梢",
                "🪙 口袋鼓起来",
                "😎 今天主角是你"
            ],
            2000: [
                "🔥 运气真不错",
                "💎 小发一笔",
                "🚀 进阶的幸运",
                "📈 收益翻倍",
                "🎁 奖励满满",
                "🥳 好运降临",
                "🎀 价值不菲",
                "💡 惊喜升级",
                "🏅 好运选中你",
                "🌈 生活添彩"
            ],
            5000: [
                "🚀 大运当头",
                "⭐ 天选之子",
                "🎉 惊喜大奖",
                "💎 收获满满",
                "🎯 大吉大利",
                "🥳 超级幸运",
                "🌟 光芒四射",
                "📦 意外之喜",
                "💰 小金库补充",
                "🧧 红运当头"
            ],
            10000: [
                "💥 发财了",
                "🎆 运气爆棚",
                "🎊 好运炸裂",
                "🌟 星光加持",
                "🚀 十倍惊喜",
                "🏆 幸运冠军",
                "💎 闪闪发光",
                "🥂 值得大庆",
                "🎯 万里挑一",
                "🧨 福运连连"
            ],
            "三等奖": [
                "🎉 恭喜中三等奖",
                "🍀 幸运降临",
                "🎯 不错的运气",
                "💎 小有收获",
                "🌟 咕咕嘎嘎池分红"
            ],
            "二等奖": [
                "🎊 恭喜中二等奖",
                "🚀 运气爆棚",
                "💰 半池奖金",
                "👑 实力与运气并存",
                "🎆 令人羡慕"
            ],
            "一等奖": [
                "🎆🎉 恭喜中一等奖 🎉🎆",
                "👑 恭喜成为咕咕嘎嘎之王 👑",
                "💰💰 咕咕嘎嘎池全归你 💰💰",
                "🌟 命运的奇迹",
                "🚀 一飞冲天",
                "🏆 传奇人生",
                "🎇 财富巅峰",
                "💎 无敌好运",
                "🥂 全服瞩目",
                "🎊 史诗时刻"
            ]
        }

    async def scratch_card(self, event: AstrMessageEvent):
        """咕咕嘎嘎功能"""
        try:
            user_id = str(event.get_sender_id())
            nickname = event.get_sender_name()
        except AttributeError:
            yield event.plain_result('无法获取用户信息，请检查消息事件对象。')
            return

        # 获取用户数据
        user_data_obj = get_user_data(user_id)
        current_coins = user_data_obj["coins"]
        
        # 检查金币是否足够
        if current_coins < self.SCRATCH_COST:
            yield event.plain_result(f': {nickname}，咕咕嘎嘎需要{self.SCRATCH_COST}金币，你当前只有{current_coins}金币，金币不足！')
            return
        
        # 扣除费用并添加到咕咕嘎嘎池
        new_coins = current_coins - self.SCRATCH_COST
        add_to_prize_pool(self.SCRATCH_COST)
        
        # 随机抽取奖励
        reward_result = self._get_random_reward()
        
        # 处理奖励
        if isinstance(reward_result[0], str):
            # 咕咕嘎嘎池奖励
            prize_type = reward_result[0]
            description = reward_result[1]
            current_pool = get_prize_pool()
            
            if prize_type == "三等奖":
                reward_amount = int(current_pool * 0.2)
                # 清空咕咕嘎嘎池的20%
                reduce_prize_pool(reward_amount)
            elif prize_type == "二等奖":
                reward_amount = int(current_pool * 0.5)
                # 清空咕咕嘎嘎池的50%
                reduce_prize_pool(reward_amount)
            elif prize_type == "一等奖":
                reward_amount = current_pool
                # 清空整个咕咕嘎嘎池
                clear_prize_pool()
        else:
            # 普通奖励
            reward_amount = reward_result[0]
            description = reward_result[1]
            prize_type = None
        
        # 加上奖励
        final_coins = new_coins + reward_amount
        
        # 更新用户金币
        update_user_data(user_id, coins=final_coins)
        
        # 构建结果消息
        result_msg = self._build_result_message(nickname, reward_amount, description, current_coins, final_coins, prize_type)
        
        yield event.plain_result(result_msg)
    
    async def prize_pool_query(self, event: AstrMessageEvent):
        """咕咕嘎嘎咕咕嘎嘎池查询功能"""
        current_pool = get_prize_pool()
        
        pool_msg = "🎊 咕咕嘎嘎咕咕嘎嘎池状态 🎊\n\n"
        pool_msg += f"💰 当前咕咕嘎嘎池金额: {current_pool:,}金币\n\n"
        pool_msg += "🏆 咕咕嘎嘎池奖励说明:\n"
        pool_msg += f"🥇 一等奖: {current_pool:,}金币 (咕咕嘎嘎池100%)\n"
        pool_msg += f"🥈 二等奖: {int(current_pool * 0.5):,}金币 (咕咕嘎嘎池50%)\n"
        pool_msg += f"🥉 三等奖: {int(current_pool * 0.2):,}金币 (咕咕嘎嘎池20%)\n\n"
        pool_msg += "💡 每次咕咕嘎嘎花费100金币，全部进入咕咕嘎嘎池\n"
        pool_msg += "🍀 中奖概率极低，运气决定一切！"
        
        yield event.plain_result(pool_msg)

    def _get_random_reward(self):
        """根据权重随机获取奖励"""
        # 构建权重列表
        rewards = []
        weights = []
        
        for amount, weight, desc in self.SCRATCH_REWARDS:
            rewards.append((amount, desc))
            weights.append(weight)
        
        # 加权随机选择
        chosen_reward = random.choices(rewards, weights=weights)[0]
        return chosen_reward

    def _build_result_message(self, nickname, reward_amount, description, old_coins, new_coins, prize_type=None):
        """构建结果消息"""
        # 咕咕嘎嘎动画效果
        scratch_animation =  "▓▓▓▓▓▓▓▓▓▓\n"
        scratch_animation += "▓░░░░░░░░░▓\n"
        scratch_animation += "▓░░ 咕咕嘎嘎 ░░▓\n"
        scratch_animation += "▓░░░░░░░░░▓\n"
        scratch_animation += "▓▓▓▓▓▓▓▓▓▓\n\n"
        
        # 获取特殊效果文本
        if prize_type:
            effect_text = random.choice(self.EFFECT_TEXTS.get(prize_type, ["🎉 恭喜中奖"]))
        else:
            effect_text = random.choice(self.EFFECT_TEXTS.get(reward_amount, ["🎉 恭喜中奖"]))
        
        result_msg = f": {nickname} 🎫 咕咕嘎嘎结果 🎫\n\n"
        result_msg += scratch_animation
        
        if prize_type == "一等奖":
            # 一等奖特殊展示
            result_msg += "🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆\n"
            result_msg += "🎉    一等奖大奖    🎉\n"
            result_msg += f"👑  {reward_amount:,}金币大奖  👑\n" 
            result_msg += "🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆\n\n"
            result_msg += f"🏆 恭喜 {nickname} 成为咕咕嘎嘎传奇！\n"
            result_msg += f"💰 咕咕嘎嘎池全归你：{reward_amount:,}金币\n"
            result_msg += f"💎 余额：{old_coins:,} → {new_coins:,}金币\n"
            result_msg += f"\n🌟 {effect_text}"
        elif prize_type == "二等奖":
            # 二等奖展示
            result_msg += "🎊🎊🎊🎊🎊🎊🎊🎊\n"
            result_msg += f"🌟  {description}  🌟\n"
            result_msg += "🎊🎊🎊🎊🎊🎊🎊🎊\n\n"
            result_msg += f"🎯 {effect_text}\n"
            result_msg += f"💰 咕咕嘎嘎池50%：{reward_amount:,}金币\n"
            result_msg += f"💎 余额：{old_coins:,} → {new_coins:,}金币"
        elif prize_type == "三等奖":
            # 三等奖展示
            result_msg += "✨✨✨✨✨✨\n"
            result_msg += f"🎉 {description} 🎉\n"
            result_msg += "✨✨✨✨✨✨\n\n"
            result_msg += f"🚀 {effect_text}\n"
            result_msg += f"💰 咕咕嘎嘎池20%：{reward_amount:,}金币\n"
            result_msg += f"💎 余额：{old_coins:,} → {new_coins:,}金币"
        elif reward_amount == 0:
            result_msg += f"💔 {description} - {effect_text}\n"
            result_msg += f"💸 花费：{self.SCRATCH_COST}金币\n"
            result_msg += f"💰 余额：{old_coins} → {new_coins}金币\n"
        else:
            # 普通奖励展示
            result_msg += f"🎁 {description} - {effect_text}\n"
            if reward_amount > 0:
                result_msg += f"💰 奖励：{reward_amount}金币\n"
            result_msg += f"💸 花费：{self.SCRATCH_COST}金币\n"
            result_msg += f"💰 余额：{old_coins} → {new_coins}金币"
        
        # 添加鼓励文字
        if prize_type:
            result_msg += f"\n🌟 你的运气简直逆天了！\n⭐️咕咕嘎嘎池当前还有{get_prize_pool():,}金币"
        elif reward_amount == 0:
            result_msg += f"\n🍀 别灰心，下次一定能嘎嘎咕咕的！\n⭐️咕咕嘎嘎池已达{get_prize_pool():,}金币"
        elif reward_amount < self.SCRATCH_COST:
            result_msg += f"\n🎯 运气还不错，继续加油！\n⭐️咕咕嘎嘎池已达{get_prize_pool():,}金币"
        else:
            result_msg += f"\n🎊 不错的收益！\n⭐️咕咕嘎嘎池已达{get_prize_pool():,}金币"
        
        return result_msg
