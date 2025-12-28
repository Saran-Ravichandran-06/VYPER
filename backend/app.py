import eventlet
eventlet.monkey_patch()  # MUST be first

import os
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

from sockets.game_socket import register_game_socket

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "snake-game-secret")

# CORS (explicit, not lazy)
CORS_ORIGINS = [
    "http://localhost:5173",
    "https://vyper.vercel.app"
    ]

CORS(app, origins=CORS_ORIGINS)

socketio = SocketIO(
    app,
    cors_allowed_origins=CORS_ORIGINS,
    async_mode="eventlet"
)

register_game_socket(socketio)

@app.route("/")
def health_check():
    return {
        "status": "running",
        "message": "Snake Game Backend is active"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Backend running on port {port}")
    socketio.run(app, host="0.0.0.0", port=port)
