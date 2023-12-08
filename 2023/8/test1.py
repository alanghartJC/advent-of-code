import pytest
import textwrap

from main1 import solve

def test_sample():
  sample_input = textwrap.dedent("""
    RL

    AAA = (BBB, CCC)
    BBB = (DDD, EEE)
    CCC = (ZZZ, GGG)
    DDD = (DDD, DDD)
    EEE = (EEE, EEE)
    GGG = (GGG, GGG)
    ZZZ = (ZZZ, ZZZ)
    """).strip()

  assert solve(sample_input) == 2

def test_sample2():
  sample_input = textwrap.dedent("""
    LLR

    AAA = (BBB, BBB)
    BBB = (AAA, ZZZ)
    ZZZ = (ZZZ, ZZZ)
    """).strip()

  assert solve(sample_input) == 6
