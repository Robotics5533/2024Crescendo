import wpilib

from subsystems.index import SubSystems
from utils.math.algebra import almost_equal


class Tasks2:
    def __init__(self, timer: wpilib.Timer, subsystems: SubSystems):

        self.timer = timer
        self.subsystems = subsystems

        self.running_idx = 0
        self.command_idx = 0
        print("running the init function of tasks2")

    def reset(self):
        self.running_idx = 0
    
    def general(self, func, next, after):
        def decorated(*args,**kwargs):
            if self.command_idx != self.running_idx:
                self.running_idx += 1
            else:
            

                func(*args,**kwargs)
                
                if next():
                    self.increase_command_idx()
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

    def timed_task(self,**kwargs):
        duration = kwargs["duration"]

        def after():
            self.timer.reset()
            if "after" in kwargs:
                kwargs["after"]()
        # if "after" in kwargs:
        #     def x():
        #         kwargs["after"]()
        #         after()
        #     after = x
        
        return self.taskify(lambda : self.timer.get() >= duration, after = after)
    
    def increase_command_idx(self):
        self.command_idx += 1

    def position_task(self, **kwargs):
        local_unit = 1 / self.subsystems.drive.drive.conversion
        distance = kwargs["distance"]
        duration = kwargs["duration"]
        def after():
            self.timer.reset()
            self.subsystems.drive.drive.set_position(0)
            self.subsystems.drive.drive.set_averages(0)
            self.subsystems.drive.drive.reset_pid()
            print("we hit the target position!")
            print(self.command_idx)
            if "after" in kwargs:
                kwargs["after"]()
            

        
        task_condition = lambda: almost_equal(self.subsystems.drive.drive.get_position() * local_unit, distance, 2.5) or self.timer.get() >= duration
        return self.taskify(task_condition, after = after)
           
