from autons.auton2 import Auton
from autons.autons.TwoPiece import TwoPiece
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.math.algebra import linear_remap


class ThreePieceFast(Auton):
    def __init__(self, subsystems: SubSystems, timer, tasks = None):
        super().__init__(subsystems, timer, tasks)
        self.subsystems = subsystems
        self.two_piece = TwoPiece(subsystems, timer, self.tasks)
        


    
    def shoot_note(self):
        self.shoot(speed = Auton.Speeds.shooter, direction = 1, duration = 0.7)
        self.intake(speed = Auton.Speeds.intake, direction = -1, duration = 0.45)
        self.stop()

    def move_left(self, duration: float, speed: float):
        self.drive(velocity = Vector(linear_remap(self.timer.get(), self.tasks.total_time - duration, self.tasks.total_time, 0, -speed), 0, self.subsystems.gyro.calculate(0)), duration = duration)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
    
    def move_right(self, duration: float, speed: float):
        self.move_left(duration, -speed)

    
    def get_note(self):
        self.flip(direction = -1, duration = 0.45)
        self.flip(direction = 1, duration = 0.05, speed = 0)
        self.intake(direction = 1, duration = 0.05, speed = Auton.Speeds.intake)
        self.drive(velocity = Vector(0, -0.9, 0), duration = 0.6)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.05, brake = True)
        self.flip(direction = 1, duration = 0.5)
        self.flip(direction = -1, duration = 0.05, speed = 0)
        self.intake(speed = 0, direction = 0, duration = 0.05)
        self.drive(velocity = Vector(0, 0.9, 0), duration = 0.45)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.05, brake = True)

    def run(self):
        self.two_piece.initate()

        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.2)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.15, brake = True)


        self.drive(velocity = Vector(0, 0, 0.9), duration = 0.25)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.15, brake = True)

        self.get_note()

        self.drive(velocity = Vector(0, 0, -0.9), duration = 0.18)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.15, brake = True)
        
        # Shoot Third Note
        self.two_piece.shoot_note()

        self.drive(velocity = Vector(0, -0.9, 0), duration = 0.6)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.05, brake = True)

        




        # Taxi
        # self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.75)
        # self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        
        self.tasks.reset()
