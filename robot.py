# from components.auton.PathPlanner import PathPlanner
# from components.drive.MecanumDrive import MecanumDrive
# from constants import Robot
# import wpilib
# import wpilib.drive
# import os

# class Arpeggio(wpilib.TimedRobot):
#     def robotInit(self):
#         self.drive = MecanumDrive(1, 2, 3, 4)
#         self.stick = wpilib.Joystick(0)
#         self.timer = wpilib.Timer()
#         self.PathPlanner = PathPlanner("/home/lvuser/py/paths/Forwardybackwardy.json", self.timer)

#     def autonomousInit(self):
#         self.timer.reset()
#         self.timer.start()

#     def autonomousPeriodic(self):
#         self.PathPlanner.run(self.drive)

#     def teleopPeriodic(self):
#         x, y, z = (
#             self.stick.getX(),
#             self.stick.getY(),
#             self.stick.getZ(),
#         )
#         self.drive.move(x, y, z)
     

# if __name__ == "__main__":
#     wpilib.run(Arpeggio)
import wpilib
from robotcontainer import RobotContainer
from commands2 import TimedCommandRobot
class Arpeggio(TimedCommandRobot):
    def robotInit(self):
        self.container = RobotContainer()
        """Robot initialization function"""

        self.encoder = wpilib.Encoder(1, 2, False, wpilib.Encoder.EncodingType.k4X)

        # Defines the number of samples to average when determining the rate.
        # On a quadrature encoder, values range from 1-255;
        # larger values result in smoother but potentially
        # less accurate rates than lower values.
        self.encoder.setSamplesToAverage(5)

        # Defines how far the mechanism attached to the encoder moves per pulse. In
        # this case, we assume that a 360 count encoder is directly
        # attached to a 3 inch diameter (1.5inch radius) wheel,
        # and that we want to measure distance in inches.
        self.encoder.setDistancePerPulse(1.0 / 360.0 * 2.0 * math.pi * 1.5)

        # Defines the lowest rate at which the encoder will
        # not be considered stopped, for the purposes of
        # the GetStopped() method. Units are in distance / second,
        # where distance refers to the units of distance
        # that you are using, in this case inches.
        self.encoder.setMinRate(1.0)

    def teleopPeriodic(self):
        wpilib.SmartDashboard.putNumber("Encoder Distance", self.encoder.getDistance())
        wpilib.SmartDashboard.putNumber("Encoder Rate", self.encoder.getRate())
    def teleopPeriodic(self) -> None:
        """return super().teleopPeriodic()"""
        print("distance:"+str(self.encoder.getDistance()))
        print("rate:"+str(self.encoder.getRate()))
if __name__ == "__main__":
    wpilib.run(Arpeggio)