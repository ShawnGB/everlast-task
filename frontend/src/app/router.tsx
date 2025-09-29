import { Routes, Route } from "react-router-dom";

export function AppRouter() {
  return (
    <Routes>
      <Route path="/" element={<div>Home</div>} />
      <Route path="/leads" element={<div>Lead List</div>} />
      <Route path="/leads/:id" element={<div>Lead Detail</div>} />
    </Routes>
  );
}
