import "../styles/gameOverModal.css";

const GameOver = ({ reason, score, onPlayAgain, onHome }) => {
  return (
    <div className="game-over-overlay">
      <div className="game-over-modal">
        <h2>Game Over</h2>
        <p className="game-over-reason">{reason}</p>
        <p className="game-over-score">Final Score: {score}</p>

        <div className="game-over-buttons">
          <button onClick={onPlayAgain} className="btn-play-again">
            Play Again
          </button>
          <button onClick={onHome} className="btn-home">
            Home
          </button>
        </div>
      </div>
    </div>
  );
};

export default GameOver;