# WebSocket handlers
from flask_socketio import emit
import socketio
from core.game_engine import GameEngine
from sockets.events import (
    INIT_GAME,
    CHANGE_DIRECTION,
    GAME_STATE,
    GAME_OVER,
    ERROR
)
from sockets.events import PAUSE_GAME, RESUME_GAME

# Store active game instance (single-player)
game_engine = None


def register_game_socket(socketio):
    """
    Registers all WebSocket events related to the game.
    """

    @socketio.on(INIT_GAME)
    def handle_init_game(data):
        global game_engine
        try:
            grid_stage = data.get("grid_stage", 1)
            speed_stage = data.get("speed_stage", 1)
        # If an existing game is running, mark it over so its loop exits
            if game_engine and not game_engine.game_over:
                # End previous game but suppress its GAME_OVER emission
                game_engine.end_game("Restarted", emit_game_over=False)

            # Create a fresh engine instance and keep a global reference
            engine = GameEngine(grid_stage, speed_stage)
            game_engine = engine

            # Start background loop bound to the specific engine instance
            socketio.start_background_task(run_game_loop, socketio, engine)
        except Exception as e:
            emit(ERROR, {"message": str(e)})


    @socketio.on(CHANGE_DIRECTION)
    def handle_change_direction(data):
        """
        data = {
            direction: "UP" | "DOWN" | "LEFT" | "RIGHT"
        }
        """
        global game_engine

        if not game_engine or game_engine.game_over:
            return

        direction = data.get("direction")
        if direction:
            game_engine.update_direction(direction)

    @socketio.on(PAUSE_GAME)
    def handle_pause_game(_data=None):
        """Pause the active game loop so the engine does not advance."""
        global game_engine
        if game_engine and not game_engine.game_over:
            try:
                game_engine.pause()
            except Exception:
                pass

    @socketio.on(RESUME_GAME)
    def handle_resume_game(_data=None):
        """Resume the active game loop."""
        global game_engine
        if game_engine and not game_engine.game_over:
            try:
                game_engine.resume()
            except Exception:
                pass


def run_game_loop(socketio, engine):
    """
    Background game loop bound to a specific engine instance.
    This prevents previously-started background tasks from accidentally
    continuing to drive newly-created engines when the global reference
    is reassigned.
    """

    while engine and not engine.game_over:
        socketio.sleep(engine.speed_delay)
        # If paused, do not advance the engine; still emit current state so
        # connected clients see the board frozen.
        if getattr(engine, "paused", False):
            socketio.emit(GAME_STATE, engine.get_game_state())
            continue

        engine.step()
        socketio.emit(GAME_STATE, engine.get_game_state())

    if engine and getattr(engine, "emit_game_over", True):
        socketio.emit(GAME_OVER, {
            "final_score": engine.score,
            "reason": engine.reason
        })


