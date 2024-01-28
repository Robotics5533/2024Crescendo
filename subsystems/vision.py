from components.vision.Limelight import Limelight
from utils.math.Vector import Vector


class VisionSubSystem(Limelight):
    def __init__(self) -> None:
        super().__init__()
        self.can_run = True
        
    def correct_error(self, drive_subsystem):
        offset = self.getError()
        drive_subsystem.drive.set_speed(50)
        drive_subsystem.drive.move(Vector(offset[0], offset[1], offset[2]))
        
    def update_state(self, state: bool):
        self.can_run = state