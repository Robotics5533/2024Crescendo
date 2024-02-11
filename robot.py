from asyncio import sleep
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
        
    def autonomousPeriodic(self):
        # self.robot_container.teleop_lock.lock()
        # self.robot_container.process()
        # self.follower.update()
        # drive_to_meters(self.subsystems.drive.drive, 50)
        # self.subsystems.shooter.run(75)
        # sleep(2000)
        # self.subsystems.shooter.run(0)
        # self.subsystems.intake.run(-0.5)
        # sleep(2000)
        # self.subsystems.intake.run(0)
        # self.subsystems.drive.drive(Vector(0, 0.25, 0))
        # sleep(5000)
        # self.subsystems.drive.drive(Vector(0, 0, 0))
        pass
    def teleopPeriodic(self):
        self.robot_container.process()

if __name__ == "__main__":
    wpilib.run(Arpeggio)