from phoenix6 import hardware, controls
from typing import Union
import wpilib
class Climb:
    def __init__(self, motor: Union[hardware.TalonFX, wpilib.PWMSparkMax]): 
        self.motor = motor
        self.motor_controler = controls.DutyCycleOut(0)
    def run(self, speed: float):
        self.motor_controler.output = speed
        self.motor.set_control(self.motor_controler)