from math import pi
from phoenix6 import hardware, controls, configs

from components.motor.Motor5533 import MotorModes

class Talon5533:
    def __init__(self, id: int, conversion = pi * 6, mode = MotorModes.voltage):
        self.talonmotor = hardware.TalonFX(id)
        self.controller = controls.DutyCycleOut(0)
        self.mode = mode
        self.conversion = conversion
        self.set_mode(self.mode)

    def set(self, value):
        if self.mode == MotorModes.velocity:
            self.controller.slot = 0
            self.talonmotor.set_control(self.controller.with_velocity(value * (self.conversion if self.mode != MotorModes.voltage else 1)))
        else:
            self.controller.output = value * (self.conversion if self.mode != MotorModes.voltage else 1)
            self.talonmotor.set_control(self.controller)
        
    
    def set_mode(self, mode):
        if mode == MotorModes.position:
            self.controller = controls.PositionDutyCycle(0)
        elif mode == MotorModes.voltage:
            self.controller = controls.DutyCycleOut(0)
        elif mode == MotorModes.velocity:
            slot0_config = configs.Slot0Configs()
            slot0_config.k_v = 0.12
            slot0_config.k_p = 0.11
            slot0_config.k_i = 0.48
            slot0_config.k_d = 0.01
            configurator = self.talonmotor.configurator
            configurator.apply(slot0_config)
            self.controller = controls.VelocityVoltage(0)
        self.mode = mode

    def get_position(self):
        return self.talonmotor.get_position().value_as_double
    
    def set_position(self, position: float = 0):
        self.talonmotor.set_position(position)
