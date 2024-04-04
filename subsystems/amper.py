from phoenix6 import hardware, controls
from typing import Union
import wpilib
from wpimath.controller import PIDController
from components.motor.Motor5533 import MotorModes
from utils.math.algebra import almost_equal, clamp, linear_remap

class Amper:
    up = 0
    down = 1

class Positions:
    up = 5.2
    down = 0

class AmperSubSystem:
    def __init__(self, position_motor):  
        
        self.position_motor = position_motor
        self.spinny_motor = wpilib.PWMSparkMax(3)
        self.can_run = True
        self.state = Amper.down
        self.pid = PIDController(0.03, 0.0015, 0.0001  * 3)
        
        
    def update_state(self, state: bool):
        self.can_run = state
    
        
    def run(self, speed: float, state):
        self.state = state

        if self.state == Amper.up:
                self.position_motor.set_mode(MotorModes.voltage)
                self.position_motor.set(self.pid.calculate(self.position_motor.get_position(), Positions.up) * 1.1)
                if almost_equal(self.position_motor.get_position(), Positions.up, 0.1):
                     self.spinny_motor.set(-0.35)
        elif self.state == Amper.down:
                self.pid.reset()
                self.spinny_motor.set(0)
                if not almost_equal(self.position_motor.get_position(), Positions.down, 0.9):
                    self.position_motor.set_mode(MotorModes.voltage)
                    self.position_motor.set(-0.04)
                else:
                    self.position_motor.set_mode(MotorModes.voltage)
                    self.position_motor.set(0)
            