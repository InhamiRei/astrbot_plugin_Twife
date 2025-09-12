"""碎片系统处理器"""

from ..core import data_manager
from ..config.travel_config import FRAGMENT_CONVERSION


class FragmentHandler:
    """碎片系统处理器"""
    
    def __init__(self):
        pass
    
    def can_use_fragments(self, user_id, fragment_type, required_amount=100):
        """检查用户是否有足够的碎片"""
        user_data = data_manager.get_user_data(user_id)
        backpack = user_data.get("backpack", {})
        
        fragment_name = FRAGMENT_CONVERSION[fragment_type]["name"]
        current_amount = backpack.get(fragment_name, 0)
        
        return current_amount >= required_amount
    
    def use_fragments(self, user_id, fragment_type, amount_to_use=100):
        """使用碎片提升属性"""
        try:
            # 检查碎片配置
            if fragment_type not in FRAGMENT_CONVERSION:
                return False, "未知的碎片类型"
            
            fragment_config = FRAGMENT_CONVERSION[fragment_type]
            fragment_name = fragment_config["name"]
            required_amount = fragment_config["required_amount"]
            effect = fragment_config["effect"]
            
            # 检查用户碎片数量
            user_data = data_manager.get_user_data(user_id)
            backpack = user_data.get("backpack", {})
            current_amount = backpack.get(fragment_name, 0)
            
            if current_amount < amount_to_use:
                return False, f"碎片不足，需要{amount_to_use}个，当前只有{current_amount}个"
            
            if amount_to_use % required_amount != 0:
                return False, f"使用数量必须是{required_amount}的倍数"
            
            # 计算能提升的属性点数
            times = amount_to_use // required_amount
            
            # 扣除碎片
            new_amount = current_amount - amount_to_use
            if new_amount <= 0:
                del backpack[fragment_name]
            else:
                backpack[fragment_name] = new_amount
            
            # 更新背包
            data_manager.update_user_data(user_id, backpack=backpack)
            
            # 应用属性效果
            effect_result = {}
            for attr_name, attr_value in effect.items():
                total_effect = attr_value * times
                effect_result[attr_name] = total_effect
                
                # 更新老婆特殊属性
                self._apply_special_attribute_effect(user_id, attr_name, total_effect)
            
            return True, {
                "fragment_name": fragment_name,
                "used_amount": amount_to_use,
                "attribute_increases": effect_result,
                "remaining_fragments": new_amount
            }
            
        except Exception as e:
            print(f"使用碎片时出错: {e}")
            return False, f"系统错误: {str(e)}"
    
    def _apply_special_attribute_effect(self, user_id, attr_name, value):
        """应用特殊属性效果到老婆数据"""
        try:
            wife_data = data_manager.get_user_wife_data(user_id)
            if not wife_data:
                return
            
            # 确保老婆数据包含所有属性
            if len(wife_data) < 19:
                while len(wife_data) < 19:
                    wife_data.append(0)
                data_manager.save_global_wife_data()
            
            if attr_name == "charm_contrast":
                # 反差萌属性 - 存储在 wife_data[18]
                current_value = wife_data[18]
                new_value = max(0, current_value + value)  # 只限制不能为负数
                data_manager.update_user_wife_data(user_id, contrast_cute=new_value)
                
            elif attr_name == "blackening":
                # 黑化率属性 - 存储在 wife_data[17]
                current_value = wife_data[17]
                new_value = max(0, current_value + value)  # 只限制不能为负数
                data_manager.update_user_wife_data(user_id, dark_rate=new_value)
                
        except Exception as e:
            print(f"应用特殊属性效果时出错: {e}")
    
    def get_fragment_info(self, user_id):
        """获取用户的碎片信息"""
        try:
            user_data = data_manager.get_user_data(user_id)
            backpack = user_data.get("backpack", {})
            
            fragment_info = {}
            for fragment_type, config in FRAGMENT_CONVERSION.items():
                fragment_name = config["name"]
                current_amount = backpack.get(fragment_name, 0)
                can_use_times = current_amount // config["required_amount"]
                
                fragment_info[fragment_type] = {
                    "name": fragment_name,
                    "current_amount": current_amount,
                    "required_amount": config["required_amount"],
                    "can_use_times": can_use_times,
                    "description": config["description"]
                }
            
            return fragment_info
            
        except Exception as e:
            print(f"获取碎片信息时出错: {e}")
            return {}


# 全局碎片处理器实例
fragment_handler = FragmentHandler()
