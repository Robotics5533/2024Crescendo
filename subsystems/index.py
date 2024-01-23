from constants import Robot
from typing import Union
from components.motor.talon5533 import Talon5533
from subsystems.drive import DriveSubSystem
from subsystems.vision import VisionSubSystem


class SubSystems:
    def __init__(self):
        self.limelight = VisionSubSystem()
        self.drive = DriveSubSystem(
            Talon5533(Robot.motors.front_left),
            Talon5533(Robot.motors.front_right),
            Talon5533(Robot.motors.back_left),
            Talon5533(Robot.motors.back_right),
        )

    def setup(self, func, condition, requirements):
        for requirement in requirements:
                requirement.update_state(condition)

        func()
