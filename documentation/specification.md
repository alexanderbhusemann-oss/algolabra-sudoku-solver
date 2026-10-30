
# Sudoku Solver – Specification Document

## 1. Project Overview

The goal of this project is to develop a Sudoku solver in Python. The program will take an 
incomplete 9x9 Sudoku puzzle and attempt to find a valid solution while following the standard Sudoku rules.
The main focus of the project will be implementing a recursive backtracking algorithm. 
I would also like to investigate possible optimizations and compare their performance with a basic implementation.

This project will help me develop a better understanding of recursion, algorithm design and computational complexity.

## 2. Algorithms and Data Structures

The Sudoku board will be represented as a two-dimensional Python list containing nine rows and nine columns. 
Empty cells will be represented by zero.

The main algorithm will use backtracking. It will find an empty cell, 
try numbers from 1 to 9, and check whether each number follows the Sudoku rules. 
If a number is valid, the algorithm will continue recursively. 
If no solution can be found using the current choice, the algorithm will undo that choice and try another number.

The validity checks will ensure that a number does not already appear in the same row, column or 3x3 subgrid.

As a possible optimization, I plan to investigate choosing the empty cell with the fewest valid candidates first.

## 3. Input and Output

The input will be a partially completed 9x9 Sudoku board. Initially, puzzles will be represented directly as 
Python lists. The output will be a completed Sudoku board that satisfies the Sudoku rules. 
If the puzzle cannot be solved, the program should report that no solution was found.

A graphical user interface is not planned. The focus will be on the algorithm itself.

## 4. Time and Space Complexity

A basic backtracking solver can require exponential time in the worst case. If there are m empty cells, 
a simple upper bound for the search is O(9^m), because each empty cell can have up to nine candidate values. 
This bound does not account for pruning invalid choices.

The board uses O(1) space for a fixed 9x9 Sudoku. The recursive search can use O(m) additional stack space, 
where m is the number of empty cells.

I plan to investigate how validity checks and different cell-selection strategies affect practical running time.

## 5. Testing

I plan to test the solver with puzzles of different difficulty levels, including easy and difficult puzzles, 
already completed boards and puzzles with no valid solution.

The tests will verify that the output preserves the original clues and satisfies the Sudoku rules. 
I also plan to compare execution times and the number of recursive calls between the basic solver and an 
optimized version.

Testing will be performed using Python's unittest framework or another suitable testing approach.

## 6. Sources

I plan to consult the Algorithms and AI Lab course materials, Python documentation and educational resources 
about recursive backtracking and Sudoku-solving algorithms.

Specific references will be added as I use them. Any external code or AI assistance will be documented according 
to the course requirements. The implementation code will be written by me.

## 7. Project Information

- Student: Alexander Berk Husemann
- Degree programme: Computer Science (B.Sc.), TU Dortmund University; Erasmus exchange student at the University of Helsinki
- Programming language: Python
- Documentation language: English
- Peer-review programming languages: Python
- Project status: Proposed topic, awaiting instructor approval
  
