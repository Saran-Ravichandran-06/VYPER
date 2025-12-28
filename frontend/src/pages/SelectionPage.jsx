import { useState } from "react";
import "../styles/app.css";

import plainImg from "../assets/plain.png";
import mazeImg from "../assets/maze.png";
import fastImg from "../assets/fast.jpg";
import slowImg from "../assets/slow.jpg";
import mediumImg from "../assets/medium.jpg";

const SelectionPage = ({ onPlay }) => {
  const [gameMode, setGameMode] = useState("classic");
  const [difficulty, setDifficulty] = useState("medium");

  const handlePlayClick = () => {
    onPlay(gameMode, difficulty);
  };

  return (
    <div className="game-container">
      <h1 style={{ marginTop: "40px" }}>VYPER 🐍</h1>

      <div style={{ marginBottom: "30px" }}>
        {/* Game Mode Selection */}
        <div style={{ marginBottom: "30px" }}>
          <label style={{ marginRight: "10px", fontSize: "18px", display: "block", marginBottom: "15px" }}>
            Game Mode:
          </label>

          <div className="selection-grid selection-grid-2">
            <div
              className={`option-card ${gameMode === "classic" ? "selected" : ""}`}
              onClick={() => setGameMode("classic")}
              role="button"
              tabIndex={0}
              onKeyDown={(e) => e.key === "Enter" && setGameMode("classic")}
            >
              <img src={plainImg} alt="Classic" />
              <div className="option-label">Classic</div>
            </div>

            <div
              className={`option-card ${gameMode === "time-attack" ? "selected" : ""}`}
              onClick={() => setGameMode("time-attack")}
              role="button"
              tabIndex={0}
              onKeyDown={(e) => e.key === "Enter" && setGameMode("time-attack")}
            >
              <img src={mazeImg} alt="Time Attack" />
              <div className="option-label">Time Attack</div>
            </div>
          </div>
        </div>

        {/* Difficulty Selection */}
        <div style={{ marginBottom: "30px" }}>
          <label style={{ marginRight: "10px", fontSize: "18px", display: "block", marginBottom: "15px" }}>
            Difficulty:
          </label>

          <div className="selection-grid selection-grid-3">
            <div
              className={`option-card ${difficulty === "easy" ? "selected" : ""}`}
              onClick={() => setDifficulty("easy")}
              role="button"
              tabIndex={0}
              onKeyDown={(e) => e.key === "Enter" && setDifficulty("easy")}
            >
              <img src={slowImg} alt="Easy" />
              <div className="option-label">Easy</div>
            </div>

            <div
              className={`option-card ${difficulty === "medium" ? "selected" : ""}`}
              onClick={() => setDifficulty("medium")}
              role="button"
              tabIndex={0}
              onKeyDown={(e) => e.key === "Enter" && setDifficulty("medium")}
            >
              <img src={mediumImg} alt="Medium" />
              <div className="option-label">Medium</div>
            </div>

            <div
              className={`option-card ${difficulty === "hard" ? "selected" : ""}`}
              onClick={() => setDifficulty("hard")}
              role="button"
              tabIndex={0}
              onKeyDown={(e) => e.key === "Enter" && setDifficulty("hard")}
            >
              <img src={fastImg} alt="Hard" />
              <div className="option-label">Hard</div>
            </div>
          </div>
        </div>

        <center>
          <button
            onClick={handlePlayClick}
            style={{
              fontSize: "18px",
              padding: "12px 40px",
              marginTop: "20px",
            }}
          >
            Play
          </button>
        </center>
      </div>
    </div>
  );
};

export default SelectionPage;