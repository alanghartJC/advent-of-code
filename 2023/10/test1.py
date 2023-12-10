import pytest
import textwrap

from main1 import solve

def test_sample1():
  sample_input = textwrap.dedent("""
    -L|F7
    7S-7|
    L|7||
    -L-J|
    L|-JF
    """).strip()

  assert solve(sample_input) == 4

def test_sample2():
  sample_input = textwrap.dedent("""
    ..F7.
    .FJ|.
    SJ.L7
    |F--J
    LJ...
    """).strip()

  assert solve(sample_input) == 8
