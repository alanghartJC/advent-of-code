import numpy as np

def calc_load(np_grid: np.ndarray) -> int:
  output = 0
  for r, row in enumerate(np_grid):
    output += len([c for c in row if c == 'O']) * (len(np_grid) - r)
  return output

def tilt(np_grid: np.ndarray):
  for col_idx in range(np_grid.shape[1]):
    col = np_grid[:, col_idx]
    copy_index = 0
    for row_idx in range(np_grid.shape[0]):
      if col[row_idx] == 'O':
        tmp = col[copy_index]
        col[copy_index] = col[row_idx]
        col[row_idx] = tmp
        copy_index += 1
      elif col[row_idx] == '#':
        copy_index = row_idx+1


def solve(input_str: str):
  grid_raw = []
  for line in input_str.splitlines():
    grid_raw.append(list(line))

  np_grid = np.array(grid_raw)
  print(np_grid)
  tilt(np_grid)
  print(np_grid)
  return calc_load(np_grid)

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
