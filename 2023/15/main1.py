def genhash(s: str) -> int:
  cur = 0
  for c in s:
    cur += ord(c)
    cur *= 17
    cur %= 256
  return cur

def solve(input_str: str):
  steps = []
  # import pdb; pdb.set_trace()
  for line in input_str.splitlines():
    steps.extend([x for x in line.split(',')])

  output = 0
  for step in steps:
    output += genhash(step)

  return output

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
