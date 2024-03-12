from autons.auton2 import Auton
from autons.autons.TwoPiece import TwoPiece
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.math.algebra import linear_remap
from wpilib import DriverStation
class ThreePieceRightUnstable(Auton):
    def __init__(self, subsystems: SubSystems, timer, tasks = None):
        super().__init__(subsystems, timer, tasks)
        self.subsystems = subsystems
        self.two_piece = TwoPiece(subsystems, timer, self.tasks)

    def run(self):
        self.two_piece.initate()

       # Grab third
        self.move_right(1.15, 0.9)
        self.get_note(0.425, 0.5)
        self.move_left(1.15, 0.9)


        self.drive(velocity = Vector(0, 0.9, self.subsystems.gyro.calculate(0)), duration = 0.45)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.6, brake = True)


        #Shoot third note
        self.shoot_note()


       # Taxi
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.7)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
        
        self.tasks.reset()

