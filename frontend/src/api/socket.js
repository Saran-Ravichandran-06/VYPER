import { io } from "socket.io-client";
import { SOCKET_EVENTS } from "../constants/events";

const SOCKET_URL =
  import.meta.env.VITE_SOCKET_URL ?? "http://localhost:5000";

const socket = io(SOCKET_URL, {
  transports: ["polling"],   // 🔥 FORCE polling
  upgrade: false,            // 🔥 DO NOT try websocket
  autoConnect: false,
  withCredentials: false,
});

// --------------------
// Connection control
// --------------------

export const connectSocket = () => {
  if (!socket.connected) {
    socket.connect();
  }
};

export const disconnectSocket = () => {
  if (socket.connected) {
    socket.disconnect();
  }
};

// --------------------
// Emitters
// --------------------

export const startGame = (gridStage, speedStage) => {
  connectSocket();
  socket.emit(SOCKET_EVENTS.INIT_GAME, {
    grid_stage: gridStage,
    speed_stage: speedStage,
  });
};

export const pauseGame = () => {
  socket.emit(SOCKET_EVENTS.PAUSE_GAME);
};

export const resumeGame = () => {
  socket.emit(SOCKET_EVENTS.RESUME_GAME);
};

export const changeDirection = (direction) => {
  socket.emit(SOCKET_EVENTS.CHANGE_DIRECTION, { direction });
};

// --------------------
// Listeners (safe)
// --------------------

export const onGameState = (callback) => {
  socket.off(SOCKET_EVENTS.GAME_STATE);
  socket.on(SOCKET_EVENTS.GAME_STATE, callback);
};

export const onGameOver = (callback) => {
  socket.off(SOCKET_EVENTS.GAME_OVER);
  socket.on(SOCKET_EVENTS.GAME_OVER, callback);
};

export const onError = (callback) => {
  socket.off(SOCKET_EVENTS.ERROR);
  socket.on(SOCKET_EVENTS.ERROR, callback);
};

export default socket;
