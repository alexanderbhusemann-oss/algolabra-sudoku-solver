# Weekly Report

## Work Completed

After a period with little progress, I resumed work on the project and added a basic command-line interface for entering a Sudoku board.

The `read_board()` function asks for nine rows of nine digits, using `0` for empty cells. It checks the length and allowed characters of each row and asks for another input if the format is invalid. Valid rows are converted into lists of integers and stored in a two-dimensional list.

The `enter_board()` function calls the input function and prints the resulting board.

## Current Status

The program can accept and store a board, but it does not yet check whether the input satisfies Sudoku rules. The exact-cover representation and the Algorithm X solver with Dancing Links have not been implemented yet.

## Challenges

I made less progress than planned during the previous weeks and am behind my original schedule. The main challenge ahead is understanding how to represent Sudoku as an exact-cover problem and implement the linked structure required for Dancing Links.

## Plans for Next Week

- Add checks for repeated numbers in rows, columns and 3×3 boxes, ignoring empty cells.
- Study the exact-cover representation of Sudoku.
- Begin implementing the exact-cover representation.
- Add tests for input handling and board validation.

## Time Spent

A few minutes on the initial input-handling implementation.

## AI Assistance

ChatGPT was used to assist with the initial input-handling code and the wording of this report.
