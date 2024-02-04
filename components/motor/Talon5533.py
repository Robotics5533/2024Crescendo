from math import pi
from phoenix6 import hardware, controls, configs

class Talon5533:
    def __init__(self, id: int, conversion = pi * 6):
        self.talonmotor = hardware.TalonFX(id)
        self.controller = controls.DutyCycleOut(0)
        self.mode = 1
        self.conversion = conversion

    def set(self, value):
        self.controller.output = value * (self.conversion if self.mode == 0 else 1)
        self.talonmotor.set_control(self.controller)
    
    def set_mode(self, mode: int):
        self.controller = controls.PositionDutyCycle(0) if mode == 0 else controls.DutyCycleOut(0)
        self.mode = mode
    
    def get_position(self):
        return self.talonmotor.get_position().value_as_double
    
    def set_position(self, position: float = 0):
        self.talonmotor.set_position(position)
