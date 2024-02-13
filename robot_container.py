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
        self.action_map.register_action("control_intake", self.teleop_lock.lockify(lambda: (self.xbox.getLeftTriggerAxis() + self.xbox.getRightTriggerAxis()) > 0.1))
        self.action_map.register_action("control_intake_STOP", self.teleop_lock.lockify(lambda: not self.action_map.get_action_pressed("control_intake")))
    
    def get_motion(self):
        return (self.stick.getX(), self.stick.getY(), self.stick.getZ())
        
    def process(self):

         self.subsystems.setup(
            self.subsystems.intake_control.run,
            self.action_map.get_action_pressed("control_intake"),
            [],

                0        
                )
         
         
        #  self.subsystems.setup(
        #     self.subsystems.intake_control.run,
        #     self.action_map.get_action_pressed("control_intake_STOP"),
        #     [],

        #     0
            
        # )
         
         self.subsystems.reset()
         