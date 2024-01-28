from components.inputs.ActionMap import ActionMap
from components.inputs.Lockdown import Lockdown
from utils.math.Vector import Vector


class RobotContainer:
    def __init__(self, subsystems, stick):
        self.subsystems = subsystems
        self.stick = stick
        self.teleop_lock = Lockdown()
        ActionMap.register_action("activate_limelight", self.teleop_lock.lockify(lambda: self.stick.getRawButton(1)))
        ActionMap.register_action("activate_climb", self.teleop_lock.lockify(lambda: self.stick.getRawButton(2)))
        ActionMap.register_action("activate_gyro", self.teleop_lock.lockify(lambda: self.stick.getRawButton(3)))
        
    def get_motion(self):
        return self.stick.getX(), self.stick.getY(), self.stick.getZ()
        
    def process(self):
         x, y, z = self.get_motion()
         self.subsystems.setup(
            self.subsystems.limelight.correct_error,
            ActionMap.get_action_pressed("activate_limelight"),
            [self.subsystems.drive, self.subsystems.limelight],
            
            self.subsystems.drive
        )
         
         self.subsystems.setup(
            self.subsystems.climb.move, 
            ActionMap.get_action_pressed("activate_climb"),
            [self.subsystems.climb],
            
            -y
        )
         
         self.subsystems.setup(
            self.subsystems.gyro.update_angle,
            ActionMap.get_action_pressed("activate_gyro"),
            [self.subsystems.drive, self.subsystems.gyro],
        )
         print(x, y, z)
         if not ActionMap.get_action_pressed("activate_climb"):
           self.subsystems.drive.move(Vector(x, y, z))
           
         self.subsystems.reset()