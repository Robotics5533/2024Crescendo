from components.drive.Drive import Drive
import math
from components.motor.Motor5533 import MotorModes
from utils.math.Vector import Vector


class MecanumDrive(Drive):
    def __init__(
        self,
        front_left,
        front_right,
        back_right,
        back_left,
    ):

        super().__init__()
        self.front_left_motor = front_left
        self.front_right_motor = front_right
        self.back_left_motor = back_left
        self.back_right_motor = back_right
        
        self.motors = [front_left, front_right, back_left, back_right]
        self.speed_multiplier = 1
        self.mode = MotorModes.voltage
        self.conversion = 10.78/(6*math.pi)
        
    def set_mode(self, mode: int):
        self.mode = mode
        for motor in self.motors:
            motor.set_mode(mode)
            
    def get_position(self):
        return sum(map(lambda x: abs(x.get_position()), self.motors)) / len(self.motors)
    
    def set_position(self, position: float):
        for motor in self.motors:
            motor.set_position(position)
    
    def set_averages(self, value = 0):
        for motor in self.motors:
            motor.rotating_average.set(value)

    def process(self):
        for motor in self.motors:
            motor.process(0)
            
    def move(self, data: Vector):
        data = Vector(*data.deadzone())*self.speed_multiplier

        if self.mode == MotorModes.position:
            data.c *= -6*math.pi/50.61
            # data.a *= 1.2

        fl = data.b - data.c - data.a
        fr = data.b + data.c + data.a
        bl = data.b - data.c + data.a
        br = data.b + data.c - data.a

        
        
        m = max(abs(x) for x in [fl, fr, bl, br])

        if m > 1 and self.mode == MotorModes.voltage:
            fl /= m
            fr /= m
            bl /= m
            br /= m

        if self.mode == MotorModes.position:
            fr *= -1
            br *= -1
            fl *= -1
            bl *= -1



            fr *= self.conversion
            fl *= self.conversion
            br *= self.conversion
            bl *= self.conversion


            

        self.front_left_motor.set(fl)
        self.front_right_motor.set(fr)
        self.back_left_motor.set(bl)
        self.back_right_motor.set(br)
