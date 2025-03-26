import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import PaginaInicio from "./paginas/PaginaInicio";

createRoot(document.getElementById("root")).render(
    <StrictMode>
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<PaginaInicio />} />
            </Routes>
        </BrowserRouter>
    </StrictMode>
);
