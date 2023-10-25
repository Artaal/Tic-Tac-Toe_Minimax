# Tic Tac Toe with Minimax Algorithm

This is a simple implementation of the **Tic Tac Toe** game using the Minimax algorithm in Python. The game consists of two Python files: `tictactoe.py` and `runner.py`.

## tictactoe.py

### Overview

This file contains the core logic for playing **Tic Tac Toe**. It defines the game state, player actions, board setup, winning conditions, and the Minimax algorithm for AI decision making.

### Functions

1. **`initial_state()`**
   - Returns the starting state of the board.

2. **`player(board)`**
   - Returns the player (X or O) who has the next turn on the board.

3. **`actions(board)`**
   - Returns a set of all possible actions (i, j) available on the board.

4. **`result(board, action)`**
   - Returns the board that results from making a move (i, j) on the board.

5. **`winner(board)`**
   - Returns the winner of the game (X or O), if there is one.

6. **`terminal(board)`**
   - Returns `True` if the game is over, `False` otherwise.

7. **`utility(board)`**
   - Returns the utility value for the current state: 1 if X has won, -1 if O has won, or 0 for a tie or ongoing game.

8. **`minimax(board)`**
   - Returns the optimal action for the current player on the board using the Minimax algorithm.

### Usage

You can use the `tictactoe.py` file to play the game or integrate it into other applications.

## runner.py

### Overview

This file is a graphical user interface for playing **Tic Tac Toe** against the AI implemented in `tictactoe.py`. It uses the Pygame library for rendering the game board and handling user interactions.

### Features

- Allows the user to choose to play as X or O.
- Provides a graphical interface for playing the game against the AI.
- Displays game over messages when the game ends.
- Offers an option to play again.

### Usage

Run `runner.py` to play the game with the graphical interface. Follow the on-screen instructions to make your moves and enjoy a game of **Tic Tac Toe** against the Minimax AI.

## Getting Started

1. Make sure you have Python and Pygame installed.
2. Run `runner.py` to play the game interactively.

Enjoy the game and challenge the AI with your **Tic Tac Toe** skills!
