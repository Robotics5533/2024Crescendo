"""
highly experimental change, see 

https://github.com/robotpy/examples/blob/main/FrisbeeBot/robot.py

for reference code
"""
from robot_container import RobotContainer

#robot.py code is often very bair with this mentality, 
#as the default functions on the robot are used primarily
#to set specific triggers or start and stop commands that may or may
#not be running
#see robot_container.py for where the "action" is :D
class Arpeggio(wpilib.TimedRobot):
    def robotInit(self):
        self.container = RobotContainer()

