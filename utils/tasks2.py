import wpilib

from subsystems.index import SubSystems
from utils.math.algebra import almost_equal


class Tasks2:
    def __init__(self, timer: wpilib.Timer, subsystems: SubSystems):

        self.timer = timer
        self.subsystems = subsystems

        self.running_idx = 0
        self.command_idx = 0

    def reset(self):
        self.running_idx = 0
    
    def general(self, func, next, after):
        def decorated(*args,**kwargs):
            if self.command_idx != self.running_idx:
                self.running_idx += 1
                return
            func(*args,**kwargs)
            
            if next():
                self.command_idx += 1
                after()
            
            self.running_idx += 1
        return decorated


    def taskify(self, next,*args, **kwargs):
        
        after = lambda : 1
        if "after" in kwargs:
            after = kwargs["after"]

        def decorator(func):
            ret_val  = self.general(func,next,after)
            ret_val(*args,**kwargs)
            return ret_val
        
        return decorator

    def timed(self,**kwargs):
        run_time = kwargs["run_time"]

        def after():
            self.timer.reset()
            if "after" in kwargs:
                kwargs["after"]()
        # if "after" in kwargs:
        #     def x():
        #         kwargs["after"]()
        #         after()
        #     after = x
        
        return self.taskify(lambda : self.timer.get() >= run_time, after = after)
    
    def positioned(self, **kwargs):
        distance = kwargs["distance"]
        run_time = kwargs["run_time"]
        def after():
            self.timer.reset()
            if "after" in kwargs:
                kwargs["after"]()
        task_condition = lambda: almost_equal(self.subsystems.drive.drive.get_position(), distance) or self.timer.get() >= run_time
        return self.taskify(task_condition, after = after)
           
