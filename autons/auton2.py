from wpilib import DriverStation
from components.motor.Motor5533 import MotorModes
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.math.algebra import linear_remap
from utils.tasks import Tasks




class Auton:
    class Speeds:
        shooter = 90
        intake = 95
    def __init__(self, subsystems, timer, tasks = None):
        self.subsystems = subsystems
        self.timer = timer
        self.tasks = Tasks(self.timer, subsystems) if tasks == None else tasks
        self.subsystems.drive.drive.speed_multiplier = 12 / DriverStation.getBatteryVoltage()
        self.invert = {}
    
    def is_inverted(self, axis: str) -> bool:
        return axis in self.invert and self.invert[axis]
    
    def invert(self, **kwargs):
        self.invert = kwargs

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
            subsystems.drive.move(velocity.map(lambda x, i: -x if self.is_inverted(Vector.index_to_name(i)) else x))
            if brake:
                subsystems.drive.drive.set_mode(MotorModes.static_brake)
                subsystems.drive.move(Vector(0, 0, 0))

    def rotate(self, **kwargs):
        angle = kwargs["angle"]
        @self.tasks.gyro_task(angle, self.subsystems)
        def rotate(subsystems: SubSystems):
            subsystems.drive.move(Vector(0,0, subsystems.gyro.calculate(angle)))

    def flip(self, **kwargs):
        duration = kwargs["duration"]
        direction = kwargs["direction"]
        speed = kwargs["speed"] if "speed" in kwargs else 0.0035
        @self.tasks.timed_task(duration, self.subsystems)
        def intake_control(subsystems: SubSystems):
            print(speed * direction)
            subsystems.intake_control.run(speed * direction)
    
    def get_note(self):
        self.flip(direction = -1, duration = 0.3)
        self.flip(direction = 1, duration = 0.1, speed = 0)
        self.intake(direction = 1, duration = 0.9, speed = Auton.Speeds.intake)
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.56)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.5, brake = True)
        self.flip(direction = 1, duration = 0.5)
        self.flip(direction = -1, duration = 0.1, speed = 0)
        self.intake(speed = 0, direction = 0, duration = 0.2)
        self.drive(velocity = Vector(0, 0.9, self.subsystems.gyro.calculate(0)), duration = 0.525)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
    
    def shoot_note(self):
        self.shoot(speed = Auton.Speeds.shooter, direction = 1, duration = 0.7)
        self.intake(speed = Auton.Speeds.intake, direction = -1, duration = 0.45)
        self.stop()

    def move_left(self, duration: float, speed: float):
        self.drive(velocity = Vector(linear_remap(self.timer.get(), self.tasks.total_time - duration, self.tasks.total_time, 0, -speed), 0, self.subsystems.gyro.calculate(0)), duration = duration)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
    
    def move_right(self, duration: float, speed: float):
        self.move_left(duration, -speed)
