from typing import Callable
from phoenix6 import hardware, controls
import wpilib
from constants import Robot
from components.motor.talon5533 import Talon5533
from components.drive.MecanumDrive import MecanumDrive
from components.drive.TankDrive import TankDrive
from subsystems.climb import ClimbSubSystem
from subsystems.drive import DriveSubSystem
from subsystems.vision import VisionSubSystem


class SubSystems:
    def __init__(self):
        self.limelight = VisionSubSystem()
        self.drive = DriveSubSystem(Robot.Drive.tank)
        self.climb = ClimbSubSystem(Talon5533(Robot.motors.climb))

    def setup(self, func, condition: bool, requirements):
        for requirement in requirements:
                requirement.update_state(not condition)
        func()
