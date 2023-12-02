from typing import Tuple
from collections import defaultdict
import functools
import operator
import pprint
import re


MAXES = {
  "red": 12,
  "green": 13,
  "blue": 14
}

game_re = re.compile(r'Game ([0-9]+): (.*) *')

def solve_line(line: str) -> int:
  print(f"line:{line}")
  match = game_re.search(line).groups()
  game_number = int(match[0])
  game_results = match[1]

  highest = defaultdict(int)
  for sample_set in game_results.split(';'):
    for (count, color) in [sample.split() for sample in sample_set.split(", ")]:
      highest[color] = max(highest[color], int(count))

  game_power = functools.reduce(operator.mul, highest.values())
  print(f'highest:{pprint.pformat(highest)}')
  print(f"power = {game_power}")
  return game_power

def solve(inputstr: str) -> int:
  output = 0
  for line in inputstr.splitlines():
    output += solve_line(line)
  return output

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
