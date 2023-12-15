from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Lens:
  orig_str: str
  name: str
  is_add: bool
  focal: int
  hashnum: str
  next: "Lens" = None
  prev: "Lens" = None

@dataclass
class Bucket:
  id: int
  names: Dict[str, Lens] = field(default_factory=dict)
  first: Lens = None
  last: Lens = None

def genhash(s: str) -> int:
  cur = 0
  for c in s:
    cur += ord(c)
    cur *= 17
    cur %= 256
  return cur

def parse_step(s: str) -> Lens:
  focal = None
  if s[-1] == "-":
    is_add = False
    name = s[:-1]
  else:
    is_add = True
    name, focal = s.split("=")
    focal = int(focal)
  return Lens(s, name, is_add, focal, hashnum=genhash(name))


def solve(input_str: str):
  steps: List[Lens] = []
  # import pdb; pdb.set_trace()
  for line in input_str.splitlines():
    steps.extend([parse_step(x) for x in line.split(',')])

  map: List[Bucket] = [Bucket(x) for x in range(256)]

  for s in steps:
    # import pdb; pdb.set_trace()
    b = map[s.hashnum]
    if s.is_add:
      if s.name in b.names:
        existing = b.names[s.name]
        prev = existing.prev
        next = existing.next
        if b.first == existing:
          # b.first = existing.next
          b.first = s
        if b.last == existing:
          b.last = s
        existing.prev = None
        existing.next = None
        if prev:
          prev.next = s
        if next:
          next.prev = s
        s.next = next
        s.prev = prev
      else:
        if b.first:
          s.next = b.first
          b.first.prev = s
        b.first = s
        if b.last is None:
          b.last = s
      b.names[s.name] = s
    else:
      # Removing
      if s.name in b.names:
        existing = b.names[s.name]
        prev = existing.prev
        next = existing.next
        existing.prev = None
        existing.next = None
        if prev:
          prev.next = next
        if next:
          next.prev = prev
        if b.first == existing:
          b.first = next
        if b.last == existing:
          b.last = prev
        del b.names[s.name]

  output = 0

  for b in map:
    if b.first:
      print(f"{b.id}: ", end="")
      cur = b.last
      slot_num = 1
      while cur:
        output += (1 + b.id) * slot_num * cur.focal
        print(f"{cur.orig_str},", end="")
        cur = cur.prev
        slot_num += 1
      print("")
  return output

def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
