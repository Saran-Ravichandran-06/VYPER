# Symbols and constants
# ==============================
# Grid Cell Symbols
# ==============================

EMPTY = "  "
WALL = "##"

SNAKE_HEAD = "██"
SNAKE_BODY = "▓▓"

CHICKEN = "🍗"
MUTTON = "🥩"


# ==============================
# Food Configuration
# ==============================

FOOD_TYPES = {
    "chicken": {
        "symbol": CHICKEN,
        "score": 1
    },
    "mutton": {
        "symbol": MUTTON,
        "score": 2
    }
}


# ==============================
# Directions
# ==============================

UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

DIRECTION_VECTORS = {
    UP: (-1, 0),
    DOWN: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1)
}

# Opposite directions (to prevent reverse movement)
OPPOSITE_DIRECTIONS = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT
}


# ==============================
# Game Settings
# ==============================

INITIAL_SNAKE_LENGTH = 3
GAME_TIME_LIMIT = 60  # seconds
