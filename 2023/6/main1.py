from bisect import bisect_left

def solve(input_str: str):
  times = [int(x) for x in input_str.splitlines()[0].split(':')[1].split()]
  dists = [int(x) for x in input_str.splitlines()[1].split(':')[1].split()]

  races = zip(times, dists)

  output = 1
  for max_time, win_dist in races:
    ways_to_win = 0

    for charge_time in range(1, max_time-1):
      travel_time = max_time - charge_time
      speed = charge_time
      if (travel_time * speed) > win_dist:
        print(f'Win: hold for {charge_time}, travel_time={travel_time}, speed={speed}, dist={travel_time * speed} > {win_dist}')
        ways_to_win += 1
      elif ways_to_win:
        print(f'Losing again, breaking')
        break

    print(f'Multiplying {output} by {ways_to_win} (ways) = {output * ways_to_win}')
    output *= ways_to_win

  return output

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
