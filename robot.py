"""
highly experimental change, see 

https://github.com/robotpy/examples/blob/main/FrisbeeBot/robot.py

for reference code
"""
from robot_container import RobotContainer
import wpimath

#robot.py code is often very bair with this mentality, 
#as the default functions on the robot are used primarily
#to set specific triggers or start and stop commands that may or may
#not be running
#see robot_container.py for where the "action" is :D
class Arpeggio(wpilib.TimedRobot):
    def robotInit(self):
        self.container = RobotContainer()
        wpimath.kinematics.MecanumDriveKinematics.toWheelSpeeds(
                wpimath.kinematics.ChassisSpeeds(1,1,0.1),
                wpimath.geometry.Transform2d(1,0,0)
                )
        wpimath.kinematics.ChassisSpeeds(1,1,0.5)
