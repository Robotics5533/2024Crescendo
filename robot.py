from components.auton.PathPlanner import PathPlanner
from components.drive.MecanumDrive import MecanumDrive
import wpilib
import wpilib.drive
from components.vision.limelight import Limelight
from constants import Robot
from phoenix6 import hardware

from systems.Climb import Climb


class Arpeggio(wpilib.TimedRobot):
    def robotInit(self):
        self.drive = MecanumDrive(hardware.TalonFX(Robot.motors.front_left),
                                  hardware.TalonFX(Robot.motors.front_right),
                                  hardware.TalonFX(Robot.motors.back_left),
                                  hardware.TalonFX(Robot.motors.back_right))
        self.stick = wpilib.Joystick(0)
        self.timer = wpilib.Timer()
#        self.PathPlanner = PathPlanner("/home/lvuser/py/paths/Forwardybackwardy.json", self.timer)
        self.limelight=Limelight()
        self.climb = Climb(hardware.TalonFX(Robot.motors.climb))

    def autonomousInit(self):
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
#        self.PathPlanner.run(self.drive)
        pass

    def teleopPeriodic(self):
        self.climb.run()
        # if self.stick.getRawButton(1):
        #     offset = self.limelight.getError()
        #     self.drive.move(offset[0]*.5, offset[1], offset[2]*.5)
        # elif self.stick.getRawButton(2):
        #     self.climb.run()
        # else:
        #     x, y, z = (
        #     self.stick.getX(),
        #     self.stick.getY(),
        #     self.stick.getZ(),
        #     )
        #     self.drive.move(x, y, z)


if __name__ == "__main__":
    wpilib.run(Arpeggio)
