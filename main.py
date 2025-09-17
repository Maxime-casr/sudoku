
import argparse
from sudoku import Sudoku
from backtracking import BacktrackingSolver


def run(path: str, use_color: bool = True) -> None:
    sudoku = Sudoku.from_file(path)
    print("Grille initiale :")
    print(sudoku.pretty(use_color=use_color))

    solver = BacktrackingSolver(sudoku)
    solved = solver.solve()

    if solved:
        print("\nSolution :")
        print(sudoku.pretty(use_color=use_color))
        print(f"Résolu en {solver.steps} placements.")
    else:
        print("\nAucune solution trouvée.")


def main():
    parser = argparse.ArgumentParser(
        description="Solveur de Sudoku"
    )
    parser.add_argument(
        "path",
        help="Chemin du fichier de grille"
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Désactiver les couleurs dans l'affichage"
    )
    args = parser.parse_args()

    try:
        run(args.path, use_color=not args.no_color)
    except Exception as e:
        print(f"Erreur {e}")


if __name__ == "__main__":
    main()

