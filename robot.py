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
    def autonomousInit(self) -> None:
        super().autonomousInit()
        self.robot_container.teleop_lock.lock()
        self.subsystems.intake_control.motor.set_position(0)
        # self.subsystems.drive.drive.set_mode(MotorModes.position)
        # self.subsystems.drive.drive.set_position(0)
        # self.timer.restart()
        # self.timer.start()
        self.timer.restart()
       
    
    def autonomousPeriodic(self):

        # self.robot_container.process()
        # self.follower.update()
        # drive_to_meters(self.subsystems.drive.drive, 50)
        
        self.subsystems.drive.drive.set_mode(MotorModes.voltage)
        auton_name = SmartDashboard.getString("Auto Selector", "TwoPiece")
        auton = create_auton(self.subsystems, auton_name, self.timer)
        auton.run()

        # if self.timer.get() < 1.0:
        #     self.subsystems.shooter.shoot(50)
        # elif self.timer.get() < 1.7:
        #     self.subsystems.intake.run(-50)
        # elif self.timer.get() < 2.3:
        #     self.subsystems.intake.run(0)
        #     self.subsystems.shooter.shoot(0) # shot first note
        # elif self.timer.get() < 2.7:
        #     self.subsystems.intake_control.run(-0.0025)
        # elif self.timer.get() < 3:
        #     self.subsystems.intake_control.run(0)
        #     self.subsystems.intake.run(50)
        # elif self.timer.get() < 4.5:
        #     self.subsystems.drive.move(Vector(0, -0.1, 0))
        # elif self.timer.get() < 4.8:
        #     self.subsystems.drive.move(Vector(0, 0, 0))
        #     self.subsystems.intake.run(0)
        # elif self.timer.get() < 6.2:
        #     self.subsystems.intake_control.run(0.0025)
        # elif self.timer.get() < 7:
        #     self.subsystems.intake_control.run(0)
        # elif self.timer.get() < 7.6:
        #     self.subsystems.shooter.shoot(50)
        # elif self.timer.get() < 9:
        #     self.subsystems.drive.move(Vector(0, 0.3, 0))
        # elif self.timer.get() < 9.3:
        #     self.subsystems.drive.move(Vector(0, 0, 0))
        # elif self.timer.get() < 10:
        #     self.subsystems.intake.run(-50)
        # elif self.timer.get() < 10.8:
        #     self.subsystems.intake.run(0)
        #     self.subsystems.shooter.shoot(0)
        # elif self.timer.get() < 10.3:
        #     self.subsystems.drive.move(Vector(0, 0, -0.1))
        # elif self.timer.get() < 10.7:
        #     self.subsystems.drive.move(Vector(0, 0, 0))
        # elif self.timer.get() < 13.0:
        #     self.subsystems.drive.move(Vector(0, -0.1, 0))
        # else:
        #     self.subsystems.drive.move(Vector(0, 0, 0))
        
        
        
        # pass
        # self.subsystems.drive.drive.set_mode(MotorModes.position)
        # self.subsystems.drive.drive.set_position(0)
        # self.subsystems.drive.move(Vector(0, 12, 0))

    def teleopPeriodic(self):
        self.robot_container.process()

if __name__ == "__main__":
    wpilib.run(Arpeggio)