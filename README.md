# Tic Tac Toe Game with Minimax Algorithm

A Tic Tac Toe game using the **Tkinter** library for the gGUI and the **Minimax algorithm** for calculating computer's best move.

---

## Features
- **Single-player mode**: Play against the computer, which uses the Minimax algorithm to make optimal moves.
- **Dynamic UI**: Built with Tkinter, featuring a simple and responsive design.
- **Restart Option**: Reset the game board and start over without restarting the application.

---

## Minimax Algorithm
The computer uses the **Minimax algorithm** to evaluate all possible moves and choose the best one. This ensures that:
- The computer will either win or draw but never lose.
- The evaluation checks for winning states, losing states, or draws.

---

## Project Structure
The code is divided into two main components:
1. **`main.py`**: Contains the Tkinter-based GUI and handles user interactions.
2. **`logic.py`**: Implements the Minimax algorithm, calculating the computer's best move , checking for winners and draws.

---

## Installation
1. Clone this repository:
   ```bash
    git clone https://github.com/Muhammed-Amer/TicTacToe.git
    cd TicTacToe
    python3 main.py
