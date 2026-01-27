from agent.memory import Memory
from agent.planner import Planner
from agent.executor import Executor

class LLMGamingAgent:
    def __init__(self, llm):
        self.memory = Memory()
        self.planner = Planner(llm)
        self.executor = Executor(llm)

    def step(self, game_state):
        plan = self.planner.create_plan(game_state, self.memory)
        action = self.executor.execute(plan, game_state)
        self.memory.store(game_state, plan, action)
        return action
