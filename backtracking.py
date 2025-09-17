# backtracking.py
from __future__ import annotations
from typing import Optional, Tuple
from sudoku import Sudoku


class BacktrackingSolver:
    

    def __init__(self, sudoku: Sudoku):
        self.sudoku = sudoku
        self.steps = 0 

    def solve(self) -> bool:
        
        empty = self.sudoku.find_empty()
        if not empty:
            return True  

        r, c = empty
        for val in range(1, 10):
            if self.sudoku.is_valid(r, c, val):
                self.sudoku.grid[r][c] = val
                self.steps += 1
                if self.solve():
                    return True
                self.sudoku.grid[r][c] = 0
        return False
