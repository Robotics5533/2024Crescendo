from autons.auton2 import Auton
from autons.autons.OnePieceNoTaxi import OnePieceNoTaxi
from autons.autons.TwoPiece import TwoPiece
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.math.algebra import linear_remap
from wpilib import DriverStation
class TwoPieceRight(Auton):
    def __init__(self, subsystems: SubSystems, timer):
        super().__init__(subsystems, timer)
        self.subsystems = subsystems
        self.one_piece = OnePieceNoTaxi(subsystems, timer, self.tasks)


    def get_note(self, last_duration = 0.425, first_duration = 0.3):
        self.flip(direction = -1, duration = 0.325)
        self.flip(direction = 1, duration = 0.1, speed = 0)
        self.intake(direction = 1, duration = 0.9, speed = Auton.Speeds.intake)
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = first_duration)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)

        self.flip(direction = 1, duration = 0.5)
        self.flip(direction = -1, duration = 0.1, speed = 0)
        self.intake(speed = 0, direction = 0, duration = 0.2)
        
    
    def shoot_note(self):
        self.shoot(speed = Auton.Speeds.shooter, direction = 1, duration = 0.7)
        self.intake(speed = Auton.Speeds.intake, direction = -1, duration = 0.45)
        self.stop()

    def move_left(self, duration: float, speed: float):
        self.drive(velocity = Vector(linear_remap(self.timer.get(), self.tasks.total_time - duration, self.tasks.total_time, 0, -speed), 0, self.subsystems.gyro.calculate(0)), duration = duration)
        self.drive(velocity = Vector(0, 0, self.subsystems.gyro.calculate(0)), duration = 0.3, brake = True)
    
    def move_right(self, duration: float, speed: float):
        self.move_left(duration, -speed)

    def run(self):
        self.shoot_note()
        
        self.drive(velocity = Vector(0, -0.9, self.subsystems.gyro.calculate(0)), duration = 0.285)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)


        self.drive(velocity = Vector(0, 0, -0.5), duration = 0.275)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        
        @self.tasks.timed_task(0.1, self.subsystems)
        def reset_gyro(subsystems: SubSystems):
            subsystems.gyro.reset()
            
        self.get_note(0.425, 0.485)

        self.drive(velocity = Vector(0, 0.9, 0), duration = 0.285)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)

        self.drive(velocity = Vector(0, 0, 0.5), duration = 0.35)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)

        self.drive(velocity = Vector(0, 0.9, 0), duration = 0.38)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        
        # self.drive(velocity = Vector(0, 0, -0.5), duration = 0.)
        # self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        
        self.shoot_note()

        self.drive(velocity = Vector(0, 0, -0.5), duration = 0.2)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)



        # Taxi
        self.drive(velocity = Vector(0, -0.9, 0), duration = 0.65)
        self.drive(velocity = Vector(0, 0, 0), duration = 0.3, brake = True)
        
        self.tasks.reset()

