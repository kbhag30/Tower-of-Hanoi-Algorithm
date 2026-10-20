# Tower-of-Hanoi-Algorithm

Description

This project implements the Tower of Hanoi puzzle using Python. The goal is to move a stack of disks from the first rod to the third rod while following the rules of the puzzle. The solution demonstrates algorithmic problem-solving and the process of moving disks between three rods.

Rules of the Puzzle

Only one disk can be moved at a time.

Only the top disk of a rod can be moved.

A larger disk cannot be placed on top of a smaller disk.

All disks must be moved from the starting rod to the destination rod.

Features

Implements a hanoi_solver() function that accepts the number of disks as an argument.

Represents the three rods using Python lists.

Displays the starting arrangement and each subsequent move.

Returns the complete sequence of rod configurations as a string.

Solves the puzzle using the minimum number of moves, (2^n - 1), where n is the number of disks.
