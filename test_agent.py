from agent.llm_agent import LLMGamingAgent

def fake_llm(prompt):
    print("PROMPT:", prompt)
    return "move north"

agent = LLMGamingAgent(fake_llm)

state = {
    "location": "forest",
    "health": 100,
    "inventory": []
}

print(agent.step(state))
