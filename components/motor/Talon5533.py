from math import pi
from phoenix6 import hardware, controls, configs
from utils.math.algebra import linear_remap
from components.motor.Motor5533 import MotorModes

class Talon5533:
    def __init__(self, id: int, conversion = pi * 6, mode = MotorModes.voltage, **kwargs):
        self.talonmotor = hardware.TalonFX(id)
        self.controller = controls.DutyCycleOut(0)
        self.mode = mode
        self.conversion = conversion
        self.set_mode(self.mode, **kwargs)
        self.target = 0
        self.zero_position = 0
    def set(self, value):
        if self.mode == MotorModes.velocity:
            self.controller.slot = 0
            self.talonmotor.set_control(self.controller.with_velocity(value * self.conversion))
        elif self.mode == MotorModes.position:
            self.target = value
            #print(value, "position")
        else:
            self.set_voltage(value)
    
    def set_voltage(self,value):
        self.controller.output = value
        self.talonmotor.set_control(self.controller)

    
    def set_mode(self, mode, **kwargs):
        if mode == MotorModes.position:
           
            self.controller = controls.DutyCycleOut(0)

            self.position_slowdown_threshhold = kwargs["position_slowdown_threshhold"] if "position_slowdown_threshhold" in kwargs else 5
            self.max_position_correction_voltage = kwargs["max_position_correction_voltage"] if "max_position_correction_voltage" in kwargs else 1
            self.position_correction_bias = kwargs["position_correction_bias"] if "position_correction_bias" in kwargs else 0
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
        return self.talonmotor.get_position().value_as_double - self.zero_position
    
    def set_position(self, position: float = 0):
        # c = configs.TalonFXConfiguration
        # configs.cancoder_configs.CANcoderConfiguration()
        # configurator = self.talonmotor.configurator
        # configurator.set_position(position) 
        # configurator.set_position
        self.zero_position =  self.get_position() - position

    def process(self, delta):
        #how far from target, use answer with math function that reverses positive/negative
        #x is error, y is correction
        error = self.get_position() - self.target
        voltage = self.get_error_voltage(error)
        self.set_voltage(voltage)
        #print(error, "error")
        #print(self.get_position(), "grabbed position")
        pass

    def get_error_voltage(self, error):
        if abs(error) >= self.position_slowdown_threshhold:
            return -(error / abs(error) )* self.max_position_correction_voltage
        bias = self.position_correction_bias
        if error >= 0:
            bias = -bias
        return bias + (linear_remap(error,+self.position_slowdown_threshhold, -self.position_slowdown_threshhold, -self.max_position_correction_voltage, self.max_position_correction_voltage))