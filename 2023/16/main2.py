from typing import List, Tuple
from dataclasses import dataclass, field
import numpy as np
from pprint import pprint, pformat

DOWN = (1,0)
RIGHT = (0,1)
UP = (-1,0)
LEFT = (0,-1)

@dataclass
class Node:
  ntype: str
  col: int
  row: int
  streams: int = 0

  def __hash__(self) -> int:
    return hash((self.col, self.row))

@dataclass
class Cursor:
  id: int
  cur: Node = None
  direction: Tuple[int, int] = RIGHT

  def __hash__(self) -> int:
    return hash((self.id))

def next(ndgrid: np.ndarray, cur: Node, direction: Tuple[int, int]) -> Node:
  # import pdb; pdb.set_trace()
  nextrow = cur.row + direction[0]
  nextcol = cur.col + direction[1]

  if 0 <= nextrow < ndgrid.shape[0] and 0 <= nextcol < ndgrid.shape[1]:
    return ndgrid[nextrow][nextcol]
  return None

def print_energized(ndgrid):
  for row in ndgrid:
    for node in row:
      if node.streams:
        print("#", end="")
      else:
        print(".", end="")
    print("")


def get_energized_tiles(ndgrid: np.ndarray, start_node: Node, start_direction: Tuple[int, int]) -> int:
  cursors = {Cursor(id=0, cur=start_node, direction=start_direction)}

  # Re-initialize all nodes
  for n in ndgrid.flatten():
    n.streams = 0

  cursor_states = set()

  while cursors:
    for cursor in list(cursors):
      while cursor.cur:

        # pprint(cursors)
        # print_energized(ndgrid)
        cursor.cur.streams += 1

        if cursor.cur.ntype == ".":
          cursor.cur = next(ndgrid, cursor.cur, cursor.direction)
        elif cursor.cur.ntype == "\\":
          # import pdb; pdb.set_trace()
          # Causes direction to transpose
          cursor.direction = (cursor.direction[1], cursor.direction[0])
          cursor.cur = next(ndgrid, cursor.cur, cursor.direction)
        elif cursor.cur.ntype == "/":
          # import pdb; pdb.set_trace()
          # Causes direction to transpose and negate
          cursor.direction = (-cursor.direction[1], -cursor.direction[0])
          cursor.cur = next(ndgrid, cursor.cur, cursor.direction)
        elif cursor.cur.ntype == "-":
          if cursor.direction[0]:
            lsplit = next(ndgrid, cursor.cur, LEFT)
            if lsplit:
              cursors.add(Cursor(id=len(cursors), cur=lsplit, direction=LEFT))
            cursor.cur = next(ndgrid, cursor.cur, RIGHT)
            cursor.direction = RIGHT
          else:
            cursor.cur = next(ndgrid, cursor.cur, cursor.direction)
        elif cursor.cur.ntype == "|":
          if cursor.direction[1]:
            usplit = next(ndgrid, cursor.cur, UP)
            if usplit:
              cursors.add(Cursor(id=len(cursors), cur=usplit, direction=UP))
            cursor.cur = next(ndgrid, cursor.cur, DOWN)
            cursor.direction = DOWN
          else:
            cursor.cur = next(ndgrid, cursor.cur, cursor.direction)

        if (cursor.cur, cursor.direction) in cursor_states:
          break
        cursor_states.add((cursor.cur, cursor.direction))

      # print(f"Finished cursor {cursor}")
      cursors.remove(cursor)

  # print(ndgrid)
  output = 0
  for n in ndgrid.flatten():
    if n.streams:
      output += 1

  return output

def solve(input_str: str):
  print("")
  grid_raw: List[List[str]] = []

  for r, row in enumerate(input_str.splitlines()):
    grid_raw.append([Node(ntype=val, col=c, row=r) for c, val in enumerate(list(row))])

  # import pdb; pdb.set_trace()
  ndgrid: np.ndarray = np.array(grid_raw)

  max_energized = 0
  for r in range(ndgrid.shape[0]):
    energized = get_energized_tiles(ndgrid, ndgrid[r,0], (0,1))
    max_energized = max(max_energized, energized)

    energized = get_energized_tiles(ndgrid, ndgrid[r,-1], (0,-1))
    max_energized = max(max_energized, energized)

  for c in range(ndgrid.shape[1]):
    energized = get_energized_tiles(ndgrid, ndgrid[0,c], (1,0))
    max_energized = max(max_energized, energized)

    energized = get_energized_tiles(ndgrid, ndgrid[-1,c], (-1,0))
    max_energized = max(max_energized, energized)

  return max_energized

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
