"""刮刮乐处理器"""
import random
from astrbot.api.all import *
from ..core.data_manager import *

class ScratchCardHandler:
    def __init__(self):
        # 定义刮刮乐的奖励配置
        self.SCRATCH_COST = 50  # 每次刮刮乐花费50金币
        
        # 奖励配置：(奖励金额, 权重, 描述)
        self.SCRATCH_REWARDS = [
            # 小奖（高概率）
            (0, 400, "谢谢参与"),
            (20, 200, "小奖"),
            (50, 150, "回本奖"),
            (100, 100, "双倍奖"),
            (200, 80, "小赚一笔"),
            
            # 中奖（中等概率）
            (500, 40, "中奖啦"),
            (1000, 25, "幸运儿"),
            (2000, 15, "运气不错"),
            (5000, 10, "大运当头"),
            (10000, 8, "发财了"),
            
            # 大奖（低概率）
            (20000, 5, "暴富"),
            (50000, 3, "一夜暴富"),
            (100000, 2, "人生赢家"),
            (200000, 1, "传说中的幸运儿"),
            
            # 超级大奖（极低概率）
            (800000, 0.1, "史诗级大奖🎉")  # 80万大奖，极低概率
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
                "✨ 刚好回本",
                "⚖️ 不亏不赚",
                "🔄 平平稳稳",
                "🙂 有来有回",
                "💸 保本就好",
                "⚪ 小圈完整闭合",
                "🪙 运气在原地踏步",
                "🔔 小小响一下",
                "🧘 心态稳住",
                "🛟 稳住阵脚"
            ],
            100: [
                "🎊 双倍收益",
                "📈 小有收获",
                "💡 开始发亮",
                "🌟 幸运加持",
                "🪄 运气显灵",
                "💎 还不错嘛",
                "📀 有点赚头",
                "🛎️ 喜讯传来",
                "🎯 稍微开心一下",
                "😎 小赚怡情"
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
            20000: [
                "🎊 暴富啦",
                "💸 一夜暴富的感觉",
                "🌈 好运彩虹",
                "🚀 飞速致富",
                "🏆 幸运非凡",
                "💎 小目标达成",
                "🥳 狂欢时刻",
                "🎉 惊天好消息",
                "🍀 好运全开",
                "📈 人生高光"
            ],
            50000: [
                "🌟 传说级运气",
                "👑 你就是天选之人",
                "🎇 好运盛典",
                "💎 财富爆棚",
                "🚀 直上云霄",
                "🎯 超级大奖",
                "🏅 好运榜首",
                "🥳 传说再现",
                "🍀 好运无敌",
                "🎆 星辰守护"
            ],
            100000: [
                "🏆 人生赢家",
                "💎 钻石级运气",
                "🌟 光芒万丈",
                "🎉 百万预备",
                "📈 财运大涨",
                "👑 王者降临",
                "🚀 冲破天际",
                "🥂 豪气冲天",
                "💥 超级好运",
                "🎯 一击必中"
            ],
            200000: [
                "🎯 传说中的幸运儿",
                "🌈 彩虹般的运气",
                "🏆 高光时刻",
                "💎 财富升级",
                "🎉 令人艳羡",
                "🚀 好运极速",
                "👑 王者气质",
                "🥳 全民羡慕",
                "🍀 大奖收割机",
                "🎆 历史留名"
            ],
            800000: [
                "🎆🎉 史诗级大奖 🎉🎆",
                "👑 恭喜成为刮刮乐之王 👑",
                "💰💰 80万巨奖到手 💰💰",
                "🌟 命运的奇迹",
                "🚀 一飞冲天",
                "🏆 百万级荣誉",
                "🎇 财富巅峰",
                "💎 传奇人生",
                "🥂 世界见证",
                "🎊 无敌好运"
            ]
        }

    async def scratch_card(self, event: AstrMessageEvent):
        """刮刮乐功能"""
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
            yield event.plain_result(f': {nickname}，刮刮乐需要{self.SCRATCH_COST}金币，你当前只有{current_coins}金币，金币不足！')
            return
        
        # 扣除费用
        new_coins = current_coins - self.SCRATCH_COST
        
        # 随机抽取奖励
        reward_amount, description = self._get_random_reward()
        
        # 加上奖励
        final_coins = new_coins + reward_amount
        
        # 更新用户金币
        update_user_data(user_id, coins=final_coins)
        
        # 构建结果消息
        result_msg = self._build_result_message(nickname, reward_amount, description, current_coins, final_coins)
        
        yield event.plain_result(result_msg)

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

    def _build_result_message(self, nickname, reward_amount, description, old_coins, new_coins):
        """构建结果消息"""
        # 刮刮乐动画效果
        scratch_animation =  "▓▓▓▓▓▓▓▓▓▓\n"
        scratch_animation += "▓░░░░░░░░░▓\n"
        scratch_animation += "▓░░ 刮刮乐 ░░▓\n"
        scratch_animation += "▓░░░░░░░░░▓\n"
        scratch_animation += "▓▓▓▓▓▓▓▓▓▓\n\n"
        
        # 获取特殊效果文本
        effect_text = random.choice(self.EFFECT_TEXTS.get(reward_amount, ["🎉 恭喜中奖"]))
        
        result_msg = f": {nickname} 🎫 刮刮乐结果 🎫\n\n"
        result_msg += scratch_animation
        
        if reward_amount == 0:
            result_msg += f"💔 {description} - {effect_text}\n"
            result_msg += f"💸 花费：{self.SCRATCH_COST}金币\n"
            result_msg += f"💰 余额：{old_coins} → {new_coins}金币\n"
        elif reward_amount == 800000:
            # 特殊的大奖展示
            result_msg += "🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆\n"
            result_msg += "🎉    史诗级大奖    🎉\n"
            result_msg += "👑   80万金币大奖   👑\n" 
            result_msg += "🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆\n\n"
            result_msg += f"🏆 恭喜 {nickname} 成为刮刮乐传奇！\n"
            result_msg += f"💰 奖励：{reward_amount:,}金币\n"
            result_msg += f"💎 余额：{old_coins:,} → {new_coins:,}金币\n"
            result_msg += f"\n🌟 {random.choice(self.EFFECT_TEXTS[800000])}"
        elif reward_amount >= 100000:
            # 高级大奖展示
            result_msg += "🎊🎊🎊🎊🎊🎊🎊🎊\n"
            result_msg += f"🌟  {description}  🌟\n"
            result_msg += "🎊🎊🎊🎊🎊🎊🎊🎊\n\n"
            result_msg += f"🎯 {effect_text}\n"
            result_msg += f"💰 奖励：{reward_amount:,}金币\n"
            result_msg += f"💎 余额：{old_coins:,} → {new_coins:,}金币"
        elif reward_amount >= 10000:
            # 中级大奖展示
            result_msg += "✨✨✨✨✨✨\n"
            result_msg += f"🎉 {description} 🎉\n"
            result_msg += "✨✨✨✨✨✨\n\n"
            result_msg += f"🚀 {effect_text}\n"
            result_msg += f"💰 奖励：{reward_amount:,}金币\n"
            result_msg += f"💎 余额：{old_coins:,} → {new_coins:,}金币"
        else:
            # 普通奖励展示
            result_msg += f"🎁 {description} - {effect_text}\n"
            if reward_amount > 0:
                result_msg += f"💰 奖励：{reward_amount}金币\n"
            result_msg += f"💸 花费：{self.SCRATCH_COST}金币\n"
            result_msg += f"💰 余额：{old_coins} → {new_coins}金币"
        
        # 添加鼓励文字
        if reward_amount == 0:
            result_msg += "\n🍀 别灰心，下次一定能中大奖！"
        elif reward_amount < self.SCRATCH_COST:
            result_msg += "\n🎯 运气还不错，继续加油！"
        elif reward_amount >= 100000:
            result_msg += "\n🌟 你的运气简直逆天了！"
        
        return result_msg
