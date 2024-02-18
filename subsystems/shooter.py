from phoenix6 import hardware, controls
from typing import Union
import wpilib

class ShooterSubSystem:
    def __init__(self, motors): 
        self.motors = motors
        self.can_run = True
        
    def update_state(self, state: bool):
        self.can_run = state
        
    def shoot(self, speed: float):
        self.motors[0].set(-(speed / 100))
        currentVoltage = self.motors[0].currentVoltage
        self.motors[1].set(currentVoltage)
            