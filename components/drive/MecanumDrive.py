from typing import Union
import wpilib
from components.drive.Drive import Drive
from phoenix6 import hardware, controls
class MecanumDrive(Drive):
    def __init__(self,front_left: Union[hardware.TalonFX,wpilib.PWMSparkMax],
                 front_right: Union[hardware.TalonFX,wpilib.PWMSparkMax],
                 back_right: Union[hardware.TalonFX,wpilib.PWMSparkMax],
                 back_left: Union[hardware.TalonFX, wpilib.PWMSparkMax]):
       
        super().__init__()
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

        x *= self.speed
        y *= self.speed
        z *= self.speed
        
        self.duty_output_front_left.output = (y-z-x)        
        self.front_left_motor.set_control(self.duty_output_front_left)
        self.duty_output_front_right.output = (y+z+x)        
        self.front_right_motor.set_control(self.duty_output_front_right)

        self.duty_output_back_left.output = (y-z+x)         
        self.back_left_motor.set_control(self.duty_output_back_left)
        self.duty_output_back_right.output = (y+z-x)   
        self.back_right_motor.set_control(self.duty_output_back_right)