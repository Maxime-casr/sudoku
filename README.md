# Solveur de Sudoku — Test d’entrée Bachelor IA

Ce projet implémente un **solveur de Sudoku** en Python selon la consigne du test d’entrée *Bachelor IA - 02*.  
La résolution utilise la méthode du backtracking.


## Fonctionnalités

- Chargement d’une grille depuis un fichier texte (format 9×9, `_` pour vide).
- Affichage clair dans le terminal :  
  - Chiffres d’origine en bleu,
  - Chiffres ajoutés par l’algorithme en vert.
- Validation basique de la grille initiale (détecte les conflits).

---

## Format de la grille (input)

- 9 lignes, 9 caractères par ligne.
- `1` à `9` = valeur présente.
- `_` = case vide.

## Pour lancer un test

- python main.py data/exemple1.txt ou python main.py data/exemple1.txt --no-color
