import wpilib


class Tasks:
    def __init__(self, timer):
        self.timer = timer
        self.ran = False
        self.total_time = 0
        
    def reset(self):
         self.ran = False
         self.total_time = 0

    def timed_task(self, duration: float, *args):
        self.total_time += duration

        def decorator(func):
                if self.ran:
                     return
                print(self.timer.get())
                if self.timer.get() < self.total_time:
                    func(*args)
                    self.ran = True
                return func
        return decorator