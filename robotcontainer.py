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
        self.joystick = button.CommandJoystick(
            Robot.controllers.driver.joystick)
        self.limelight_follow_speed = 8
        self.teleop_speed = 25
        self.drive_subsystem.setDefaultCommand(
            cmd.run(self.command_drive, [self.drive_subsystem]))
        self.configureButtongBindings()

    def command_drive(self):
        self.drive_subsystem.drive.set_speed(self.teleop_speed)
        self.drive_subsystem.drive.move(
            self.joystick.getX(),
            self.joystick.getY(),
            self.joystick.getZ(),
        )

    def follow_limelight(self):
        self.drive_subsystem.drive.set_speed(self.limelight_follow_speed)
        x, y, z = self.vision_subsystem.limelight.getoffset()
        self.drive_subsystem.drive.move(x, -y, z)

    def configureButtongBindings(self):
        self.joystick.button(Robot.ButtonInputs.follow_limelight_btnid).whileTrue(
            cmd.run(self.follow_limelight, [self.drive_subsystem, self.vision_subsystem]))


# avada kedavra
