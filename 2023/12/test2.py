import pytest
import textwrap

from main2 import solve, get_pattern_runs

def test_sample1():
  sample_input = textwrap.dedent("""
    ???.### 1,1,3
    """).strip()

  assert solve(sample_input, 5) == 1

def test_sample2():
  sample_input = textwrap.dedent("""
    .??..??...?##. 1,1,3
    """).strip()

  assert solve(sample_input, 5) == 16384

def test_sample3():
  sample_input = textwrap.dedent("""
    ?#?#?#?#?#?#?#? 1,3,1,6
    """).strip()

  assert solve(sample_input, 5) == 1

def test_sample4():
  sample_input = textwrap.dedent("""
    ????.#...#... 4,1,1
    """).strip()

  assert solve(sample_input, 5) == 16

def test_sample5():
  sample_input = textwrap.dedent("""
    ????.######..#####. 1,6,5
    """).strip()

  assert solve(sample_input, 5) == 2500

def test_sample6():
  sample_input = textwrap.dedent("""
    ?###???????? 3,2,1
    """).strip()

  assert solve(sample_input, 5) == 506250
