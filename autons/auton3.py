from wpilib import DriverStation
from components.motor.Motor5533 import MotorModes
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.tasks2 import Tasks2


class Auton3:
    class Speeds:
        shooter = 90
        intake = 95
    def __init__(self, subsystems, timer, tasks = None):
        self.subsystems = subsystems
        self.timer = timer
        self.tasks = Tasks2(self.timer, subsystems) if tasks == None else tasks
        self.subsystems.drive.drive.speed_multiplier = 12 / DriverStation.getBatteryVoltage()

    def shoot(self, **kwargs):
        duration = kwargs["duration"]
        speed = kwargs["speed"]
        direction = kwargs["direction"]
        @self.tasks.timed_task(duration = duration)
        def shooter(*args, **kwargs):
            self.subsystems.shooter.shoot(speed * direction)

    def intake(self, **kwargs):
        duration = kwargs["duration"]
        speed = kwargs["speed"]
        direction = kwargs["direction"]
        @self.tasks.timed_task(duration = duration)
        def intake(*args, **kwargs):
            self.subsystems.intake.run(speed * direction)

    def stop(self):
        @self.tasks.timed_task(duration = 0.05)
        def stop(*args, **kwargs):
            self.subsystems.shooter.shoot(0)
            self.subsystems.intake.run(0)
            self.subsystems.intake_control.run(0)


    def drive(self, **kwargs):
        duration = kwargs["duration"] if "duration" in kwargs else 999
        position = kwargs["position"]
        distance = kwargs["distance"] if "distance" in kwargs else position.magnitude()
        brake = kwargs["brake"] if "brake" in kwargs else False
        @self.tasks.position_task(duration = duration, distance = distance)
        def drive(*args, **kwargs):
            self.subsystems.drive.drive.set_mode(MotorModes.position)
            self.subsystems.drive.move(position)
            if brake:
                self.subsystems.drive.drive.set_mode(MotorModes.static_brake)
                self.subsystems.drive.move(Vector(0, 0, 0))


    def flip(self, **kwargs):
        duration = kwargs["duration"]
        direction = kwargs["direction"]
        speed = kwargs["speed"] if "speed" in kwargs else 0.0035
        @self.tasks.timed_task(duration = duration)
        def intake_control(*args, **kwargs):
            self.subsystems.intake_control.run(speed * direction)

    def reset(self, **kwargs):
        @self.tasks.timed_task(duration = 0.05)
        def reset_position(*args, **kwargs):
            self.subsystems.drive.drive.set_position(0)
