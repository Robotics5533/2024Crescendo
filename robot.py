import wpilib
import wpilib.drive
from constants import Robot
from robot_container import RobotContainer
from subsystems.index import SubSystems
from utils.context import Context
from utils.follower import Follower
from utils.math.Vector import Vector
from phoenix6 import hardware, controls


class Arpeggio(wpilib.TimedRobot):
    def robotInit(self):
        self.robot_container = RobotContainer(SubSystems(), wpilib.Joystick(Robot.controllers.joystick))
        self.context = Context(
            self,
            2.5,
        )
        self.follower = Follower(self.context)

    def autonomousPeriodic(self):
        self.robot_container.teleop_lock.lock()
        self.robot_container.process()
        self.follower.update()

    def teleopPeriodic(self):
        self.robot_container.process()

if __name__ == "__main__":
    wpilib.run(Arpeggio)
