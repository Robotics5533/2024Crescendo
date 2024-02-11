import wpilib
from components.drive.TankDrive import TankDrive
from components.drive.MecanumDrive import MecanumDrive
from components.motor.Talon5533 import Talon5533

front_left = 1
front_right = 2
back_left = 3
back_right = 4
class Robot:
    class Drive:
        # tank = TankDrive(
        #     wpilib.MotorControllerGroup(wpilib.PWMSparkMax(0), wpilib.PWMSparkMax(1)),
        #     wpilib.MotorControllerGroup(wpilib.PWMSparkMax(2), wpilib.PWMSparkMax(3)),
        # )
        mecanum = MecanumDrive(
            Talon5533(front_left),
            Talon5533(front_right),
            Talon5533(back_left),
            Talon5533(back_right),
        )

    class Controllers:
        joystick = 0
        xbox = 1
    class motors:
        front_left = front_left
        front_right = front_right
        back_left = back_left
        back_right = back_right
        climb = 5
