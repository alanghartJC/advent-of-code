import re
import bisect
from pprint import pprint
from typing import List

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

  sections = []
  for section_str in section_strs[1:]:
    section = []
    for mapping in section_str.splitlines()[1:]:
      dest, src, size = [int(x) for x in mapping.split()]
      section.append((dest, src, dest+size-1, src+size-1, dest-src))

    section = sorted(section, key=lambda x:x[0])
    i = 0
    prev_end = -1
    while i < len(section)-1:
      dest, src, dest_end, src_end, shift = section[i]
      if prev_end + 1 < dest:
        print(f'Adding: {(prev_end+1, prev_end+1, dest-1, dest-1, 0)}')
        section.insert(i, (prev_end+1, prev_end+1, dest-1, dest-1, 0))
        print(f'Section: ')
        pprint(section)
        prev_end = dest
      else:
        prev_end = dest_end
        i += 1
    sections.append(section)

  pprint(sections)
  location_num = 0
  cur_val = 0
  while True:
    cur_val = location_num
    bad_path = False
    for layer_index, layer in enumerate(reversed(sections)):
      if bad_path:
        break
      i = max(0, bisect.bisect_left(layer, cur_val+1, key=lambda e:e[0])-1)
      dest, src, dest_end, src_end, shift = layer[i]
      if cur_val >= dest and cur_val <= dest_end:
        cur_val -= shift
    if layer_index == len(sections)-1 and has_seed(seed_nums, cur_val):
      if bad_path:
        import pdb; pdb.set_trace()
      return location_num

    location_num += 1


def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
