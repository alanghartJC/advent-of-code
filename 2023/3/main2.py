import numpy as np
from numpy.typing import NDArray
from typing import Dict, Tuple, List
from dataclasses import dataclass, field
from pprint import pprint, pformat

DIGITS = set(str(x) for x in range(10))

@dataclass
class PartNumber:
  number: int
  row: int
  col: int
  len: int
  has_adj_symbol: bool = False

@dataclass
class Symbol:
  adj_parts: List[int] = field(default_factory=list)

def update_adj_symbols(grid: NDArray[np.str_], part_number: PartNumber):
  cells = []
  # First check the rows above and below
  start_col = part_number.col-1
  end_col = start_col + part_number.len + 1
  for row in [grid[part_number.row-1], grid[part_number.row+1]]:
    for cell in row[start_col:end_col+1]:
      cells.append(cell)

  cells.append(grid[part_number.row][start_col])
  cells.append(grid[part_number.row][end_col])

  for cell in cells:
    if isinstance(cell, Symbol):
      cell.adj_parts.append(part_number.number)

def is_digit(s: str):
  return type(s) == str and s in DIGITS

def is_symbol(s: str):
  return s == "*"

def solve(input_str: str):
  grid = np.array([list(l) for l in input_str.split()])

  # Add a border of "." cells around the whole grid, to make adjacency easier to handle
  bordered_grid = np.full((grid.shape[0] + 2, grid.shape[1] + 2), ".", dtype=object)
  bordered_grid[1:-1, 1:-1] = grid

  symbols: List[Symbol] = []

  # Replace all symbols with a Symbol instance
  for row_num, row in enumerate(bordered_grid[1:-1]):
    for col_num, cell in enumerate(row[1:-1]):
      if is_symbol(cell):
        symbols.append(Symbol())
        row[col_num+1] = symbols[-1]

  for row_num, row in enumerate(bordered_grid[1:-1]):
    x = 1
    print(f"Row {row_num}")
    while x < len(row)-1:
      x2 = x
      if is_digit(row[x]):
        while x2 < len(row):
          if not is_digit(row[x2+1]):
            break
          x2 += 1
        part_number = PartNumber(number=int("".join(row[x:x2+1])), row=row_num+1, col=x, len=x2-x+1)

        update_adj_symbols(bordered_grid, part_number)
      x = x2 + 1

  output = 0
  pprint(symbols)
  for symbol in symbols:
    if len(symbol.adj_parts) == 2:
      output += (symbol.adj_parts[0] * symbol.adj_parts[1])

  return output

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
