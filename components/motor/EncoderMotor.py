#EncoderModer
from math import pi
from phoenix6 import hardware, controls, configs3
from components.motor.Motor5533 import MotorModes
from components.sensors.encoder5533 import BufferedEncoder5533
import wpilib
from math import atan
from typing import Union
from utils.math.algebra import clamp
class EncoderMotor:
    def getDistance(self):
        return self.encoder.getDistance() * self.conversion
        

    def __init__(self, encoder: Union[BufferedEncoder5533, "wpilib.encoder"], motor, mode = MotorModes.velocity):
        self.encoder = encoder 
        self.motor = motor
        self.mode = mode
        self.target = 0
        self.conversion = 1

    def process(self):
        
        if self.mode == MotorModes.voltage:
            return
        
        if self.mode == MotorModes.position:
            error = self.getDistance() - self.target
            correction = clamp(-atan(error), -1, 1)
            self.motor.set(correction)
            
    def set(self, value):
        if self.mode == MotorModes.voltage:
            self.motor.set(value)
        elif self.mode == MotorModes.position:
            self.target = value

    def set_mode(self, mode: int):
        self.mode = mode
    
    def get_position(self):
        return self.talonmotor.get_position().value_as_double
    
    def set_position(self, position: float = 0):
        self.talonmotor.set_position(position)
