
class Drive:
    def __init__(self):
        self.set_speed(25)
        
    def set_speed(self, speed):
        self.speed = speed / 100
    

    # def deadzoneify(error = 0.3):
    #     def create_deadzone_error(f):
    #         def deadzoned_f():
    #             value = f()
    #             return 0 if almost_equal(value,0,error) else value
    #         return deadzoned_f
    #     return create_deadzone_error
    


    def speed_calculation(self, x: float, i: int):
        return x * self.speed
    
    def move(self):
        pass