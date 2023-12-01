import os
import sys

digits = set(str(x) for x in range(10))

def solve(input_str: str):
  output = 0
  for line in input_str.splitlines():
    output += solve_line(line)
  return output

def solve_line(line: str):
  numstr = ""
  for ordered in [line, reversed(line)]:
    for c in ordered:
      if c in digits:
        numstr += c
        break
  return int(numstr or "0")


def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
