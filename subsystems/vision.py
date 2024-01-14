import commands2
from components.drive.Drive import Drive

from components.vision.limelight import Limelight


class VisionSubSystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        
        self.limelight = Limelight()