from components.drive.Drive import Drive
from components.drive.MecanumDrive import MecanumDrive
import json
class PathPlanner:
    def __init__(self, path: str):
        with open(path, "r") as file:
            self._keyframes = json.load(file)
        self.current_speed = 0
        self.elapsed_time = 0
    @staticmethod
    def calculate(position_one: dict, position_two: dict, speed: float):
        f = lambda o, t: (t - o) / speed
        return {
            "x": f(position_one["x"], position_two["x"]),
            "y": f(position_one["y"], position_two["y"]),
            "z": f(position_one["z"], position_two["z"]),
        }

    def run(self, driveType: Drive):
        keyframes_list = self._keyframes["keyframes"]
        for i in range(len(keyframes_list) - 1):
            keyframe, next_keyframe = keyframes_list[i], keyframes_list[i + 1]
            delta_time = keyframe["frame_time"] + next_keyframe["frame_time"]
            length = self.calculate(
                keyframe["position"],
                next_keyframe["position"],
                delta_time
            )
            self.elapsed_time += delta_time
            driveType.move(length.x, length.y, length.z)
            