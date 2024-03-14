from wpimath.controller import PIDController


class GyroSubSystem:
    def __init__(self, gyroscope): 
        self.gyro = gyroscope
        self.can_run = True
        # self.pid = PIDController(3/360, .3/360, 0.5/360) # PID values for 180
        self.pid = PIDController(7/360, 4/360, .6/360)
        
    def update_state(self, state: bool):
        self.can_run = state
        
    def reset(self):
        self.gyro.reset()


    def calculate(self, target_angle: float):
        return self.pid.calculate(self.gyro.getAngle(), target_angle)
        # angle = self.gyro.getAngle()
        # error = target_angle - angle
        # if abs(error) >= 180:
        #     error = 360 - error
        # v = error / 180
        # v = v * 7
        # if abs(v) > 1:
        #    v = v / abs(v)
        # return v
        

    def run(self, speed: float):
        pass
    