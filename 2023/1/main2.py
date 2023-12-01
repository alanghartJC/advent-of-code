import re

digits = set(str(x) for x in range(10))

digit_names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit_names_dict = {name:str(index+1) for index, name in enumerate(digit_names)}
digit_names_re = re.compile(f"({'|'.join(digit_names_dict.keys())})")
digit_names_dict_rev = {name[::-1]:index for name, index in digit_names_dict.items()}
digit_names_rev_re = re.compile(f"({'|'.join(digit_names_dict_rev.keys())})")

def solve(input_str: str):
  output = 0
  for line in input_str.splitlines():
    val = solve_line(line)
    print(f"{line} = {val}")
    output += val
  return output

def solve_line(line: str):
  replaced_line = digit_names_re.sub(lambda match: digit_names_dict[match.groups()[0]], line)
  replaced_line_rev = digit_names_rev_re.sub(lambda match: digit_names_dict_rev[match.groups()[0]], line[::-1])
  numstr = ""

  for ordered in [replaced_line, replaced_line_rev]:
    for c in ordered:
      if c in digits:
        numstr += c
        break
  return int(numstr)


def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
