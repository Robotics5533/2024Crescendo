from phoenix6 import hardware, controls
from typing import Union
import wpilib

from components.motor.Talon5533 import Talon5533
class ClimbControlSubSystem:
    def __init__(self, motor): 
        self.motor = motor
        self.can_run = True
        
    def update_state(self, state: bool):
        self.can_run = state
        
    def move(self, speed: float):
        if self.can_run:
            self.motor.set(speed / 100)