import wpilib
from autons.auton import Auton
from components.motor.Motor5533 import MotorModes
from subsystems.index import SubSystems
from utils.math.Vector import Vector
from utils.tasks import Tasks

class FourPiece(Auton):
    def __init__(self, subsystems, timer):
        self.subsystems = subsystems
        self.timer = timer
        self.tasks = Tasks(self.timer, subsystems)

    def run(self):
        @self.tasks.timed_task(0.5, self.subsystems, 50)
        def shooter(subsystems: SubSystems, speed: float):
            subsystems.shooter.shoot(speed)

        @self.tasks.timed_task(0.45, self.subsystems, -80)
        def intake(subsystems: SubSystems, speed: float):
            subsystems.intake.run(speed)

        @self.tasks.timed_task(0.2, self.subsystems)
        def stop(subsystems: SubSystems):
            subsystems.shooter.shoot(0)
            subsystems.intake.run(0)

        @self.tasks.timed_task(0.3, self.subsystems)
        def intake_control(subsystems: SubSystems):
            subsystems.intake_control.run(-0.0035)


        @self.tasks.timed_task(0.6, self.subsystems, 95)
        def intake(subsystems: SubSystems, speed: float):
            subsystems.intake_control.run(0)
            subsystems.intake.run(speed)
        
        @self.tasks.timed_task(0.4, self.subsystems)
        def drive(subsystems: SubSystems):
            subsystems.drive.drive.set_mode(MotorModes.voltage)
            subsystems.drive.move(Vector(0, -0.7, 0))
        
        @self.tasks.timed_task(0.5, self.subsystems)
        def drive(subsystems: SubSystems):
            subsystems.drive.drive.set_mode(MotorModes.static_brake)
            subsystems.drive.move(Vector(0, 0, 0))
            subsystems.drive.drive.set_mode(MotorModes.voltage)
            subsystems.drive.move(Vector(0, 0, 0))

        @self.tasks.timed_task(0.5, self.subsystems)
        def intake_control(subsystems: SubSystems):
            subsystems.intake.run(0)
            subsystems.intake_control.run(0.0035)

        @self.tasks.timed_task(0.2, self.subsystems)
        def intake(subsystems: SubSystems):
            subsystems.intake_control.run(0)

        @self.tasks.timed_task(0.5, self.subsystems)
        def drive(subsystems: SubSystems):
            subsystems.drive.drive.set_mode(MotorModes.voltage)
            subsystems.drive.move(Vector(0, 0.9, 0))

        @self.tasks.timed_task(0.3, self.subsystems)
        def drive(subsystems: SubSystems):
            subsystems.drive.drive.set_mode(MotorModes.static_brake)
            subsystems.drive.move(Vector(0, 0, 0))
            subsystems.drive.drive.set_mode(MotorModes.voltage)
            subsystems.drive.move(Vector(0, 0, 0))

        @self.tasks.timed_task(0.5, self.subsystems, 50)
        def shooter(subsystems: SubSystems, speed: float):
            subsystems.shooter.shoot(speed)

        @self.tasks.timed_task(0.45, self.subsystems, -90)
        def intake(subsystems: SubSystems, speed: float):
            subsystems.intake.run(speed)

        @self.tasks.timed_task(0.3, self.subsystems)
        def stop(subsystems: SubSystems):
            subsystems.shooter.shoot(0)
            subsystems.intake.run(0)
        
        @self.tasks.timed_task(0.9, self.subsystems)
        def drive(subsystems: SubSystems):
            subsystems.drive.drive.set_mode(MotorModes.voltage)
            subsystems.drive.move(Vector(-0.9, 0, 0))
        
        @self.tasks.timed_task(0.6, self.subsystems)
        def intake_control(subsystems: SubSystems):
            subsystems.drive.drive.set_mode(MotorModes.static_brake)
            subsystems.drive.move(Vector(0, 0, 0))
            subsystems.drive.drive.set_mode(MotorModes.voltage)
            subsystems.drive.move(Vector(0, 0, 0))
            subsystems.intake_control.run(-0.0025)

        @self.tasks.timed_task(0.4, self.subsystems)
        def drive(subsystems: SubSystems):
            subsystems.drive.drive.set_mode(MotorModes.voltage)
            subsystems.drive.move(Vector(0, -0.7, 0))
        
        @self.tasks.timed_task(0.5, self.subsystems)
        def drive(subsystems: SubSystems):
            subsystems.drive.drive.set_mode(MotorModes.static_brake)
            subsystems.drive.move(Vector(0, 0, 0))
            subsystems.drive.drive.set_mode(MotorModes.voltage)
            subsystems.drive.move(Vector(0, 0, 0))

        @self.tasks.timed_task(0.3, self.subsystems)
        def intake(subsystems: SubSystems):
            subsystems.intake_control.run(0)
            subsystems.intake.run(80)

        @self.tasks.timed_task(0.3, self.subsystems)
        def intake(subsystems: SubSystems):
            subsystems.intake_control.run(0)
            subsystems.intake.run(0)

        

        

        self.tasks.reset()