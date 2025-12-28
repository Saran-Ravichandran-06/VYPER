// Cell component
import "../styles/grid.css";

const Cell = ({ value }) => {
  let className = "cell empty";

  if (value === "##") className = "cell wall";
  else if (value === "██") className = "cell snake-head";
  else if (value === "▓▓") className = "cell snake-body";
  else if (value === "🍎" || value === "🍉") className = "cell food";

  return <div className={className}>{value}</div>;
};

export default Cell;