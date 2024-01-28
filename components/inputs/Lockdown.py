class Lockdown:
    def __init__(self):
        self.lock_value = False
        
    def lock(self):
        self.lock_value = True
        
    def unlock(self):
        self.lock_value = False
        
    def lockify(self, f):
        return lambda: False if self.lock_value else f()
    
