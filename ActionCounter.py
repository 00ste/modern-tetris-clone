

class ActionCounter:
    def __init__(self, action, max_value, start_value=0) -> None:
        self.value = start_value
        self.max_value = max_value
        self.action = action

    def reset(self):
        self.value = 0
    
    def increment(self, delta=1):
        self.value += delta
        if self.value >= self.max_value:
            self.action()
            self.value = 0