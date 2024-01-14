import ctre
from typing import Union

import wpilib

from components.drive.Drive import Drive

class MecanumDrive(Drive):
    def __init__(self, front_left: Union[ctre.WPI_TalonSRX, wpilib.PWMSparkMax], front_right: Union[ctre.WPI_TalonSRX, wpilib.PWMSparkMax], back_right: Union[ctre.WPI_TalonSRX, wpilib.PWMSparkMax], back_left: Union[ctre.WPI_TalonSRX, wpilib.PWMSparkMax]):
        # ctre._ctre.ControlMode, float, https://robotpy.readthedocs.io/projects/ctre/en/stable/ctre/TalonSRX.html
        super().__init__()
        self.front_left_motor = front_left
        self.front_right_motor = front_right
        self.back_left_motor = back_left
        self.back_right_motor = back_right
        self.back_left_motor.setInverted(True)
        self.back_right_motor.setInverted(True)
        
    
    """
    x -> Give the horizontal data for the bot
    y -> Give the vertical data for the bot
    z -> Give the rotational data for the bot
    """
    def move(self, x: int, y: int, z: int):
        t = x
        x = y
        y = t
        x *= self.speed
        y *= self.speed
        z *= self.speed
        self.front_left_motor.set((-x + y + z)) 
        self.front_right_motor.set(x + y + z)
        self.back_left_motor.set(x + y + -z ) 
        self.back_right_motor.set((-x + y + -z))