from math import pi
from typing import Callable
import navx
from phoenix6 import hardware, controls
import wpilib
from constants import Robot
from components.motor.Talon5533 import Talon5533
from components.drive.MecanumDrive import MecanumDrive
from components.drive.TankDrive import TankDrive
from components.motor.Motor5533 import MotorModes
from components.motor.EncoderMotor import EncoderMotor
from subsystems.amper import AmperSubSystem
from subsystems.climb import ClimbSubSystem
from subsystems.climb_control import ClimbControlSubSystem
from subsystems.drive import DriveSubSystem
from subsystems.gyro import GyroSubSystem
from subsystems.intake_control import IntakeControlSubSystem
from subsystems.shooter import ShooterSubSystem
from subsystems.vision import VisionSubSystem
from subsystems.intake import IntakeSubSystem
from utils.math.algebra import RotatingAverage

class SubSystems:
    def __init__(self):
        self.intake_control = Talon5533(7, pi * 64, MotorModes.velocity)
        self.intake_follow_motor = Talon5533(8, pi * 64, MotorModes.velocity)
        self.intake_control.rotating_input_signal.pass_through = True
        
        self.limelight = VisionSubSystem()
        self.shooter = ShooterSubSystem([wpilib.Spark(1), wpilib.Spark(0)])
        self.drive = DriveSubSystem(Robot.Drive.mecanum)
        
        #the drive motors are tuned to not average their input signals,
        #so we need to turn off their averaging
        for m in self.drive.drive.motors:
            m.rotating_input_signal.pass_through = True

        self.climb = ClimbSubSystem(Talon5533(Robot.motors.climb, pi * 64, MotorModes.static_brake))
        self.gyro = GyroSubSystem(self.drive)
        self.intake = IntakeSubSystem([wpilib.Spark(2)])
        self.intake_control = IntakeControlSubSystem(self.intake_control,self.intake_follow_motor)
        self.amper = AmperSubSystem(Talon5533(9, pi * 64, MotorModes.voltage))
        self.sub_indexes = [self.limelight, self.drive, self.climb, self.gyro, self.shooter, self.intake, self.intake_control, self.amper]

    def setup(self, func, condition: bool, requirements, *args):
        if not any(map(lambda x: not x.can_run, requirements)) and condition:
            func(*args)
            for requirement in requirements:
                requirement.update_state(False)
                
    def reset(self):
        for sub in self.sub_indexes:
            sub.update_state(True)
