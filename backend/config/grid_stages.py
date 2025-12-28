# Grid stages
# Grid difficulty stages
# Each stage defines HEIGHT and WIDTH

"""Grid configuration.

This project now supports two named grid types:
- `freestyle`: an open 10x10 board (no internal walls)
- `maze`: a 10x10 board with an internal maze layout

For backward compatibility the function will also accept numeric stages
and map them to `freestyle`.
"""


def get_grid_config(stage):
    """Return a dict with `height`, `width` and optional `walls` list.

    `stage` can be a string: 'freestyle' or 'maze', or an int for
    backward compatibility (treated as 'freestyle').
    """
    # Default size (width x height) changed to 24x18 per request
    height = 19
    width = 27

    # Maze layout: mirrored Ls in corners and a central 4-way joint (plus).
    maze_walls = []

    # Parameters for arms
    left_col = 4
    right_col = width - 5  
    top_v_start = 3
    top_v_end = 6
    bottom_v_start = height - 7  
    bottom_v_end = height - 4
    arm_h_len = 6

    # Top-left mirrored L (vertical then horizontal to the right)
    maze_walls += [(r, left_col) for r in range(top_v_start, top_v_end + 1)]
    maze_walls += [(top_v_end, c) for c in range(left_col, left_col + arm_h_len-1)]

    # Top-right L (vertical then horizontal to the left)
    maze_walls += [(r, right_col) for r in range(top_v_start, top_v_end + 1)]
    maze_walls += [(top_v_end, c) for c in range(right_col - arm_h_len + 2, right_col + 1)]

    # Bottom-left upside-down L (horizontal then vertical downward)
    maze_walls += [(bottom_v_start, c) for c in range(left_col, left_col + arm_h_len-1)]
    maze_walls += [(r, left_col) for r in range(bottom_v_start, bottom_v_end + 1)]

    # Bottom-right mirrored upside-down L
    maze_walls += [(bottom_v_start, c) for c in range(right_col - arm_h_len + 2, right_col + 1)]
    maze_walls += [(r, right_col) for r in range(bottom_v_start, bottom_v_end + 1)]

    # Central plus (4-way joint)
    center_row = height // 2  
    center_col = width // 2   
    plus_arm = 3
    maze_walls += [(center_row, c) for c in range(center_col - plus_arm, center_col + plus_arm + 1)]
    maze_walls += [(r, center_col) for r in range(center_row - plus_arm, center_row + plus_arm + 1)]

    # Normalize input
    if isinstance(stage, str):
        stage_name = stage.lower()
    else:
        stage_name = "freestyle"

    if stage_name == "maze":
        return {"name": "Maze", "height": height, "width": width, "walls": maze_walls}

    # Default: freestyle
    return {"name": "Freestyle", "height": height, "width": width}
