from dataclasses import dataclass
from typing import Dict, Tuple, List, Set
from collections import defaultdict, deque

@dataclass
class Node:
  value: str
  row: int
  col: int
  depth: int = None

  def __hash__(self) -> int:
    return hash((self.row, self.col))


DOWN = (1,0)
RIGHT = (0,1)
UP = (-1,0)
LEFT = (0,-1)

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

# Mapping the direction of this node from the source's perspective to the degree change
# Numbers are in units of 90-degree turns. 1 is turning right 90 degrees, -1 is left
ROTATIONS = {
    "S": {DOWN: 0, RIGHT: 0, LEFT: 0, UP: 0},
    "F": {UP: 1, LEFT: -1},
    "7": {RIGHT: 1, UP: -1},
    "J": {RIGHT: -1, DOWN: 1},
    "L": {DOWN: -1, LEFT: 1},
    "|": {UP: 0, DOWN: 0},
    "-": {LEFT: 0, RIGHT: 0},
}

def find_loops(start_node: Node, adj_list: Dict[Node, Set[Node]]) -> List[List[Node]]:
  output = []
  for branch in adj_list[start_node]:
    # We only want unique loops. Check if another loop ended on this branch node.
    if branch in [x[-1] for x in output]:
      continue
    path = [start_node]
    node = branch
    while node != start_node:
      for adj in adj_list[node]:
        if adj != path[-1]:
          break
      path.append(node)
      node = adj
    output.append(path)
  return output

def get_loop_rotation(loop: List[Node]) -> int:
  """Returns 1 for clockwise, -1 for counterclockwise"""
  cumulative_rotation = 0
  for i, node in enumerate(loop[:-1]):
    next_node = loop[i+1]
    direction_to_next = (next_node.row-node.row, next_node.col-node.col)
    cumulative_rotation += ROTATIONS[next_node.value][direction_to_next]
  return int(cumulative_rotation/abs(cumulative_rotation))

def get_adj_node(node: Node, node_grid: List[List[Node]], direction: Tuple[int, int]) -> Node:
  row, col = node.row + direction[0], node.col + direction[1]
  if row < 0 or row >= len(node_grid):
    return None
  if col < 0 or col >= len(node_grid[0]):
    return None
  return node_grid[row][col]

def find_interior_nodes(loop: List[Node], node_grid: List[List[Node]], rotation: int) -> int:
  found = set(loop)
  queue = deque()

  for i, node in enumerate(loop[:-1]):
    next_node = loop[i+1]
    direction_to_next = (next_node.row-node.row, next_node.col-node.col)
    negate = 0
    if direction_to_next in [UP, DOWN]:
      negate = -1
    direction_to_side = (direction_to_next[1]*negate*rotation, direction_to_next[0]*negate*rotation)
    queue.append(get_adj_node(node, node_grid, direction_to_side))
    queue.append(get_adj_node(next_node, node_grid, direction_to_side))

  while queue:
    node = queue.popleft()
    if node in found:
      continue
    found.add(node)

    for direction in [UP, DOWN, LEFT, RIGHT]:
      adj_node = get_adj_node(node, node_grid, direction)
      if not adj_node:
        continue
      if adj_node not in found:
        queue.append(adj_node)

  internal = found - set(loop)
  return len(internal)


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

  loops = sorted(find_loops(start_node, adj_list), key=lambda x: len(x), reverse=True)

  rotation = get_loop_rotation(loops[0])
  print(f"Path rotation: {rotation}")
  interior_nodes = find_interior_nodes(loops[0], node_grid, rotation)
  return interior_nodes

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
