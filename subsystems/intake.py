from phoenix6 import hardware, controls
from typing import Union
import wpilib

class IntakeSubSystem:
    def __init__(self, motors): 
        self.motors = motors
        self.can_run = True
        
    def update_state(self, state: bool):
        self.can_run = state
        
    def run(self, speed: float):
        for motor in self.motors:
            motor.set(speed)
            