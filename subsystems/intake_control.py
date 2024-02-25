from phoenix6 import hardware, controls
from typing import Union
import wpilib

from utils.math.algebra import linear_remap

class IntakeControlSubSystem:
    def __init__(self, motor): 
        self.motor = motor
        self.can_run = True
        
        
    def update_state(self, state: bool):
        self.can_run = state
    
    @staticmethod
    def calculate(x,s):
        if s > 0:
            x = -3.30 - x
        if x > -3.30/2:
            return 1.85
        else:
            return linear_remap(x, -3.30/2, -3.30, 1/100, 0)
        
    def run(self, speed: float):
        speed = self.calculate(self.motor.get_position(), speed) * speed
        self.motor.set(speed)
            