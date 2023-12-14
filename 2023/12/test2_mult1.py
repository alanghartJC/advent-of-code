import pytest
import textwrap

from main2 import solve, solve_questionmark_section, get_pattern_runs

def test_sample1():
  sample_input = textwrap.dedent("""
    ???.### 1,1,3
    """).strip()

  assert solve(sample_input, 1) == 1

def test_sample2():
  sample_input = textwrap.dedent("""
    .??..??...?##. 1,1,3
    """).strip()

  assert solve(sample_input, 1) == 4

def test_sample3():
  sample_input = textwrap.dedent("""
    ?#?#?#?#?#?#?#? 1,3,1,6
    """).strip()

  assert solve(sample_input, 1) == 1

def test_sample4():
  sample_input = textwrap.dedent("""
    ????.#...#... 4,1,1
    """).strip()

  assert solve(sample_input, 1) == 1

def test_sample5():
  sample_input = textwrap.dedent("""
    ????.######..#####. 1,6,5
    """).strip()

  assert solve(sample_input, 1) == 4

def test_sample6():
  sample_input = textwrap.dedent("""
    ?###???????? 3,2,1
    """).strip()

  assert solve(sample_input, 1) == 10
