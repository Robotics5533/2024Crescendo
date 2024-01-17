from phoenix5 import hardware, configs,signals
import wpilib
import commands2
from components.drive.MecanumDrive import MecanumDrive
from constants import Robot


class DriveSubSystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        back_left_motor = hardware.TalonFX(Robot.motors.back_left)
        configurator=back_left_motor.configurator
        back_left_motor_new_configs = configs.MotorOutputConfigs()
        back_left_motor_new_configs.inverted = signals.InvertedValue.CLOCKWISE_POSITIVE
        configurator.apply(back_left_motor_new_configs)

        back_right_motor = hardware.TalonFX(Robot.motors.back_right)
        configurator=back_right_motor.configurator
        back_right_motor_new_configs = configs.MotorOutputConfigs()
        back_right_motor_new_configs.inverted = signals.InvertedValue.CLOCKWISE_POSITIVE
        configurator.apply(back_right_motor_new_configs)

        self.drive = MecanumDrive(hardware.TalonFX(Robot.motors.front_left),
                                  hardware.TalonFX(Robot.motors.front_right),
                                  back_right_motor,
                                  back_left_motor)
