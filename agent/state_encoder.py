
def encode_state(world):
    state = world.get_state()
    Observation = f"""
    
    You are an explorer in a survival game.

    Location: {world.location}
    Health: {world.health}
    Inventory: {world.inventory}
    Visible Objects: {world.visible_objects}
    Grid Size: {state['grid_size']}
    Agent Position: {state['agent_pos']}
    
    Choose one action from:
    MOVE_NORTH,MOVE_SOUTH,MOVE_EAST,MOVE_WEST,PICKUP,WAIT

    """
 
    return Observation.strip()
