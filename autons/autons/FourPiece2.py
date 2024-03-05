from autons.auton2 import Auton
from subsystems.index import SubSystems
from utils.math.Vector import Vector


class FourPiece2(Auton):
    def __init__(self, subsystems: SubSystems, timer):
        super().__init__(subsystems, timer)
        self.subsystems = subsystems


    def get_note(self):
        self.flip(direction = -1, duration = 0.3)
        self.flip(direction = 1, duration = 0.1, speed = 0)
        self.intake(direction = 1, duration = 0.9, speed = Auton.Speeds.intake)
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.4)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
        self.intake(speed = 0, direction = 0, duration = 0.2)
        self.flip(direction = 1, duration = 0.5)
        self.flip(direction = -1, duration = 0.1, speed = 0)
        self.drive(velocity = Vector(0, 0.9, self.subsystems.gyro.calculate(0)), duration = 0.4)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
    
    def shoot_note(self):
        self.shoot(speed = Auton.Speeds.shooter, direction = 1, duration = 0.7)
        self.intake(speed = Auton.Speeds.intake, direction = -1, duration = 0.45)
        self.stop()

    def run(self):
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.25)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        # Shoot first note
        self.shoot(speed = Auton.Speeds.shooter, direction = 1, duration = 0.9)
        self.intake(speed = Auton.Speeds.intake, direction = -1, duration = 0.45)
        self.stop()
        # Grab Second Note
        self.get_note()

        # Shoot second note
        self.shoot_note()

        # Grab third
        self.drive(velocity = Vector(-0.9, 0, self.subsystems.gyro.calculate(0)), duration = 1.4)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
        self.get_note()
        self.drive(velocity = Vector(0.9, 0, self.subsystems.gyro.calculate(0)), duration = 1.1)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)

        #Shoot third note
        self.shoot_note()

        # Grab fourth note
        self.drive(velocity = Vector(0.9, 0, self.subsystems.gyro.calculate(0)), duration = 0.9)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
        self.get_note()
        self.drive(velocity = Vector(-0.9, 0, self.subsystems.gyro.calculate(0)), duration = 0.9)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)

        # Shoot Fourth note
        self.shoot_note()

        # self.rotate(angle = 180)
        
        self.tasks.reset()
