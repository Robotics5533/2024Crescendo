import ctre
import wpilib
import commands2
from components.drive.MecanumDrive import MecanumDrive
from constants import Robot


class DriveSubSystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        self.drive = MecanumDrive(ctre.WPI_TalonSRX(Robot.motors.front_left), ctre.WPI_TalonSRX(
            Robot.motors.front_right), ctre.WPI_TalonSRX(Robot.motors.back_left), ctre.WPI_TalonSRX(Robot.motors.back_right))
