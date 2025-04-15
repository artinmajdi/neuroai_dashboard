import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import K99R00Slides from "./grants/k99r00-slide-deck";
import NSFCareerSlides from "./grants/nsf-career-slide-deck";
import McKnightScholarsSlides from "./grants/mcknight-scholars-slide-deck";

function Home() {
  return (
    <div style={{ padding: 32, textAlign: "center" }}>
      <h1>NeuroAI Grant Slide Decks</h1>
      <p>Select a grant route: /k99r00, /nsf-career, or /mcknight-scholars</p>
    </div>
  );
}

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/k99r00" element={<K99R00Slides />} />
      <Route path="/nsf-career" element={<NSFCareerSlides />} />
      <Route path="/mcknight-scholars" element={<McKnightScholarsSlides />} />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}
