from collections import deque, defaultdict
from pprint import pprint
from typing import Tuple

letter_to_num = {
  "T": 10,
  "J": 11,
  "Q": 12,
  "K": 13,
  "A": 14
}
def hand_to_sortable(hand: str) -> Tuple[int]:
  vals = []
  for c in hand:
    val = letter_to_num.get(c)
    if val:
      vals.append(val)
    else:
      vals.append(int(c))
  # import pdb; pdb.set_trace()
  return tuple(vals)
  # return tuple(sorted(vals, reverse=True))

def handsort(hand: str) -> str:
  vals = []
  for c in hand:
    val = letter_to_num.get(c)
    if val:
      vals.append((val, c))
    else:
      vals.append((int(c), c))
  # import pdb; pdb.set_trace()
  return ''.join(c for _, c in sorted(vals, reverse=True))

HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_KIND = 3
FULL_HOUSE = 4
FOUR_KIND = 5
FIVE_KIND = 6

def hand_type(hand: str) -> int:
  hand = sorted(hand)
  matches = defaultdict(int)
  for c in hand:
    matches[c] += 1

  for val, count in sorted(matches.items(), key=lambda x: x[1], reverse=True):
    if count == 5:
      return FIVE_KIND
    if count == 4:
      return FOUR_KIND
    if count == 3:
      if len(matches) == 2:
        return FULL_HOUSE
      return THREE_KIND
    if count == 2:
      if len(matches) == 3:
        return TWO_PAIR
      return ONE_PAIR
    return HIGH_CARD

def solve(input_str: str):
  bets = [line.split() for line in input_str.splitlines()]

  by_type = [[] for _ in range(7)]


  for (hand, wager) in bets:
    # by_type[hand_type(hand)].append((hand_to_sortable(hand), handsort(hand)))
    by_type[hand_type(hand)].append((hand_to_sortable(hand), int(wager)))

  ordered_hands = []

  for type, bets in enumerate(by_type):
    by_type[type] = sorted(bets)

  for bets in by_type:
    ordered_hands.extend([wager for _, wager in sorted(bets)])

  pprint(by_type)
  # import pdb; pdb.set_trace()
  return sum(wager * (i + 1) for (i, wager) in enumerate(ordered_hands))

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
