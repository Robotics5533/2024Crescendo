from components.auton.PathPlanner import PathPlanner
from components.drive.MecanumDrive import MecanumDrive
import wpilib
import wpilib.drive
from components.vision.limelight import Limelight
from constants import Robot


class Arpeggio(wpilib.TimedRobot):
    def robotInit(self):
        self.drive = MecanumDrive(self.Robot.motors.front_left, self.Robot.motors.front_right, self.Robot.motors.back_left, self.Robot.motors.back_right)
        self.stick = self.Robot.controllers.driver.joystick()
        self.timer = wpilib.Timer()
        self.PathPlanner = PathPlanner("/home/lvuser/py/paths/Forwardybackwardy.json", self.timer)
        self.limelight=Limelight()

    def autonomousInit(self):
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        self.PathPlanner.run(self.drive)

    def teleopPeriodic(self):
        
        if self.follow_limelight_btnid():
            offset = self.limelight.getoffset()
            self.drive.move(-offset[0], offset[1], -offset[2])
        x, y, z = (
            self.stick.getX(),
            self.stick.getY(),
            self.stick.getZ(),
        )
        self.drive.move(x, y, z)


if __name__ == "__main__":
    wpilib.run(Arpeggio)
