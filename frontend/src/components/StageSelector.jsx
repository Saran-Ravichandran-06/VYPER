// Stage selector
const StageSelector = ({
  gridStage,
  speedStage,
  setGridStage,
  setSpeedStage,
  startGame,
}) => {
  return (
    <div style={{ marginBottom: "15px" }}>
      <label>
        Grid Stage:
        <select
          value={gridStage}
          onChange={(e) => setGridStage(Number(e.target.value))}
        >
          <option value={1}>Small</option>
          <option value={2}>Medium</option>
          <option value={3}>Large</option>
        </select>
      </label>

      <br />
      <br></br>
      <label>
        Speed Stage:
        <select
          value={speedStage}
          onChange={(e) => setSpeedStage(Number(e.target.value))}
        >
          <option value={1}>Slow</option>
          <option value={2}>Medium</option>
          <option value={3}>Fast</option>
        </select>
      </label>

      <br />

      <button onClick={startGame} style={{ marginTop: "10px" }}>
        Start Game
      </button>
    </div>
  );
};

export default StageSelector;
