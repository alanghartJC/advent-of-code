import pytest
import textwrap

from main1 import solve

def test_sample():
  sample_input = textwrap.dedent("""
    Time:      7  15   30
    Distance:  9  40  200
    """).strip()

  assert solve(sample_input) == 288
