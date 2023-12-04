import re



def solve(input_str: str):
  output = 0
  card_re = re.compile(r'^Card *[0-9]+: *([^\|]+) *\| *(.*)')
  for line in input_str.splitlines():
    match = card_re.search(line)
    winning_nums_str = match.groups()[0]
    nums_str = match.groups()[1]

    winning_nums = {int(x) for x in winning_nums_str.split()}
    nums = [int(x) for x in nums_str.split()]

    winner_count = len([x for x in nums if x in winning_nums])
    print(f'{line}')
    print(f'Winners: {winner_count}')
    if winner_count:
      points = (2**(winner_count - 1))
      print(f'Points: {points}')
      output += points

  return int(output)



def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
