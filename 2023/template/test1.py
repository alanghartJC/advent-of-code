import pytest
import textwrap

from main1 import solve

def test_sample():
  sample_input = textwrap.dedent("""
    """).strip()

  assert solve(sample_input) == 2
