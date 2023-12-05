import re
from typing import List
import math
from pprint import pprint, pformat
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class Range:
  min: int
  max: int
  layer: "Layer"
  shift: int = 0
  corresponding_range: "Range" = None
  adjacent_range_higher: "Range" = None
  adjacent_range_lower: "Range" = None
  seeds: List[int] = field(default_factory=list)

  def size(self):
    return self.max-self.min+1

  def __repr__(self):
    return f'Range(min={self.min}, max={self.max}, size={self.size()}, shift={self.shift})'

@dataclass
class Layer:
  id: int
  left_ranges: List[Range] = field(default_factory=list)
  right_ranges: List[Range] = field(default_factory=list)
  left_layer: "Layer" = None
  right_layer: "Layer" = None

  def __repr__(self):
    return f'''Layer(
      id={self.id},
      left_ranges={pformat(self.left_ranges)},
      right_ranges={pformat(self.right_ranges)})'''

def solve(input_str):
  section_strs = re.split('\n\n', input_str)
  seed_nums = [int(s) for s in section_strs[0].split(':')[1].split()]

  # mappings = defaultdict(lambda: defaultdict(dict))

  max_num = 0
  sections = []
  for section_str in section_strs[1:]:
    section = []
    for mapping in section_str.splitlines()[1:]:
      dest, src, size = [int(x) for x in mapping.split()]
      section.append((dest, src, size))
      max_num = max(max_num, dest, src, dest+size, src+size)
    sections.append(section)

  # Pipeline layers are ordered left-to-right (seeds on start on left, location ends on right)
  layers: List[Layer] = []
  next_id = 0
  for section in sections:
    layer = Layer(id=next_id)
    next_id += 1
    for dest, src, size in section:
      src_range = Range(min=src, max=src+size-1, shift=src-dest, layer=layer)
      dst_range = Range(min=dest, max=dest+size-1, shift=dest-src, corresponding_range=src_range, layer=layer)
      src_range.corresponding_range = dst_range

      layer.left_ranges.append(src_range)
      layer.right_ranges.append(dst_range)

    layer.left_ranges = sorted(layer.left_ranges, key=lambda x: x.min)

    range_index = 0
    prev_max = -1
    # import pdb; pdb.set_trace()
    while range_index <= len(layer.left_ranges) and prev_max < max_num:
      if range_index == len(layer.left_ranges):
        new_max = max_num
        new_min = prev_max+1
      else:
        cur_range = layer.left_ranges[range_index]
        if prev_max+1 == cur_range.min:
          prev_max = cur_range.max
          range_index += 1
          continue
        else:
          new_max = cur_range.min-1
          new_min = prev_max+1

      left_range = Range(min=new_min, max=new_max, layer=layer)
      right_range = Range(min=new_min, max=new_max, layer=layer, corresponding_range=left_range)
      left_range.corresponding_range = right_range
      layer.left_ranges.insert(range_index, left_range)
      layer.right_ranges.append(right_range)
      prev_max = new_max
      range_index += 1

    layer.right_ranges = sorted(layer.right_ranges, key=lambda x: x.min)

    for r in [layer.left_ranges, layer.right_ranges]:
      prev_range = None
      for i in range(len(r)):
        if i+1 < len(r):
          next_range = r[i+1]
        else:
          next_range = None
        r[i].adjacent_range_higher = next_range
        r[i].adjacent_range_lower = prev_range
        prev_range = r[i]

    layers.append(layer)

  prev_layer = None
  for i in range(len(layers)):
    if i+1 < len(layers):
      next_layer = layers[i+1]
    else:
      next_layer = None
    layers[i].left_layer = prev_layer
    layers[i].right_layer = next_layer
    prev_layer = layers[i]

  # Add seeds to the left ranges of the leftmost layer
  for r in layers[0].left_ranges:
    for s in range(0, len(seed_nums), 2):
      start_seed = seed_nums[s]
      seed_count = seed_nums[s+1]
      end_seed = start_seed + seed_count - 1
      if end_seed < r.min or start_seed > r.max:
        continue

      r.seeds.append((max(start_seed, r.min), min(end_seed, r.max)))

  pprint(layers)
  for i, r in enumerate(layers[-1].right_ranges):
    # import pdb; pdb.set_trace()
    res = search(r, [i])
    if res:
      pprint(res)
      min_val, max_val = res[0]
      # return min_val

def search(right_range: Range, history):
  if history == [2, 3, 4, 1, 1, 1, 0]:
    import pdb; pdb.set_trace()
  left_range = right_range.corresponding_range
  shift = left_range.min - right_range.min
  if left_range.seeds:
    if left_range.min == 50:
      print(history)
      # import pdb; pdb.set_trace()
    return [(seed_start-shift, seed_end-shift) for (seed_start, seed_end) in left_range.seeds]
  next_layer = right_range.layer.left_layer
  if next_layer is None:
    return []
  output = []
  for i, r in enumerate(next_layer.right_ranges):
    if r.min > left_range.max or r.max < left_range.min:
      # ranges don't intersect any
      continue
    res = search(r, [i, *history])
    if res:
      for seed_start, seed_end in res:
        if seed_end < left_range.min or seed_start > left_range.max:
          continue
        output.append((max(left_range.min, seed_start-shift), min(left_range.max, seed_end-shift)))
  return output


def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
