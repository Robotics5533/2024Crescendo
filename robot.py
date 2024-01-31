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
from components.sensors.encoder5533 import BufferedEncoder5533

class Arpeggio(wpilib.TimedRobot):
    def robotInit(self):
        self.encoder = wpilib.Encoder(0,1)
        self.BufferedEncoder = BufferedEncoder5533(self.encoder, 3)
        self.stick = wpilib.Joystick(0)
        self.spark = wpilib.Spark(0)
    #     self.timer = wpilib.Timer()

    # def autonomousInit(self) -> None:
    #     self.timer.reset()
    #     self.timer.start()
    # def autonomousPeriodic(self) -> None:
    #     if self.timer.get() <= 5:
    #         self.container.drive_subsystem.drive.move(0.5, 0, 0)
    def teleopPeriodic(self) -> None:
        """return super().teleopPeriodic()"""
        self.spark.set(self.stick.getRawAxis(3))
        print(f"sliderPOS {self.stick.getRawAxis(3)}")
        print(self.BufferedEncoder.getDistance())
        
if __name__ == "__main__":
    wpilib.run(Arpeggio)
    
    