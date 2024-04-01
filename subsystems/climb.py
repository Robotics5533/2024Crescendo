from phoenix6 import hardware, controls
from typing import Union
import wpilib

from components.motor.Talon5533 import Talon5533
from components.motor.Motor5533 import MotorModes
class ClimbSubSystem:
    def __init__(self, motor: Talon5533): 
        self.motor = motor
        self.can_run = True
        
    def update_state(self, state: bool):
        self.can_run = state
        
    def move(self, speed: float):
        self.motor.set_mode(MotorModes.velocity)
        if self.can_run:
            self.motor.set(speed)