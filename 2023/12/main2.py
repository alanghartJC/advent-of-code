from typing import List, Dict, Tuple
import math
import re

def prefix_len(pattern: str) -> int:
  c = pattern[0]
  output = 0
  for x in pattern:
    if x == c:
      output += 1
    else:
      break
  return output

def solve_questionmark_group(q_count: int, sizes: List[int]) -> int:
  """Returns number of ways the given sizes can be distributed in the section
  of question marks. ALL sizes must be accounted for.

  This assumes that the first and last ? will be #."""
  # Example input:  ????????????? 1,2,3
  # The only thing that varies is the spacing *between* each segment of #'s.
  # To simplify, each segment of #'s can be shrunk to a single #
  # (here, remove 3 ?'s)
  # ?????????? 1,1,1
  # Now it is simply 2 parameters: number of ?'s and number of sizes
  # if q_count == len("???????????????"):
  size_count = len(sizes)

  q_count -= sum([x-1 for x in sizes])

  if size_count == 1:
    if q_count <= 0:
      return 0
    return q_count

  # buckets are segments where dots can go
  buckets = size_count - 1

  # these are *moveable* dots. does not include one dot per bucket that cannot move
  # (otherwise the two adjacent # segments would be combined into one)
  dots = q_count - (2*size_count - 1)

  if dots == 0:
    return 1
  if dots < 0:
    return 0
  # It is a combinatorial problem: how many different ways can the moveable dots be distributed
  # among the buckets?
  if (dots + buckets - 1) < 0:
    import pdb; pdb.set_trace()
  if (buckets - 1) < 0:
    import pdb; pdb.set_trace()
  combos = 0
  # Bookends are "#"
  combos += math.factorial(dots + buckets - 1) // (math.factorial(dots) * math.factorial(buckets - 1))
  if (dots >= 2):
    # Bookends are "."
    combos += math.factorial((dots-2) + (buckets+2) - 1) // (math.factorial(dots-2) * math.factorial((buckets+2) - 1))
  if (dots >= 1):
    # Bookends are "#" and "."
    combos += 2*math.factorial((dots-1) + (buckets+1) - 1) // (math.factorial(dots-1) * math.factorial((buckets+1) - 1))
  return combos


def memoize(memo, key, val, prefix):
  # print(f"prefix={prefix} key={key} val={val}")
  memo[key] = val
  return val

def count_matches(memo: Dict[Tuple[int, Tuple[int]], int], pattern: str, sizes: List[int], depth: int, prefix: str) -> int:
  """Recursively search for matching arrangements and return how many"""
  # print(f"pattern={running_pattern}-{pattern}\tsizes={sizes}\tcur_group_type={cur_group_type}\tcur_group_len={cur_group_len}\tspace_required={space_required}")
  # import pdb; pdb.set_trace()
  memo_key = (pattern, tuple(sizes))
  memo_res = memo.get(memo_key)
  # if memo_key == ("????????#?", (3,1,1)):
  #   import pdb; pdb.set_trace()
  if memo_res:
    # print(f"Found memo for {memo_key}: {memo_res}")
    return memo_res

  # print(" "*depth, end="")
  if not sizes:
    # print(f"\t\t\t\tsolution: {prefix}")
    if "#" in pattern:
      return memoize(memo, memo_key, 0, prefix)
    return memoize(memo, memo_key, 1, prefix)

  if not pattern:
    # Out of space. Invalid arrangement
    return memoize(memo, memo_key, 0, prefix)

  if "#" not in pattern:
    res = solve_questionmark_group(len(pattern), sizes)
    return memoize(memo, memo_key, res, prefix)

  # Start with 1, assuming
  output = 0
  cur_size = sizes[0]
  # import pdb; pdb.set_trace()
  for i in range(len(pattern)):
    if len(pattern) < cur_size:
      # Out of space. Invalid arrangement
      return memoize(memo, memo_key, 0, prefix)
    if i > 0 and pattern[i-1] == "#":
      # Anything beyond this would be invalid because the previous character (a #) would
      # either cause the current size to be +1 (if adjacent) or it would mean there
      # was a block of #'s not accounted for in the sizes list
      break

    if i+cur_size < len(pattern) and pattern[i+cur_size] == "#":
      # Invalid arrangement. Character after this size block would increase the block
      # by 1.
      # Can continue though, because it'll get covered/included in the size block next.
      continue

    if i+cur_size < len(pattern):
      output += count_matches(memo, pattern[i+cur_size+1:], sizes[1:], depth+1, prefix + ("."*i + "#"*cur_size)+".")
    elif i+cur_size == len(pattern) and len(sizes) == 1:
      # End of pattern. Arrangement found
      # print(f"\t\t\t\t\t\t\tsolution: {prefix}")
      output += 1

  return memoize(memo, memo_key, output, prefix)


def get_pattern_runs(pattern_group: str) -> List[Tuple[str, int]]:
  # a "run" is a contiguous segment of the pattern that is all ? or all # (all the same)
  if not pattern_group:
    return []
  runs = []
  cur_type = '#'
  cur_type_count = 0
  for c in pattern_group:
    # print(runs)
    if c == cur_type:
      cur_type_count += 1
    else:
      runs.append((cur_type, cur_type_count))
      cur_type_count = 1
      cur_type = c

  runs.append((cur_type, cur_type_count))
  if runs[-1][0] == '?' or len(runs) == 1:
    runs.append(('#', 0))
  # print(runs)
  return runs


def solve_pattern_group(memo: dict, pattern_group: str, sizes: List[int]) -> int:
  """pattern_group has no '.' values, only '#' and '?' """
  # a "run" is a contiguous segment of the pattern that is all ? or all # (all the same)
  runs = get_pattern_runs(pattern_group)
  for a_idx, a in enumerate(runs[:-1]):
    for b_idx, b in enumerate(runs[1:]):
      solve_questionmark_section()


def solve_pattern_groups(group_memo, memo, pattern_groups, sizes, depth: int):
  """Each pattern group is separated by '.' the sizes can be distributed among them
  atomically."""
  memo_key = (tuple(pattern_groups), tuple(sizes))
  if memo_key in group_memo:
    # print(f"{' '*depth}Found group memo: {group_memo[memo_key]}")
    return group_memo[memo_key]

  if not pattern_groups or not sizes:
    if not sizes and all(["#" not in g for g in pattern_groups]):
      # print(f"{' '*depth}pattern_groups={pattern_groups}, sizes={sizes} RETURN 1")
      group_memo[memo_key] = 1
      return 1
    # print(f"{' '*depth}pattern_groups={pattern_groups}, sizes={sizes} RETURN 0")
    group_memo[memo_key] = 0
    return 0

  if len(pattern_groups[0]) < sizes[0] and "#" not in pattern_groups[0]:
    output = solve_pattern_groups(group_memo, memo, pattern_groups[1:], sizes, depth+1)
    # print(f"{' '*depth}pattern_groups={pattern_groups}, sizes={sizes} RETURN {output}")
    group_memo[memo_key] = output
    return output

  found_matches = False
  output = 0
  for i in reversed(list(range(len(sizes)))):
  # for i in range(len(sizes)):
    # if len(pattern_groups[0]) < sum(sizes[:i+1]):
      # import pdb; pdb.set_trace()
      # break

    # import pdb; pdb.set_trace()
    if sum(sizes[:i+1]) > (len(pattern_groups[0]) - (len(sizes[:i+1])-1)):
      # print(f"**** breaking early because pattern too short {pattern_groups[0]} {sizes[:i+1]}")
      continue
    # if depth == 1:
      # print("")
    # print(f"{' '*depth}Counting {pattern_groups[0]} {sizes[:i+1]}")
    if all(c == "?" for c in pattern_groups[0]):
      # print(f"{' '*depth}Short circuiting for ?-only group")
      # group_count = solve_questionmark_section(len(pattern_groups[0]), sizes[:i+1])
      group_count = count_matches(memo, pattern_groups[0], sizes[:i+1], 0, "")
    else:
      group_count = count_matches(memo, pattern_groups[0], sizes[:i+1], 0, "")
    # group_count = count_matches(memo, pattern_groups[0], sizes[:i+1])
    remaining_count = solve_pattern_groups(group_memo, memo, pattern_groups[1:], sizes[i+1:], depth+1)
    # print(f"{' '*depth}i={i} group_count={group_count} remaining_count={remaining_count} (adding to output:{group_count * remaining_count})")
    output += (group_count * remaining_count)

    if group_count or remaining_count:
      found_matches = True
    else:
      if found_matches:
        break

  if "#" not in pattern_groups[0]:
    # import pdb; pdb.set_trace()
    output += solve_pattern_groups(group_memo, memo, pattern_groups[1:], sizes, depth+1)

  # print(f"{' '*depth}pattern_groups={pattern_groups}, sizes={sizes} RETURN output={output}")
  group_memo[memo_key] = output
  # print(f"{' '*(depth-1)}Returning group result {output}")
  return output

def solve(input_str: str, multiplier: int):
  # print("")

  output = 0
  total_lines = len(input_str.splitlines())
  for lineno, line in enumerate(input_str.splitlines()):
    print(f"Line {lineno}/{total_lines} ({100.0*lineno/total_lines:2f}%): {line}")
    orig_pattern, sizes_str = line.split()
    # Simplify by merging any contiguous series of .'s into a single .
    # e.g. ##.....## becomes ##.##
    pattern = re.sub(r'\.+', '.', orig_pattern)
    pattern = "?".join([pattern]*multiplier)
    pattern_groups = [x for x in pattern.split(".") if x]
    sizes = [int(x) for x in sizes_str.split(",")]*multiplier
    group_memo = dict()
    memo = dict()
    # import pdb; pdb.set_trace()
    # print(f"{lineno}:\t{orig_pattern}\t{sizes}")
    count = solve_pattern_groups(group_memo, memo, pattern_groups, sizes, 0)
    print(f"count={count}")
    output += count
  return output


def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str, 5)
  # print(result)

if __name__ == "__main__":
  main()
