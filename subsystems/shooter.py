from phoenix6 import hardware, controls
from typing import Union
import wpilib

from components.motor.EncoderMotor import EncoderMotor
from components.motor.Motor5533 import MotorModes

class ShooterSubSystem:
    def __init__(self, encoder_motor: EncoderMotor, motor): 
        self.encoder_motor = encoder_motor
        self.motor = motor
        self.can_run = True
        
    def update_state(self, state: bool):
        self.can_run = state
        

    def stop(self, speed: float):
        self.encoder_motor.set_mode(MotorModes.voltage)
        self.encoder_motor.set(0)
        self.motor.set(0)

    def shoot(self, speed: float, multiplier: float = 1):
        self.encoder_motor.set_mode(MotorModes.velocity)
        voltage = self.encoder_motor.set(-speed)
        self.motor.set(voltage * multiplier)
        # for motor in self.motors:
        #     motor.set(-(speed / 100))
            