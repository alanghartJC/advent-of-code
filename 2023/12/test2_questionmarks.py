import pytest
import textwrap

from main2 import solve, solve_questionmark_group

def test_sample_0():
  assert solve_questionmark_group(3, [1]) == 3

def test_sample_1():
  assert solve_questionmark_group(3, [1,1]) == 1

def test_sample_2():
  assert solve_questionmark_group(4, [1]) == 4

def test_sample_3():
  assert solve_questionmark_group(4, [1,1]) == 3

def test_sample_4():
  assert solve_questionmark_group(5, [1,1]) == 6

def test_sample_5():
  assert solve_questionmark_group(7, [1,1,1]) == 10