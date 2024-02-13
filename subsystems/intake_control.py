from phoenix6 import hardware, controls
from typing import Union
import wpilib

class IntakeControlSubSystem:
    def __init__(self, motor): 
        self.motor = motor
        self.can_run = True
        
    def update_state(self, state: bool):
        self.can_run = state
        
    def run(self, speed: float):
        print(self.motor.get_position())
        self.motor.set(speed)
            