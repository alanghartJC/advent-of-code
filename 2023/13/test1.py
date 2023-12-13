import pytest
import textwrap

from main1 import solve

def test_sample1():
  sample_input = textwrap.dedent("""
    #.##..##.
    ..#.##.#.
    ##......#
    ##......#
    ..#.##.#.
    ..##..##.
    #.#.##.#.
    """).strip()

  assert solve(sample_input) == 5

def test_sample2():
  sample_input = textwrap.dedent("""
    #...##..#
    #....#..#
    ..##..###
    #####.##.
    #####.##.
    ..##..###
    #....#..#
    """).strip()

  assert solve(sample_input) == 400

def test_sample3():
  sample_input = textwrap.dedent("""
    #.##..##.
    ..#.##.#.
    ##......#
    ##......#
    ..#.##.#.
    ..##..##.
    #.#.##.#.

    #...##..#
    #....#..#
    ..##..###
    #####.##.
    #####.##.
    ..##..###
    #....#..#
    """).strip()

  assert solve(sample_input) == 405

# def test_sample4():
#   sample_input = textwrap.dedent("""
#     ########.#.#..#
#     ##.#..##..####.
#     #####..#.......
#     ####.##..#.####
#     #..#.##.###.#..
#     .....#.#.#.####
#     #####....#...#.
#     #####.#.......#
#     .##...#..#.#...
#     .##...#..#.#...
#     #####.#.......#
#     """).strip()

#   assert solve(sample_input) == 405