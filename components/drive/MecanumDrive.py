import ctre

from components.drive.Drive import Drive

class MecanumDrive:
    """
    top_left -> Top left Motor on the bot
    top_right -> Top right Motor on the bot
    bottom_left -> Bottom left Motor on the bot
    bottom_right -> Bottom right Motor on the bot
    """
    def __init__(self, top_left: int, top_right: int, bottom_left: int, bottom_right: int):
        self.top_left_motor = ctre.WPI_TalonSRX(top_left)
        self.top_right_motor = ctre.WPI_TalonSRX(top_right)
        self.bottom_left_motor = ctre.WPI_TalonSRX(bottom_left)
        self.bottom_right_motor = ctre.WPI_TalonSRX(bottom_right)
    
    """
    *args -> Do the math for a deadzone with any amount of args as possible
    """
    @staticmethod
    def deadzone(*args):
        for value in args:
            if value < -0.3 or value > 0.3:
                return True
        return False
    
    """
    x -> Give the horizontal data for the bot
    y -> Give the vertical data for the bot
    z -> Give the rotational data for the bot
    """
    def move(self, x: int, y: int, z: int):
        x *= 0.5
        y *= 0.5
        z *= 0.5
        self.top_left_motor.set(-(-x + y + -z)) 
        self.top_right_motor.set(x + y + z)
        self.bottom_left_motor.set(-x + y + z ) 
        self.bottom_right_motor.set(-(x + y + -z))