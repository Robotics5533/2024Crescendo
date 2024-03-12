from autons.auton2 import Auton
from autons.autons.OnePieceNoTaxi import OnePieceNoTaxi
from autons.autons.TwoPiece import TwoPiece
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.math.algebra import linear_remap
from wpilib import DriverStation
class TwoPieceRight(Auton):
    def __init__(self, subsystems: SubSystems, timer, tasks = None):
        super().__init__(subsystems, timer, tasks)
        self.subsystems = subsystems
        self.one_piece = OnePieceNoTaxi(subsystems, timer, self.tasks)

    def run(self):
        self.one_piece.initiate()
        
        
        self.drive(velocity = Vector(0, 0, -0.15), duration = 0.3)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        
        @self.tasks.timed_task(0.1, self.subsystems)
        def reset_gyro(subsystems: SubSystems):
            subsystems.gyro.reset()
            
        self.get_note()
        
        self.drive(velocity = Vector(0, 0, 0.15), duration = 0.3)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        
        self.one_piece.initiate()
        
       # Taxi
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.7)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
        
        self.tasks.reset()

