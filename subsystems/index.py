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
from subsystems.climb import ClimbSubSystem
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
        self.shooter = ShooterSubSystem([wpilib.Spark(0), wpilib.Spark(1)])
        self.drive = DriveSubSystem(Robot.Drive.mecanum)
        self.climb = ClimbSubSystem(Talon5533(Robot.motors.climb))
        self.gyro = GyroSubSystem(navx.AHRS.create_i2c())
        self.intake = IntakeSubSystem([wpilib.Spark(2)])
        self.intake_control = IntakeControlSubSystem(self.intake_control)
        self.sub_indexes = [self.limelight, self.drive, self.climb, self.gyro, self.shooter, self.intake, self.intake_control]

    def setup(self, func, condition: bool, requirements, *args):
        if not any(map(lambda x: not x.can_run, requirements)) and condition:
            func(*args)
            for requirement in requirements:
                requirement.update_state(False)
                
    def reset(self):
        for sub in self.sub_indexes:
            sub.update_state(True)
