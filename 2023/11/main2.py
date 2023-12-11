import numpy as np
from typing import List, Tuple, Set

def solve(input_str: str):
  print("")
  grid: List[List[str]] = []

  for line in input_str.splitlines():
    grid.append(list(line))

  np_grid = np.array(grid)

  print(np_grid)

  expanded_cols: Set[int] = set()
  expanded_rows: Set[int] = set()

  row_index = 0
  while row_index < np_grid.shape[0]:
    if np.all(np_grid[row_index, :] == "."):
      print(f"Adding new row at {row_index}")
      expanded_rows.add(row_index)
    row_index += 1

  col_index = 0
  while col_index < np_grid.shape[1]:
    if np.all(np_grid[:, col_index] == "."):
      print(f"Adding new col at {col_index}")
      expanded_cols.add(col_index)
    col_index += 1

  print(f"Expanded rows: {expanded_rows}")
  print(f"Expanded cols: {expanded_cols}")

  galaxies: List[Tuple[int, int]] = []

  for r, row in enumerate(np_grid):
    for c, cell in enumerate(row):
      if cell != ".":
        galaxies.append((r, c))

  print(galaxies)

  output = 0
  count = 0
  for a, g1 in enumerate(galaxies):
    for b, g2 in enumerate(galaxies[a:]):
      if g1 == g2:
        continue
      count += 1
      rowdiff = 0
      for row in range(min(g2[0], g1[0]), max(g2[0], g1[0])):
        if row in expanded_rows:
          rowdiff += 1000000
        else:
          rowdiff += 1
      coldiff = 0
      for col in range(min(g2[1], g1[1]), max(g2[1], g1[1])):
        if col in expanded_cols:
          coldiff += 1000000
        else:
          coldiff += 1
      print(f"{count}: Adding rowdiff={rowdiff} coldiff={coldiff} ({rowdiff + coldiff}) for {g1} to {g2}")
      output += rowdiff
      output += coldiff

  return output



def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
