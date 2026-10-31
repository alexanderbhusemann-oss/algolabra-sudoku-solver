
# Sudoku Solver – Specification Document

## 1. Project Overview


The goal of this project is to develop a Sudoku solver in Python. The program will take an 
incomplete 9x9 Sudoku puzzle and attempt to find a valid solution while following the standard Sudoku rules.
The main focus of the project will be implementing Algorithm X using the Dancing Links technique to solve Sudoku puzzles represented as exact-cover problems.
I would also like to investigate possible optimizations and compare their performance with a basic implementation.

This project will help me develop a better understanding of recursion, algorithm design and computational complexity.

## 2. Algorithms and Data Structures


The main algorithm of this project will be Donald Knuth's Algorithm X, implemented using the Dancing Links (DLX) technique.

Sudoku will be represented as an exact-cover problem. Each possible placement of a number in a cell corresponds to a candidate row in an exact-cover matrix. 
The constraints ensure that each cell receives one number and that every number occurs exactly once in each row, column and 3x3 box.
Algorithm X will search for a set of candidates satisfying all constraints. Dancing Links will use a circular doubly linked structure to efficiently remove 
and restore candidates during the search.

The Sudoku board itself will be represented using a two-dimensional Python list.
I plan to implement the exact-cover representation and the linked data structure myself.
I will study the algorithm and its implementation using the relevant literature before beginning the main implementation.


## 3. Input and Output

The input will be a partially completed 9x9 Sudoku board. Initially, puzzles will be represented directly as 
Python lists. The output will be a completed Sudoku board that satisfies the Sudoku rules. 
If the puzzle cannot be solved, the program should report that no solution was found.

A graphical user interface is not planned. The focus will be on the algorithm itself.

## 4. Time and Space Complexity


Algorithm X is a recursive search algorithm with potentially exponential worst-case running time. 
Its practical performance depends on the structure of the exact-cover problem and the choices made during the search.

For a standard 9x9 Sudoku, the exact-cover representation contains 324 constraints and up to 729 candidate placements.
Dancing Links is designed to make removing and restoring matrix entries efficient. 
I plan to investigate the algorithm's complexity in more detail and measure its performance using Sudoku puzzles of different difficulty levels.

The space requirements will include the exact-cover data structure and the recursive search stack.


## 5. Testing

I plan to test the solver with puzzles of different difficulty levels, including easy and difficult puzzles, 
already completed boards and puzzles with no valid solution.

The tests will verify that the output preserves the original clues and satisfies the Sudoku rules. 
I also plan to compare execution times and the number of recursive calls between the basic solver and an 
optimized version.

Testing will be performed using Python's unittest framework or another suitable testing approach.

## 6. Sources


Knuth, Donald E. (2000). Dancing Links.

https://arxiv.org/abs/cs/0011047

I will use this paper as the primary reference for studying Algorithm X and the Dancing Links technique.
Additional references, including Python documentation and course materials, will be documented as they are used.

AI assistance: ChatGPT was used to help plan the project, understand the proposed algorithms and draft the initial documentation. 
All implementation code will be written by me.


## 7. Project Information

- Student: Alexander Berk Husemann
- Degree programme: Computer Science (B.Sc.), TU Dortmund University; Erasmus exchange student at the University of Helsinki
- Programming language: Python
- Documentation language: English
- Peer-review programming languages: Python
- Project status: Proposed topic, awaiting instructor approval
  
