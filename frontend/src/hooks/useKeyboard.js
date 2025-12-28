// Keyboard hook
import { useEffect } from "react";
import { changeDirection } from "../api/socket";
import { DIRECTIONS } from "../constants/directions";

const KEY_DIRECTION_MAP = {
  ArrowUp: DIRECTIONS.UP,
  ArrowDown: DIRECTIONS.DOWN,
  ArrowLeft: DIRECTIONS.LEFT,
  ArrowRight: DIRECTIONS.RIGHT,
};

const useKeyboard = (enabled = true) => {
  useEffect(() => {
    if (!enabled) return;

    const handleKeyDown = (event) => {
      const direction = KEY_DIRECTION_MAP[event.key];
      if (direction) {
        changeDirection(direction);
      }
    };

    window.addEventListener("keydown", handleKeyDown);

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, [enabled]);
};

export default useKeyboard;
