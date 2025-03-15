import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import GraphPage from "./pages/GraphPage";

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/graph" element={<GraphPage />} />
      </Routes>
    </Router>
  );
};

export default App;
