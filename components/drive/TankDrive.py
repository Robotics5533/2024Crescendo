import wpilib
from components.drive.Drive import Drive


class TankDrive(Drive):
    def __init__(self, left_motors, right_motors):
        super().__init__()
        self.left_motors = left_motors
        self.right_motors = right_motors

    @staticmethod
    def calculate_direction(type: int, x: int, y: int, z: int) -> int:
        if type == 0:
            return -(x + -y + -z)
        else:
            return -(x + y + -z)
        
    def move(self, data):
        self.left_motors.set(self.calculate_direction(1, data.a, data.b, data.c))
        self.right_motors.set(self.calculate_direction(0, data.a, data.b, data.c))