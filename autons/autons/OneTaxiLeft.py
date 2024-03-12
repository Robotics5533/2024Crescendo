from autons.auton2 import Auton
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.math.algebra import linear_remap


class OneTaxiLeft(Auton):
    def __init__(self, subsystems: SubSystems, timer):
        super().__init__(subsystems, timer)
        self.subsystems = subsystems
        
    def run(self):
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.3)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        # Shoot first note
        self.shoot(speed = Auton.Speeds.shooter, direction = 1, duration = 0.9)
        self.intake(speed = Auton.Speeds.intake, direction = -1, duration = 0.45)
        self.stop()
        
        self.drive(velocity = Vector(0, 0, 0.5), duration = 0.3)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        # Taxi
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 1)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        
        self.tasks.reset()
