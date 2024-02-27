import wpilib
import wpilib.drive
from autons.auton import Auton
from autons.factory import AutonList, create_auton
from constants import Robot
from components.motor.Motor5533 import MotorModes
from robot_container import RobotContainer
from subsystems.index import SubSystems
from utils.context import Context
from utils.follower import Follower
from utils.math.Vector import Vector
from phoenix6 import hardware, controls
from wpilib import SmartDashboard
from utils.math.motors import drive_to_meters

class Arpeggio(wpilib.TimedRobot):
    def robotInit(self):
        self.robot_container = RobotContainer(SubSystems(), wpilib.Joystick(Robot.Controllers.joystick), wpilib.XboxController(Robot.Controllers.xbox))
        self.context = Context(
            self,
            2.5,
        )
        self.follower = Follower(self.context)
        self.subsystems = self.robot_container.subsystems
        self.timer = wpilib.Timer()
        SmartDashboard.putStringArray("Auto List", AutonList)

        self.subsystems.intake_control.motor.set_position(0)
        
    def teleopInit(self) -> None:
        super().teleopInit()
        
        self.robot_container.teleop_lock.unlock()
        self.subsystems.drive.drive.set_mode(MotorModes.voltage)


    def autonomousInit(self) -> None:
        super().autonomousInit()
        self.robot_container.teleop_lock.lock()
        self.subsystems.intake_control.motor.set_position(0)
        self.timer.restart()
       
    
    def autonomousPeriodic(self):
        self.subsystems.drive.drive.set_mode(MotorModes.voltage)
        auton_name = SmartDashboard.getString("Auto Selector", "TwoPiece")
        auton = create_auton(self.subsystems, auton_name, self.timer)
        auton.run()


    def teleopPeriodic(self):
        # self.subsystems.intake_control.motor.set_position(0)
        # print(self.subsystems.intake_control.motor.get_position())  
        self.robot_container.process()
       

if __name__ == "__main__":
    wpilib.run(Arpeggio)