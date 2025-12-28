# Unit tests
import time

from core.snake import Snake
from core.food import Food
from core.timer import GameTimer
from core.game_engine import GameEngine


# -----------------------------
# Snake Logic Tests
# -----------------------------

def test_snake_initial_state():
    snake = Snake(start_row=1)

    # Snake should have initial length
    assert len(snake.body) >= 3

    # Initial direction must be RIGHT
    assert snake.direction == "RIGHT"


def test_snake_moves_forward():
    snake = Snake(start_row=1)
    initial_head = snake.get_head()

    snake.move()
    new_head = snake.get_head()

    assert initial_head != new_head


def test_snake_prevents_reverse():
    snake = Snake(start_row=1)

    snake.set_direction("LEFT")  # Opposite of RIGHT
    assert snake.direction == "RIGHT"


# -----------------------------
# Food Logic Tests
# -----------------------------

def test_food_generation_not_on_snake():
    food = Food(grid_height=10, grid_width=10)
    snake_cells = {(1, 1), (1, 2), (1, 3)}

    food.generate(snake_cells)

    assert food.position not in snake_cells
    assert food.position is not None
    assert food.type in ["APPLE", "WATERMELON"]


# -----------------------------
# Timer Logic Tests
# -----------------------------

def test_timer_starts_with_full_time():
    timer = GameTimer()
    time_left = timer.time_left()

    assert time_left <= 60
    assert time_left > 0


def test_timer_not_over_immediately():
    timer = GameTimer()
    assert not timer.is_time_over()


# -----------------------------
# Game Engine Tests
# -----------------------------

def test_game_engine_initial_state():
    game = GameEngine(grid_stage=1, speed_stage=1)
    state = game.get_game_state()

    assert state["score"] == 0
    assert not state["game_over"]
    assert "grid" in state
    assert "time_left" in state


def test_game_engine_wall_collision():
    game = GameEngine(grid_stage=1, speed_stage=1)

    # Keep moving until wall collision happens
    for _ in range(100):
        game.step()
        if game.game_over:
            break

    assert game.game_over is True
    assert game.reason in ["Hit the wall", "Time over"]


def test_game_engine_food_consumption():
    game = GameEngine(grid_stage=1, speed_stage=1)

    # Force food in front of snake head
    head_x, head_y = game.snake.get_head()
    game.food.position = (head_x, head_y + 1)
    game.food.type = "APPLE"

    previous_score = game.score
    game.step()

    assert game.score > previous_score
