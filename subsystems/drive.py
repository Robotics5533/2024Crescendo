from components.drive.MecanumDrive import MecanumDrive
from utils.math.Vector import Vector


class DriveSubSystem():
    def __init__(self, drive) -> None:
        super().__init__()
        self.can_run = True
        self.mecanum = drive
        

    def update_state(self, state: bool):
        self.can_run = state

    def move(self, data: Vector):
        if self.can_run:
            self.drive.move(data)