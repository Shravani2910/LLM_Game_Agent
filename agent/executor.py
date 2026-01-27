class Executor:
    def __init__(self, llm):
        self.llm = llm

    def execute(self, plan, state):
        prompt = f"""
Plan:
{plan}

State:
{state}

Choose ONE valid action.
"""
        return self.llm(prompt)
