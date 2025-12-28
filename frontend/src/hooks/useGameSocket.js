// Game socket hook
import { useEffect } from "react";
import socket, { onGameState, onGameOver, onError } from "../api/socket";
import { SOCKET_EVENTS } from "../constants/events";

const useGameSocket = ({
  setGrid,
  setScore,
  setTimeLeft,
  setGameOver,
  setGameOverReason,
  paused = false,
}) => {
  useEffect(() => {
    // Listen for live game state updates
    onGameState((state) => {
      if (paused) return;
      setGrid(state.grid);
      setScore(state.score);
      setTimeLeft(state.time_left);
    });

    // Listen for game over event
    onGameOver((data) => {
      if (paused) return;
      setGameOver(true);
      setGameOverReason(data.reason);
    });

    // Optional: error handling
    onError((err) => {
      console.error("Socket Error:", err.message);
    });

    // Cleanup listeners when component unmounts or paused changes
    return () => {
      if (socket && socket.off) {
        socket.off(SOCKET_EVENTS.GAME_STATE);
        socket.off(SOCKET_EVENTS.GAME_OVER);
        socket.off(SOCKET_EVENTS.ERROR);
      }
    };
  }, [paused]);
};

export default useGameSocket;
