class Goal:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def check_completion(self, world):
        if "stone" in world.inventory:
            self.completed = True
