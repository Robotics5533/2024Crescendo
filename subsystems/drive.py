import commands2
from phoenix6 import hardware
from components.drive.MecanumDrive import MecanumDrive
from constants import Robot


class DriveSubSystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        back_left_motor = hardware.TalonFX(Robot.motors.back_left)
        back_right_motor = hardware.TalonFX(Robot.motors.back_right)
        front_left_motor = hardware.TalonFX(Robot.motors.front_left)
        front_right_motor = hardware.TalonFX(Robot.motors.front_right)
        self.drive = MecanumDrive(front_left_motor, front_right_motor, back_left_motor, back_right_motor)