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

def solve_questionmark_section(q_count: int, sizes: List[int]) -> int:
  """Returns number of ways the given sizes can be distributed in the section
  of question marks. ALL sizes must be accounted for.

  This assumes that the first and last ? will be #."""
  # Example input:  ????????????? 1,2,3
  # The only thing that varies is the spacing *between* each segment of #'s.
  # To simplify, each segment of #'s can be shrunk to a single #
  # (here, remove 3 ?'s)
  # ?????????? 1,1,1
  # Now it is simply 2 parameters: number of ?'s and number of sizes
  import pdb; pdb.set_trace()
  size_count = len(sizes)
  if size_count == 2:

    return 1

  q_count -= sum([x-1 for x in sizes])
  # buckets are segments where dots can go
  buckets = size_count - 1
  # these are *moveable* dots. does not include one dot per bucket that cannot move
  # (otherwise the two adjacent # segments would be combined into one)
  dots = q_count - (2*size_count - 1)
  # It is a combinatorial problem: how many different ways can the moveable dots be distributed
  # among the buckets?
  combos = math.factorial(dots + buckets - 1) // (math.factorial(dots) * math.factorial(buckets - 1))
  return combos


def count_matches(memo: Dict[Tuple[str, Tuple[int]], int], pattern: str, sizes: List[int], cur_group_type: str = None, cur_group_len: int = 0, space_required: bool = False, running_pattern: str = "") -> int:
  """Recursively search for matching arrangements and return how many"""
  # print(f"pattern={running_pattern}-{pattern}\tsizes={sizes}\tcur_group_type={cur_group_type}\tcur_group_len={cur_group_len}\tspace_required={space_required}")
  # import pdb; pdb.set_trace()
  memo_key = (pattern, cur_group_type, cur_group_len, tuple(sizes))
  memo_res = memo.get(memo_key)
  if memo_res:
    print(f"Found memo for {memo_key}: {memo_res}")
    return memo_res

  if not pattern:
    if not sizes:
      # Match found
      # print(f"*****************Match found ({running_pattern})")
      res = 1
      memo[memo_key] = res
      return res
    # Invalid arrangement
    # print("Invalid")
    res = 0
    memo[memo_key] = res
    return res

  if not sizes:
    if "#" not in pattern:
      res = 1
      memo[memo_key] = res
      return res

  # pref_len = prefix_len(pattern)
  pref_type = pattern[0]

  if pref_type == ".":
    if cur_group_type == "#":
        res = 0
        memo[memo_key] = res
        return res
    pref_len = prefix_len(pattern)
    if sizes:
      pref_len = min(prefix_len(pattern), sizes[0])
    res = count_matches(memo, pattern[pref_len:], sizes, cur_group_type=pref_type, cur_group_len=cur_group_len+1, running_pattern=running_pattern+pattern[:pref_len])
    memo[memo_key] = res
    return res

  elif pref_type == "#":
    if not sizes:
      # print(f"Invalid (# found with no remaining size)")
      res = 0
      memo[memo_key] = res
      return res
    if space_required:
      # Invalid arrangement; ### groups not separated by .
      # print("Invalid (space required)")
      res = 0
      memo[memo_key] = res
      return res
    pref_len = prefix_len(pattern)
    # import pdb; pdb.set_trace()
    if cur_group_type != pref_type:
      # Starting new group
      cur_group_len = 0

    if pref_len + cur_group_len > sizes[0]:
      # Invalid arrangement; # group size exceeds expected size (without a ? or . to separate from next group)
      # import pdb; pdb.set_trace()
      # print("Invalid ()")
      res = 0
      memo[memo_key] = res
      return res
    elif pref_len + cur_group_len == sizes[0]:
      # Group found/matched, remove its size from the sizes list and move on to next group
      res = count_matches(memo, pattern[pref_len:], sizes[1:], space_required=True, running_pattern=running_pattern+pattern[:pref_len])
      memo[memo_key] = res
      return res
    else:
      # Starting new group
      res = count_matches(memo, pattern[pref_len:], sizes, cur_group_type=pref_type, cur_group_len=pref_len + cur_group_len, running_pattern=running_pattern+pattern[:pref_len])
      memo[memo_key] = res
      return res
  elif pref_type == "?":
    next_pattern = pattern[:]
    if space_required:
      next_pattern = "." + pattern[1:]
      res = count_matches(memo, next_pattern, sizes, cur_group_type=".", cur_group_len=1, running_pattern=running_pattern)
      memo[memo_key] = res
      return res
    else:
      output = 0
      next_pattern = "." + pattern[1:]
      # print(f"trying . ({next_pattern})")
      output += count_matches(memo, next_pattern, sizes, cur_group_type=cur_group_type, cur_group_len=cur_group_len, running_pattern=running_pattern)
      next_pattern = "#" + pattern[1:]
      # print(f"trying # ({next_pattern})")
      output += count_matches(memo, next_pattern, sizes, cur_group_type=cur_group_type, cur_group_len=cur_group_len, running_pattern=running_pattern)
      return output

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


def solve_pattern_groups(group_memo, memo, pattern_groups, sizes):
  """Each pattern group is separated by '.' the sizes can be distributed among them
  atomically."""
  memo_key = (tuple(pattern_groups), tuple(sizes))
  if memo_key in group_memo:
    print(f"Found group memo: {group_memo[memo_key]}")
    return group_memo[memo_key]

  if not pattern_groups or not sizes:
    if not sizes and all(["#" not in g for g in pattern_groups]):
      # print(f"pattern_groups={pattern_groups}, sizes={sizes} RETURN 1")
      group_memo[memo_key] = 1
      return 1
    # print(f"pattern_groups={pattern_groups}, sizes={sizes} RETURN 0")
    group_memo[memo_key] = 0
    return 0
  if len(pattern_groups[0]) < sizes[0] and "#" not in pattern_groups[0]:
    output = solve_pattern_groups(group_memo, memo, pattern_groups[1:], sizes)
    # print(f"pattern_groups={pattern_groups}, sizes={sizes} RETURN {output}")
    group_memo[memo_key] = output
    return output


  output = 0
  for i in range(len(sizes)):
    if len(pattern_groups[0]) < sum(sizes[:i+1]):
      break

    group_count = count_matches(memo, pattern_groups[0], sizes[:i+1])
    remaining_count = solve_pattern_groups(group_memo, memo, pattern_groups[1:], sizes[i+1:])
    # print(f"i={i} group_count={group_count} remaining_count={remaining_count}")
    output += group_count * remaining_count

  if "#" not in pattern_groups[0]:
    # import pdb; pdb.set_trace()
    output += solve_pattern_groups(group_memo, memo, pattern_groups[1:], sizes)

  # print(f"pattern_groups={pattern_groups}, sizes={sizes} RETURN output={output}")
  group_memo[memo_key] = output
  return output

def solve(input_str: str):
  print("")

  MULTIPLIER = 5
  output = 0
  total_lines = len(input_str.splitlines())
  for lineno, line in enumerate(input_str.splitlines()):
    # print(f"Line {lineno}/{total_lines} ({100.0*lineno/total_lines:2f}): {line}")
    orig_pattern, sizes_str = line.split()
    pattern = re.sub(r'\.+', '.', orig_pattern)
    pattern = "?".join([pattern]*MULTIPLIER)
    pattern_groups = [x for x in pattern.split(".") if x]
    sizes = [int(x) for x in sizes_str.split(",")]*MULTIPLIER
    group_memo = dict()
    memo = dict()
    # import pdb; pdb.set_trace()
    count = solve_pattern_groups(group_memo, memo, pattern_groups, sizes)
    print(f"{lineno}:\tcount={count}\t{orig_pattern}\t{sizes}")
    output += count
  return output


def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
