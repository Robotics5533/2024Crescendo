import wpilib
from components.drive.Drive import Drive
from components.drive.MecanumDrive import MecanumDrive
import json
class PathPlanner:
    def __init__(self, path: str, timer: wpilib.Timer):
        with open(path, "r") as file:
            self._keyframes = json.load(file)
        self.current_speed = 0
        self.timer = timer
        self.elapsed_time = 0
        self.previous_time = 0
        self.index = 0

    @staticmethod
    def calculate(position_one: dict, position_two: dict, time_absolute: float, time_relative: float):
        f = lambda o, t: ((t - o) / (1 if time_relative == 0 else time_relative)) * time_absolute
        return {
            "x": f(position_one["x"], position_two["x"]),
            "y": f(position_one["y"], position_two["y"]),
            "z": f(position_one["z"], position_two["z"]),
        }
    def run(self, driveType: Drive):
        keyframes_list = self._keyframes["keyframes"]
        i = self.index
        unit = self._keyframes["unit"]
        keyframe = keyframes_list[i]
        if i >= len(keyframes_list) or i + 1 >= len(keyframes_list):
            return
        next_keyframe = keyframes_list[i + 1]
        delta_time_absolute = self.timer.get() - self.previous_time
        delta_time_relative = (next_keyframe["frame_time"] - keyframe["frame_time"]) * unit
        length = self.calculate(
            keyframe["position"],
            next_keyframe["position"],
            delta_time_absolute,
            delta_time_relative
        )
        if self.elapsed_time >= (delta_time_relative): 
            self.index += 1
            self.elapsed_time = 0
        self.elapsed_time += delta_time_absolute
        driveType.move(length["x"], length["y"], length["z"])
            