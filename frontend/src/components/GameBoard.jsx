// Grid rendering
import Cell from "./Cell";

const GameBoard = ({ grid }) => {
  if (!grid || grid.length === 0) return null;

  return (
    <div
      style={{
        display: "grid",
        gridTemplateRows: `repeat(${grid.length}, 1fr)`,
        gap: "2px",
      }}
    >
      {grid.map((row, rowIndex) => (
        <div
          key={rowIndex}
          style={{
            display: "grid",
            gridTemplateColumns: `repeat(${row.length}, 1fr)`,
            gap: "2px",
          }}
        >
          {row.map((cell, colIndex) => (
            <Cell key={colIndex} value={cell} />
          ))}
        </div>
      ))}
    </div>
  );
};

export default GameBoard;

