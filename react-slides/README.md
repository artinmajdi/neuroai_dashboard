# React Slide Decks for NeuroAI Dashboard

This is a minimal React app for rendering grant slide decks. It is designed to be embedded in the main Streamlit dashboard via an iframe.

## Setup

1. `cd react-slides`
2. `npm install`
3. `npm run dev` (for development, default port: 3000)

## Adding/Editing Slide Decks

- Place/edit slide deck components in `src/grants/`.
- Add routes for each slide deck in `src/App.tsx`.

## Usage in Streamlit

- Embed the slide deck using an iframe pointing to the correct route (e.g., `http://localhost:3000/k99r00`).
