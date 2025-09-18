"""咕咕嘎嘎排行榜处理器"""
import os
from astrbot.api.all import *
from ..core import data_manager
from ..core.data_manager import load_user_data, get_user_wife_data, get_prize_pool

class ScratchRankingHandler:
    def __init__(self):
        pass
    
    async def scratch_ranking(self, event: AstrMessageEvent):
        """咕咕嘎嘎排行榜功能"""
        try:
            # 加载用户数据
            load_user_data()
            
            # 收集所有有咕咕嘎嘎记录的用户数据
            ranking_data = []
            
            for user_id, user_info in data_manager.user_data.items():
                stats = user_info.get("scratch_stats")
                if stats and stats["total_count"] > 0:  # 只统计有过咕咕嘎嘎记录的用户
                    # 获取用户昵称
                    wife_data = get_user_wife_data(user_id)
                    if wife_data and len(wife_data) > 2:
                        nickname = wife_data[2]
                    else:
                        nickname = f"用户{user_id}"
                    
                    ranking_data.append({
                        "user_id": user_id,
                        "nickname": nickname,
                        "total_count": stats["total_count"],
                        "total_cost": stats["total_cost"],
                        "total_reward": stats["total_reward"],
                        "net_gain": stats["net_gain"]
                    })
            
            # 检查是否有数据
            if not ranking_data:
                yield event.plain_result("暂无咕咕嘎嘎记录，快来尝试第一次咕咕嘎嘎吧！")
                return
            
            # 生成各种排行榜
            ranking_msg = "🎊 咕咕嘎嘎排行榜 🎊\n\n"
            
            # 1. 咕咕嘎嘎次数排行榜（前15名）
            count_ranking = sorted(ranking_data, key=lambda x: x["total_count"], reverse=True)[:15]
            ranking_msg += "🏆 咕咕嘎嘎次数排行榜 TOP15\n"
            for i, user in enumerate(count_ranking, 1):
                if i <= 3:
                    medals = ["🥇", "🥈", "🥉"][i-1]
                    ranking_msg += f"{medals} {user['nickname']}: {user['total_count']:,}次\n"
                else:
                    ranking_msg += f"{i:2d}. {user['nickname']}: {user['total_count']:,}次\n"
            
            # 2. 投入金额排行榜（前15名）
            cost_ranking = sorted(ranking_data, key=lambda x: x["total_cost"], reverse=True)[:15]
            ranking_msg += "\n💸 投入金额排行榜 TOP15\n"
            for i, user in enumerate(cost_ranking, 1):
                if i <= 3:
                    medals = ["🥇", "🥈", "🥉"][i-1]
                    ranking_msg += f"{medals} {user['nickname']}: {user['total_cost']:,}金币\n"
                else:
                    ranking_msg += f"{i:2d}. {user['nickname']}: {user['total_cost']:,}金币\n"
            
            # 3. 总收益排行榜（前15名）
            reward_ranking = sorted(ranking_data, key=lambda x: x["total_reward"], reverse=True)[:15]
            ranking_msg += "\n💰 总收益排行榜 TOP15\n"
            for i, user in enumerate(reward_ranking, 1):
                if i <= 3:
                    medals = ["🥇", "🥈", "🥉"][i-1]
                    ranking_msg += f"{medals} {user['nickname']}: {user['total_reward']:,}金币\n"
                else:
                    ranking_msg += f"{i:2d}. {user['nickname']}: {user['total_reward']:,}金币\n"
            
            # 4. 净收益排行榜（前15名，包含负数）
            net_gain_ranking = sorted(ranking_data, key=lambda x: x["net_gain"], reverse=True)[:15]
            ranking_msg += "\n📈 净收益排行榜 TOP15\n"
            for i, user in enumerate(net_gain_ranking, 1):
                net_gain = user["net_gain"]
                if i <= 3:
                    medals = ["🥇", "🥈", "🥉"][i-1]
                    if net_gain >= 0:
                        ranking_msg += f"{medals} {user['nickname']}: +{net_gain:,}金币\n"
                    else:
                        ranking_msg += f"{medals} {user['nickname']}: {net_gain:,}金币\n"
                else:
                    if net_gain >= 0:
                        ranking_msg += f"{i:2d}. {user['nickname']}: +{net_gain:,}金币\n"
                    else:
                        ranking_msg += f"{i:2d}. {user['nickname']}: {net_gain:,}金币\n"
            
            # 5. 净亏损排行榜（前15名，只显示亏损用户）
            loss_users = [user for user in ranking_data if user["net_gain"] < 0]
            net_loss_ranking = sorted(loss_users, key=lambda x: x["net_gain"])[:15]
            
            if net_loss_ranking:
                ranking_msg += "\n📉 净亏损排行榜 TOP15\n"
                for i, user in enumerate(net_loss_ranking, 1):
                    net_loss = user["net_gain"]
                    if i <= 3:
                        medals = ["🥇", "🥈", "🥉"][i-1]
                        ranking_msg += f"{medals} {user['nickname']}: {net_loss:,}金币\n"
                    else:
                        ranking_msg += f"{i:2d}. {user['nickname']}: {net_loss:,}金币\n"
            else:
                ranking_msg += "\n📉 净亏损排行榜 TOP15\n暂无亏损用户，大家都是赚钱的！🎉\n"
            
            # 6. 咕咕嘎嘎池状态
            current_pool = get_prize_pool()
            ranking_msg += f"\n🎊 当前咕咕嘎嘎池: {current_pool:,}金币\n"

            yield event.plain_result(ranking_msg)
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            yield event.plain_result(f"查询咕咕嘎嘎排行榜时出现错误: {str(e)}")
