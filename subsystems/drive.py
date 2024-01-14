import wpilib
import commands2
from components.drive.MecanumDrive import MecanumDrive

class DriveSubSystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        self.drive = MecanumDrive(1, 2, 3, 4)