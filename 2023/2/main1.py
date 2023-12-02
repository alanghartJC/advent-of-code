from typing import Tuple
import re

MAXES = {
  "red": 12,
  "green": 13,
  "blue": 14
}

game_re = re.compile(r'Game ([0-9]+): (.*) *')

def solve_line(line: str) -> Tuple[bool, int]:
  match = game_re.search(line).groups()
  game_number = int(match[0])
  game_results = match[1]

  for game in game_results.split(';'):
    for (count, color) in [sample.split() for sample in game.split(", ")]:
      if int(count) > MAXES[color]:
        return False, game_number

  return True, game_number

def solve(inputstr: str) -> int:
  output = 0
  for line in inputstr.splitlines():
    possible, game_number = solve_line(line)
    if possible:
      output += game_number
  return output

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
