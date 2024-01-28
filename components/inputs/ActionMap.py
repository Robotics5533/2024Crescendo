class ActionMap:
    def __init__(self):
        self.actions = {}
        
    def get_action_pressed(self, action: str):
        return self.is_action_registered(action) and any([function() for function in self.actions[action]])
    
    def register_action(self, action: str, func):
        if not self.is_action_registered(action):
            self.actions[action] = []
        
        self.actions[action].append(func)
        return self.actions
    
    def is_action_registered(self, action: str):
        return action in self.actions