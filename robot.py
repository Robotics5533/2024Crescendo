import wpilib
import wpilib.drive
from constants import Robot
from subsystems.index import SubSystems
from utils.context import Context
from utils.follower import Follower
from utils.math.Vector import Vector
from phoenix6 import hardware, controls

class Arpeggio(wpilib.TimedRobot):
    def robotInit(self):
        self.subsystems = SubSystems()
        self.context = Context(
            self,
            2.5,
        )
        self.follower = Follower(self.context)
        self.stick = wpilib.Joystick(Robot.controllers.driver.joystick)
    def limelight_subsystem(self):
        offset = self.subsystems.limelight.getError()
        self.subsystems.drive.drive.set_speed(50)
        self.subsystems.drive.move(Vector(offset[0], offset[1], offset[2]))
    def climb_subsystem(self):
        self.subsystems.climb.move(-self.stick.getY())
    def autonomousPeriodic(self):
        self.follower.update()

    def teleopPeriodic(self):
        self.subsystems.setup(
            self.limelight_subsystem,
            self.stick.getRawButton(1),
            [self.subsystems.drive],
        )
        self.subsystems.setup(
            self.climb_subsystem, 
            self.stick.getRawButton(2), 
            [self.subsystems.drive]
        )
        x, y, z = (
            self.stick.getX(),
            self.stick.getY(),
            self.stick.getZ(),
        )
        self.subsystems.drive.move(Vector(x, y, z))


if __name__ == "__main__":
    wpilib.run(Arpeggio)
