import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { Providers } from "./app/providers";
import { LeadsPage } from "./features/leads";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Providers>
      <LeadsPage />
    </Providers>
  </StrictMode>,
);
