import pytest
import textwrap

from main2 import solve, solve_questionmark_section

def test_sample1():
  sample_input = textwrap.dedent("""
    ???.### 1,1,3
    """).strip()

  assert solve(sample_input) == 1

def test_sample2():
  sample_input = textwrap.dedent("""
    .??..??...?##. 1,1,3
    """).strip()

  assert solve(sample_input) == 16384

def test_sample3():
  sample_input = textwrap.dedent("""
    ?###???????? 3,2,1
    """).strip()

  assert solve(sample_input) == 506250

def test_sample4():
  sample_input = textwrap.dedent("""
    ???.### 1,1,3
    .??..??...?##. 1,1,3
    ?#?#?#?#?#?#?#? 1,3,1,6
    ????.#...#... 4,1,1
    ????.######..#####. 1,6,5
    ?###???????? 3,2,1
    """).strip()

  assert solve(sample_input) == 525152

def test_mult1_1():
  sample_input = textwrap.dedent("""
    ?.#???#?.?? 2,1,1
    """).strip()

  assert solve(sample_input) == 2

def test_mult1_2():
  sample_input = textwrap.dedent("""
    ?...#...##. 1,2
    """).strip()

  assert solve(sample_input) == 1

def test_mult1_3():
  sample_input = textwrap.dedent("""
    ?.?.?.?#???? 1,1,6
    """).strip()

  assert solve(sample_input) == 3

def test_component_1():
  assert solve_questionmark_section(q_count=7, sizes=[1,1,2]) == 2

def test_component_2():
  assert solve_questionmark_section(q_count=11, sizes=[1,2,3]) == 4
  assert solve_questionmark_section(q_count=11, sizes=[3,2,1]) == 4

def test_component_3():
  assert solve_questionmark_section(q_count=11, sizes=[2,3]) == 1
