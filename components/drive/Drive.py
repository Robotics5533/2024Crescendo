class Drive:
    def __init__(self):
        self.set_speed((25, 25, 25))
        
    def set_speed(self, speed: tuple(float)):
        self.speed = map(speed, lambda x: x / 100)
    
    """
    *args -> Do the math for a deadzone with any amount of args as possible
    """
    @staticmethod
    def deadzone(*args):
        for value in args:
            if value < -0.3 or value > 0.3:
                return True
        return False
    def speed_calculation(self, x: float, i: int):
        return x * self.speed[i]
    def move(self):
        pass