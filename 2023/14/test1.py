import pytest
import textwrap

from main1 import solve

def test_sample_1():
  sample_input = textwrap.dedent("""
    O....#....
    O.OO#....#
    .....##...
    OO.#O....O
    .O.....O#.
    O.#..O.#.#
    ..O..#O..O
    .......O..
    #....###..
    #OO..#....
    """).strip()

  assert solve(sample_input) == 136
