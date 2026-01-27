class RewardEvaluator:
    def evaluate(self, world, goal):
        if goal and goal.completed:
            return "success"

        if world.health <= 0:
            return "failure"

        return "in_progress"
