import wpilib


class Context:
    def __init__(self, robot, run_time: float = 0):
        self.robot = robot
        self.last_position = (0, 0)
        self.time = 0
        self.timer = wpilib.Timer()
        self.run_time = run_time
    def next(self):
        if self.timer.get() == 0:
            self.timer.start()
        return self.timer.get() - self.time > self.run_time
    def rotate(self, angle: float):
        pass
    def move(self, t):
        (x2, y2) = t
        (x1, y1) = self.last_position
        speed = abs(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
        self.robot.drive.set_speed(speed)
        self.robot.drive.move(x2, y2, 0)
        self.time = self.timer.get()
        self.last_position = (x2, y2)


    def get_position():
        pass