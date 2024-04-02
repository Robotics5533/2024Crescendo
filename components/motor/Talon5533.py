from math import pi
from phoenix6 import hardware, controls, configs
from utils.math.algebra import linear_remap,clamp,RotatingAverage,almost_equal
from components.motor.Motor5533 import MotorModes
from wpimath.controller import PIDController
class Talon5533:
    def __init__(self, id: int, conversion = pi * 6, mode = MotorModes.voltage, **kwargs):
        self.talonmotor = hardware.TalonFX(id)
        self.controller = controls.DutyCycleOut(0)
        self.mode = mode
        self.conversion = conversion
        self.set_mode(self.mode, **kwargs)
        self.zero_position = 0
        
        speed = 0.1

        kp = 0.2*speed

        self.position_controller = PIDController(kp, 0.05, 0)
        self.position_controller.setIZone(2)

        self.lazy_mode: bool = False
        self.rotating_average = RotatingAverage(1)
        self.rotating_input_signal = RotatingAverage(1)

    def set(self, value):
        if self.mode == MotorModes.velocity:
            self.controller.slot = 0
            self.talonmotor.set_control(self.controller.with_velocity(value * self.conversion))
        elif self.mode == MotorModes.position:

            if almost_equal(self.get_position(),value,1):
                self.lazy_mode = False
            else:
                self.lazy_mode = True
            
            self.lazy_mode = False
            print(self.get_position() - value)
            self.set_voltage(
                clamp(
                        self.position_controller.calculate(self.get_position(), value)
                        ,-0.6
                        ,0.6
                        )
                )
        elif self.mode == MotorModes.static_brake:
            pass #no response to motion in this mode, see set_mode static_break
        else:
            self.set_voltage(value)

    def set_voltage(self,value):
        
        if self.lazy_mode:
            self.controller.output = self.rotating_average.set_through(value)
        else:
            self.controller.output = value
        self.talonmotor.set_control(self.controller)

    def set_mode(self, mode, **kwargs):
        if mode == MotorModes.position:
            self.lazy_mode = True
            self.controller = controls.DutyCycleOut(0)
        elif mode == MotorModes.voltage:
            self.controller = controls.DutyCycleOut(0)
        elif mode == MotorModes.velocity:
            slot0_config = configs.Slot0Configs()
            slot0_config.k_v = kwargs["kv"] if "kv" in kwargs else 2.7668
            slot0_config.k_p = kwargs["kp"] if "kp" in kwargs else 0.1475
            # slot0_config.k_i = kwarg0s["ki"] if "ki" in kwargs else 0
            slot0_config.k_d = kwargs["kd"] if "kd" in kwargs else 0
            configurator = self.talonmotor.configurator
            configurator.apply(slot0_config)
            self.controller = controls.VelocityVoltage(0) 
        elif mode == MotorModes.static_brake:
            self.talonmotor.set_control(controls.StaticBrake())
        else:
            self.lazy_mode = False
        self.mode = mode

    def get_position(self):
        return self.rotating_input_signal.set_through(
                            (self.talonmotor.get_position().value_as_double - self.zero_position)
                        )
    
    def set_position(self, position: float = 0):
        self.zero_position = self.talonmotor.get_position().value_as_double - position