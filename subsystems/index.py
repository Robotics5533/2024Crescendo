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
from subsystems.climb import ClimbSubSystem
from subsystems.climb_control import ClimbControlSubSystem
from subsystems.drive import DriveSubSystem
from subsystems.gyro import GyroSubSystem
from subsystems.intake_control import IntakeControlSubSystem
from subsystems.shooter import ShooterSubSystem
from subsystems.vision import VisionSubSystem
from subsystems.intake import IntakeSubSystem

class SubSystems:
    def __init__(self):
        self.intake_control = Talon5533(7, pi * 64, MotorModes.velocity)
        self.limelight = VisionSubSystem()
        self.encoder = wpilib.Encoder(1,0)
        self.encoder.setDistancePerPulse(1/4030)
        self.encoder.setSamplesToAverage(100)
        self.shooter = ShooterSubSystem(EncoderMotor(self.encoder, wpilib.Spark(1), MotorModes.velocity), wpilib.Spark(0))
        self.drive = DriveSubSystem(Robot.Drive.mecanum)
        self.climb = ClimbSubSystem(Talon5533(Robot.motors.climb))
        self.climb_control = ClimbControlSubSystem(wpilib.Spark(3))
        self.gyro = GyroSubSystem(navx.AHRS.create_i2c())
        self.intake = IntakeSubSystem([wpilib.Spark(2)])
        self.intake_control = IntakeControlSubSystem(self.intake_control)
        self.sub_indexes = [self.limelight, self.drive, self.climb, self.gyro, self.shooter, self.intake, self.intake_control, self.climb_control]

    def setup(self, func, condition: bool, requirements, *args):
        if not any(map(lambda x: not x.can_run, requirements)) and condition:
            func(*args)
            for requirement in requirements:
                requirement.update_state(False)
                
    def reset(self):
        for sub in self.sub_indexes:
            sub.update_state(True)
