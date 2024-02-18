from math import pi
from phoenix6 import hardware, controls, configs

from components.motor.Motor5533 import MotorModes

class Talon5533:
    def __init__(self, id: int, conversion = pi * 6, mode = MotorModes.voltage, **kwargs):
        self.talonmotor = hardware.TalonFX(id)
        self.controller = controls.DutyCycleOut(0)
        self.mode = mode
        self.conversion = conversion
        self.set_mode(self.mode, **kwargs)

    def set(self, value):
        if self.mode == MotorModes.velocity:
            self.controller.slot = 0
            self.talonmotor.set_control(self.controller.with_velocity(value * self.conversion))
        elif self.mode == MotorModes.position:
            self.controller.slot = 0
            self.talonmotor.set_control(self.controller.with_position(value / self.conversion))
        else:
            self.controller.output = value
            self.talonmotor.set_control(self.controller)
        
    
    def set_mode(self, mode, **kwargs):
        if mode == MotorModes.position:
           
            self.controller = controls.PositionVoltage(0)
            slot0_config = configs.Slot0Configs()
            # slot0_config.k_v = kwargs["kv"] if "kv" in kwargs else 0
            slot0_config.k_p = kwargs["kp"] if "kp" in kwargs else 16
            slot0_config.k_i = kwargs["ki"] if "ki" in kwargs else 0
            slot0_config.k_d = kwargs["kd"] if "kd" in kwargs else 0.23
            configurator = self.talonmotor.configurator
            configurator.apply(slot0_config)
           
            
        elif mode == MotorModes.voltage:
            
            self.controller = controls.DutyCycleOut(0)
            
        elif mode == MotorModes.velocity:
            
            slot0_config = configs.Slot0Configs()
            slot0_config.k_v = kwargs["kv"] if "kv" in kwargs else 2.7668
            slot0_config.k_p = kwargs["kp"] if "kp" in kwargs else 0.1475
            # slot0_config.k_i = kwargs["ki"] if "ki" in kwargs else 0
            slot0_config.k_d = kwargs["kd"] if "kd" in kwargs else 0
            configurator = self.talonmotor.configurator
            configurator.apply(slot0_config)
            self.controller = controls.VelocityVoltage(0) 
        self.mode = mode

    def get_position(self):
        return self.talonmotor.get_position().value_as_double
    
    def set_position(self, position: float = 0):
        # c = configs.TalonFXConfiguration
        # configs.cancoder_configs.CANcoderConfiguration()
        # configurator = self.talonmotor.configurator
        # configurator.set_position(position) 
        # configurator.set_position
        pass