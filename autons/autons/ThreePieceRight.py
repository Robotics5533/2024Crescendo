from autons.auton2 import Auton
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.math.algebra import linear_remap
from wpilib import DriverStation
class ThreePieceRight(Auton):
    def __init__(self, subsystems: SubSystems, timer):
        super().__init__(subsystems, timer)
        self.subsystems = subsystems
    def run(self):
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.3)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
        # Shoot first note
        self.shoot(speed = Auton.Speeds.shooter, direction = 1, duration = 0.9)
        self.intake(speed = Auton.Speeds.intake, direction = -1, duration = 0.45)
        self.stop()
        # Grab Second Note
        self.get_note(0.5)
        self.drive(velocity = Vector(0, 0.9, self.subsystems.gyro.calculate(0)), duration = 0.35)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)

        # Shoot second note
        self.shoot_note()

        # Grab third
        self.move_right(1.15, 0.9)
        self.get_note(0.425, 0.45)
        self.move_left(1, 0.9)


        self.drive(velocity = Vector(0, 0.9, self.subsystems.gyro.calculate(0)), duration = 0.45)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.6, brake = True)


        #Shoot third note
        self.shoot_note()


       # Taxi
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.5)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
        
        self.tasks.reset()
