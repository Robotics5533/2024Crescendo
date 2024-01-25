from typing import Callable
from constants import Robot
from components.motor.talon5533 import Talon5533
from components.drive.MecanumDrive import MecanumDrive
from subsystems.drive import DriveSubSystem
from subsystems.vision import VisionSubSystem


class SubSystems:
    def __init__(self):
        self.limelight = VisionSubSystem()
        mecanum_drive = MecanumDrive(
            Talon5533(Robot.motors.front_left),
            Talon5533(Robot.motors.front_right),
            Talon5533(Robot.motors.back_left),
            Talon5533(Robot.motors.back_right),
        )
        self.drive = DriveSubSystem(mecanum_drive)

    def setup(self, func, condition: bool, requirements):
        for requirement in requirements:
                requirement.update_state(not condition)
        func()
