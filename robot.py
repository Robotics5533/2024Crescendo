from components.auton.PathPlanner import PathPlanner
from components.drive.MecanumDrive import MecanumDrive
import wpilib
import wpilib.drive
from components.vision.limelight import Limelight
from constants import Robot
from phoenix6 import hardware
import navx
from utils.math import fmod

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
        self.gyro = navx.AHRS.create_i2c()
        self.gyro.reset
        # self.gyro = navx.AHRS.create_spi()
        self.targetAngle = 180
        
    def autonomousInit(self):
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
#        self.PathPlanner.run(self.drive)
        pass

    def teleopPeriodic(self):
        print(self.gyro.getAngle())
        print(fmod(self.gyro.getAngle(),360))
        print("-")
        if self.stick.getRawButton(2):
            self.gyro.reset()
        elif self.stick.getRawButton(3):
            self.correct_angle()
        elif self.stick.getRawButton(1):
            offset = self.limelight.getError()
            self.drive.move(offset[0]*.5, offset[1], offset[2]*.5)
        else:
            x, y, z = (
            self.stick.getX(),
            self.stick.getY(),
            self.stick.getZ(),
            )
            self.drive.move(x, y, z)

    def correct_angle(self):
        angle = self.gyro.getAngle()
        error = self.targetAngle - angle
        if abs(error) >= 180:
            error = 360 - error
        v = error / 180
        v = v * 5
        if abs(v) > 1:
            v = v/abs(v)
        self.drive.move (0,0,v)
if __name__ == "__main__":
    wpilib.run(Arpeggio)
