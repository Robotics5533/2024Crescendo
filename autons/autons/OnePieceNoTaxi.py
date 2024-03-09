from autons.auton2 import Auton
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.math.algebra import linear_remap


class OnePieceNoTaxi(Auton):
    def __init__(self, subsystems: SubSystems, timer):
        super().__init__(subsystems, timer)
        self.subsystems = subsystems
        


    def get_note(self):
        self.flip(direction = -1, duration = 0.3)
        self.flip(direction = 1, duration = 0.1, speed = 0)
        self.intake(direction = 1, duration = 0.9, speed = Auton.Speeds.intake)
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.35)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.5, brake = True)
        self.intake(speed = 0, direction = 0, duration = 0.2)
        self.flip(direction = 1, duration = 0.5)
        self.flip(direction = -1, duration = 0.1, speed = 0)
        self.drive(velocity = Vector(0, 0.9, self.subsystems.gyro.calculate(0)), duration = 0.425)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
    
    def shoot_note(self):
        self.shoot(speed = Auton.Speeds.shooter, direction = 1, duration = 0.7)
        self.intake(speed = Auton.Speeds.intake, direction = -1, duration = 0.45)
        self.stop()

    def move_left(self, duration: float, speed: float):
        self.drive(velocity = Vector(linear_remap(self.timer.get(), self.tasks.total_time - duration, self.tasks.total_time, 0, -speed), 0, self.subsystems.gyro.calculate(0)), duration = duration)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
    
    def move_right(self, duration: float, speed: float):
        self.move_left(duration, -speed)

    def run(self):
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.3)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        # Shoot first note
        self.shoot(speed = Auton.Speeds.shooter, direction = 1, duration = 0.9)
        self.intake(speed = Auton.Speeds.intake, direction = -1, duration = 0.45)
        self.stop()
        
        
        self.tasks.reset()
