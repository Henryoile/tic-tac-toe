# Tic-Tac-Toe

A command-line tic-tac-toe game written in Python. You play `O`. The computer plays `X`, opens in the center, and picks its moves at random.

Built as a learning project to practice lists, loops, functions, input validation, and the `random` module.

## Demo

```
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
```

## Features

- Board drawn in the console, one numbered square per cell
- Computer always makes the first move, in the center
- Move validation: the input must be a whole number from 1 to 9 and the square must be free
- Win detection for rows, columns, and both diagonals
- Tie detection when the board is full
- Computer picks a random free square, so it can never choose a taken one
- Four possible outcomes: game continues, tie, you win, computer wins

## Requirements

- Python 3.6 or newer
- No external packages. The game uses only the standard library.

## How to run

```
git clone https://github.com/Henryoile/tic-tac-toe.git
cd tic-tac-toe
python tic_tac_toe.py
```

On some systems the command is `python3 tic_tac_toe.py`.

## How to play

1. The board starts with the computer's `X` in the middle.
2. Type the number of the square you want and press Enter.
3. The computer answers with its own move.
4. Repeat until someone wins or the board fills up.

Squares are numbered row by row:

```
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
```

### Messages you may see

| Message                                      | Meaning                                        |
| -------------------------------------------- | ---------------------------------------------- |
| `Invalid input. Enter a number from 1 to 9.` | You typed something that is not a whole number |
| `Invalid number must be between 1 and 9.`    | The number is outside the board                |
| `That square is already taken.`              | The square already holds an `X` or an `O`      |
| `You won!`                                   | You completed a line of `O`s                   |
| `The computer won!`                          | The computer completed a line of `X`s          |
| `It's a tie!`                                | The board is full and nobody won               |

## How it works

### Board

The board is a list of three lists. Each inner list is a row, and each square is read as `board[row][column]`, counting from 0.

```python
board = [[1, 2, 3],
         [4, 'X', 6],
         [7, 8, 9]]
```

A square holds either `'X'`, `'O'`, or its own number. A number means the square is free.

### Functions

| Function                          | What it does                                                                       |
| --------------------------------- | ---------------------------------------------------------------------------------- |
| `display_board(board)`            | Prints the board in the exact grid format shown above                              |
| `enter_move(board)`               | Asks for a move, validates it, and places an `O`. Repeats until the input is valid |
| `make_list_of_free_fields(board)` | Returns a list of `(row, column)` tuples for every free square                     |
| `victory_for(board, sign)`        | Returns `True` if `sign` (`'X'` or `'O'`) has three in a row, otherwise `False`    |
| `draw_move(board)`                | Picks a random free square and places an `X`                                       |

### Game loop

Each round runs in this order:

1. You move, and the board is shown.
2. If you won, the game ends.
3. The computer moves, and the board is shown.
4. If the computer won, the game ends.
5. If no free squares are left, the game ends in a tie.

The tie check comes after the computer's move because the computer plays the 1st, 3rd, 5th, 7th, and 9th moves. The board can only fill up on the computer's turn.

### Converting a square number to a position

`enter_move` turns the number you type into a row and column:

```python
row = (move - 1) // 3
col = (move - 1) % 3
```

| Square | Row | Column |
| ------ | --- | ------ |
| 1      | 0   | 0      |
| 5      | 1   | 1      |
| 6      | 1   | 2      |
| 7      | 2   | 0      |

## Project structure

```
tic-tac-toe/
├── tic_tac_toe.py
└── README.md
```

## Python concepts practiced

- Nested lists and indexing
- Tuples and tuple unpacking
- `for` and `while` loops, with `break` and `continue`
- Functions with parameters and return values
- `input()`, `int()`, `str()`, `len()`, `range()`
- String methods such as `.isdigit()`
- List methods such as `.append()`
- `random.randrange()`

## Ideas for improvement

- Make the computer take a winning move when it has one
- Make the computer block your winning move
- Add a "play again" option
- Let the player choose to go first
- Keep a score across several games

## Author

Henry ([@Henryoile](https://github.com/Henryoile))
