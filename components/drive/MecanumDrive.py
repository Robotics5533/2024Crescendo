from phoenix5 import hardware, controls
from typing import Union

import wpilib

from components.drive.Drive import Drive

class MecanumDrive(Drive):
    def __init__(self,
                 front_left: Union[hardware.TalonFX,wpilib.PWMSparkMax],
                 front_right: Union[hardware.TalonFX,wpilib.PWMSparkMax],
                 back_right: Union[hardware.TalonFX,wpilib.PWMSparkMax],
                 back_left: Union[hardware.TalonFX, wpilib.PWMSparkMax]):
# hardware._ctre.ControlMode, float, https://robotpy.readthedocs.io/projects/ctre/en/stable/ctre/TalonSRX.html
        super().__init__()
        #the talonsrx modules are controled by the phoenix control modules
        #different control modules set the output for the motors through different methods
        self.duty_output_front_left  = controls.DutyCycleOut(0)
        self.duty_output_front_right = controls.DutyCycleOut(0)
        self.duty_output_back_right  = controls.DutyCycleOut(0)
        self.duty_output_back_left   = controls.DutyCycleOut(0)

        
        self.front_left_motor  = front_left
        self.front_right_motor = front_right
        self.back_left_motor   = back_left
        self.back_right_motor  = back_right

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
        
        self.duty_output_front_left.output = (-x + y + z)        
        self.front_left_motor.set_control(self.duty_output_front_left)
        
        self.duty_output_front_right.output = (x + y + z)        
        self.front_right_motor.set_control(self.duty_output_front_right)
        
        self.duty_output_back_left.output = (x + y + -z)         
        self.back_left_motor.set_control(self.duty_output_back_left)
        
        self.duty_output_back_right.output = (-x + y + -z)       
        self.back_right_motor.set_control(self.duty_output_back_left)
        
