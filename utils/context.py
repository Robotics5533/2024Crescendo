import wpilib

from utils.math.Vector import Vector


class Context:
    def __init__(self, robot, run_time: float = 0):
        self.robot = robot
        self.last_position = Vector(0, 0, 0)
        self.time = 0
        self.timer = wpilib.Timer()
        self.run_time = run_time
    def next(self):
        if self.timer.get() == 0:
            self.timer.start()
        return self.timer.get() - self.time > self.run_time
    def rotate(self, angle: float):
        pass

    def move(self, point: Vector):
        speed = abs(point.pythagorean(self.last_position))
        self.robot.subsystems.drive.mecanum.set_speed((speed, speed, speed))
        self.robot.subsystems.drive.mecanum.move(point)
        self.time = self.timer.get()
        self.last_position = point


    def get_position():
        pass