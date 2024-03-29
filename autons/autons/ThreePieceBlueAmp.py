from autons.auton2 import Auton
from autons.autons.TwoPiece import TwoPiece
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.math.algebra import linear_remap
from wpilib import DriverStation
class ThreePieceBlueAmp(Auton):
    def __init__(self, subsystems: SubSystems, timer):
        super().__init__(subsystems, timer)
        self.subsystems = subsystems
        self.two_piece = TwoPiece(subsystems, timer, self.tasks)


    def get_note(self):
        self.flip(direction = -1, duration = 0.45)
        self.flip(direction = 1, duration = 0.05, speed = 0)
        self.intake(direction = 1, duration = 0.05, speed = Auton.Speeds.intake)
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.35)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.05, brake = True)
        self.flip(direction = 1, duration = 0.5)
        self.flip(direction = -1, duration = 0.05, speed = 0)
        self.intake(speed = 0, direction = 0, duration = 0.05)
        self.drive(velocity = Vector(0, 0.9, self.subsystems.gyro.calculate(0)), duration = 0.085)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.05, brake = True)

    def get_note_the_sequel(self):
        self.flip(direction = -1, duration = 0.45)
        self.flip(direction = 1, duration = 0.05, speed = 0)
        self.intake(direction = 1, duration = 0.05, speed = Auton.Speeds.intake)
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.55)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.05, brake = True)
        self.flip(direction = 1, duration = 0.5)
        self.flip(direction = -1, duration = 0.05, speed = 0)

        self.intake(speed = 0, direction = 0, duration = 0.05)
        self.drive(velocity = Vector(0, 0.9, self.subsystems.gyro.calculate(0)), duration = 0.085)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.05, brake = True)
        
    

    def move_left(self, duration: float, speed: float):
        self.drive(velocity = Vector(linear_remap(self.timer.get(), self.tasks.total_time - duration, self.tasks.total_time, 0, -speed), 0, self.subsystems.gyro.calculate(0)), duration = duration)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.05, brake = True)
    
    def move_right(self, duration: float, speed: float):
        self.move_left(duration, -speed)

    def run(self):
        self.two_piece.initate()

       # Grab third
        self.move_left(0.975, 0.9)
        self.get_note()
        self.move_right(1.05, 0.9)


        self.drive(velocity = Vector(0, 0.875, self.subsystems.gyro.calculate(0)), duration = 0.3)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.15, brake = True)
        #Shoot third note
        self.two_piece.shoot_note()

        # # Grab fourth
        # self.move_left(1.2, 0.9)
        # self.get_note_the_sequel()
        # self.move_right(1.1, 0.9)

        # self.drive(velocity = Vector(0, 0.9, self.subsystems.gyro.calculate(0)), duration = 0.4)
        # self.drive(velocity = Vector(0, 0, 0), duration = 0.05, brake = True)

        # self.two_piece.shoot_note()




        # Taxi
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.7)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
        
        self.tasks.reset()

