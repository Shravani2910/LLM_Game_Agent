from agent.state_encoder import encode_state
from agent.action_mapper import map_action
from agent.brain import think
from agent.reflection import reflect


class ExplorerAgent:
    def __init__(self, goal, memory, brain):
        self.goal = goal
        self.memory = memory
        self.brain = brain

    def act(self, world):
        context = {
            "observation": world,
            "goal": self.goal,
            "memory": self.memory
        }

        decision = self.brain(context)
        return decision