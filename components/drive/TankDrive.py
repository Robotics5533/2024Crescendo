from components.drive.Drive import Drive


class TankDrive(Drive):
    def __init__(self, left_motors: [], right_motors: []):
        self.left_motors = left_motors
        self.right_motors = right_motors

        for i in range(len(self.left_motors)):
            self.__dict__[f"left_motor_{i + 1}"] = self.left_motors[i]
            
        for i in range(len(self.right_motors)):
            self.__dict__[f"right_motor_{i + 1}"] = self.right_motors[i]

    @staticmethod
    def calculate_direction(type: int, x: int, y: int, z: int) -> int:
        if type == 0:
            return -(x + -y + -z)
        else:
            return -(x + y + -z)
    @staticmethod
    def deadzone(*args):
        for value in args:
            if value < -0.3 or value > 0.3:
                return True
        return False
    
    
    def move(self, x: int = 0, y: int = 0, z: int = 0):  
        x *= 0.5
        y *= 0.5
        z *= 0.5
        for motor in self.left_motors:
            motor.set(self.calculate_direction(1, x, y, z))
        for motor in self.right_motors:
            motor.set(self.calculate_direction(0, x, y, z))