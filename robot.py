from components.drive.MecanumDrive import MecanumDrive
from constants import Robot
import wpilib
import wpilib.drive


class Arpeggio(wpilib.TimedRobot):
    def robotInit(self):
        self.drive = MecanumDrive(1, 2, 3, 4)
        self.stick = wpilib.Joystick(Robot.controllers.driver.joystick)

    def autonomousInit(self):
        return 0

    def autonomousPeriodic(self):
        if self.timer.get() < 2.0:
            self.drive.move(self.stick.getRawAxis(0), self.stick.getRawAxis(1))
        else:
            self.drive.move(0, 0)
    def teleopPeriodic(self):
        x, y, z = (
            self.stick.getX(),
            self.stick.getY(),
            self.stick.getZ(),
        )
        self.drive.move(x, y, z)


if __name__ == "__main__":
    wpilib.run(Arpeggio)
