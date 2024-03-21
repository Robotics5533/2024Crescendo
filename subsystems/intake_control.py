from phoenix6 import hardware, controls
from typing import Union
import wpilib

from utils.math.algebra import linear_remap

class IntakeControlSubSystem:
    def __init__(self, motor, follow_motor): 
        self.motor = motor
        self.follow_motor = follow_motor
        self.can_run = True
        
        
    def update_state(self, state: bool):
        self.can_run = state
    
    @staticmethod
    def calculate(x,s):
        if s > 0: # Invert for in
            x = -3.30 - x # Go this speed
        if x > -3.30/1.8: # If x is greater than the midpoint
            return 1.85 # Go this speed
        else:
            return linear_remap(x, -3.30/1.8, -3.30, 1/100, 0) # Slow down when in desired zones
        
    def run(self, speed: float):
        speed = self.calculate(self.motor.get_position(), speed) * speed
        self.motor.set(speed)
        self.follow_motor.set(-speed)
            