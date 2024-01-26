import wpilib
from components.drive.Drive import Drive


class TankDrive(Drive):
    """
    left_motors -> List of left motor controllers
    right_motors -> List of right motor controllers
    """
    def __init__(self, left_motors, right_motors):
        super().__init__()
        self.left_motors = left_motors
        self.right_motors = right_motors
    """
    Using x, y, and z calculate the correct direction based on if it's the left or right motors
    """
    @staticmethod
    def calculate_direction(type: int, x: int, y: int, z: int) -> int:
        if type == 0:
            return -(x + -y + -z)
        else:
            return -(x + y + -z)
    """
    x -> Give the horizontal data for the bot
    y -> Give the vertical data for the bot
    z -> Give the rotational data for the bot
    """
    def move(self, data):
        # data = data.map(lambda x: x * self.speed)
        self.left_motors.set(self.calculate_direction(1, data.a, data.b, data.c))
        self.right_motors.set(self.calculate_direction(0, data.a, data.b, data.c))
        # for motor in self.left_motors:
        #     motor.set(self.calculate_direction(1, x, y, z))
        # for motor in self.right_motors:
        #     motor.set(self.calculate_direction(0, x, y, z))