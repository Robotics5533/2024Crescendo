from phoenix6 import hardware, controls
from typing import Union
import wpilib
class ClimbSubSystem:
    def __init__(self, motor: Union[hardware.TalonFX, wpilib.PWMSparkMax]): 
        self.motor = motor
    def move(self, speed: float):
        self.motor.set_control(speed / 100)