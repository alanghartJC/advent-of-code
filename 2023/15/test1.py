import pytest
import textwrap

from main1 import solve

def test_sample():
  sample_input = textwrap.dedent("""
    HASH
    """).strip()

  assert solve(sample_input) == 52

def test_sample2():
  sample_input = textwrap.dedent("""
    rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
    """).strip()

  assert solve(sample_input) == 1320
