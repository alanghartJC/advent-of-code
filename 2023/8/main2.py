import math

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

  cursors = []
  for node in adj_dict.keys():
    if node[-1] == 'A':
      cursors.append(node)

  print("")

  path_lens = []
  for cursor in cursors:
    if cursor[-1] != 'A':
      continue
    cur = cursor
    count = 0
    notfound = True
    while notfound:
      for instr in instructions:
        if cur[-1] == 'Z':
          path_lens.append(count)
          notfound = False
          break
        cur = adj_dict[cur][instr]
        count += 1

  lcm = math.lcm(*path_lens)
  return lcm

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
