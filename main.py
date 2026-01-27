from game.explorer_world import ExplorerWorld
from game.explorer_agent import ExplorerAgent
from agent.goals import Goal
from agent.memory import Memory
from agent.brain import think
from agent.reward import RewardEvaluator

def main():
    world = ExplorerWorld()
    memory = Memory()

    agent = ExplorerAgent(brain=think,memory=memory,goal=Goal.EXPLORE)

    for step in range(10):
        print(f"\n--- Step {step} ---")

        action = agent.act(world)
        print("Agent decided:", action)

        world.apply_action(action)
if __name__ == "__main__":
    main()

 
