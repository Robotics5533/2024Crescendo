from phoenix6 import hardware, controls
from typing import Union
import wpilib

from components.motor.Motor5533 import MotorModes
from utils.math.algebra import almost_equal, linear_remap

class Amper:
    up = 0
    down = 1

class Positions:
    up = 0
    down = 0

class AmperSubSystem:
    def __init__(self, position_motor):  
        
        self.position_motor = position_motor
        self.can_run = True
        self.state = Amper.down
        
        
    def update_state(self, state: bool):
        self.can_run = state
    
        
    def run(self, speed: float, state):
        self.state = state
        if self.state == Amper.up:
            if self.position_motor.get_position() >= Positions.up:
                self.position_motor.set_mode(MotorModes.static_break)
                self.position_motor.set(0)
            else: 
                self.position_motor.set(0.2)
        elif self.state == Amper.down:
            if almost_equal(self.position_motor.get_position(), Positions.down):
                self.position_motor.set_mode(MotorModes.static_break)
                self.position_motor.set(0)
            else: 
                self.position_motor.set(-0.2)
            