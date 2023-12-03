import pytest
import textwrap

from main1 import solve

def test_sample():
  sample_input = textwrap.dedent("""
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
    """).strip()

  assert solve(sample_input) == 4361
