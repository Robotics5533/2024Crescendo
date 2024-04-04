
from subsystems.drive import DriveSubSystem
from utils.math.algebra import RotatingAverage, clamp


class GyroSubSystem:
    def __init__(self, drive_subsystem): 
        self.drive_subsystem: DriveSubSystem  = drive_subsystem
        self.wheel_error_average = RotatingAverage(10)
        # self.wheel_error_average.pass_through = True
        self.can_run = True
        
    def update_state(self, state: bool):
        self.can_run = state

    def calculate(self, target: float):
        left_motors = [self.drive_subsystem.drive.front_left_motor, self.drive_subsystem.drive.back_left_motor]
        right_motors = [self.drive_subsystem.drive.front_right_motor, self.drive_subsystem.drive.back_right_motor]
        
        err = target - (self.wheel_error_average.set_through((sum([(x.get_position()) for x in left_motors]) - sum([(x.get_position()) for x in right_motors])) / 2))
        print(err)
        return clamp((-err / 40), -0.3, 0.3)

    def run(self, speed: float):
        pass


    