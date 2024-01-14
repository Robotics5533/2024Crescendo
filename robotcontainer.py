from components.vision.limelight import Limelight
from subsystems.drive import DriveSubSystem
import commands2
import wpilib
from commands2 import button
from commands2 import cmd
from constants import Robot
from subsystems.vision import VisionSubSystem

class RobotContainer:
    def __init__(self) -> None:
        self.drive_subsystem = DriveSubSystem()
        self.vision_subsystem = VisionSubSystem()
        self.joystick = button.CommandJoystick(Robot.controllers.driver.joystick)
        command_drive = lambda: self.drive_subsystem.drive.move(
            self.joystick.getX(),
            self.joystick.getY(),
            self.joystick.getZ(),
        )
        self.drive_subsystem.setDefaultCommand(cmd.run(command_drive, [self.drive_subsystem]))
        self.configureButtongBindings()
        
    def follow_limelight(self): 
        x, y, z = self.vision_subsystem.limelight.getoffset()
        self.drive_subsystem.drive.move(x, -y, z)
        
    def configureButtongBindings(self):
        self.joystick.button(Robot.ButtonInputs.follow_limelight_btnid).whileTrue(cmd.run(self.follow_limelight, [self.drive_subsystem, self.vision_subsystem]))
        


## avada kedavra
