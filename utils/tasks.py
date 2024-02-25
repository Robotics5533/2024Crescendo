import wpilib
from components.motor.Motor5533 import MotorModes

from subsystems.index import SubSystems
from utils.math.algebra import almost_equal


class Tasks:
    def __init__(self, timer, subsystems: SubSystems):
        self.timer = timer
        self.subsystems = subsystems
        self.total_time = 0
        self.command_idx = 0
        self.running_idx = -1
        
    def reset(self):
         self.running_idx = -1
         self.total_time = 0


    def timed_task(self, duration: float, *args):
        self.total_time += duration
        self.running_idx += 1
        def decorator(func):
                if self.command_idx != self.running_idx:
                     return
                if self.timer.get() < self.total_time:
                    func(*args)
                    self.command_idx += 1
                return func
        return decorator
    
    def position_task(self, distance: float, *args):
        self.running_idx += 1
        def decorator(func):
                if self.command_idx != self.running_idx:
                     return
                
                if almost_equal(self.subsystems.drive.drive.get_position(), distance):
                    self.command_idx += 1
                else: 
                     func(*args)
                return func
        return decorator