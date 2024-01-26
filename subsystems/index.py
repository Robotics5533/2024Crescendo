from typing import Callable

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
        # mecanum_drive = MecanumDrive(
        #     Talon5533(Robot.motors.front_left),
        #     Talon5533(Robot.motors.front_right),
        #     Talon5533(Robot.motors.back_left),
        #     Talon5533(Robot.motors.back_right),
        # )
        tank =   self.drive = TankDrive(wpilib.MotorControllerGroup(wpilib.PWMSparkMax(0), wpilib.PWMSparkMax(1)), wpilib.MotorControllerGroup(wpilib.PWMSparkMax(2), wpilib.PWMSparkMax(3)))
        self.drive = DriveSubSystem(tank)
        self.climb = ClimbSubSystem()

    def setup(self, func, condition: bool, requirements):
        for requirement in requirements:
                requirement.update_state(not condition)
        func()
