from dataclasses import dataclass
from typing import Dict, List, Set, Union, Deque
from collections import defaultdict, deque
import numpy as np

@dataclass
class Node:
  value: str
  row: int
  col: int
  depth: int = None

  def __hash__(self) -> int:
    return hash((self.row, self.col))

def bfs(node: Node, queue: Deque[Node], adj_list: Dict[Node, Set[Node]], all_depths: List[List[Union[int, str]]], found: Set[Node]) -> int:
  max_depth = 0

  found.add(node)
  node.depth = 0
  all_depths[node.row][node.col] = 0
  queue.append(node)

  while queue:
    node = queue.popleft()
    max_depth = max(max_depth, node.depth)

    for subnode in adj_list[node]:
      if subnode not in found:
        found.add(subnode)
        subnode.depth = node.depth + 1
        all_depths[subnode.row][subnode.col] = subnode.depth
        queue.append(subnode)
  return max_depth


DOWN = (1,0)
RIGHT = (0,1)
UP = (-1,0)
LEFT = (0,-1)

OPPOSITE = {
  DOWN: UP,
  UP: DOWN,
  RIGHT: LEFT,
  LEFT: RIGHT,
}

DIRECTIONS = {
    "S": (DOWN, RIGHT, UP, LEFT),
    "F": (DOWN, RIGHT),
    "7": (LEFT, DOWN),
    "J": (LEFT, UP),
    "L": (RIGHT, UP),
    "|": (UP, DOWN),
    "-": (LEFT, RIGHT),
    ".": tuple(),
}


def solve(input_str: str):
  grid = [list(line) for line in input_str.splitlines()]

  adj_list: Dict[Node, Set[Node]] = defaultdict(set)
  start_node: Node = None
  node_grid: List[List[Node]] = []
  all_nodes: List[Node] = []

  for row_idx, row in enumerate(grid):
    node_row = []
    for col_idx, cell in enumerate(row):
      node = Node(value=cell, row=row_idx, col=col_idx)
      node_row.append(node)
      all_nodes.append(node)
      if node.value == "S":
        start_node = node
    node_grid.append(node_row)

  row_count = len(grid)
  col_count = len(grid[0])

  for node in all_nodes:
    adj_deltas = []
    # (row, col) delta. Higher row number means lower in visual grid
    adj_deltas.extend(DIRECTIONS[node.value])

    for row_delta, col_delta in adj_deltas:
      adj_row, adj_col = node.row + row_delta, node.col + col_delta
      if adj_row < 0 or adj_row >= row_count:
        continue
      if adj_col < 0 or adj_col >= col_count:
        continue
      adj_value = node_grid[adj_row][adj_col].value
      if (-row_delta, -col_delta) not in DIRECTIONS[adj_value]:
        continue
      adj_list[node].add(node_grid[adj_row][adj_col])
      if len(adj_list[node]) > 2:
        import pdb; pdb.set_trace()


  found = set()
  queue = deque()
  all_depths = np.array([["." for _ in range(col_count)] for _ in range(row_count)])

  depth = bfs(start_node, queue, adj_list, all_depths, found)

  return depth


def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
