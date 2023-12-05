import re
import math
from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Mapping:
  src: int
  dest: int
  size: int

def solve(input_str):
  sections = re.split('\n\n', input_str)
  seeds = [int(s) for s in sections[0].split(':')[1].split()]

  # mappings = defaultdict(lambda: defaultdict(dict))
  map_groups = []
  for section in sections[1:]:
    # match = re.search(r'([^-]+)-to-([^ ]+) map:', section)
    # src_name, dest_name = match.groups()
    map_group = []
    for mapping in section.splitlines()[1:]:
      dest, src, size = [int(x) for x in mapping.split()]
      print(f'Mapping: dest={dest}, src={src}, size={size}')
      mapping = Mapping(src=src, dest=dest, size=size)
      map_group.append(mapping)

    map_groups.append(map_group)

  min_location = math.inf
  for seed in seeds:
    print(f'Seed {seed}')
    src = seed
    dest = None
    for map_group in map_groups:
      print(f'Next group')
      for mapping in map_group:
        if src >= mapping.src and src <= (mapping.src + mapping.size):
          dest = src + (mapping.dest - mapping.src)
          print(f'src ({src}) -> dest ({dest})')
          src = dest
          break
        else:
          print(f'False: {src} >= {mapping.src} and {src} <= {(mapping.src + mapping.size)}')

    min_location = min(src, min_location)

  return min_location

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
