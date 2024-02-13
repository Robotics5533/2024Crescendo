import math
from components.inputs.ActionMap import ActionMap
from components.inputs.Lockdown import Lockdown
from components.motor.Talon5533 import Talon5533
from utils.math.Vector import Vector
from utils.math.motors import drive_to_meters
from utils.math.algebra import clamp

class RobotContainer:
    def __init__(self, subsystems, stick, xbox):
        self.subsystems = subsystems
        self.stick = stick
        self.xbox = xbox
        self.teleop_lock = Lockdown()
        self.action_map = ActionMap()
        # self.action_map.register_action("activate_limelight", self.teleop_lock.lockify(lambda: self.xbox.getXButton()))
        # self.action_map.register_action("activate_climb_up", self.teleop_lock.lockify(lambda: self.xbox.getYButton()))
        # self.action_map.register_action("activate_climb_down", self.teleop_lock.lockify(lambda: self.xbox.getAButton()))
        # self.action_map.register_action("deactivate_climb", self.teleop_lock.lockify(lambda: not (self.xbox.getAButton() or self.xbox.getYButton())))
        # self.action_map.register_action("move_gyro", self.teleop_lock.lockify(lambda: abs(self.xbox.getLeftX() + self.xbox.getLeftY()) > 0.25327548326587563845682347658735682736483765736573465))
        self.action_map.register_action("activate_shooter", self.teleop_lock.lockify(lambda: self.xbox.getBButton()))
        self.action_map.register_action("deactivate_shooter", self.teleop_lock.lockify(lambda: not self.xbox.getBButton()))
        self.action_map.register_action("run_intake_in", self.teleop_lock.lockify(lambda: self.xbox.getRightBumper()))
        self.action_map.register_action("run_intake_out", self.teleop_lock.lockify(lambda: self.xbox.getLeftBumper()))
        self.action_map.register_action("unrun_intake", self.teleop_lock.lockify(lambda: not (self.xbox.getRightBumper() or self.xbox.getLeftBumper())))
        self.action_map.register_action("control_intake", self.teleop_lock.lockify(lambda: (self.xbox.getLeftTriggerAxis() + self.xbox.getRightTriggerAxis()) > 0.1))
        self.action_map.register_action("control_intake_STOP", self.teleop_lock.lockify(lambda: not self.action_map.get_action_pressed("control_intake")))
    
    def get_motion(self):
        return (self.stick.getX(), self.stick.getY(), self.stick.getZ())
        
    def process(self):
         x, y, z = self.get_motion()
        #  self.subsystems.setup(
        #     self.subsystems.limelight.correct_error,
        #     self.action_map.get_action_pressed("activate_limelight"),
        #     [self.subsystems.drive, self.subsystems.limelight],
            
        #     self.subsystems.drive
        # )
         
         self.subsystems.setup(
            self.subsystems.shooter.shoot, 
            self.action_map.get_action_pressed("activate_shooter"),
            [],

        50
        )
         self.subsystems.setup(
            self.subsystems.shooter.shoot, 
            self.action_map.get_action_pressed("deactivate_shooter"),
            [],

            0
         )
         self.subsystems.setup(
            self.subsystems.intake.run,
            self.action_map.get_action_pressed("run_intake_in"),
            [],

            0.5
        )
         self.subsystems.setup(
            self.subsystems.intake.run,
            self.action_map.get_action_pressed("unrun_intake"),
            [],

            0
        )
         
         self.subsystems.setup(
            self.subsystems.intake.run,
            self.action_map.get_action_pressed("run_intake_out"),

            [],

            -0.5
        )
         self.subsystems.setup(
            self.subsystems.intake_control.run,
            self.action_map.get_action_pressed("control_intake"),
            [],

            clamp((self.xbox.getLeftTriggerAxis() - self.xbox.getRightTriggerAxis()), -0.0027, 0.0027)
        )
         
         self.subsystems.setup(
            self.subsystems.intake_control.run,
            self.action_map.get_action_pressed("control_intake_STOP"),
            [],

            0
            
        )
         
        #  self.subsystems.setup(
        #     self.subsystems.climb.move, 
        #     self.action_map.get_action_pressed("activate_climb_up"),
        #     [self.subsystems.climb],

        #     0.25
        # )
        #  self.subsystems.setup(
        #     self.subsystems.climb.move, 
        #     self.action_map.get_action_pressed("activate_climb_down"),
        #     [self.subsystems.climb],

        #     -0.25
        # )
        #  self.subsystems.setup(
        #     self.subsystems.climb.move, 
        #     self.action_map.get_action_pressed("deactivate_climb"),
        #     [self.subsystems.climb],

        #     0
        # )
         
        #  self.subsystems.drive.drive.set_mode(1)
        #  self.subsystems.drive.move(Vector(x, y, z))
         self.subsystems.reset()
         
        #  self.subsystems.setup(
        #     self.subsystems.gyro.reset,
        #     self.action_map.get_action_pressed("reset_gyro"),
        #     [self.subsystems.gyro],
        # )
         
        #  self.subsystems.setup(
        #     self.subsystems.gyro.move,
        #     self.action_map.get_action_pressed("move_gyro"),
        #     [self.subsystems.gyro, self.subsystems.drive],

        #     self.stick.getPOV(0)
        # )
         
        