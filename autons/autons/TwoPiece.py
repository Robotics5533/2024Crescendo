from autons.auton2 import Auton
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.math.algebra import linear_remap


class TwoPiece(Auton):
    def __init__(self, subsystems: SubSystems, timer, tasks = None):
        super().__init__(subsystems, timer, tasks)
        self.subsystems = subsystems
        


    def get_note(self):
        self.flip(direction = -1, duration = 0.45)
        self.flip(direction = 1, duration = 0.05, speed = 0)
        self.intake(direction = 1, duration = 0.05, speed = Auton.Speeds.intake)
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.52)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.05, brake = True)
        self.flip(direction = 1, duration = 0.5)
        self.flip(direction = -1, duration = 0.05, speed = 0)
        self.intake(speed = 0, direction = 0, duration = 0.05)
        self.drive(velocity = Vector(0, 0.9, self.subsystems.gyro.calculate(0)), duration = 0.48)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.05, brake = True)
    
    def shoot_note(self):
        self.shoot(speed = 100, direction = 1, duration = 0.33)
        self.intake(speed = Auton.Speeds.intake, direction = -1, duration = 0.35)
        self.stop()

    def move_left(self, duration: float, speed: float):
        self.drive(velocity = Vector(linear_remap(self.timer.get(), self.tasks.total_time - duration, self.tasks.total_time, 0, -speed), 0, self.subsystems.gyro.calculate(0)), duration = duration)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
    
    def move_right(self, duration: float, speed: float):
        self.move_left(duration, -speed)

    def initate(self):
        self.shoot(speed = 100, direction = 1, duration = 0.05)
        self.drive(velocity = Vector(0, -0.875, self.subsystems.gyro.calculate(0)), duration = 0.18)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.15, brake = True)
        self.intake(speed = Auton.Speeds.intake, direction = -1, duration = 0.35)
        self.stop()

        # Grab Second Note
        self.get_note()

        # Shoot second note
        self.shoot_note()
    def run(self):
        self.initate()
        
        # Taxi
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.75)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        
        self.tasks.reset()
