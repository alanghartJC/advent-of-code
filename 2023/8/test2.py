import pytest
import textwrap

from main2 import solve

def test_sample1():
  sample_input = textwrap.dedent("""
    LR

    11A = (11B, XXX)
    11B = (XXX, 11Z)
    11Z = (11B, XXX)
    22A = (22B, XXX)
    22B = (22C, 22C)
    22C = (22Z, 22Z)
    22Z = (22B, 22B)
    XXX = (XXX, XXX)
    """).strip()

  assert solve(sample_input) == 6

def test_sample2():
  sample_input = textwrap.dedent("""
    LR

    11A = (11B, XXX)
    11B = (XXX, 11Z)
    11Z = (11B, XXX)
    22A = (22B, XXX)
    22B = (22R, 22R)
    22R = (22C, 22C)
    22C = (22Z, 22Z)
    22Z = (22B, 22B)
    XXX = (XXX, XXX)
    """).strip()

  assert solve(sample_input) == 6

def test_sample3():
  sample_input = textwrap.dedent("""
    LR

    11A = (11B, XXX)
    11B = (XXX, 11Z)
    11Z = (11B, XXX)
    22A = (22B, XXX)
    22B = (22R, 22R)
    22R = (22S, 22S)
    22S = (22C, 22C)
    22C = (22Z, 22Z)
    22Z = (22B, 22B)
    XXX = (XXX, XXX)
    """).strip()

  assert solve(sample_input) == 6
