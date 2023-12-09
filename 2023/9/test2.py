import pytest
import textwrap

from main2 import solve_line

def test_sample():
  sample_input = textwrap.dedent("""
    0   3   6   9  12  15
    1   3   6  10  15  21
    10  13  16  21  30  45
    """).strip()

  assert solve(sample_input) == 114

def test_sample():
  sample_input = textwrap.dedent("""
    0   3   6   9  12  15
    """).strip()

  assert solve_line(sample_input) == -3

def test_sample2():
  sample_input = textwrap.dedent("""
    1   3   6  10  15  21
    """).strip()

  assert solve_line(sample_input) == 0

def test_sample3():
  sample_input = textwrap.dedent("""
    10  13  16  21  30  45
    """).strip()

  assert solve_line(sample_input) == 5
