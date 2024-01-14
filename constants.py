from utils.FormatDictionary import FormatDictionary


Robot = FormatDictionary(
    {
        "controllers": {
            "driver": {"joystick": 0},
        },
        "directories": {"code": "/home/lvuser/py"},
        "ButtonInputs": {"follow_limelight_btnid": 0},
        "motors": {"front_left": 1, "front_right": 2, "back_left": 3, "back_right": 4}
    }
)
