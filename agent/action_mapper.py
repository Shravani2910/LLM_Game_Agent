def map_action(llm_output):
    llm_output = llm_output.upper()

    if "MOVE_NORTH" in llm_output:
        return "MOVE_NORTH"
    if "PICKUP" in llm_output:
        return "PICKUP"

    return "STAY"