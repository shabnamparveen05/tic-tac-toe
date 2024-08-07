# Tic Tac Toe Game

This project is a Python script for a simple Tic Tac Toe game, created to demonstrate basic game logic and user interaction in Python.

## How to Use

### Prerequisites

- Python 3.x installed on your system.
- No additional libraries are required.

### Running the Script

1. *Save the script* as tic_tac_toe.py or any name you prefer.
2. *Open a terminal or command prompt*.
3. *Navigate to the directory* where the script is saved.
4. *Run the script* by executing the following command:

    bash
    python tic_tac_toe.py
    

### Script Details

The script defines several functions to manage the game state, print the game board, check for a winner, and handle user input.

#### Functions

- *sum(a, b, c)*:
  - Returns the sum of three numbers.

- *printScreen(xstate, ystate)*:
  - Prints the current state of the game board.
  - xstate and ystate are lists that track the positions marked by X and O, respectively.

- *checkwin(xstate, ystate)*:
  - Checks if there is a winner.
  - Returns 1 if X wins, 0 if O wins, and -1 if there is no winner yet.

### Example

The following example demonstrates how the game runs:

1. The script initializes two lists, xstate and ystate, to keep track of the positions marked by X and O.
2. The game starts with X's turn.
3. Players take turns entering a position number to mark their spot on the board.
4. After each move, the script checks for a winner.
5. The game continues until there is a winner or all positions are filled.

By following the above instructions, you can easily run and play the Tic Tac Toe game in your terminal.
