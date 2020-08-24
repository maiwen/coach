from agent.agent import Agent
from env.env_cmd import EnvCmd


# 智能体命名需要有红蓝信息, 以便于被大规模对战调度程序自动区分和加载
# 即要求红方智能体类名中包含Red字段, 蓝方智能体类名中包含Blue字段
class BlueAgent(Agent):
    def __init__(self, name, config, **kwargs):
        super().__init__(name, config['side'])

        self._init()

    def _init(self):
        self.forms_own = {}  # 己方编队字典
        self.units_oppo = {}  # 敌方可见平台字典
        self.threats = {}  # 要处理的威胁描述字典
        self.instructions = []  # 指令列表

    def reset(self):
        self._init()

    def step(self, sim_time, obs_blue, **kwargs):
        self.instructions.clear()
        # 生成指令
        pass
        # 返回指令列表
        return self.instructions
