import numpy as np
from typing import List, Dict
from pprint import pprint, pformat
from collections import defaultdict


# def find_symmetry_line_broken(hashes: List[int], hash_dict: Dict[int, List[int]]) -> int:
#   # import pdb; pdb.set_trace()
#   for direction, is_reversed in [(hashes, False), (list(reversed(hashes)), True)]:
#     for other_idx, other in list(reversed(list(enumerate(direction)))):
#       invalid = False
#       if other_idx != 0 and other == direction[0]:
#         for x in range((other_idx+1)//2):
#           if direction[x] != direction[other_idx - x]:
#             # print(f"Invalid (x={x}): {direction[x]} != {direction[other_idx - x]}")
#             invalid = True
#             break
#           # print(f"Matching ({x}) {direction[x]} == ({other_idx - x}) {direction[other_idx - x]}")
#         if not invalid:
#           if is_reversed:
#             # print(f"Returning {len(hashes) - (other_idx//2) - 1}")
#             return len(hashes) - (other_idx//2) - 1
#           else:
#             # print(f"Returning {(other_idx+1)//2}")
#             return (other_idx+1)//2

#   return -1

def find_symmetry_line(hashes: List[int], hash_dict: Dict[int, List[int]], exclude: int = -1) -> int:
  max_radius = 0
  result_index = -1
  for matches in hash_dict.values():
    for x in range(len(matches)-1):
      for y in range(x+1, len(matches)):
        xval = matches[x]
        yval = matches[y]
        diff = abs(xval - yval)
        if diff == 1:
          high = max(xval, yval)
          low = min(xval, yval)

          found = False
          while high <= len(hashes)-1 and low >= 0:
            found = False
            for m in hash_dict.values():
              if high in m and low in m:
                found = True
                break

            if not found:
              break
            high += 1
            low -= 1

          high -= 1
          low += 1

          if found:
            radius = (high - low + 1) // 2
            if radius > max_radius:
              if low == 0:
                if exclude == radius:
                  continue
              else:
                if exclude == len(hashes)-radius:
                  continue

              max_radius = radius
              if low == 0:
                result_index = radius
              else:
                result_index = len(hashes)-radius

  return result_index

def gen_hashes(grid):
  # print(f"\n\nNext grid:\n{grid}")
  row_hashes = [hash(tuple(grid[row,:])) for row in range(grid.shape[0])]
  # print(f'Row hashes: {row_hashes}')
  col_hashes = [hash(tuple(grid[:,col])) for col in range(grid.shape[1])]
  # print(f'Col hashes: {col_hashes}')
  # print("\n\n")

  row_hash_dict: Dict[int, List[int]] = defaultdict(list)
  for i, h in enumerate(row_hashes):
    row_hash_dict[h].append(i)
  col_hash_dict: Dict[int, List[int]] = defaultdict(list)
  for i, h in enumerate(col_hashes):
    col_hash_dict[h].append(i)

  row_hash_dict = {h: sorted(indexes) for h, indexes in row_hash_dict.items()}
  col_hash_dict = {h: sorted(indexes) for h, indexes in col_hash_dict.items()}
  return row_hashes, col_hashes, row_hash_dict, col_hash_dict

def solve(input_str: str):
  print("")
  np_grids: List[np.array] = []
  grid_raw = []
  for line in input_str.splitlines():
    if not line.strip():
      np_grids.append(np.array(grid_raw))
      grid_raw = []
      continue
    grid_raw.append(list(line))
  if grid_raw:
    np_grids.append(np.array(grid_raw))

  row_hashes: List[int] = []
  col_hashes: List[int] = []

  opposite = {"#": ".",
              ".": "#"}
  output = 0
  for grid_no, grid in enumerate(np_grids):
    row_hashes, col_hashes, row_hash_dict, col_hash_dict = gen_hashes(grid)

    # print(f"row_hash_dict:\n{pformat(row_hash_dict)}")
    # print(f"col_hash_dict:\n{pformat(col_hash_dict)}")

    # if grid_no == 11:
    #   import pdb; pdb.set_trace()
    row_res = find_symmetry_line(row_hashes, row_hash_dict)
    if row_res >= 0:
      sym_size = min(grid.shape[0]-row_res, row_res)
      print(f"Grid {grid_no}: Inserting row {row_res} (sym_size={sym_size})")
      print(f"Grid {grid_no}: output += {100*row_res}")
      # print(np.insert(grid, row_res, ["X"] * grid.shape[1], axis=0)[max(0,row_res-sym_size-1):row_res+sym_size+2, :].transpose())
      print(np.insert(grid, row_res, ["X"] * grid.shape[1], axis=0).transpose())

      # output += 100*row_res
    col_res = find_symmetry_line(col_hashes, col_hash_dict)
    if col_res >= 0:
      sym_size = min(grid.shape[1]-col_res, col_res)
      print(f"Grid {grid_no}: Inserting col {col_res} (sym_size={sym_size})")
      print(f"Grid {grid_no}: output += {col_res}")
      # print(np.insert(grid, col_res, ["X"] * grid.shape[0], axis=1)[:, max(0,col_res-sym_size-1):col_res+sym_size+2])
      print(np.insert(grid, col_res, ["X"] * grid.shape[0], axis=1))
      # output += col_res
    if row_res < 0 and col_res < 0:
      print(f"Symmetry not found!")
      import pdb; pdb.set_trace()
    if row_res >= 0 and col_res >= 0:
      print(f"Two symmetries found!")
      import pdb; pdb.set_trace()

    found = False
    for row in range(grid.shape[0]):
      if found:
        break
      for col in range(grid.shape[1]):
        if found:
          break
        grid[row][col] = opposite[grid[row][col]]
        row_hashes, col_hashes, row_hash_dict, col_hash_dict = gen_hashes(grid)
        new_row_res = find_symmetry_line(row_hashes, row_hash_dict, exclude=row_res)
        new_col_res = find_symmetry_line(col_hashes, col_hash_dict, exclude=col_res)
        print(f"new_row_res={new_row_res}")
        print(f"new_col_res={new_col_res}")
        if new_row_res >= 0 and new_row_res != row_res:
          output += 100*new_row_res
          # import pdb; pdb.set_trace()
          found = True
          break
        if new_col_res >= 0 and new_col_res != col_res:
          output += new_col_res
          # import pdb; pdb.set_trace()
          found = True
          break
        grid[row][col] = opposite[grid[row][col]]
    if not found:
      print(f"Not found for {grid_no}")
      import pdb; pdb.set_trace()
  print(f"Total output: {output}")
  return output

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
