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
        

    def __init__(self, encoder: Union[BufferedEncoder5533, "wpilib.encoder"] , motor , mode = MotorModes.velocity):
        self.encoder = encoder 
        self.motor = motor
        self.mode = mode
        self.timer = wpilib.Timer()
        self.target = 0
        self.conversion = 1
        self.wheelDiameter = 22 # inches
        self.lastTime = 0
        self.lastPosition = 0

    def process(self):
        
        if self.mode == MotorModes.voltage:
            return
        
        if self.mode == MotorModes.position or self.mode == MotorModes.velocity:
            error = self.get_target_error()
            correction = clamp(-atan(error), -1, 1)
            self.motor.set(correction)
        self.lastPosition = self.get_position()
        self.lastTime = self.timer.get()

    def get_target_error(self) -> float:
        if self.mode == MotorModes.position:
            return self.get_position() - self.target
        if self.mode == MotorModes.velocity:
            return self.get_velocity()-self.target
        return 00.0
            




    def get_velocity(self)->float:
    
        deltaPosition = self.get_position() - self.lastPosition
        deltaTime = self.timer.get() - self.lastTime
        if deltaTime == 0:
            return 0
        return deltaPosition/deltaTime # = velocity
        

    def set(self, value):
        if self.mode == MotorModes.voltage:
            self.motor.set(value)
        
        if self.mode == MotorModes.position or self.mode == MotorModes.velocity:
            self.target = value
        

    def set_mode(self, mode: int):
        self.mode = mode
    
    def get_position(self) -> float:
        return self.encoder.getDistance() * pi * self.wheelDiameter
    
    
    def set_position(self, position: float = 0):
        self.encoder.setDistance(position)
