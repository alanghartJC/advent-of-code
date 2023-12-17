from typing import List, Tuple, Dict, Set
from dataclasses import dataclass, field
from pprint import pprint, pformat
import numpy as np

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
  # maps (direction, straight_len) -> min_loss
  memo: Dict[Tuple[Tuple[int, int], int], int] = field(default_factory=dict)

  def __hash__(self) -> int:
    return hash((self.row, self.col))

def get_adj(ndgrid: np.ndarray, cur: Node, direction: Tuple[int, int]) -> Node:
  # import pdb; pdb.set_trace()
  nextrow = cur.row + direction[0]
  nextcol = cur.col + direction[1]

  if 0 <= nextrow < ndgrid.shape[0] and 0 <= nextcol < ndgrid.shape[1]:
    return ndgrid[nextrow][nextcol]
  return None

def print_path(ndgrid: np.ndarray[Node]):
  for row in ndgrid:
    for node in row:
      if node.cur_direction is None:
        print(node.heatloss, end="")
      else:
        if node.is_head:
          print("*", end="")
        else:
          pchar = {
            UP: "^",
            DOWN: "v",
            LEFT: "<",
            RIGHT: ">"
          }[node.cur_direction]
          print(pchar, end="")
    print("")
  print("")

def search_path(ndgrid: np.ndarray[Node], node: Node = None, cur_loss: int = 0, min_loss: int = None, direction: Tuple[int, int] = None, straight_len: int = 1, visited: Set[Node] = None, losses: List[int] = []) -> int:
  if node is None:
    node = ndgrid[0][0]
    visited = set([node])
    losses = [node.heatloss]
    cur_loss = node.heatloss
    # import pdb; pdb.set_trace()


  # print(f"depth={len(visited)}")

  # print(f"Visiting {node} cur_loss={cur_loss}, direction={direction}, straight_len={straight_len}")
  if node == ndgrid[-1,-1]:
    # import pdb; pdb.set_trace()
    if min_loss is None or cur_loss < min_loss:
      print(f"New minimum: {cur_loss}")
      pprint(losses)
      print(sum(losses))
      node.is_head = True
      print_path(ndgrid)
      node.is_head = False
    # import pdb; pdb.set_trace()
    return cur_loss

  # if node == ndgrid[1][3]:
  #   import pdb; pdb.set_trace()

  must_turn = False
  if direction is not None and straight_len == 3:
    must_turn = True
    straight_len = 0

  # Ordering of the directions is important here, making it an A* search
  all_adj = [(d, get_adj(ndgrid, node, d)) for d in [RIGHT, DOWN, UP, LEFT]]
  # all_adj = sorted([(d, n) for (d, n) in all_adj if n is not None and n not in visited], key=lambda x:x[1].heatloss)
  # all_adj = [(d, n) for (d, n) in all_adj if n is not None and n not in visited]

  output = None
  for d, adj_node in all_adj:
    if adj_node is None:
      continue
    if adj_node in visited:
      continue
    if must_turn and direction == d:
      continue
    next_cur_loss = cur_loss+adj_node.heatloss
    if min_loss is not None and next_cur_loss > min_loss:
      continue

    next_straight_len = straight_len + 1
    if d != direction:
      next_straight_len = 1

    memo_key = (d, next_straight_len)
    # if node == ndgrid[5,11]:
    #   import pdb; pdb.set_trace()
    if memo_key in adj_node.memo:
      if adj_node.memo[memo_key] is None:
        continue
      adj_result = next_cur_loss + adj_node.memo[memo_key]
      # print(f"Using memo {adj_node} ({d}, {next_straight_len}) = {adj_result}")
    else:
      visited.add(adj_node)
      adj_node.cur_direction = d
      adj_result = search_path(ndgrid, adj_node, next_cur_loss, min_loss, d, next_straight_len, visited, losses + [adj_node.heatloss])
      adj_node.cur_direction = None
      visited.remove(adj_node)

      if adj_result is None:
        adj_node.memo[memo_key] = None
        continue
      adj_node.memo[memo_key] = adj_result - next_cur_loss
      print(f"{adj_node}: {adj_result - next_cur_loss}")
    if min_loss is None:
      min_loss = adj_result
      output = adj_result
    elif adj_result < min_loss:
      min_loss = adj_result
      output = adj_result

  return output


def solve(input_str: str):
  grid_raw: List[List[int]] = []

  for r, line in enumerate(input_str.splitlines()):
    grid_raw.append([Node(row=r, col=c, heatloss=int(x)) for c, x in enumerate(line)])

  ndgrid: np.ndarray = np.array(grid_raw)


  output = search_path(ndgrid)
  import pdb; pdb.set_trace()
  return output


def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
