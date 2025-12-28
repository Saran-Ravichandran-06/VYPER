import { useState } from "react";
import SelectionPage from "./pages/SelectionPage";
import GamePage from "./pages/GamePage";

const App = () => {
  const [currentPage, setCurrentPage] = useState("selection"); // "selection" or "game"
  const [gameMode, setGameMode] = useState("classic");
  const [difficulty, setDifficulty] = useState("medium");

  const handlePlayClick = (mode, diff) => {
    setGameMode(mode);
    setDifficulty(diff);
    setCurrentPage("game");
  };

  const handleBackToHome = () => {
    setCurrentPage("selection");
  };

  return (
    <>
      {currentPage === "selection" && (
        <SelectionPage onPlay={handlePlayClick} />
      )}
      {currentPage === "game" && (
        <GamePage
          gameMode={gameMode}
          difficulty={difficulty}
          onBackToHome={handleBackToHome}
        />
      )}
    </>
  );
};

export default App;