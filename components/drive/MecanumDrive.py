import ctre
from typing import Union

import wpilib

from components.drive.Drive import Drive

class MecanumDrive:
    def __init__(self, front_left: Union[ctre.WPI_TalonSRX, wpilib.PWMSparkMax], front_right: Union[ctre.WPI_TalonSRX, wpilib.PWMSparkMax], back_right: Union[ctre.WPI_TalonSRX, wpilib.PWMSparkMax], back_left: Union[ctre.WPI_TalonSRX, wpilib.PWMSparkMax]):
        # ctre._ctre.ControlMode, float, https://robotpy.readthedocs.io/projects/ctre/en/stable/ctre/TalonSRX.html
        self.front_left_motor = front_left
        self.front_right_motor = front_right
        self.back_left_motor = back_left
        self.back_right_motor = back_right
        self.back_left_motor.setInverted(True)
        self.back_right_motor.setInverted(True)
        
    
    """
    *args -> Do the math for a deadzone with any amount of args as possible
    """
    @staticmethod
    def deadzone(*args):
        for value in args:
            if value < -0.3 or value > 0.3:
                return True
        return False
    
    """
    x -> Give the horizontal data for the bot
    y -> Give the vertical data for the bot
    z -> Give the rotational data for the bot
    """
    def move(self, x: int, y: int, z: int):
        t = x
        x = y
        y = t
        x *= 0.1
        y *= 0.1
        z *= 0.1
        self.front_left_motor.set((-x + y + z)) 
        self.front_right_motor.set(x + y + z)
        self.back_left_motor.set(x + y + -z ) 
        self.back_right_motor.set((-x + y + -z))