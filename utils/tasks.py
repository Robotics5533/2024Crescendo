import wpilib
from components.motor.Motor5533 import MotorModes

from subsystems.index import SubSystems
from utils.math.algebra import almost_equal


class Tasks:
    def __init__(self, timer: wpilib.Timer, subsystems: SubSystems):
        self.timer = timer
        self.subsystems = subsystems
        self.command_idx = 0
        self.total_time = 0
        self.running_idx = -1

    def reset(self):
        self.running_idx = -1
        self.total_time = 0

    def timed_task(self, duration: float, *args, **kwargs):
        self.total_time += duration
        return self.general(
            lambda: self.timer.get() >= self.total_time, *args, **kwargs
        )

    def position_task(self, distance: float, *args, **kwargs):
        return self.general(
            lambda: almost_equal(self.subsystems.drive.drive.get_position(), distance),
            *args,
            **kwargs
        )

    def next(self):
        self.command_idx += 1


    def reset_time(self) -> None:
        self.total_time = 0
        self.timer.reset()

    def gyro_task(self, angle: float, *args, **kwargs):
        kwargs["after"] = self.reset_time
        return self.general(
            lambda: almost_equal(self.subsystems.gyro.calculate(angle), 0),
            *args,
            **kwargs
        )

    def general(self, next, *args, **kwargs):
        def decorator(func):
            self.running_idx += 1
            if self.command_idx != self.running_idx:
                return
            if next():
                self.next()
            else:
                func(*args, **kwargs)

            return func

        return decorator
