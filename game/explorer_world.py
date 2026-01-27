class ExplorerWorld:
    def __init__(self, grid_size=5):
        self.grid_size = grid_size
        self.agent_pos = [0, 0]
        self.location = "forest"
        self.health = 100
        self.inventory = []
        self.visible_objects = ["tree", "stone"]

    def apply_action(self, action):
        if action == "MOVE_NORTH":
            self.location = "mountain"
        elif action == "PICKUP":
            self.inventory.append("stone")
        elif action == "WAIT":
            pass

    def is_game_over(self):
        return self.health <= 0

    def get_state(self):
        return {
            "agent_pos": self.agent_pos,
            "grid_size": self.grid_size
        }