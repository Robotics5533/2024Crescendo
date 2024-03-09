
class GyroSubSystem:
    def __init__(self, gyroscope): 
        self.gyro = gyroscope
        self.can_run = True
        
    def update_state(self, state: bool):
        self.can_run = state
        
    def reset(self):
        self.gyro.reset()


    def calculate(self, target_angle: float):
        angle = self.gyro.getAngle()
        error = target_angle - angle
        if abs(error) >= 180:
            error = 360 - error
        v = error / 180
        v = v * 7
        if abs(v) > 1:
           v = v / abs(v)
        return v
        

    def run(self, speed: float):
        pass
    