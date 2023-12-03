import numpy as np
from numpy.typing import NDArray
from typing import Dict, Tuple
from dataclasses import dataclass

DIGITS = set(str(x) for x in range(10))

@dataclass
class PartNumber:
  number: int
  row: int
  col: int
  len: int
  has_adj_symbol: bool = False

def has_adj_symbol(grid: NDArray[np.str_], part_number: PartNumber):
  # First check the rows above and below
  start_col = part_number.col-1
  end_col = start_col + part_number.len + 1
  for row in [grid[part_number.row-1], grid[part_number.row+1]]:
    for cell in row[start_col:end_col+1]:
      if is_symbol(cell):
        return True

  # Then check the row of the part number itself
  return is_symbol(grid[part_number.row][start_col]) or is_symbol(grid[part_number.row][end_col])

def is_digit(s: str):
  return s in DIGITS

def is_symbol(s: str):
  return isinstance(s, str) and len(s) == 1 and not is_digit(s) and s != "."

def solve(input_str: str):
  grid = np.array([list(l) for l in input_str.split()])

  # Add a border of "." cells around the whole grid, to make adjacency easier to handle
  bordered_grid = np.full((grid.shape[0] + 2, grid.shape[1] + 2), ".", dtype=str)
  bordered_grid[1:-1, 1:-1] = grid

  output = 0

  for row_num, row in enumerate(bordered_grid[1:-1]):
    x = 1
    while x < len(row)-1:
      x2 = x
      if is_digit(row[x]):
        while x2 < len(row):
          if not is_digit(row[x2+1]):
            break
          x2 += 1
        part_number = PartNumber(number=int("".join(row[x:x2+1])), row=row_num+1, col=x, len=x2-x+1)

        if has_adj_symbol(bordered_grid, part_number):
          print(f"Adding {part_number.number}")
          output += part_number.number

      x = x2 + 1

  return output

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
