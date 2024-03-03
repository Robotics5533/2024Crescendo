
from utils.math.algebra import calculate_for_gyro


class GyroSubSystem:
    def __init__(self, gyroscope): 
        self.gyro = gyroscope
        self.can_run = True
        
    def update_state(self, state: bool):
        self.can_run = state
        
    def reset(self):
        self.gyro.reset()

    
    def calculate(self, target_angle: float):
        angle = self.gyro.getAngle() % 360
        error = target_angle - angle
        if abs(error) >= 180:
            error = 360 - error
        v = error / 180
        return calculate_for_gyro(x = v, si = -1, sf = 1, ei = 1/3, ef = -1/3, mi = -1/3, mx = 1/3)
        

    def run(self, speed: float):
        pass
    