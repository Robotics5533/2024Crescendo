from drive.MecanumDrive import MecanumDrive
from utils.math.Vector import Vector


class DriveSubSystem(MecanumDrive):
    def __init__(self) -> None:
        super().__init__()
        self.can_run = True
        

    def update_state(self, state: bool):
        self.can_run = state

    def move(self, data: Vector):
        if self.can_run:
            super().move(data)