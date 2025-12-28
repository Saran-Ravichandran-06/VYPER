# Game loop and logic
import time
from core.snake import Snake
from core.food import Food
from core.timer import GameTimer
from core.state_manager import StateManager
from config.grid_stages import get_grid_config
from config.speed_stages import SPEED_STAGES
from config.constants import FOOD_TYPES

class GameEngine:
    def __init__(self, grid_stage, speed_stage):
        grid = get_grid_config(grid_stage)
        self.height = grid["height"]
        self.width = grid["width"]
        # internal maze walls (list of (x,y))
        self.internal_walls = grid.get("walls", [])
        self.grid_stage = grid_stage

        # Get speed stage config including mutton duration
        speed_config = SPEED_STAGES.get(speed_stage, SPEED_STAGES[1])
        self.speed_delay = speed_config["delay"]
        self.mutton_duration = speed_config["mutton_duration"]

        self.snake = Snake(start_row=1)
        self.food = Food(self.height, self.width, mutton_duration=self.mutton_duration)
        self.timer = GameTimer(grid_stage)
        self.state_manager = StateManager(self.height, self.width, additional_walls=self.internal_walls)

        self.score = 0
        self.game_over = False
        self.reason = ""
        self.emit_game_over = True
        self.paused = False

        # Generate food avoiding snake body and internal walls
        blocked = set(self.snake.body) | set(self.internal_walls)
        self.food.generate(blocked)

    def update_direction(self, direction):
        self.snake.set_direction(direction)

    def pause(self):
        self.paused = True
        try:
            self.timer.pause()
        except Exception:
            pass

    def resume(self):
        self.paused = False
        try:
            self.timer.resume()
        except Exception:
            pass

    def step(self):
        if self.game_over:
            return

        new_head = self.snake.move()

        x, y = new_head

        # Wall collision (border)
        if x == 0 or x == self.height - 1 or y == 0 or y == self.width - 1:
            self.end_game("Hit the wall")
            return

        # Internal wall collision (maze)
        if (x, y) in self.internal_walls:
            self.end_game("Hit the wall")
            return

        # Self collision
        if self.snake.check_self_collision():
            self.end_game("Snake bit itself")
            return

        # Check for chicken (primary food) collision
        if new_head == self.food.position:
            self.score += self.food.get_score()
            self.snake.move(grow=True)
            # If mutton was present, it should disappear when chicken is eaten
            blocked = set(self.snake.body) | set(self.internal_walls)
            self.food.generate(blocked)
        
        # Check for mutton (secondary food) collision
        elif new_head == self.food.secondary_position and self.food.secondary_position:
            self.score += FOOD_TYPES["mutton"]["score"]
            self.snake.move(grow=True)
            # After eating mutton, generate new food (chicken only, no dual)
            blocked = set(self.snake.body) | set(self.internal_walls)
            self.food.generate(blocked, spawn_dual=False)

        # Time over
        if self.timer.is_time_over():
            self.end_game("Time over")

    def end_game(self, reason, emit_game_over=True):
        """Mark the game as over. `emit_game_over` controls whether the
        background loop should emit a GAME_OVER event for this engine.
        """
        self.game_over = True
        self.reason = reason
        self.emit_game_over = emit_game_over

    def get_game_state(self):
        return {
            "grid": self.state_manager.build_grid(self.snake, self.food),
            "score": self.score,
            "time_left": self.timer.time_left(),
            "game_over": self.game_over,
            "reason": self.reason
        }
