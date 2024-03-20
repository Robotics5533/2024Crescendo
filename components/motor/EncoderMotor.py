from components.motor.Motor5533 import MotorModes
import wpilib
from wpimath.controller import PIDController

class EncoderMotor:        
    def __init__(self, encoder: wpilib.Encoder, motor, mode = MotorModes.velocity):
        self.encoder : wpilib.Encoder = encoder 
        self.motor = motor
        self.mode = mode

        self.velocity_controller = PIDController(1/16,1/32,0.00005)
            

    def get_velocity(self)->float:
        return self.encoder.getRate()
        

    def set(self, value):
        if self.mode == MotorModes.voltage:
            self.motor.set(value)
        elif self.mode == MotorModes.velocity:
            print("setting based on velocity")
            self.motor.set(self.velocity_controller.calculate(-self.get_velocity(),value))
        

    def set_mode(self, mode: int):
        self.mode = mode
    
    def get_position(self) -> float:
        return self.encoder.getDistance()
    
    
    # def set_position(self, position: float = 0):
    #     curr_position = self.get_position()
    #     self.zero = position - curr_position

