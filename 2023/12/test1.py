import pytest
import textwrap

from main1 import solve

def test_sample1():
  sample_input = textwrap.dedent("""
    ???.### 1,1,3
    """).strip()

  assert solve(sample_input) == 1

def test_sample2():
  sample_input = textwrap.dedent("""
    .??..??...?##. 1,1,3
    """).strip()

  assert solve(sample_input) == 4

def test_sample3():
  sample_input = textwrap.dedent("""
    ?###???????? 3,2,1
    """).strip()

  assert solve(sample_input) == 10

def test_sample4():
  sample_input = textwrap.dedent("""
    ???.### 1,1,3
    .??..??...?##. 1,1,3
    ?#?#?#?#?#?#?#? 1,3,1,6
    ????.#...#... 4,1,1
    ????.######..#####. 1,6,5
    ?###???????? 3,2,1
    """).strip()

  assert solve(sample_input) == 21
