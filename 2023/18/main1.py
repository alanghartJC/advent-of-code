import numpy as np
from typing import Tuple
from dataclasses import dataclass, field
from collections import deque

dirs = {
  "D": np.array((1,0)),
  "U": np.array((-1,0)),
  "L": np.array((0,-1)),
  "R": np.array((0,1)),
}

def print_ground(grid):
  for r, row in enumerate(grid):
    print(f"{r:03}: {''.join(row)}")
  print("")

def get_adj(ndgrid: np.ndarray, cur: Tuple[int,int], direction: Tuple[int, int]) -> int:
  # import pdb; pdb.set_trace()
  nextrow = cur[0] + direction[0]
  nextcol = cur[1] + direction[1]

  if 0 <= nextrow < ndgrid.shape[0] and 0 <= nextcol < ndgrid.shape[1]:
    return (nextrow, nextcol)
  return None

def find_inner_nodes(start_node: Tuple[int,int], grid: np.ndarray) -> int:
  inner_count = 1
  visited = set(start_node)

  queue = deque()
  queue.append(start_node)

  while queue:
    node = queue.popleft()

    for direction in dirs.values():
      n = get_adj(grid, node, direction)
      if n is None or n in visited:
        continue
      visited.add(n)
      try:
        if grid[n[0],n[1]] == "#":
          continue
      except:
        import pdb; pdb.set_trace()
      grid[n[0],n[1]] = "#"
      queue.append(n)

  return len(visited)


def solve(input_str: str):
  print("")
  digs = []
  for line in input_str.splitlines():
    direction, count, color = line.split()
    count = int(count)
    color = color[2:-1]
    digs.append((direction, count, color))

  ground = None
  cursor = np.array((0, 0))
  for direction, count, color in digs:
    print(f"direction={direction} count={count}")
    if ground is None:
      assert(direction == "R")
      ground = np.array([["#"]*count])
      cursor = np.array((0, count-1))
      continue
    if direction == "D" and ground.shape[0] < cursor[0] + count:
      # print(f"Expanding rows")
      new_rows = np.full((cursor[0]+count+1-ground.shape[0],ground.shape[1]), ".")
      ground = np.concatenate((ground, new_rows), axis=0)
    if direction == "U":
      if cursor[0] < count:
        # print(f"Expanding rows")
        new_rows = np.full((count-cursor[0],ground.shape[1]), ".")
        ground = np.concatenate((new_rows, ground), axis=0)
        cursor[0] = 0
      else:
        cursor -= (count, 0)
    if direction == "R" and ground.shape[1] < cursor[1] + count:
      # print(f"Expanding cols")
      new_cols = np.full((ground.shape[0],cursor[1]+count+1-ground.shape[1]), ".")
      ground = np.concatenate((ground, new_cols), axis=1)
    if direction == "L":
      if cursor[1] < count:
        # print(f"Expanding cols")
        new_cols = np.full((ground.shape[0],count-cursor[1]), ".")
        ground = np.concatenate((new_cols, ground), axis=1)
        cursor[1] = 0
      else:
        cursor -= (0, count)

    range_start = cursor
    range_end = cursor + abs(dirs[direction] * count)

    # if direction == "U":
    #   tmp = range_end
    #   range_end = range_start - [0,1]
    #   range_start = tmp - [0,1]
    # if direction == "L":
    #   tmp = range_end
    #   range_end = range_start - [1,0]
    #   range_start = tmp - [1,0]
    # print(ground)
    # print(f"Setting rows={range_start[0]}:{range_end[0]+1}, cols={range_start[1]}:{range_end[1]+1}")
    # import pdb; pdb.set_trace()
    ground[range_start[0]:range_end[0]+1, range_start[1]:range_end[1]+1] = "#"
    if direction in ["R", "D"]:
      cursor = range_end
    # print_ground(ground)
    # print(f"(after {direction} {count})")
    # print(f"new cursor = {cursor}")

  print_ground(ground)

  # Find a single inner cell to start the tree search
  inner_cell = None
  for r, row in enumerate(ground):
    if inner_cell is not None:
      break
    prev_val = "."
    for col, val in enumerate(row):
      if val == "#":
        if prev_val == ".":
          prev_val = "#"
          continue
        else:
          break
      else:
        if prev_val == "#":
          inner_cell = (r, col)
          break

  find_inner_nodes(inner_cell, ground)
  print_ground(ground)

  return len([x for x in ground.flatten() if x == "#"])



def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
