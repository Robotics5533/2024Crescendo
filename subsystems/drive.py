from components.drive.MecanumDrive import MecanumDrive
from utils.math.Vector import Vector


class DriveSubSystem():
    def __init__(self, mecanum_drive: MecanumDrive) -> None:
        super().__init__()
        self.can_run = True
        self.drive = mecanum_drive
        

    def update_state(self, state: bool):
        self.can_run = state

    def move(self, data: Vector):
        if self.can_run:
            self.drive.move(data)