class Memory:
    def __init__(self):
        self.logs = []

    def remember(self, observation, action, result):
        self.logs.append({
            "observation": observation,
            "action": action,
            "result": result
        })
    def last(self):
        return self.logs[-1] if self.logs else None
    def summary(self, n=5):
        return self.logs[-n:]