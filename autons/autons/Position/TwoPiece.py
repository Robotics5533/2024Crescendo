import math
from autons.auton3 import Auton3
from components.motor.Motor5533 import MotorModes
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.math.algebra import linear_remap
from utils.math.conversion import convert


class TwoPiecePosition(Auton3):
    def __init__(self, subsystems: SubSystems, timer, tasks = None):
        super().__init__(subsystems, timer, tasks)
        self.subsystems = subsystems
        

    def get_note(self):

        note_distance = convert("3 ft", "in")
        self.flip(direction = -1, duration = 0.45)
        self.flip(direction = 1, duration = 0.05, speed = 0)

        # Start running intake
        self.intake(direction = 1, duration = 0.05, speed = Auton3.Speeds.intake)

        # Drive backwards to next note
        self.drive(position = Vector(0, note_distance, 0))
        self.drive(position = Vector(0, 0, 0), brake = True, duration = 0.05)

        # Flip in intake
        self.flip(direction = 1, duration = 0.5)
        self.flip(direction = -1, duration = 0.05, speed = 0)

        # Stop running intake
        self.intake(speed = 0, direction = 0, duration = 0.05)

        # Drive back with note
        self.drive(position = Vector(0, -note_distance, 0))
        self.drive(position = Vector(0, 0, 0), duration = 0.05, brake = True)
    
    def shoot_note(self):
        # Shoot note
        self.shoot(speed = 100, direction = 1, duration = 0.33)
        self.intake(speed = Auton3.Speeds.intake, direction = -1, duration = 0.35)
        self.stop()


    def initate(self):
        # Start running shooter
        self.shoot(speed = 100, direction = 1, duration = 0.05)
        
        # # Do a little jump back
        self.drive(position = Vector(0, 8, 0))
        self.drive(position = Vector(0, 0, 0), brake = True)

        # # Start running intake
        self.intake(speed = Auton3.Speeds.intake, direction = -1, duration = 0.35)

        
        self.stop()

        # Grab Second Note
        self.get_note()

        # Shoot second note
        self.shoot_note()

    def run(self):
        self.initate()
        
        # # Taxi
        # self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.75)
        # self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
 
         
        
        self.tasks.reset()
