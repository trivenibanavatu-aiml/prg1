# Tic Tac Toe

Simple browser Tic-Tac-Toe game (HTML/CSS/JS).

Files:
- `index.html` — game UI
- `styles.css` — styles
- `script.js` — game logic (two-player local + optional simple AI for O)

How to run:
1. Open `index.html` in your browser (double-click or right-click -> Open with).
2. Click any empty cell to place a mark. Players alternate X and O.
3. Optionally check "Play vs Computer (O)" to play against a simple computer opponent (tries to win or block, otherwise random).
4. Use Restart to clear the board. Scores persist in localStorage.

Notes and next steps:
- The AI is simple; for a perfect opponent, implement minimax.
- Accessibility: basic ARIA attributes added. Further keyboard support can be added.
