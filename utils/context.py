import wpilib

from utils.math.Vector import Vector


class Context:
    def __init__(self, robot, run_time: float = 0):
        self.robot = robot
        self.last_position = Vector(0, 0, 0)
        self.time = 0
        self.timer = wpilib.Timer()
        self.run_time = run_time
        self.operation = lambda: True
        self.move_distance = 0
        
    def get_operation(self):
        return self.operation
    
    def set_operation(self, operation):
        self.operation = operation
        
    @staticmethod
    def get_rotation():
        pass
    
    @staticmethod
    def get_position():
        pass
    
    def get_data(self):
        return self.data
        
    def next(self):
        if self.timer.get() == 0:
            self.timer.start()
        # self.timer.get() - self.time > self.run_time
        return self.get_operation()()
    
    def rotate(self, angle: float):
        pass
    
    
    
    def move_operation(self):
        return self.robot.subsystems.drive.drive.get_position() > self.move_distance
        
    def move(self, data):
        self.data = data
        # self.robot.subsystems.drive.drive.set_mode(0)
        self.set_operation(self.move_operation)
        distance = self.last_position.pythagorean(self.get_data())
        self.move_distance = distance
        self.robot.subsystems.drive.move(Vector(0, distance, 0))
        self.last_position = self.get_data()
