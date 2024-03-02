from autons.auton2 import Auton
from subsystems.index import SubSystems
from utils.math.Vector import Vector


class FourPiece2(Auton):
    def __init__(self, subsystems: SubSystems, timer):
        super().__init__(subsystems, timer)
        self.subsystems = subsystems

    def run(self):
        
        # Shoot first note
        self.shoot(speed = Auton.Speeds.shooter, direction = 1, duration = 0.5)
        self.intake(speed = Auton.Speeds.intake, direction = -1, duration = 0.45)
        self.stop()

        # Grab Second Note
        self.flip(direction = -1, duration = 0.3)
        self.flip(direction = 1, duration = 0.1, speed = 0)
        self.intake(direction = 1, duration = 0.7, speed = Auton.Speeds.intake)
        self.drive(velocity = Vector(0, -0.7, self.subsystems.gyro.calculate(0)), duration = 0.5)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
        self.intake(speed = 0, direction = 0, duration = 0.2)
        self.flip(direction = 1, duration = 0.5)
        self.flip(direction = -1, duration = 0.1, speed = 0)
        self.drive(velocity = Vector(0, 0.9, self.subsystems.gyro.calculate(0)), duration = 0.4)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)

        # Shoot second note
        self.shoot(speed = Auton.Speeds.shooter, direction = 1, duration = 0.5)
        self.intake(speed = Auton.Speeds.intake, direction = -1, duration = 0.45)
        self.stop()

        # Rotate to third piece
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(35)), duration = 0.3)

        # Drive back to speaker
        self.flip(direction = -1, duration = 0.3)
        self.flip(direction = 1, duration = 0.1, speed = 0)
        self.intake(direction = 1, duration = 0.7, speed = Auton.Speeds.intake)
        self.drive(velocity = Vector(0, -0.7, self.subsystems.gyro.calculate(35)), duration = 0.6)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        
        self.intake(speed = 0, direction = 0, duration = 0.2)
        self.flip(direction = 1, duration = 0.5)
        self.flip(direction = -1, duration = 0.1, speed = 0)
        self.drive(velocity = Vector(0, 0.9, self.subsystems.gyro.calculate(35)), duration = 0.4)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        

        # Shoot Third note
        self.shoot(speed = Auton.Speeds.shooter, direction = 1, duration = 0.5)
        self.intake(speed = Auton.Speeds.intake, direction = -1, duration = 0.45)
        self.stop()
        # self.rotate(angle = 180)
        
        self.tasks.reset()
