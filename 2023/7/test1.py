import pytest
import textwrap

from main1 import solve

def test_sample():
  sample_input = textwrap.dedent("""
    32T3K 765
    T55J5 684
    KK677 28
    KTJJT 220
    QQQJA 483
    """).strip()

  assert solve(sample_input) == 6440
