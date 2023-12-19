from typing import List, Tuple, Dict, Set
from dataclasses import dataclass, field
from pprint import pprint, pformat
import numpy as np
import time
from copy import deepcopy
from heapq import heapify, heappop, heappush

DOWN = (1,0)
RIGHT = (0,1)
UP = (-1,0)
LEFT = (0,-1)

@dataclass
class Node:
  row: int
  col: int
  heatloss: int
  cur_direction: Tuple[int, int] = None
  is_head: bool = False
  is_goal: bool = False
  # maps (direction, straight_len) -> min_loss
  # memo: Dict[Tuple[Tuple[int, int], int], int] = field(default_factory=dict)

  def __hash__(self) -> int:
    return hash((self.row, self.col))

def rough_distance(ndgrid, node):
  return (ndgrid.shape[0]-node.row) + (ndgrid.shape[1]-node.col)

@dataclass
class Cursor:
  id: int
  heatloss: int
  rough_distance: int
  cur_direction: Tuple[int, int] = None
  path: List[Node] = field(default_factory=list)
  visited: Set[Node] = field(default_factory=set)

  def jump(self, ndgrid, direction: Tuple[int, int], nodes: List[Node]):
    assert(len(nodes) <= 3)
    assert(direction != self.cur_direction)
    self.cur_direction = direction
    for node in nodes:
      self.heatloss += node.heatloss
      self.path.append(node)
      self.visited.add(node)
      if node.is_goal:
        # print(f"Goal found. heatloss sum = {self.heatloss}")
        # import pdb; pdb.set_trace()
        return self.heatloss
    self.rough_distance = rough_distance(ndgrid, self.path[-1])

  def __lt__(self, other: "Cursor"):
    return self.heatloss*self.rough_distance < other.heatloss*other.rough_distance

def get_adj(ndgrid: np.ndarray, cur: Node, direction: Tuple[int, int]) -> Node:
  output = []
  for x in range(3):
    nextrow = cur.row + direction[0]
    nextcol = cur.col + direction[1]

    if 0 <= nextrow < ndgrid.shape[0] and 0 <= nextcol < ndgrid.shape[1]:
      output.append(ndgrid[nextrow][nextcol])
      cur = output[-1]
    else:
      break
  return output

def print_path(ndgrid: np.ndarray[Node], path: List[Node]):
  for row in ndgrid:
    for node in row:
      node.is_head = False

  for node in path:
    node.is_head = True

  for row in ndgrid:
    for node in row:
      if node.is_head:
        print("*", end="")
      else:
        print(node.heatloss, end="")
      # if node.cur_direction is None:
      #   print(node.heatloss, end="")
      # else:
      #   if node.is_head:
      #     print("*", end="")
      #   else:
      #     pchar = {
      #       UP: "^",
      #       DOWN: "v",
      #       LEFT: "<",
      #       RIGHT: ">"
      #     }[node.cur_direction]
      #     print(pchar, end="")
    print("")
  print("")

final_losses = None
debug = 0
min_len = None


def best_first_search(ndgrid: np.ndarray[Node]) -> int:
  cursor_count = 0
  first_node = ndgrid[0][0]
  heap: List[Cursor] = [Cursor(id=cursor_count, heatloss=0, rough_distance=rough_distance(ndgrid, first_node), cur_direction=DOWN, path=[first_node], visited={first_node})]

  cursor_count += 1
  iter_count = 0
  cur_min_heatloss = None
  while heap:
    iter_count += 1
    # import pdb; pdb.set_trace()
    cursor = heappop(heap)
    if cur_min_heatloss is not None and cursor.heatloss >= cur_min_heatloss:
      continue
    reused = False
    cur_node = cursor.path[-1]
    if iter_count % 1000 == 0:
      print(f"{iter_count}: cursor count: {len(heap)} top of heap: {(cursor.path[-1].row, cursor.path[-1].col)} heatloss={cursor.heatloss} pathlen={len(cursor.path)}")

    cursors_to_jump = []

    for negate in [1, -1]:
      new_direction = (negate * cursor.cur_direction[1], negate * cursor.cur_direction[0])
      jump_nodes = get_adj(ndgrid, cur_node, new_direction)
      for delta in range(len(jump_nodes)):
        if not reused:
          new_cursor = cursor
          reused = True
        else:
          new_cursor = Cursor(id=cursor_count, heatloss=cursor.heatloss, rough_distance=rough_distance(ndgrid, cursor.path[-1]), cur_direction=cursor.cur_direction, path=list(cursor.path), visited={*cursor.visited})
        cursor_count += 1
        cursors_to_jump.append((new_cursor, new_direction, jump_nodes[:delta+1]))

    for new_cursor, new_direction, jump_nodes in cursors_to_jump:
      if any([n in new_cursor.visited for n in jump_nodes]):
        continue
      complete_path_heatloss = new_cursor.jump(ndgrid, new_direction, jump_nodes)
      if complete_path_heatloss is not None:
        if cur_min_heatloss is None or complete_path_heatloss < cur_min_heatloss:
          cur_min_heatloss = complete_path_heatloss
          print(f"Setting cur_min_heatloss={cur_min_heatloss}")
          print_path(ndgrid, new_cursor.path)
          # print([x.heatloss for x in new_cursor.path])
          # print(sum([x.heatloss for x in new_cursor.path]))
          # print([])
      # print(f"Adding cursor id={new_cursor.id} row,col={new_cursor.path[-1].row},{new_cursor.path[-1].col} ({len(heap)} live cursors)")
      elif cur_min_heatloss is None or new_cursor.heatloss <= cur_min_heatloss:
        heappush(heap, new_cursor)
      # else:
      #   print(f"Discarding cursor (heatloss={new_cursor.heatloss}, remain={len(heap)})")

  return


def solve(input_str: str):
  grid_raw: List[List[int]] = []

  for r, line in enumerate(input_str.splitlines()):
    grid_raw.append([Node(row=r, col=c, heatloss=int(x)) for c, x in enumerate(line)])

  ndgrid: np.ndarray = np.array(grid_raw)
  ndgrid[-1][-1].is_goal = True

  output = best_first_search(ndgrid)

  # for node in final_losses:
  #   ndgrid[node.row,node.col].cur_direction = node.cur_direction
  # pprint(final_losses)
  # print_path(ndgrid)
  import pdb; pdb.set_trace()
  return output


def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
