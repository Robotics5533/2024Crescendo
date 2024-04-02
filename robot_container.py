import math

import wpilib
from components.inputs.ActionMap import ActionMap
from components.inputs.Lockdown import Lockdown
from components.motor.Talon5533 import Talon5533
from components.motor.Motor5533 import MotorModes
from subsystems.amper import Amper
from utils.actions import Actions
from utils.math.Vector import Vector
from utils.math.algebra import almost_equal, clamp
from utils.math.motors import drive_to_meters
from math import pi

class RobotContainer:
    def __init__(self, subsystems, stick: wpilib.Joystick, xbox: wpilib.XboxController):
        self.subsystems = subsystems
        self.stick = stick
        self.xbox = xbox
        self.teleop_lock = Lockdown()
        self.action_map = ActionMap()
        self.last_action = -1
        """
        Actions that operate the climb up
        """
        self.action_map.register_action("activate_climb_in", self.teleop_lock.lockify(lambda: self.xbox.getRightY() < -0.3))
        self.action_map.register_action("activate_climb_out", self.teleop_lock.lockify(lambda: self.xbox.getRightY() > 0.3))
        self.action_map.register_action("deactivate_climb", self.teleop_lock.lockify(lambda: not (self.action_map.get_action_pressed("activate_climb_in") or self.action_map.get_action_pressed("activate_climb_out"))))

        """
        Actions that flip the intake in and out
        """
        self.action_map.register_action("intake_flip_in", self.teleop_lock.lockify(lambda: self.xbox.getXButton()))
        self.action_map.register_action("intake_flip_out", self.teleop_lock.lockify(lambda: self.xbox.getBButton()))
        self.action_map.register_action("intake_flip_stop", self.teleop_lock.lockify(lambda: not (self.action_map.get_action_pressed("intake_flip_out") or self.action_map.get_action_pressed("intake_flip_in"))))


        """
        Actions that flip the amper up and down
        """
        self.action_map.register_action("amper_flip_up", self.teleop_lock.lockify(lambda: self.xbox.getLeftBumper()))
        self.action_map.register_action("amper_flip_down", self.teleop_lock.lockify(lambda: self.xbox.getAButton()))
        self.action_map.register_action("amper_flip_stop", self.teleop_lock.lockify(lambda: not (self.action_map.get_action_pressed("amper_flip_up") or self.action_map.get_action_pressed("amper_flip_down"))))


        """
        Actions that run the intake in and out
        """
        self.action_map.register_action("intake_run_in", self.teleop_lock.lockify(lambda: self.xbox.getRightTriggerAxis() > 0.1))
        self.action_map.register_action("intake_run_out", self.teleop_lock.lockify(lambda: self.xbox.getRightBumper()))
        self.action_map.register_action("intake_run_stop", self.teleop_lock.lockify(lambda: not (self.action_map.get_action_pressed("intake_run_out") or self.action_map.get_action_pressed("intake_run_in"))))

        """
        Actions that run the shooter
        """
        self.action_map.register_action("shooter_run_speaker", self.teleop_lock.lockify(lambda: self.xbox.getLeftTriggerAxis() > 0.1))
        self.action_map.register_action("shooter_run_amp", self.teleop_lock.lockify(lambda: self.xbox.getLeftBumper()))
        self.action_map.register_action("shooter_run_backwards", self.teleop_lock.lockify(lambda: self.xbox.getYButton()))
        self.action_map.register_action("shooter_run_stop", self.teleop_lock.lockify(lambda: not (self.action_map.get_action_pressed("shooter_run_amp") or self.action_map.get_action_pressed("shooter_run_speaker") or self.action_map.get_action_pressed("shooter_run_backwards"))))


    def flip_out(self, speed: float):
        self.subsystems.intake_control.run(speed)
        self.xbox.setRumble(self.xbox.RumbleType.kBothRumble, 0)
        self.last_action = Actions.flipped_out

    def register_intake_flip(self):
         """
         Subsystems that actually operate the intake flip
         """
         self.subsystems.setup(
            self.subsystems.intake_control.run,
            self.action_map.get_action_pressed("intake_flip_in"),
            [],
            0.0035
        )
         self.subsystems.setup(
            self.subsystems.intake_control.run,
            self.action_map.get_action_pressed("intake_flip_out"),
            [],
            -0.0035
        )
         self.subsystems.setup(
            self.subsystems.intake_control.run,
            self.action_map.get_action_pressed("intake_flip_stop"),
            [],
            0
        )
         
    def register_amper_flip(self):
         """
         Subsystems that actually operate the amper flip
         """
         self.subsystems.setup(
            self.subsystems.amper.run,
            self.action_map.get_action_pressed("amper_flip_up"),
            [],
            0.0007,
            Amper.up
        )
         self.subsystems.setup(
            self.subsystems.amper.run,
            self.action_map.get_action_pressed("amper_flip_down"),
            [],
            -0.0007,
            Amper.down
        )
         self.subsystems.setup(
            self.subsystems.amper.run,
            self.action_map.get_action_pressed("amper_flip_stop"),
            [],
            0,
            self.subsystems.amper.state
        )
         
    def intake_run(self, speed: float):
        self.subsystems.intake.run(speed)
        # if speed > 0:
        #     self.last_action = Actions.flipped_out
        # self.subsystems.intake.run(speed)
        # if self.last_action == Actions.flipped_out:
        #     self.xbox.setRumble(self.xbox.RumbleType.kBothRumble, 1)
            
    def intake_run_stop(self, speed: float):
        self.subsystems.intake.run(speed)
        self.xbox.setRumble(self.xbox.RumbleType.kBothRumble, 0)

    def register_intake(self):
        """
        Subsystems that actually operate the intake
        """
        self.subsystems.setup(
            self.subsystems.intake.run,
            self.action_map.get_action_pressed("intake_run_out"),
            [],
            70
        )
        self.subsystems.setup(
            self.subsystems.intake.run,
            self.action_map.get_action_pressed("intake_run_in"),
            [],
            -75
        )
        self.subsystems.setup(
            self.subsystems.intake.run,
            self.action_map.get_action_pressed("intake_run_stop"),
            [],
            0
        )

    def amp_shooter(self):
        self.subsystems.shooter.motors[0].set(-0.36) # bottom, 0.38
        self.subsystems.shooter.motors[1].set(-0.20) # top, 0.22
        #17.5in for shooter max
    def register_climb(self):
        """
        Subsystems that operate the climb
        """
        self.subsystems.setup(
            self.subsystems.climb.move,
            self.action_map.get_action_pressed("activate_climb_in"),
            [],
            0.7
        )
         
        self.subsystems.setup(
            self.subsystems.climb.move,
            self.action_map.get_action_pressed("activate_climb_out"),
            [],
            -0.8
        )
        self.subsystems.setup(
            self.subsystems.climb.move,
            self.action_map.get_action_pressed("deactivate_climb"),
            [],
            0
        )
    def register_shooter(self):
        """
         Subsystems that operate the shooter
         """
        self.subsystems.setup(
            self.subsystems.shooter.shoot,
            self.action_map.get_action_pressed("shooter_run_speaker"),
            [],
            80
        )
        self.subsystems.setup(
            self.subsystems.shooter.shoot,
            self.action_map.get_action_pressed("shooter_run_backwards"),
            [],
            -40
        )
        self.subsystems.setup(
            self.amp_shooter,
            self.action_map.get_action_pressed("shooter_run_amp"),
            [],
        )
        self.subsystems.setup(
            self.subsystems.shooter.shoot,
            self.action_map.get_action_pressed("shooter_run_stop"),
            [],
            0
        )
    
    def get_motion(self):
        return (self.stick.getX(), self.stick.getY(), self.stick.getZ() / 2)
    
    def process(self):
         x, y, z = self.get_motion()

         if self.stick.getRawButton(1):
             y = -y
             x = -x

         if self.stick.getRawButton(5):
             self.subsystems.drive.drive.speed_multiplier = 0.5
             #
             
         elif self.stick.getRawButton(3):
             self.subsystems.drive.drive.speed_multiplier = 0.25
             #
         else: 
             #
             self.subsystems.drive.drive.speed_multiplier = 1

        #  if self.stick.getRawButton(4):
        #      angle = self.subsystems.gyro.gyro.getAngle() * -pi / 180
        #      v = Vector(x, y, z).rotate(angle)
        #      x = v.a
        #      y = v.b
        #      


         self.register_intake_flip()
         self.register_intake()
         self.register_shooter()
         self.register_climb()
         self.register_amper_flip()


         self.subsystems.drive.drive.set_mode(MotorModes.voltage)
         self.subsystems.drive.move(Vector(x, y, z))
         self.subsystems.reset()
    # 