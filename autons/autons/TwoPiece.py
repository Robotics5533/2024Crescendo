import wpilib
from autons.auton import Auton
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.tasks import Tasks

class TwoPiece(Auton):
    def __init__(self, subsystems, timer):
        self.subsystems = subsystems
        self.timer = timer
        self.tasks = Tasks(self.timer, subsystems)

    def run(self):

        @self.tasks.position_task(5, self.subsystems, 5)
        def drive(subsystems: SubSystems, y: float):
            subsystems.drive.move(Vector(0, -y, 0))

        # @self.tasks.timed_task(0.7, self.subsystems, -50)
        # def intake(subsystems: SubSystems, speed: float):
        #     subsystems.intake.run(speed)

        # @self.tasks.timed_task(0.5, self.subsystems)
        # def stop(subsystems: SubSystems):
        #     subsystems.shooter.shoot(0)
        #     subsystems.intake.run(0)
        self.subsystems.drive.drive.process()
        self.tasks.reset()
