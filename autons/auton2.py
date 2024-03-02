from components.motor.Motor5533 import MotorModes
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.tasks import Tasks


class Auton:
    class Speeds:
        shooter = 80
        intake = 95
    def __init__(self, subsystems, timer):
        self.subsystems = subsystems
        self.timer = timer
        self.tasks = Tasks(self.timer, subsystems)
        

    def shoot(self, **kwargs):
        duration = kwargs["duration"]
        speed = kwargs["speed"]
        direction = kwargs["direction"]
        @self.tasks.timed_task(duration, self.subsystems, speed)
        def shooter(subsystems: SubSystems, speed: float):
            subsystems.shooter.shoot(speed * direction)

    def intake(self, **kwargs):
        duration = kwargs["duration"]
        speed = kwargs["speed"]
        direction = kwargs["direction"]
        @self.tasks.timed_task(duration, self.subsystems, speed)
        def intake(subsystems: SubSystems, speed: float):
            subsystems.intake.run(speed * direction)

    def stop(self):
        @self.tasks.timed_task(0.2, self.subsystems)
        def stop(subsystems: SubSystems):
            subsystems.shooter.shoot(0)
            subsystems.intake.run(0)
            subsystems.intake_control.run(0)


    def drive(self, **kwargs):
        duration = kwargs["duration"]
        velocity = kwargs["velocity"]
        brake = kwargs["brake"] if "brake" in kwargs else False
        @self.tasks.timed_task(duration, self.subsystems)
        def drive(subsystems: SubSystems):
            subsystems.drive.drive.set_mode(MotorModes.voltage)
            subsystems.drive.move(velocity)
            if brake:
                subsystems.drive.drive.set_mode(MotorModes.static_brake)
                subsystems.drive.move(Vector(0, 0, 0))
    def rotate(self, **kwargs):
        angle = kwargs["angle"]
        @self.tasks.gyro_task(angle,self.subsystems)
        def rotate(subsystems : SubSystems):
            subsystems.drive.move(Vector(0,0,subsystems.gyro.calculate(angle)))

    def flip(self, **kwargs):
        duration = kwargs["duration"]
        direction = kwargs["direction"]
        speed = kwargs["speed"] if "speed" in kwargs else 0.0035
        @self.tasks.timed_task(duration, self.subsystems)
        def intake_control(subsystems: SubSystems):
            print(speed * direction)
            subsystems.intake_control.run(speed * direction)
