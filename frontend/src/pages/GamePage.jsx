import { useState, useEffect } from "react";

import GameBoard from "../components/GameBoard";
import ScorePanel from "../components/ScorePanel";
import GameOver from "../components/GameOver";

import useKeyboard from "../hooks/useKeyboard";
import useGameSocket from "../hooks/useGameSocket";

import { startGame, pauseGame, resumeGame } from "../api/socket";
import "../styles/app.css";

const GamePage = ({ gameMode, difficulty, onBackToHome }) => {
  const [grid, setGrid] = useState([]);
  const [score, setScore] = useState(0);
  const [timeLeft, setTimeLeft] = useState(60);
  const [gameOver, setGameOver] = useState(false);
  const [gameOverReason, setGameOverReason] = useState("");
  const [paused, setPaused] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  // Enable keyboard only when game is running and not paused
  useKeyboard(!gameOver && !paused);

  // Socket listeners (skip updates when paused)
  useGameSocket({
    setGrid,
    setScore,
    setTimeLeft,
    setGameOver,
    setGameOverReason,
    paused,
  });

  // Map difficulty to speed stage
  const getDifficultySpeed = (diff) => {
    const difficultyMap = { easy: 1, medium: 2, hard: 3 };
    return difficultyMap[diff] || 2;
  };

  // Map game mode to grid stage
  const getGameModeGrid = (mode) => {
    const modeMap = { classic: "freestyle", "time-attack": "maze" };
    return modeMap[mode] || "freestyle";
  };

  // Start game on component mount
  const startGameOnLoad = () => {
    setGameOver(false);
    setGameOverReason("");
    setScore(0);
    const gridStage = getGameModeGrid(gameMode);
    const speedStage = getDifficultySpeed(difficulty);
    startGame(gridStage, speedStage);
  };

  const handlePlayAgain = () => {
    startGameOnLoad();
  };

  const handleHome = () => {
    onBackToHome();
  };

  // Start game when component mounts or stages change
  useEffect(() => {
    startGameOnLoad();
  }, [gameMode, difficulty]);

  const handleOpenSettings = () => {
    setMenuOpen(true);
    setPaused(true);
    // Tell server to pause advancing the game
    pauseGame();
  };

  const handleCloseSettings = () => {
    setMenuOpen(false);
    setPaused(false);
    // Tell server to resume the game loop
    resumeGame();
  };

  const handleRestartFromMenu = () => {
    setMenuOpen(false);
    setPaused(false);
    startGameOnLoad();
  };

  const handleHomeFromMenu = () => {
    setMenuOpen(false);
    setPaused(false);
    onBackToHome();
  };

  return (
    <div className="game-container">
      <h1>VYPER 🐍</h1>
      <div className="settings-bar">
        <button className="settings-button" onClick={handleOpenSettings}>
          Settings
        </button>

        {menuOpen && (
          <div className="settings-menu">
            <button onClick={handleCloseSettings}>Resume</button>
            <button onClick={handleRestartFromMenu}>Restart</button>
            <button onClick={handleHomeFromMenu}>Home</button>
          </div>
        )}
      </div>

      <ScorePanel score={score} timeLeft={timeLeft} />

      <GameBoard grid={grid} />

      {gameOver && (
        <GameOver
          reason={gameOverReason}
          score={score}
          onPlayAgain={handlePlayAgain}
          onHome={handleHome}
        />
      )}
    </div>
  );
};

export default GamePage;