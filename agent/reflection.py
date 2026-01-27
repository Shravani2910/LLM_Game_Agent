def reflect(memory):
    if not memory.logs:
        return "No past experience."

    recent = memory.summary()

    text = "Recent experiences:\n"
    for m in recent:
        text += f"- Obs: {m['observation']} | Action: {m['action']} | Result: {m['result']}\n"

    return text
