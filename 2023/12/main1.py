from typing import List

def prefix_len(pattern: str) -> int:
  c = pattern[0]
  output = 0
  for x in pattern:
    if x == c:
      output += 1
    else:
      break
  return output

def count_matches(pattern: str, sizes: List[int], cur_group_type: str = None, cur_group_len: int = 0, space_required: bool = False, running_pattern: str = "") -> int:
  """Recursively search for matching arrangements and return how many"""
  # print(f"pattern={running_pattern}-{pattern}\tsizes={sizes}\tcur_group_type={cur_group_type}\tcur_group_len={cur_group_len}\tspace_required={space_required}")
  if not pattern:
    if not sizes:
      # Match found
      # print(f"*****************Match found ({running_pattern})")
      return 1
    # Invalid arrangement
    # print("Invalid")
    return 0

  # pref_len = prefix_len(pattern)
  pref_type = pattern[0]

  if pref_type == ".":
    if cur_group_type == "#":
      return 0
    pref_len = prefix_len(pattern)
    if sizes:
      pref_len = min(prefix_len(pattern), sizes[0])
    return count_matches(pattern[pref_len:], sizes, cur_group_type=pref_type, cur_group_len=cur_group_len+1, running_pattern=running_pattern+pattern[:pref_len])

  elif pref_type == "#":
    if not sizes:
      # print(f"Invalid (# found with no remaining size)")
      return 0
    if space_required:
      # Invalid arrangement; ### groups not separated by .
      # print("Invalid (space required)")
      return 0
    pref_len = prefix_len(pattern)
    # import pdb; pdb.set_trace()
    if cur_group_type != pref_type:
      # Starting new group
      cur_group_len = 0

    if pref_len + cur_group_len > sizes[0]:
      # Invalid arrangement; # group size exceeds expected size (without a ? or . to separate from next group)
      # import pdb; pdb.set_trace()
      # print("Invalid ()")
      return 0
    elif pref_len + cur_group_len == sizes[0]:
      # Group found/matched, remove its size from the sizes list and move on to next group
      return count_matches(pattern[pref_len:], sizes[1:], space_required=True, running_pattern=running_pattern+pattern[:pref_len])
    else:
      # Starting new group
      return count_matches(pattern[pref_len:], sizes, cur_group_type=pref_type, cur_group_len=pref_len + cur_group_len, running_pattern=running_pattern+pattern[:pref_len])
  elif pref_type == "?":
    next_pattern = pattern[:]
    if space_required:
      next_pattern = "." + pattern[1:]
      return count_matches(next_pattern, sizes, cur_group_type=".", cur_group_len=1, running_pattern=running_pattern)
    else:
      output = 0
      next_pattern = "." + pattern[1:]
      # print(f"trying . ({next_pattern})")
      output += count_matches(next_pattern, sizes, cur_group_type=cur_group_type, cur_group_len=cur_group_len, running_pattern=running_pattern)
      next_pattern = "#" + pattern[1:]
      # print(f"trying # ({next_pattern})")
      output += count_matches(next_pattern, sizes, cur_group_type=cur_group_type, cur_group_len=cur_group_len, running_pattern=running_pattern)
      return output




def solve(input_str: str):
  print("")

  output = 0
  for i, line in enumerate(input_str.splitlines()):
    pattern, sizes_str = line.split()
    sizes = [int(x) for x in sizes_str.split(",")]
    count = count_matches(pattern, sizes)
    print(f"""def test_sample_{i}():
  sample_input = textwrap.dedent("{line}").strip()

  assert solve(sample_input, 1) == {count}

  """)
    # print(f"{i}:\tcount={count}\t{pattern}\t{sizes}")
    output += count
  return output


def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
