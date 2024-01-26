from phoenix6 import hardware, controls
from typing import Union
import wpilib
class ClimbSubSystem:
    def __init__(self, motor): 
        self.motor = motor
        self.can_run = True
    def update_state(self, state: bool):
        self.can_run = state
    def move(self, speed: float):
        if self.can_run:
            self.motor.set_control(speed / 100)