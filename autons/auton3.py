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
        @self.tasks.timed_task(self.subsystems, speed, duration = duration)
        def shooter(subsystems: SubSystems, speed: float):
            subsystems.shooter.shoot(speed * direction)

    def intake(self, **kwargs):
        duration = kwargs["duration"]
        speed = kwargs["speed"]
        direction = kwargs["direction"]
        @self.tasks.timed_task(self.subsystems, speed, duration = duration)
        def intake(subsystems: SubSystems, speed: float):
            subsystems.intake.run(speed * direction)

    def stop(self):
        @self.tasks.timed_task(self.subsystems, duration = 0.05)
        def stop(subsystems: SubSystems):
            subsystems.shooter.shoot(0)
            subsystems.intake.run(0)
            subsystems.intake_control.run(0)


    def drive(self, **kwargs):
        duration = kwargs["duration"]
        distance = kwargs["distance"]
        position = kwargs["position"]
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
        @self.tasks.timed_task(self.subsystems, duration = duration)
        def intake_control(subsystems: SubSystems):

            subsystems.intake_control.run(speed * direction)
