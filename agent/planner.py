class Planner:
    def __init__(self, llm):
        self.llm = llm

    def create_plan(self, state, memory):
        prompt = f"""
You are a smart gaming agent.

State:
{state}

Recent memory:
{memory.recall()}

Goal: survive and progress.

Create a short plan.
"""
        return self.llm(prompt)
