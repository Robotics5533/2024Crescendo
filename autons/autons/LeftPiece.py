from autons.auton2 import Auton
from subsystems.index import SubSystems
from utils.math.Vector import Vector


class LeftPiece(Auton):
    def __init__(self, subsystems: SubSystems, timer):
        super().__init__(subsystems, timer)
        self.subsystems = subsystems

    def run(self):
        self.drive(after = (lambda: print("After was called")), velocity = Vector(0, -0.7, self.subsystems.gyro.calculate(0)), duration = 30)
        # self.rotate(angle = 33)
        self.tasks.reset()
