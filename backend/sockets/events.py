# Event names
# Client → Server events
INIT_GAME = "init_game"          # Start new game
CHANGE_DIRECTION = "change_dir"  # User presses arrow key
PAUSE_GAME = "pause_game"        # Pause the running game (client → server)
RESUME_GAME = "resume_game"      # Resume the running game (client → server)

# Server → Client events
GAME_STATE = "game_state"        # Send updated grid
GAME_OVER = "game_over"          # Game finished
ERROR = "error"                  # Error handling
