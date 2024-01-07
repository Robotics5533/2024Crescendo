from components.auton.PathPlanner import PathPlanner
from components.drive.MecanumDrive import MecanumDrive
from constants import Robot
import wpilib
import wpilib.drive
import os

class Arpeggio(wpilib.TimedRobot):
    def robotInit(self):
        self.drive = MecanumDrive(1, 2, 3, 4)
        self.stick = wpilib.Joystick(0)
        self.timer = wpilib.Timer()
        self.PathPlanner = PathPlanner("/home/lvuser/py/paths/Forwardybackwardy.json", self.timer)

    def autonomousInit(self):
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        self.PathPlanner.run(self.drive)

    def teleopPeriodic(self):
        x, y, z = (
            self.stick.getX(),
            self.stick.getY(),
            self.stick.getZ(),
        )
        self.drive.move(x, y, z)


if __name__ == "__main__":
    wpilib.run(Arpeggio)
