import re
import dataclasses
from typing import List

@dataclasses.dataclass
class Card:
  winner_count: int = 0
  card_subtotal: int = 0

def solve_card_count(cards: List[Card], index: int):
  card = cards[index]
  if card.card_subtotal == 0:
    for x in range(card.winner_count):
      card.card_subtotal += solve_card_count(cards, index + x + 1)

    card.card_subtotal += 1
  return card.card_subtotal

def solve(input_str: str):
  output = 0
  cards = []
  card_re = re.compile(r'^Card *[0-9]+: *([^\|]+) *\| *(.*)')
  for line in input_str.splitlines():
    match = card_re.search(line)
    winning_nums_str = match.groups()[0]
    nums_str = match.groups()[1]

    winning_nums = {int(x) for x in winning_nums_str.split()}
    nums = [int(x) for x in nums_str.split()]

    winner_count = len([x for x in nums if x in winning_nums])
    cards.append(Card(winner_count=winner_count))

  for x, card in enumerate(cards):
    output += solve_card_count(cards, x)

  return output



def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
