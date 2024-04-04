import gc
import math
import wpilib
import wpilib.drive
from autons.auton import Auton
from autons.factory import AutonList, create_auton
from constants import Robot
from components.motor.Motor5533 import MotorModes
from components.motor.Talon5533 import Talon5533
from robot_container import RobotContainer
from subsystems.index import SubSystems
from utils.context import Context
from utils.follower import Follower
from utils.math.Vector import Vector
from phoenix6 import hardware, controls
from wpilib import SmartDashboard
from wpilib import CameraServer
from utils.tasks2 import Tasks2
# from cscore import CameraServer
from utils.math.motors import drive_to_meters
class Arpeggio(wpilib.TimedRobot):
    def robotInit(self):
        self.robot_container = RobotContainer(SubSystems(), wpilib.Joystick(Robot.Controllers.joystick), wpilib.XboxController(Robot.Controllers.xbox))
        self.context = Context(
            self,
            2.5,
        )
        self.follower = Follower(self.context)
        self.subsystems: SubSystems = self.robot_container.subsystems
        self.timer = wpilib.Timer()
        SmartDashboard.putStringArray("Auto List", AutonList)
        self.garabage_iteration = 0
        self.subsystems.intake_control.motor.set_position(0)
        # camera  = CameraServer.startAutomaticCapture()      
        # camera.setResolution(10, 10)
    def teleopInit(self) -> None:
        super().teleopInit()

        self.robot_container.teleop_lock.unlock()    
        self.subsystems.amper.position_motor.set_position(0)
        self.subsystems.drive.drive.set_position(0)
        self.timer.restart()
        self.tasks = Tasks2(self.timer,self.subsystems)
        self.subsystems.drive.drive.set_mode(MotorModes.voltage)

    def autonomousInit(self) -> None:
        super().autonomousInit()
        self.robot_container.teleop_lock.lock()
        self.subsystems.drive.drive.set_position(0)
        self.subsystems.intake_control.motor.set_position(0)
        self.subsystems.amper.position_motor.set_position(0)
        # self.subsystems.drive.drive.set_mode(MotorModes.position)
        # self.subsystems.drive.drive.set_position(0)
        # self.timer.restart()
        # self.timer.start()
        auton_name = SmartDashboard.getString("Auto Selector", "TwoPiece")
        self.auton = create_auton(self.subsystems, auton_name, self.timer)
        
        self.timer.restart()
       
    
    def autonomousPeriodic(self):
        self.subsystems.drive.drive.set_mode(MotorModes.voltage)
        self.auton.run()

    def disabledInit(self) -> None:
        super().disabledInit()
        self.subsystems.drive.drive.set_mode(MotorModes.voltage)

    def teleopPeriodic(self):
        self.garabage_iteration = self.garabage_iteration + 1 % 100
        if(not (self.garabage_iteration % 100)):
            gc.collect()
        self.robot_container.process()

        # if self.robot_container.stick.getRawButton(1):
        #     self.subsystems.drive.drive.move(Vector(self.robot_container.stick.getX()/4,
        #                                             self.robot_container.stick.getY()/4,
        #                                             self.robot_container.stick.getZ()/4))
        #     print("user input")
        # else:
        #     self.subsystems.drive.drive.move(Vector(self.robot_container.stick.getX()/4,
        #                                             self.robot_container.stick.getY()/4,
        #                                             self.subsystems.gyro.calculate(0)))
        #     print("gyro code")
        # print("error", self.subsystems.gyro.calculate(0))
        # print("fl",self.subsystems.drive.drive.front_left_motor.get_position())
        # print("fr",self.subsystems.drive.drive.front_right_motor.get_position())
        # print("br",self.subsystems.drive.drive.back_right_motor.get_position())
        # print("bl",self.subsystems.drive.drive.back_left_motor.get_position())

        # self.subsystems.gyro.calculate(0)
        # if self.robot_container.stick.getRawButton(1):
        #     self.subsystems.drive.drive.move(Vector(self.robot_container.stick.getX() / 4, self.robot_container.stick.getY() / 4, 0))
        # else:
        #     self.subsystems.drive.drive.move(Vector(0, 0, 0))
        
        # print(self.subsystems.amper.position_motor.get_position())
        
        
        # self.subsystems.drive.drive.move(Vector(-6*math.pi,0, 0))

        # @self.tasks.timed(run_time=10,after = lambda : print("finished the thing!"))
        # def test_stuff(*args,**kwargs):
        #     print("running task for 10s")
        
        # @self.tasks.timed(run_time=20)
        # def test_other_stuff(*args,**kwargs):
        #     print("running other stuff")
    
        # square = 6 * math.pi
        # self.subsystems.drive.drive.set_mode(MotorModes.position)
        # self.subsystems.drive.move(Vector(0, 5*square, 0))
        # @self.tasks.positioned(run_time = 23846597, distance = square * 2, after = lambda: 1)
        # def test(*args, **kwargs):
        #     self.subsystems.drive.drive.set_mode(MotorModes.position)
        #     self.subsystems.drive.move(Vector(0, square * 2, 0))
         
        # @self.tasks.timed(run_time = 1, after = lambda: 1)
        # def test(*args, **kwargs):
        #     self.subsystems.drive.drive.set_mode(MotorModes.static_brake)
        #     self.subsystems.drive.move(Vector(0, 0, 0))

        # @self.tasks.positioned(run_time = 23846597, distance = square * 2, after = lambda: 1)
        # def test(*args, **kwargs):
        #     self.subsystems.drive.drive.set_mode(MotorModes.position)
        #     self.subsystems.drive.move(Vector(-(square * 2), 0, 0))

        # @self.tasks.timed(run_time = 1, after = lambda: 1)
        # def test(*args, **kwargs):
        #     self.subsystems.drive.drive.set_mode(MotorModes.static_brake)
        #     self.subsystems.drive.move(Vector(0, 0, 0))

        # @self.tasks.positioned(run_time = 23846597, distance = square * 2, after = lambda: 1)
        # def test(*args, **kwargs):
        #     self.subsystems.drive.drive.set_mode(MotorModes.position)
        #     self.subsystems.drive.move(Vector(0, -(square * 2), 0))

        # @self.tasks.positioned(run_time = 23846597, distance = square * 2, after = lambda: 1)
        # def test(*args, **kwargs):
        #     self.subsystems.drive.drive.set_mode(MotorModes.position)
        #     self.subsystems.drive.move(Vector((square * 2), 0, 0))

        # @self.tasks.timed(run_time = 1, after = lambda: 1)
        # def test(*args, **kwargs):
        #     self.subsystems.drive.drive.set_mode(MotorModes.static_brake)
        #     self.subsystems.drive.move(Vector(0, 0, 0))
        # self.tasks.reset()
        

if __name__ == "__main__":
    wpilib.run(Arpeggio)
