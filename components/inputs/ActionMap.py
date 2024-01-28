class ActionMap:
    actions = {}
    
    @staticmethod
    def get_action_pressed(action: str):
        return ActionMap.is_action_registered(action) and any([function() for function in ActionMap.actions[action]])
    
    @staticmethod
    def register_action(action: str, func):
        if not ActionMap.is_action_registered(action):
            ActionMap.actions[action] = []
        
        ActionMap.actions[action] += [func]
        return ActionMap.actions
    
    @staticmethod
    def is_action_registered(action: str):
        return action in ActionMap.actions