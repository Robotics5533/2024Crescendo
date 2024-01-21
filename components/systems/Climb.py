from phoenix6 import hardware, controls
from typing import Union
import wpilib
class Climb:
    def __init__(self, motor: Union[hardware.TalonFX, wpilib.PWMSparkMax]): 
        self.motor = motor
    def run(self):
        self.motor.set_control(0.5)