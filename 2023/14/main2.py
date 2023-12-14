import numpy as np

def rotate_left(np_grid: np.ndarray) -> np.ndarray:
  return np.flipud(np_grid.transpose())

def rotate_right(np_grid: np.ndarray) -> np.ndarray:
  return np.fliplr(np_grid.transpose())

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
  print("")
  grid_raw = []
  for line in input_str.splitlines():
    grid_raw.append(list(line))

  np_grid = np.array(grid_raw)
  # print(np_grid)
  cycles = 1000000000
  hashes = dict()
  cycle = 0
  first_match_cycle = None
  repeater_size = 0
  while cycle < cycles:
    print(f"Cycle {cycle}/{cycles} ({100.0*cycle/cycles:.2}%)")
    gridhash = hash(np_grid.tobytes())
    if gridhash in hashes:
      if first_match_cycle is None:
        first_match_cycle = hashes[gridhash]
      else:
        repeater_size += 1
        if first_match_cycle == hashes[gridhash]:
          cycle = 0
          cycles = (cycles-first_match_cycle) % repeater_size
          if cycles == 0:
            break
      print(f"Previous hashed: {hashes[gridhash]}")
    for _ in range(4):
      tilt(np_grid)
      np_grid = rotate_right(np_grid)
    if gridhash not in hashes:
      hashes[gridhash] = cycle
    cycle += 1


  # print(np_grid)
  return calc_load(np_grid)

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
