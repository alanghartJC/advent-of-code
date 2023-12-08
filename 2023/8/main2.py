from pprint import pprint
from hashlib import md5
import re
from typing import List, Dict
from dataclasses import dataclass, field
import math

@dataclass
class RepeatingPath:
  start_count: int
  path_len: int
  z_offset: int

def check_solution(path: RepeatingPath, possible_solution: int):
  for z_offset in path.z_offsets:
    if (possible_solution - path.start_count) % path.path_len == z_offset:
      return True
  return False

def solve(input_str: str):
  lines = input_str.splitlines()
  instructions = lines[0]
  adj_list = []
  adj_dict = {}

  for line in lines[2:]:
    node = line[0:3]
    left = line[7:10]
    right = line[12:15]
    adj_list.append((node, left, right))
    adj_dict[node] = {'L': left, 'R': right}

  cursors = []
  for node in adj_dict.keys():
    if node[-1] == 'A':
      cursors.append(node)

  print("")

  repeating_paths_dict: Dict[str, RepeatingPath] = {}
  for cursor in cursors:
    if cursor[-1] != 'A':
      continue
    starts = {}
    cur = cursor
    count = 0
    z_offset = None
    while cursor not in repeating_paths_dict:
      for instr_index, instr in enumerate(instructions):
        # It's assumed that every repeating path ends on a Z node, and each repeating path has only one Z node.
        hit = (instr_index, cur)
        suffix = ''
        if cur[-1] == 'Z':
          z_offset = count
          suffix = '  <------'
        print(f"  {count}: cur={cur} hit={hit} {suffix}")
        if hit in starts:
          print(f"Found repeat with instr_index={instr_index}, cur={cur}, prev_cur={prev_cur} path_len={count-1}, z_offset={z_offset-1} ({-(count-z_offset+1)})")
          repeating_paths_dict[cursor] = RepeatingPath(start_count=starts[hit], path_len=count-1, z_offset=z_offset-1)
          break
        starts[hit] = count
        prev_cur = cur
        cur = adj_dict[cur][instr]
        count += 1

  repeating_paths: List[RepeatingPath] = sorted(repeating_paths_dict.values(), key=lambda p:p.start_count, reverse=False)

  print(f"path lengths: {[r.path_len for r in repeating_paths]}")
  lcm = math.lcm(*[r.path_len for r in repeating_paths])
  print(f"lcm: {lcm}")
  return lcm
  return math.lcm(*[r.path_len for r in repeating_paths]) * repeating_paths[0].path_len + repeating_paths[0].start_count - repeating_paths[0].z_offset
  consolidated = repeating_paths
  while len(consolidated) > 1:
    repeating_paths = consolidated
    consolidated = []
    pprint(repeating_paths)
    for i in range(0, len(repeating_paths), 2):
      common_path = repeating_paths[i]
      path = repeating_paths[i+1]
      print(f"Common path: {common_path}")
      print(f"Other path: {path}")
      # import pdb; pdb.set_trace()
      # Find the next coincident count between the two paths
      common_repeats = 1
      path_repeats = 1
      common_len = -1
      path_len = -2
      if common_path.start_count == path.start_count:
        common_len = path_len = common_path.start_count + (math.lcm(common_path.path_len, path.path_len))
      while common_len != path_len:
        common_len = common_path.start_count + (common_repeats * common_path.path_len)
        path_len = path.start_count + (path_repeats * path.path_len)
        # print(f'{common_path.start_count} + ({common_repeats} * {common_path.path_len}) != {path.start_count} + ({path_repeats} * {path.path_len})')
        if common_len > path_len:
          # print(f"{common_len} > {path_len}")
          # import pdb; pdb.set_trace()
          path_repeats += max(((common_len - path_len) // path.path_len), 1)
        elif path_len != common_len:
          common_repeats += max(((path_len - common_len) // common_path.path_len), 1)
      print(f'{common_path.start_count} + ({common_repeats} * {common_path.path_len}) == {path.start_count} + ({path_repeats} * {path.path_len})')
      print(f"  Merging with {path}")
      consolidated.append(RepeatingPath(start_count=common_len, path_len=math.lcm(common_path.path_len, path.path_len)))

  print(f"Final path: {consolidated[0]}")
  return consolidated[0].start_count - 1

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
