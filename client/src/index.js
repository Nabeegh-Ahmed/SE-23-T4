import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.js";
import { BrowserRouter } from "react-router-dom";
import "./index.css";

import { ChainId, ThirdwebProvider } from "@thirdweb-dev/react";

const activeChainId = ChainId.Mainnet;

ReactDOM.createRoot(document.getElementById("root")).render(
  <ThirdwebProvider desiredChainId={activeChainId}>
    <BrowserRouter>
      <React.StrictMode>
        <App />
      </React.StrictMode>
    </BrowserRouter>
    ,
  </ThirdwebProvider>
);
