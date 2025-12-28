# Input validators
from config.constants import DIRECTIONS

def validate_direction(direction):
    """
    Ensures direction sent by frontend is valid.
    """
    return direction in DIRECTIONS


def validate_stage(stage):
    """
    Ensures grid/speed stage is between 1 and 3.
    """
    return stage in [1, 2, 3]
