"""学历等级配置"""

# 学历等级系统
EDUCATION_LEVELS = [
    {"name": "幼儿园", "knowledge_required": 0, "description": "🎈 刚刚开始学习的萌新阶段"},
    {"name": "小学", "knowledge_required": 100, "description": "📚 基础知识的学习阶段"},
    {"name": "初中", "knowledge_required": 1000, "description": "📖 开始接触更深入的知识"},
    {"name": "高中", "knowledge_required": 3000, "description": "📝 为高等教育做准备"},
    {"name": "专科", "knowledge_required": 5000, "description": "🎓 专业技能的学习"},
    {"name": "本科", "knowledge_required": 8000, "description": "🎓 大学本科教育"},
    {"name": "硕士", "knowledge_required": 10000, "description": "👩‍🎓 研究生学历"},
    {"name": "博士", "knowledge_required": 20000, "description": "👩‍🔬 高等学术研究"},
    {"name": "博士后", "knowledge_required": 30000, "description": "🧠 顶尖学术水平"},
    {"name": "院士", "knowledge_required": 40000, "description": "🏆 学术界的巅峰成就"},
    {"name": "诺贝尔奖", "knowledge_required": 50000, "description": "🌟 世界级的学术贡献"},
    {"name": "全知全能", "knowledge_required": 100000, "description": "💫 超越凡人的智慧境界"}
]

def get_education_info(education_level: str):
    """根据学历名称获取学历信息"""
    for education in EDUCATION_LEVELS:
        if education["name"] == education_level:
            return education
    return EDUCATION_LEVELS[0]  # 默认返回第一个（幼儿园）

def get_next_education_info(current_education: str):
    """获取下一级学历信息"""
    for i, education in enumerate(EDUCATION_LEVELS):
        if education["name"] == current_education:
            if i < len(EDUCATION_LEVELS) - 1:
                return EDUCATION_LEVELS[i + 1]
    return None

def check_education_upgrade(knowledge: int, current_education: str):
    """检查是否可以升级学历"""
    next_education = get_next_education_info(current_education)
    if next_education and knowledge >= next_education["knowledge_required"]:
        return next_education
    return None

def format_education_display(education_level: str, knowledge: int) -> str:
    """格式化学历和学识显示"""
    current_education = get_education_info(education_level)
    next_education = get_next_education_info(education_level)
    
    if next_education:
        max_knowledge = next_education["knowledge_required"]
        return f"学历：{education_level} {knowledge}/{max_knowledge}"
    else:
        return f"学历：{education_level} {knowledge} (已满级)"

def get_education_index(education_level: str) -> int:
    """根据学历名称获取数字索引"""
    for i, education in enumerate(EDUCATION_LEVELS):
        if education["name"] == education_level:
            return i
    return 0  # 默认返回幼儿园索引
