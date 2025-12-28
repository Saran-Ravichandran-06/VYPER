// Score panel
const ScorePanel = ({ score, timeLeft }) => {
  return (
    <div className="score-panel">
      <div className="score-left">
        <h3>Score: {score}</h3>
      </div>
      <div className="score-right">
        {timeLeft !== -1 && <h4>Time: {timeLeft}s</h4>}
      </div>
    </div>
  );
};

export default ScorePanel;
