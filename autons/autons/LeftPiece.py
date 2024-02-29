import wpilib
from autons.auton import Auton
from components.motor.Motor5533 import MotorModes
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.tasks import Tasks

class LeftPiece(Auton):
    def __init__(self, subsystems, timer):
        self.subsystems = subsystems
        self.timer = timer
        self.tasks = Tasks(self.timer, subsystems)

    def run(self):
        @self.tasks.timed_task(0.5, self.subsystems)
        def drive(subsystems: SubSystems):
            subsystems.drive.drive.set_mode(MotorModes.voltage)
            subsystems.drive.move(Vector(-.5, 0, subsystems.gyro.calculate(0)))
        self.tasks.reset()
