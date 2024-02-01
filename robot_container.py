from components.inputs.ActionMap import ActionMap
from components.inputs.Lockdown import Lockdown
from components.motor.Talon5533 import Talon5533
from utils.math.Vector import Vector
from constants import Robot
"""
RobotContainer is where the __root__ of our bot lives
"""
class RobotContainer:
    def __init__(self, subsystems, stick):
        self.subsystems = subsystems
        self.stick = stick
        self.teleop_lock = Lockdown()
        self.action_map = ActionMap()
        self.action_map.register_action("activate_limelight", self.teleop_lock.lockify(lambda: self.stick.getRawButton(Robot.Controllers.activate_limelight)))
        self.action_map.register_action("activate_climb", self.teleop_lock.lockify(lambda: self.stick.getRawButton(Robot.Controllers.activate_climb)))
        self.action_map.register_action("reset_gyro", self.teleop_lock.lockify(lambda: self.stick.getRawButton(Robot.Controllers.reset_gyro)))
        self.action_map.register_action("move_gyro", self.teleop_lock.lockify(lambda: self.stick.getPOV(0) >= 0))
        self.action_map.register_action("activate_shooter", self.teleop_lock.lockify(lambda: self.stick.getRawButton(Robot.Controllers.activate_shooter)))
        self.action_map.register_action("run_intake", self.teleop_lock.lockify(lambda: self.stick.getRawButton(Robot.Controllers.run_intake)))
    """
    get_motion returns the x, y and z of our joystick
    """
    def get_motion(self):
        return (self.stick.getX(), self.stick.getY(), self.stick.getZ())
    """
    process sets up all of our &subsystems&
    """
    def process(self):
         x, y, z = self.get_motion()
         self.subsystems.setup(
            self.subsystems.limelight.correct_error,
            self.action_map.get_action_pressed("activate_limelight"),
            [self.subsystems.drive, self.subsystems.limelight],
            
            self.subsystems.drive
        )
         
         self.subsystems.setup(
            self.subsystems.shooter.shoot, 
            self.action_map.get_action_pressed("activate_shooter"),
            [self.subsystems.shooter],

            0.5
        )
         
         self.subsystems.setup(
            self.subsystems.climb.move, 
            self.action_map.get_action_pressed("activate_climb"),
            [self.subsystems.climb],
            
            -y
        )
         
         self.subsystems.setup(
            self.subsystems.gyro.reset,
            self.action_map.get_action_pressed("reset_gyro"),
            [self.subsystems.gyro],
        )
         
         self.subsystems.setup(
            self.subsystems.gyro.move,
            self.action_map.get_action_pressed("move_gyro"),
            [self.subsystems.gyro, self.subsystems.drive],

            self.stick.getPOV(0)
        )
         
         self.subsystems.setup(
            self.subsystems.intake.run,
            self.action_map.get_action_pressed("run_intake"),
            [self.subsystems.drive],

            0.5
        )
         
         if not self.action_map.get_action_pressed("activate_climb"):
             self.subsystems.drive.set_mode(1)
             self.subsystems.drive.move(Vector(x, y, z))
           
         self.subsystems.reset()