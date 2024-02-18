import math
from components.inputs.ActionMap import ActionMap
from components.inputs.Lockdown import Lockdown
from components.motor.Talon5533 import Talon5533
from components.motor.Motor5533 import MotorModes
from utils.math.Vector import Vector
from utils.math.algebra import almost_equal, clamp
from utils.math.motors import drive_to_meters

class RobotContainer:
    def __init__(self, subsystems, stick, xbox):
        self.subsystems = subsystems
        self.stick = stick
        self.xbox = xbox
        self.teleop_lock = Lockdown()
        self.action_map = ActionMap()
        # """
        # Actions that operate the climb up
        # """
        # self.action_map.register_action("activate_climb_up", self.teleop_lock.lockify(lambda: self.xbox.getYButton()))
        # self.action_map.register_action("activate_climb_down", self.teleop_lock.lockify(lambda: self.xbox.getAButton()))
        # self.action_map.register_action("deactivate_climb", self.teleop_lock.lockify(lambda: not (self.action_map.get_action_pressed("activate_climb_up") or self.action_map.get_action_pressed("activate_climb_down"))))

        """
        Actions that operate the control climb
        """

        self.action_map.register_action("climb_flip_in", self.teleop_lock.lockify(lambda: self.xbox.getPOV(0) == 0))
        self.action_map.register_action("climb_flip_out", self.teleop_lock.lockify(lambda: self.xbox.getPOV(0) == 180))
        self.action_map.register_action("climb_flip_stop", self.teleop_lock.lockify(lambda: self.xbox.getPOV(0) == -1))

        """
        Actions that flip the intake in and out
        """
        self.action_map.register_action("intake_flip_in", self.teleop_lock.lockify(lambda: self.xbox.getXButton()))
        self.action_map.register_action("intake_flip_out", self.teleop_lock.lockify(lambda: self.xbox.getBButton()))
        self.action_map.register_action("intake_flip_stop", self.teleop_lock.lockify(lambda: not (self.action_map.get_action_pressed("intake_flip_out") or self.action_map.get_action_pressed("intake_flip_in"))))

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
        self.action_map.register_action("shooter_run_trap", self.teleop_lock.lockify(lambda: self.xbox.getAButton()))
        self.action_map.register_action("shooter_run_stop", self.teleop_lock.lockify(lambda: not (self.action_map.get_action_pressed("shooter_run_amp") or self.action_map.get_action_pressed("shooter_run_speaker") or self.action_map.get_action_pressed("shooter_run_backwards") or self.action_map.get_action_pressed("shooter_run_trap"))))

    def register_climb_flip(self):
        """
         Subsystems that actually operate the climb flip
         """
        self.subsystems.setup(
            self.subsystems.climb_control.move,
            self.action_map.get_action_pressed("climb_flip_in"),
            [],
            55
        )
        self.subsystems.setup(
            self.subsystems.climb_control.move,
            self.action_map.get_action_pressed("climb_flip_out"),
            [],
            -55
        )
        self.subsystems.setup(
            self.subsystems.climb_control.move,
            self.action_map.get_action_pressed("climb_flip_stop"),
            [],
            0
        )

    def register_intake_flip(self):
         """
         Subsystems that actually operate the intake flip
         """
         self.subsystems.setup(
            self.subsystems.intake_control.run,
            self.action_map.get_action_pressed("intake_flip_in"),
            [],
            0.0025
        )
         self.subsystems.setup(
            self.subsystems.intake_control.run,
            self.action_map.get_action_pressed("intake_flip_out"),
            [],
            -0.0025
        )
         self.subsystems.setup(
            self.subsystems.intake_control.run,
            self.action_map.get_action_pressed("intake_flip_stop"),
            [],
            0
        )
         
    def run_intake(self, speed: float):
        self.subsystems.intake.run(speed)
        # if almost_equal(self.subsystems.intake_control.motor.get_position(), 0):
        self.subsystems.shooter.shoot(-speed)
        # if speed == 0:
        #     self.subsystems.shooter.shoot(0)

    def register_intake(self):
        """
        Subsystems that actually operate the intake
        """
        self.subsystems.setup(
            self.subsystems.intake.run,
            self.action_map.get_action_pressed("intake_run_out"),
            [],
            50
        )
        self.subsystems.setup(
            self.subsystems.intake.run,
            self.action_map.get_action_pressed("intake_run_in"),
            [],
            -50
        )
        self.subsystems.setup(
            self.run_intake,
            self.action_map.get_action_pressed("intake_run_stop"),
            [],
            0
        )
    def trap_shooter(self, speed):
        speed = (speed / 100)
        # -56
        # -46
        self.subsystems.shooter.motors[0].set(-0.56) # bottom
        self.subsystems.shooter.motors[1].set(-0.41) # top

        #17.5in for shooter max
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
            self.trap_shooter,
            self.action_map.get_action_pressed("shooter_run_trap"),
            [],
            55
        )
        self.subsystems.setup(
            self.subsystems.shooter.shoot,
            self.action_map.get_action_pressed("shooter_run_backwards"),
            [],
            -40
        )
        self.subsystems.setup(
            self.subsystems.shooter.shoot,
            self.action_map.get_action_pressed("shooter_run_amp"),
            [],
            30
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
        #  x, y, z = self.get_motion()
        
        #  self.register_intake_flip()
        #  self.register_intake()
        #  self.register_shooter()
        self.register_climb_flip()

         
        #  self.subsystems.setup(
        #     self.subsystems.climb.move,
        #     self.action_map.get_action_pressed("activate_climb_up"),
        #     [],
        #     0.5
        # )
         
        #  self.subsystems.setup(
        #     self.subsystems.climb.move,
        #     self.action_map.get_action_pressed("activate_climb_down"),
        #     [],
        #     -0.5
        # )
        #  self.subsystems.setup(
        #     self.subsystems.climb.move,
        #     self.action_map.get_action_pressed("deactivate_climb"),
        #     [],
        #     0
        # )
         
        #  self.subsystems.drive.drive.set_mode(MotorModes.voltage)
        #  self.subsystems.drive.move(Vector(x, y, z))
        self.subsystems.reset()
        