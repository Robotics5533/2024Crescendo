from drive.MecanumDrive import MecanumDrive


class DriveSubSystem(MecanumDrive):
    def __init__(self) -> None:
        super().__init__()
        self.can_run = True
        

    def update_state(self):
        self.can_run = False