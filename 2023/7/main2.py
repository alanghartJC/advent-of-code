from collections import deque, defaultdict
from pprint import pprint
from typing import Tuple

letter_to_num = {
  "T": 10,
  "J": 0,
  "Q": 12,
  "K": 13,
  "A": 14
}
def hand_to_sortable(hand: str) -> Tuple[int]:
  vals = []
  for c in hand:
    val = letter_to_num.get(c)
    if val is not None:
      vals.append(val)
    else:
      vals.append(int(c))
  return tuple(vals)

def handsort(hand: str) -> str:
  vals = []
  for c in hand:
    val = letter_to_num.get(c)
    if val is not None:
      vals.append((val, c))
    else:
      vals.append((int(c), c))
  return ''.join(c for _, c in sorted(vals, reverse=True))

HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_KIND = 3
FULL_HOUSE = 4
FOUR_KIND = 5
FIVE_KIND = 6

def hand_type(hand: str) -> int:
  hand = [x for x in sorted(hand) if x != 'J']

  jcount = 5 - len(hand)

  if jcount == 5:
    return FIVE_KIND

  matches = defaultdict(int)
  for c in hand:
    matches[c] += 1

  count = sorted(matches.values(), reverse=True)[0]
  if count == 5:
    return FIVE_KIND
  if count == 4:
    if jcount:
      return FIVE_KIND
    return FOUR_KIND
  if count == 3:
    if len(matches) == 2:
      if jcount:
        return FOUR_KIND
      return FULL_HOUSE
    if len(matches) == 3:
      return THREE_KIND
    return FIVE_KIND
  if count == 2:
    if len(matches) == 3:
      if jcount:
        return THREE_KIND
      return TWO_PAIR
    if len(matches) == 2:
      if jcount == 2:
        return FOUR_KIND
      if jcount == 1:
        return FULL_HOUSE
      return TWO_PAIR
    if jcount:
      return FIVE_KIND
    return ONE_PAIR
  if count == 1:
    if len(matches) == 5:
      return HIGH_CARD
    if len(matches) == 4:
      return ONE_PAIR
    if len(matches) == 3:
      return THREE_KIND
    if len(matches) == 2:
      return FOUR_KIND
    if len(matches) == 1:
      return FIVE_KIND

def solve(input_str: str):
  bets = [line.split() for line in input_str.splitlines()]

  by_type = [[] for _ in range(7)]


  for (hand, wager) in bets:
    by_type[hand_type(hand)].append((hand_to_sortable(hand), int(wager), handsort(hand)))

  ordered_hands = []

  for type, bets in enumerate(by_type):
    by_type[type] = sorted(bets)

  for bets in by_type:
    ordered_hands.extend([(wager, hand) for _, wager, hand in sorted(bets)])

  pprint(by_type)
  return sum(wager * (i + 1) for (i, (wager, _)) in enumerate(ordered_hands))

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
