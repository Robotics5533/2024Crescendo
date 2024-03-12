from autons.auton2 import Auton
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.math.algebra import linear_remap


class TwoPiece(Auton):
    def __init__(self, subsystems: SubSystems, timer, tasks = None):
        super().__init__(subsystems, timer, tasks)
        self.subsystems = subsystems

    def initate(self):
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.17)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        # Shoot first note
        self.shoot(speed = Auton.Speeds.shooter, direction = 1, duration = 0.9)
        self.intake(speed = Auton.Speeds.intake, direction = -1, duration = 0.45)
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
