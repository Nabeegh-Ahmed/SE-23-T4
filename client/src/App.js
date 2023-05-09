import "./App.css";
import SheraAI from "./pages/SheraAI.js";
import ImageGenator from "./pages/ImageGenator.js";
import { Header } from "./components/Header.js";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <>
      <Header />
      <Routes>
        <Route path="/" element={<SheraAI />} exact />
        <Route path="/CSVTable" element={<ImageGenator />} exact />
      </Routes>
    </>
  );
}

export default App;
