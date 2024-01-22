from vision.limelight import Limelight


class VisionSubSystem(Limelight):
    def __init__(self) -> None:
        super().__init__()
        self.can_run = True
        
    def update_state(self):
        self.can_run = False