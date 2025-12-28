# Timer logic
import time
from config.constants import GAME_TIME_LIMIT

class GameTimer:
    def __init__(self, grid_stage="freestyle"):
        self.grid_stage = grid_stage
        self.start_time = time.time()
        self.paused = False
        self.pause_start = None
        self.accumulated_pause = 0.0
        # Only apply time limit for maze mode, not for freestyle (classic)
        self.has_time_limit = (grid_stage == "maze")

    def time_left(self):
        if not self.has_time_limit:
            return -1  # Return -1 to indicate no time limit (instead of infinity)
        
        now = time.time()
        if self.paused and self.pause_start is not None:
            elapsed = self.pause_start - self.start_time - self.accumulated_pause
        else:
            elapsed = now - self.start_time - self.accumulated_pause
        remaining = max(0, GAME_TIME_LIMIT - int(elapsed))
        return remaining

    def is_time_over(self):
        if not self.has_time_limit:
            return False
        return self.time_left() <= 0

    def pause(self):
        if not self.paused:
            self.paused = True
            self.pause_start = time.time()

    def resume(self):
        if self.paused and self.pause_start is not None:
            paused_duration = time.time() - self.pause_start
            self.accumulated_pause += paused_duration
            self.pause_start = None
            self.paused = False
