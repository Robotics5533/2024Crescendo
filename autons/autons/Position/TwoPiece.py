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
        

    # def get_note(self):
    #     # Flip out intake, 45in 3/8in
    #     self.flip(direction = -1, duration = 0.45)
    #     self.flip(direction = 1, duration = 0.05, speed = 0)

    #     # Start running intake
    #     self.intake(direction = 1, duration = 0.05, speed = Auton3.Speeds.intake)

    #     # Drive backwards to next note
    #     self.drive(position = Vector(0, -0.9, 0), duration = 0.52)
    #     self.drive(position = Vector(0, 0, 0), duration = 0.05, brake = True)

    #     # Flip in intake
    #     self.flip(direction = 1, duration = 0.5)
    #     self.flip(direction = -1, duration = 0.05, speed = 0)

    #     # Stop running intake
    #     self.intake(speed = 0, direction = 0, duration = 0.05)

    #     # Drive back with note
    #     self.drive(position = Vector(0, 0.9, 0), duration = 0.48)
    #     self.drive(position = Vector(0, 0, 0), duration = 0.05, brake = True)
    
    # def shoot_note(self):
    #     # Shoot note
    #     self.shoot(speed = 100, direction = 1, duration = 0.33)
    #     self.intake(speed = Auton3.Speeds.intake, direction = -1, duration = 0.35)
    #     self.stop()


    # def initate(self):
    #     # Start running shooter
    #     self.shoot(speed = 100, direction = 1, duration = 0.05)
        
    #     # Do a little jump back
    #     self.drive(position = Vector(0, -0.875, 0), duration = 0.18)
    #     self.drive(position = Vector(0, 0, 0), duration = 0.15, brake = True)

    #     # Start running intake
    #     self.intake(speed = Auton3.Speeds.intake, direction = -1, duration = 0.35)

        
    #     self.stop()

    #     # Grab Second Note
    #     self.get_note()

    #     # Shoot second note
    #     self.shoot_note()

    def run(self):
        # self.initate()
        
        # # Taxi
        # self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.75)
        # self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        # @self.tasks.position_task(duration = 5, distance = 45.37, after = lambda: 7)
        # def drive(*args, **kwargs):
        #     self.subsystems.drive.drive.set_mode(MotorModes.position)
        #     self.subsystems.drive.move(Vector(0, -45.375, 0))
        d = convert("4 ft", "in")
        self.drive(position = Vector(0, d, 0), distance = d, duration = 999)
        self.drive(position = Vector(0, 0, 0), distance = 999.1, duration = 999, brake = True)

        # square = 6 * math.pi
        # @self.tasks.position_task(duration = 23846597, distance = square * 2, after = lambda: 1)
        # def test(*args, **kwargs):
        #     self.subsystems.drive.drive.set_mode(MotorModes.position)
        #     self.subsystems.drive.move(Vector(0, square * 2, 0))
         
        
        self.tasks.reset()
