import pytest
import textwrap

from main2 import solve

def test_sample1():
  sample_input = textwrap.dedent("""
    """).strip()

  assert solve(sample_input) == 6
