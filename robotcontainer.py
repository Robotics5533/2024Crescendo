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
        self.drive_subsystem.drive.move(x, -y, x)

    def vision_error(self):
        self.drive_subsystem.drive.set_speed(5)
        x, y, z = self.vision_subsystem.limelight.getoffset()
        self.drive_subsystem.drive.move(0, 0, x)

    def configureButtongBindings(self):
        self.joystick.button(Robot.ButtonInputs.follow_limelight_btnid).whileTrue(
            cmd.run(self.follow_limelight, [self.drive_subsystem, self.vision_subsystem]))
        self.joystick.button(Robot.ButtonInputs.limelight_rotate).whileTrue(
            cmd.run(
                self.vision_error,
                [self.drive_subsystem, self.vision_subsystem]
            )
        )
        self.joystick.button(Robot.ButtonInputs.add_speed).whileTrue(
            cmd.run(lambda: self.drive_subsystem.drive.set_speed((self.drive_subsystem.drive.speed * 100) + 5), []))
        self.joystick.button(Robot.ButtonInputs.remove_speed).whileTrue(
            cmd.run(lambda: self.drive_subsystem.drive.set_speed((self.drive_subsystem.drive.speed * 100) - 5), []))


# avada kedavra
