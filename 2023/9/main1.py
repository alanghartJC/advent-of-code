from typing import List

def print_rows(rows: List[List[str]]):
  for i, row in enumerate(rows):
    line = "  "*i
    for n, col in enumerate(row):
      line += str(col)
      if n != len(row)-1:
        line += " "
    print(line)


def solve_line(input_str: str) -> int:
  rows = [[int(x) for x in input_str.split()]]

  while not all(x == 0 for x in rows[-1]):
    diffs = []
    for i in range(len(rows[-1])-1):
      diffs.append(rows[-1][i+1] - rows[-1][i])

    rows.append(diffs)

  print_rows(rows)

  diff = 0
  for row in reversed(rows):
    last_val = 0
    if len(row):
      last_val = row[-1]
    row.append(last_val + diff)
    diff = row[-1]

  print_rows(rows)
  return rows[0][-1]

def solve(input_str: str) -> int:
  print("")
  return sum(solve_line(line) for line in input_str.splitlines())

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
