import wpilib
import wpilib.drive
from constants import Robot
from subsystems.index import SubSystems
from utils.context import Context
from utils.follower import Follower


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
        self.subsystems.drive.move(offset[0] * 0.5, offset[1], offset[2] * 0.5)

    def autonomousPeriodic(self):
        self.follower.update()

    def teleopPeriodic(self):
        self.subsystems.setup(
            self.limelight_subsystem,
            self.stick.getRawButton(1),
            [self.subsystems.drive],
        )
        if self.subsytems.can(self.subsytems.drive):
            x, y, z = (
                self.stick.getX(),
                self.stick.getY(),
                self.stick.getZ(),
            )
            self.subsytems.drive.move(x, y, z)


if __name__ == "__main__":
    wpilib.run(Arpeggio)
