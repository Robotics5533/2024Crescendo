import wpilib
from autons.auton import Auton
from subsystems.index import SubSystems
from utils.tasks import Tasks

class TwoPiece(Auton):
    def __init__(self, subsystems, timer):
        self.subsystems = subsystems
        self.timer = timer
        self.tasks = Tasks(self.timer)
    def run(self):

        @self.tasks.timed_task(1, self.subsystems, 30)
        def shooter(subsystems: SubSystems, speed: float):
            subsystems.shooter.shoot(speed)

        @self.tasks.timed_task(0.7, self.subsystems, -50)
        def intake(subsystems: SubSystems, speed: float):
            subsystems.intake.run(speed)

        @self.tasks.timed_task(0.5, self.subsystems)
        def stop(subsystems: SubSystems):
            subsystems.shooter.shoot(0)
            subsystems.intake.run(0)

        self.tasks.reset()