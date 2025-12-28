# Food logic
import random
import time
from config.constants import FOOD_TYPES

class Food:
    def __init__(self, grid_height, grid_width, mutton_duration=5.0):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.position = None
        self.type = None
        self.secondary_position = None
        self.secondary_type = None
        self.mutton_duration = mutton_duration
        self.secondary_spawn_time = None

    def generate(self, occupied_cells, spawn_dual=None):
        """Generate food. If spawn_dual is True, spawn both chicken and mutton.
        If None, randomly decide (30% chance for dual).
        """
        # Decide whether to spawn dual food
        if spawn_dual is None:
            spawn_dual = random.random() < 0.3
        
        # Generate primary food (chicken)
        self.type = "chicken"
        self.secondary_position = None
        self.secondary_type = None
        self.secondary_spawn_time = None
        
        while True:
            x = random.randint(1, self.grid_height - 2)
            y = random.randint(1, self.grid_width - 2)
            
            if (x, y) not in occupied_cells:
                self.position = (x, y)
                break
        
        # Generate secondary food (mutton) if dual spawn
        if spawn_dual:
            occupied_cells = occupied_cells | {self.position}
            self.secondary_type = "mutton"
            self.secondary_spawn_time = time.time()
            
            while True:
                x = random.randint(1, self.grid_height - 2)
                y = random.randint(1, self.grid_width - 2)
                
                if (x, y) not in occupied_cells:
                    self.secondary_position = (x, y)
                    break
    
    def is_mutton_expired(self):
        """Check if mutton has expired based on its duration."""
        if self.secondary_spawn_time is None:
            return False
        return (time.time() - self.secondary_spawn_time) > self.mutton_duration
    
    def clear_expired_mutton(self):
        """Clear mutton if it has expired."""
        if self.is_mutton_expired():
            self.secondary_position = None
            self.secondary_type = None
            self.secondary_spawn_time = None

    def get_score(self):
        return FOOD_TYPES[self.type]["score"]
