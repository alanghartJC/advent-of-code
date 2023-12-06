import re
import numpy as np
from typing import List

def num_to_index(nums: List[int], num: int):
  for i, val in enumerate(nums):
    if num < val:
      return i-1
  return i

def has_seed(seed_nums: List[int], num: int):
  for s in range(0, len(seed_nums), 2):
    start_seed = seed_nums[s]
    seed_count = seed_nums[s+1]
    end_seed = start_seed + seed_count - 1
    if num >= start_seed and num <= end_seed:
      return True
  return False

def solve(input_str):
  section_strs = re.split('\n\n', input_str)
  seed_nums = [int(s) for s in section_strs[0].split(':')[1].split()]

  all_nums = set(seed_nums)
  all_sizes = set()
  sections = []
  for section_str in section_strs[1:]:
    section = []
    for mapping in section_str.splitlines()[1:]:
      dest, src, size = [int(x) for x in mapping.split()]
      section.append((dest, src, size))
      all_nums.update([dest, src])
      all_sizes.add(size)
    sections.append(section)

  for n in list(all_nums):
    for s in all_sizes:
      all_nums.add(n+s+1)
      all_nums.add(n+s)
      all_nums.add(n+s-1)
      all_nums.add(max(0, n-s+1))
      all_nums.add(max(0, n-s))
      all_nums.add(max(0, n-s-1))
  all_nums = sorted(list(all_nums))

  grid = np.full((len(sections), len(all_nums)), 0, dtype=int)
  for l, section in enumerate(reversed(sections)):
    layer = grid[l]
    for i in range(len(all_nums)):
      for dest, src, size in section:
        num = all_nums[i]
        shift = dest - src
        if num >= dest and num < dest + size:
          layer[i] = shift
          break

  print(f'{len(all_nums)} nums total')

  for location_index, location_num in enumerate(all_nums):
    print(f'location {location_index}/{len(all_nums)} ({float(location_index)*100.0/len(all_nums):.2}%)')
    cur_index = location_index
    for layer in grid:
      # print(f"cur_index={cur_index} num={all_nums[cur_index]} shift={layer[cur_index]}")
      cur_index = num_to_index(all_nums, all_nums[cur_index] - layer[cur_index])
    # print(f"cur_index={cur_index} num={all_nums[cur_index]}")
    if has_seed(seed_nums, all_nums[cur_index]):
      return location_num

  return -1


def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
