from phoenix6 import hardware, controls
from typing import Union
import wpilib

from components.motor.Talon5533 import Talon5533
class GyroSubSystem:
    def __init__(self, gyroscope): 
        self.mgyro = gyroscope
        self.can_run = True
        
    def update_state(self, state: bool):
        self.can_run = state
        
    def update_angle():
        pass
    def run(self, speed: float):
        pass