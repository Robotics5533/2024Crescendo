from typing import Union
import wpilib
from components.drive.Drive import Drive
from phoenix6 import hardware, controls

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
        
    def set_mode(self, mode: int):
        for motor in self.motors:
            motor.set_mode(mode)
            
    def get_position(self):
        return sum(map(lambda x: x.get_position(), self.motors)) / len(self.motors)
    
    def set_position(self, position: float):
        for motor in self.motors:
            motor.set_position(position)


    def process(self):
        for motor in self.motors:
            motor.process(0)
            
    def move(self, data: Vector):
        data = Vector(*data.deadzone())
        fl = data.b - data.c - data.a
        fr = data.b + data.c + data.a
        bl = data.b - data.c + data.a
        br = data.b + data.c - data.a

        m = max(abs(x) for x in [fl, fr, bl, br])

        if m > 1:
            fl /= m
            fr /= m
            bl /= m
            br /= m

        self.front_left_motor.set(fl)
        self.front_right_motor.set(fr)
        self.back_left_motor.set(bl)
        self.back_right_motor.set(br)
