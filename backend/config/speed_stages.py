# Speed stages
# Speed stages (in seconds per move)

SPEED_STAGES = {
    1: {
        "name": "Slow",
        "delay": 0.24,
        "mutton_duration": 5.0
    },
    2: {
        "name": "Medium",
        "delay": 0.18,
        "mutton_duration": 4.0
    },
    3: {
        "name": "Fast",
        "delay": 0.12,
        "mutton_duration": 3.0
    }
}


def get_speed_delay(stage: int):
    """
    Returns delay time for the selected speed stage.
    Defaults to Slow if invalid stage is given.
    """
    return SPEED_STAGES.get(stage, SPEED_STAGES[1])["delay"]
