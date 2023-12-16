import pytest
import textwrap

from main2 import solve

def test_sample():
  sample_input = textwrap.dedent(r"""
    .|...\....
    |.-.\.....
    .....|-...
    ........|.
    ..........
    .........\
    ..../.\\..
    .-.-/..|..
    .|....-|.\
    ..//.|....
    """).strip()

  assert solve(sample_input) == 51
