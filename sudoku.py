
from __future__ import annotations
from typing import List, Optional, Tuple


try:
    from colorama import init as colorama_init, Fore, Style
    colorama_init()
    COLOR_ORIG = Fore.BLUE + Style.BRIGHT  
    COLOR_FILL = Fore.GREEN               
    COLOR_RESET = Style.RESET_ALL
except Exception:
    COLOR_ORIG = "\033[96;1m"
    COLOR_FILL = "\033[92m"
    COLOR_RESET = "\033[0m"


class Sudoku:
    def __init__(self, grid: List[List[int]], mask_initial: List[List[bool]]):
        self.grid = grid
        self.mask_initial = mask_initial
        self._validate_dimensions()
        self._validate_initial_or_raise()

    @classmethod
    def from_file(cls, path: str) -> "Sudoku":
        with open(path, "r", encoding="utf-8") as f:
            raw = [line.strip() for line in f.readlines() if line.strip()]

        if len(raw) != 9:
            raise ValueError("Le fichier doit contenir 9 lignes non vides.")

        grid: List[List[int]] = []
        mask: List[List[bool]] = []
        for idx, line in enumerate(raw, start=1):
            if len(line) != 9:
                raise ValueError(f"Ligne {idx}: doit contenir 9 caractères.")
            row_vals: List[int] = []
            row_mask: List[bool] = []
            for ch in line:
                if ch == "_":
                    row_vals.append(0)
                    row_mask.append(False)
                elif ch.isdigit() and ch != "0":
                    row_vals.append(int(ch))
                    row_mask.append(True)
                else:
                    raise ValueError(
                        f"Erreur"
                    )
            grid.append(row_vals)
            mask.append(row_mask)

        return cls(grid, mask)


    def _validate_dimensions(self) -> None:
        if len(self.grid) != 9 or any(len(r) != 9 for r in self.grid):
            raise ValueError("La grille doit être 9x9.")
        if len(self.mask_initial) != 9 or any(len(r) != 9 for r in self.mask_initial):
            raise ValueError("Le masque initial doit être 9x9.")

    def _validate_initial_or_raise(self) -> None:
        for r in range(9):
            for c in range(9):
                v = self.grid[r][c]
                if v == 0:
                    continue
                self.grid[r][c] = 0
                ok = self.is_valid(r, c, v)
                self.grid[r][c] = v
                if not ok:
                    raise ValueError(
                        f"Erreur."
                    )

    
    def is_valid(self, r: int, c: int, val: int) -> bool:
        
        for j in range(9):
            if self.grid[r][j] == val:
                return False
        
        for i in range(9):
            if self.grid[i][c] == val:
                return False
        
        br, bc = (r // 3) * 3, (c // 3) * 3
        for i in range(br, br + 3):
            for j in range(bc, bc + 3):
                if self.grid[i][j] == val:
                    return False
        return True

    def find_empty(self) -> Optional[Tuple[int, int]]:
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None


    def pretty(self, use_color: bool = True) -> str:
        lines = []
        for i in range(9):
            if i % 3 == 0:
                lines.append("+-------+-------+-------+")
            row = []
            for j in range(9):
                if j % 3 == 0:
                    row.append("| ")
                v = self.grid[i][j]
                if v == 0:
                    row.append(". ")
                else:
                    if self.mask_initial[i][j]:
                        cell = f"{v}"
                        if use_color:
                            cell = f"{COLOR_ORIG}{cell}{COLOR_RESET}"
                    else:
                        cell = f"{v}"
                        if use_color:
                            cell = f"{COLOR_FILL}{cell}{COLOR_RESET}"
                    row.append(cell + " ")
            row.append("|")
            lines.append("".join(row))
        lines.append("+-------+-------+-------+")
        legend = "Origine = bleu, Ajouté = vert"
        lines.append(f"({legend})")
        return "\n".join(lines)
