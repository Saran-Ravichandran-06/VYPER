# Game state management
from config.constants import (
    EMPTY, WALL, SNAKE_HEAD, SNAKE_BODY,
    CHICKEN, MUTTON, FOOD_TYPES
)

class StateManager:
    def __init__(self, height, width, additional_walls=None):
        self.height = height
        self.width = width
        self.additional_walls = additional_walls or []

    def build_grid(self, snake, food):
        grid = [[EMPTY for _ in range(self.width)] for _ in range(self.height)]

        # Border Walls
        for i in range(self.height):
            grid[i][0] = WALL
            grid[i][-1] = WALL

        for j in range(self.width):
            grid[0][j] = WALL
            grid[-1][j] = WALL

        # Additional internal walls (for maze)
        for (wx, wy) in self.additional_walls:
            if 0 <= wx < self.height and 0 <= wy < self.width:
                grid[wx][wy] = WALL

        # Snake
        head_x, head_y = snake.get_head()
        grid[head_x][head_y] = SNAKE_HEAD

        for x, y in list(snake.body)[1:]:
            grid[x][y] = SNAKE_BODY

        # Food - primary (chicken)
        if food.position:
            fx, fy = food.position
            grid[fx][fy] = FOOD_TYPES[food.type]["symbol"]
        
        # Food - secondary (mutton) if it exists and hasn't expired
        food.clear_expired_mutton()
        if food.secondary_position and food.secondary_type:
            sx, sy = food.secondary_position
            if 0 <= sx < self.height and 0 <= sy < self.width:
                grid[sx][sy] = FOOD_TYPES[food.secondary_type]["symbol"]

        return grid
