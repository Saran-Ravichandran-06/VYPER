# Snake logic
from collections import deque
from config.constants import (
    DIRECTION_VECTORS,
    OPPOSITE_DIRECTIONS,
    INITIAL_SNAKE_LENGTH
)

class Snake:
    def __init__(self, start_row: int):
        # Snake starts moving LEFT → RIGHT
        self.direction = "RIGHT"

        self.body = deque()
        for col in range(INITIAL_SNAKE_LENGTH, 0, -1):
            self.body.append((start_row, col))

    def get_head(self):
        return self.body[0]

    def set_direction(self, new_direction):
        # Prevent reverse movement
        if OPPOSITE_DIRECTIONS[self.direction] != new_direction:
            self.direction = new_direction

    def move(self, grow=False):
        dx, dy = DIRECTION_VECTORS[self.direction]
        head_x, head_y = self.get_head()
        new_head = (head_x + dx, head_y + dy)

        self.body.appendleft(new_head)

        if not grow:
            self.body.pop()

        return new_head

    def check_self_collision(self):
        return self.get_head() in list(self.body)[1:]
