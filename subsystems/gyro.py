
from utils.math.algebra import calculate_for_gyro
from utils.math.algebra import linear_remap
from utils.math.algebra import clamp


class GyroSubSystem:
    def __init__(self, gyroscope): 
        self.gyro = gyroscope
        self.can_run = True
        self.init_bias = .125
        self.bias = self.init_bias
        self.last_error = 0
        self.setup_bias(90)
        
    def update_state(self, state: bool):
        self.can_run = state
        

    def reset(self):
        self.gyro.reset()


    def reset_bias(self):
        self.bias=self.init_bias
    

    def setup_bias(self, angle):
        self.dampening = linear_remap(angle, 90, 180, .75, .7)


    def calculate(self, target_angle: float):
        angle = self.gyro.getAngle() % 360
        error = target_angle - angle
        if self.last_error * error < 0:
            self.bias*=self.dampening
        self.last_error = error
        if abs(error) >= 180:
            error = 360 - error
        v = error / 180
        # print(v)
        v = linear_remap(v,-1 ,1,-0.6,0.6)
        radius = .3
        # if abs(v) < radius:
        #     v = linear_remap(v,-radius,radius,-.6,.6)
        if abs(v) < radius:
            return clamp(v+self.bias if v > 0 else v-self.bias,-1,1)
        return clamp(v, -.3, .3)

        

    def run(self, speed: float):
        pass
    