def solve(input_str: str):
  lines = input_str.splitlines()
  instructions = lines[0]
  adj_list = []
  adj_dict = {}

  for line in lines[2:]:
    node = line[0:3]
    left = line[7:10]
    right = line[12:15]
    adj_list.append((node, left, right))
    adj_dict[node] = {'L': left, 'R': right}

  cur = 'AAA'
  count = 0
  while True:
    import pdb
    for instr in instructions:
      cur = adj_dict[cur][instr]
      count += 1
      if cur == 'ZZZ':
        return count

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
