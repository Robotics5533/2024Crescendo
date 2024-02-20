import wpilib
import wpilib.drive
from constants import Robot
from robot_container import RobotContainer
from subsystems.index import SubSystems
from utils.context import Context
from utils.follower import Follower
from utils.math.Vector import Vector
from phoenix6 import hardware, controls

from utils.math.motors import drive_to_meters

class Arpeggio(wpilib.TimedRobot):
    def robotInit(self):
        self.robot_container = RobotContainer(SubSystems(), wpilib.Joystick(Robot.Controllers.joystick), wpilib.XboxController(Robot.Controllers.xbox))
        self.context = Context(
            self,
            2.5,
        )
        self.follower = Follower(self.context)
        self.subsystems = self.robot_container.subsystems
        self.timer = wpilib.Timer()
        
    def autonomousInit(self) -> None:
        super().autonomousInit()
        self.robot_container.teleop_lock.lock()
        # self.timer.restart()
        # self.timer.start()
        self.timer.restart()
       
    
    def autonomousPeriodic(self):

        # self.robot_container.process()
        # self.follower.update()
        # drive_to_meters(self.subsystems.drive.drive, 50)
        
        if self.timer.get() < 0.7:
            self.subsystems.drive.move(Vector(0, -0.1, 0))
        elif self.timer.get() < 1.5:
            self.subsystems.drive.move(Vector(0.2, 0, 0))
        elif self.timer.get() < 1.7:
            self.subsystems.shooter.shoot(80)
            self.subsystems.drive.move(Vector(0, 0, 0))
        elif self.timer.get() < 1.9:
            self.subsystems.shooter.shoot(80)
            self.subsystems.intake.run(50)
        elif self.timer.get() < 2.1:
            self.subsystems.intake.run(0)
            self.subsystems.shooter.shoot(0)
        # pass
    def teleopPeriodic(self):
        self.robot_container.process()

if __name__ == "__main__":
    wpilib.run(Arpeggio)