import pytest
import textwrap

from main2 import solve

def test_sample_0():
  sample_input = textwrap.dedent(".#??..#??.?. 3,1,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_1():
  sample_input = textwrap.dedent("???.##??#??????#???# 1,13,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_2():
  sample_input = textwrap.dedent(".??#.?#??#????#?? 2,4,1,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_3():
  sample_input = textwrap.dedent("???#??#.???#.?#??#?# 4,2,1,2,1,4").strip()

  assert solve(sample_input, 1) == 1


def test_sample_4():
  sample_input = textwrap.dedent("????#?##???#.??.? 2,2,6,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_5():
  sample_input = textwrap.dedent(".?????#???.###.##? 7,3,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_6():
  sample_input = textwrap.dedent(".###?..#??????#???? 4,8,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_7():
  sample_input = textwrap.dedent("??????????????? 1,1,1,2,1").strip()

  assert solve(sample_input, 1) == 252


def test_sample_8():
  sample_input = textwrap.dedent("???.????????#? 1,3,1,1").strip()

  assert solve(sample_input, 1) == 19


def test_sample_9():
  sample_input = textwrap.dedent("???.#..?#.?#?#??#?. 2,1,1,5,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_10():
  sample_input = textwrap.dedent(".?..??#.????. 1,3,1,2").strip()

  assert solve(sample_input, 1) == 1


def test_sample_11():
  sample_input = textwrap.dedent(".#?.??#?????##.# 1,2,1,3,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_12():
  sample_input = textwrap.dedent("?###????.#?? 5,1,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_13():
  sample_input = textwrap.dedent("?#??.????? 2,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_14():
  sample_input = textwrap.dedent("?.#????#?????#??#?? 1,6,1,4,1").strip()

  assert solve(sample_input, 1) == 5


def test_sample_15():
  sample_input = textwrap.dedent("#????????#?#?? 1,7,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_16():
  sample_input = textwrap.dedent("?#??.?????? 3,1,1").strip()

  assert solve(sample_input, 1) == 20


def test_sample_17():
  sample_input = textwrap.dedent("?..??#?###?? 1,6").strip()

  assert solve(sample_input, 1) == 3


def test_sample_18():
  sample_input = textwrap.dedent("???.?.??#??##?? 1,1,1,5,1").strip()

  assert solve(sample_input, 1) == 5


def test_sample_19():
  sample_input = textwrap.dedent("#???#.?????? 2,1,3,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_20():
  sample_input = textwrap.dedent("?###??.??.?#???..? 4,1,2,1,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_21():
  sample_input = textwrap.dedent("?.#???#?.?? 2,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_22():
  sample_input = textwrap.dedent("#??##????##??????#? 7,5,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_23():
  sample_input = textwrap.dedent("????#????????????# 1,6,1,1,2").strip()

  assert solve(sample_input, 1) == 31


def test_sample_24():
  sample_input = textwrap.dedent("#?.?.##???? 1,1,5").strip()

  assert solve(sample_input, 1) == 1


def test_sample_25():
  sample_input = textwrap.dedent(".?????.?#???????? 1,2,2,2,1").strip()

  assert solve(sample_input, 1) == 53


def test_sample_26():
  sample_input = textwrap.dedent("#??.???#?.????? 2,5,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_27():
  sample_input = textwrap.dedent("?????????.#???. 6,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_28():
  sample_input = textwrap.dedent("?????????? 1,1,4").strip()

  assert solve(sample_input, 1) == 10


def test_sample_29():
  sample_input = textwrap.dedent("?#??#??#?## 1,7").strip()

  assert solve(sample_input, 1) == 1


def test_sample_30():
  sample_input = textwrap.dedent("????#?##???#? 1,6,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_31():
  sample_input = textwrap.dedent("??#??#.???#?????? 1,1,1,7,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_32():
  sample_input = textwrap.dedent("?????##?.?#??. 1,2,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_33():
  sample_input = textwrap.dedent("???##????###????. 4,7").strip()

  assert solve(sample_input, 1) == 9


def test_sample_34():
  sample_input = textwrap.dedent("?.?.?.?#???? 1,1,6").strip()

  assert solve(sample_input, 1) == 3


def test_sample_35():
  sample_input = textwrap.dedent("???..??.????.###??. 2,2,2,5").strip()

  assert solve(sample_input, 1) == 6


def test_sample_36():
  sample_input = textwrap.dedent("????##??#????? 1,7,1,1").strip()

  assert solve(sample_input, 1) == 5


def test_sample_37():
  sample_input = textwrap.dedent("???..????#??? 2,6").strip()

  assert solve(sample_input, 1) == 6


def test_sample_38():
  sample_input = textwrap.dedent(".??.????????. 1,2").strip()

  assert solve(sample_input, 1) == 29


def test_sample_39():
  sample_input = textwrap.dedent("?.#?.????? 1,2").strip()

  assert solve(sample_input, 1) == 5


def test_sample_40():
  sample_input = textwrap.dedent("??????.#???#? 2,5").strip()

  assert solve(sample_input, 1) == 5


def test_sample_41():
  sample_input = textwrap.dedent("?????#.###???#.???# 6,7,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_42():
  sample_input = textwrap.dedent("##.????##..#??#?. 2,6,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_43():
  sample_input = textwrap.dedent("?????.??.?????????. 1,6").strip()

  assert solve(sample_input, 1) == 31


def test_sample_44():
  sample_input = textwrap.dedent("??????..#?# 4,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_45():
  sample_input = textwrap.dedent("#??????#??..?#? 10,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_46():
  sample_input = textwrap.dedent("?.?????.?#??? 1,2").strip()

  assert solve(sample_input, 1) == 13


def test_sample_47():
  sample_input = textwrap.dedent("???#??????.. 2,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_48():
  sample_input = textwrap.dedent(".#?#???####??.?#?##? 12,5").strip()

  assert solve(sample_input, 1) == 2


def test_sample_49():
  sample_input = textwrap.dedent("?.?????##??? 3,4").strip()

  assert solve(sample_input, 1) == 3


def test_sample_50():
  sample_input = textwrap.dedent("?###?###????????# 10,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_51():
  sample_input = textwrap.dedent(".?????????#? 1,5").strip()

  assert solve(sample_input, 1) == 9


def test_sample_52():
  sample_input = textwrap.dedent("#?##????#???? 1,2,2,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_53():
  sample_input = textwrap.dedent(".??????.??#???. 1,2,1,1,1").strip()

  assert solve(sample_input, 1) == 15


def test_sample_54():
  sample_input = textwrap.dedent("??#.?#.????# 1,2,1,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_55():
  sample_input = textwrap.dedent("???????.?#??????.?? 2,1,1,8,1").strip()

  assert solve(sample_input, 1) == 8


def test_sample_56():
  sample_input = textwrap.dedent("???#??.?#???? 5,2,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_57():
  sample_input = textwrap.dedent("?#??????###???. 2,8").strip()

  assert solve(sample_input, 1) == 7


def test_sample_58():
  sample_input = textwrap.dedent(".??????#???????#? 1,12").strip()

  assert solve(sample_input, 1) == 5


def test_sample_59():
  sample_input = textwrap.dedent("??..???#?#??? 1,6").strip()

  assert solve(sample_input, 1) == 11


def test_sample_60():
  sample_input = textwrap.dedent("?.??????.. 1,1,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_61():
  sample_input = textwrap.dedent("??#??.?#??#. 1,1,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_62():
  sample_input = textwrap.dedent("?#?????.??????. 1,1,6").strip()

  assert solve(sample_input, 1) == 4


def test_sample_63():
  sample_input = textwrap.dedent(".#?#?????#?#???#?.?? 5,9").strip()

  assert solve(sample_input, 1) == 2


def test_sample_64():
  sample_input = textwrap.dedent("???#???#.#?##????? 5,1,7,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_65():
  sample_input = textwrap.dedent("?#.??#??#?..?? 1,5,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_66():
  sample_input = textwrap.dedent("#???#????#?.? 1,1,6,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_67():
  sample_input = textwrap.dedent("????????.#? 4,1").strip()

  assert solve(sample_input, 1) == 5


def test_sample_68():
  sample_input = textwrap.dedent("????#?#?#??.??.?? 8,1").strip()

  assert solve(sample_input, 1) == 13


def test_sample_69():
  sample_input = textwrap.dedent("???#?????#?#?..#? 4,1,4,1").strip()

  assert solve(sample_input, 1) == 9


def test_sample_70():
  sample_input = textwrap.dedent("??.??????#??.?#??#. 1,3,1,1").strip()

  assert solve(sample_input, 1) == 18


def test_sample_71():
  sample_input = textwrap.dedent(".????????????? 1,2,2,1").strip()

  assert solve(sample_input, 1) == 70


def test_sample_72():
  sample_input = textwrap.dedent("#.?#?#?#?.??? 1,6,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_73():
  sample_input = textwrap.dedent("?#??#??..?#?? 3,2,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_74():
  sample_input = textwrap.dedent("..#?.?#??#?# 2,6").strip()

  assert solve(sample_input, 1) == 1


def test_sample_75():
  sample_input = textwrap.dedent("???#?.?..???## 3,1,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_76():
  sample_input = textwrap.dedent("?????.?#?.???## 3,3,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_77():
  sample_input = textwrap.dedent("??.?????..????? 3,5").strip()

  assert solve(sample_input, 1) == 3


def test_sample_78():
  sample_input = textwrap.dedent("?.?????##? 1,1,2").strip()

  assert solve(sample_input, 1) == 7


def test_sample_79():
  sample_input = textwrap.dedent("?.??#.#????#???.. 1,3,1,1,4").strip()

  assert solve(sample_input, 1) == 3


def test_sample_80():
  sample_input = textwrap.dedent("??#??#?#?##????.# 3,3,6,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_81():
  sample_input = textwrap.dedent("?.?.?.?####???.#. 1,8,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_82():
  sample_input = textwrap.dedent("?##?????#?.?#.. 3,1,1,2,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_83():
  sample_input = textwrap.dedent("???#???????.#. 2,4,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_84():
  sample_input = textwrap.dedent("????.??.?#???? 1,3").strip()

  assert solve(sample_input, 1) == 13


def test_sample_85():
  sample_input = textwrap.dedent(".?#?#?#??????##??? 2,11,2").strip()

  assert solve(sample_input, 1) == 1


def test_sample_86():
  sample_input = textwrap.dedent("??.?#?.#?. 2,2,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_87():
  sample_input = textwrap.dedent("????#...?#???# 4,5").strip()

  assert solve(sample_input, 1) == 1


def test_sample_88():
  sample_input = textwrap.dedent(".??..???#??#?#? 2,1,1,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_89():
  sample_input = textwrap.dedent("????#.?????? 3,6").strip()

  assert solve(sample_input, 1) == 1


def test_sample_90():
  sample_input = textwrap.dedent("????.?????? 1,1,2").strip()

  assert solve(sample_input, 1) == 40


def test_sample_91():
  sample_input = textwrap.dedent("????#?????.?# 1,2,2,2").strip()

  assert solve(sample_input, 1) == 12


def test_sample_92():
  sample_input = textwrap.dedent(".?#?????.??.? 3,1,1,1").strip()

  assert solve(sample_input, 1) == 13


def test_sample_93():
  sample_input = textwrap.dedent("???#??.?#.??. 1,3,2,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_94():
  sample_input = textwrap.dedent("?##???????#???????# 2,9,1").strip()

  assert solve(sample_input, 1) == 5


def test_sample_95():
  sample_input = textwrap.dedent("?##?????????.?? 8,1").strip()

  assert solve(sample_input, 1) == 9


def test_sample_96():
  sample_input = textwrap.dedent(".#???????.??#???? 1,4,4").strip()

  assert solve(sample_input, 1) == 9


def test_sample_97():
  sample_input = textwrap.dedent(".?#?.#??.? 1,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_98():
  sample_input = textwrap.dedent("??.?#??????#? 4,3").strip()

  assert solve(sample_input, 1) == 4


def test_sample_99():
  sample_input = textwrap.dedent("??#?#??#??.?? 3,2,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_100():
  sample_input = textwrap.dedent(".#?.???##? 1,5").strip()

  assert solve(sample_input, 1) == 2


def test_sample_101():
  sample_input = textwrap.dedent("?????.#?.???#? 2,1,1,4").strip()

  assert solve(sample_input, 1) == 6


def test_sample_102():
  sample_input = textwrap.dedent("##????#??? 4,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_103():
  sample_input = textwrap.dedent("?????????# 1,2,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_104():
  sample_input = textwrap.dedent("??#?#?????##? 4,3").strip()

  assert solve(sample_input, 1) == 4


def test_sample_105():
  sample_input = textwrap.dedent("?#.???##?#????#?##. 1,12").strip()

  assert solve(sample_input, 1) == 1


def test_sample_106():
  sample_input = textwrap.dedent("#.?##???#???..??.?? 1,6,1,2,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_107():
  sample_input = textwrap.dedent("?#????#??#.#?.##?# 5,1,1,1,4").strip()

  assert solve(sample_input, 1) == 1


def test_sample_108():
  sample_input = textwrap.dedent("?#????#.#??#..? 1,3,1,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_109():
  sample_input = textwrap.dedent("??###?.?.????. 5,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_110():
  sample_input = textwrap.dedent(".????????#.#? 5,2,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_111():
  sample_input = textwrap.dedent(".?.#.???..??#.?? 1,1,1,3,1").strip()

  assert solve(sample_input, 1) == 8


def test_sample_112():
  sample_input = textwrap.dedent("#????????.??????. 4,4,2,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_113():
  sample_input = textwrap.dedent("?.??????#? 3,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_114():
  sample_input = textwrap.dedent("...?#.#.???##? 2,1,1,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_115():
  sample_input = textwrap.dedent("??????????#.???.?#?? 7,1,1,1").strip()

  assert solve(sample_input, 1) == 17


def test_sample_116():
  sample_input = textwrap.dedent(".????##?#??.???#???? 7,5").strip()

  assert solve(sample_input, 1) == 12


def test_sample_117():
  sample_input = textwrap.dedent("??.#?.???? 1,2,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_118():
  sample_input = textwrap.dedent("?.#??#??#?? 1,4,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_119():
  sample_input = textwrap.dedent("????#?????? 1,4,2").strip()

  assert solve(sample_input, 1) == 10


def test_sample_120():
  sample_input = textwrap.dedent("??.???????? 1,1,2").strip()

  assert solve(sample_input, 1) == 40


def test_sample_121():
  sample_input = textwrap.dedent("??#????????#??#???? 3,3,7").strip()

  assert solve(sample_input, 1) == 19


def test_sample_122():
  sample_input = textwrap.dedent("?????????##?.??#?. 1,1,2,1,3,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_123():
  sample_input = textwrap.dedent("??#????????????.??? 2,11").strip()

  assert solve(sample_input, 1) == 1


def test_sample_124():
  sample_input = textwrap.dedent("??#?.?#???#?##????. 4,3,4,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_125():
  sample_input = textwrap.dedent("????.???????.?? 1,3").strip()

  assert solve(sample_input, 1) == 26


def test_sample_126():
  sample_input = textwrap.dedent("????#.##?? 1,1,4").strip()

  assert solve(sample_input, 1) == 3


def test_sample_127():
  sample_input = textwrap.dedent("#?????#?????.##?## 2,7,5").strip()

  assert solve(sample_input, 1) == 3


def test_sample_128():
  sample_input = textwrap.dedent("#??.??..?#?#.? 2,1,4").strip()

  assert solve(sample_input, 1) == 2


def test_sample_129():
  sample_input = textwrap.dedent(".??.??.?.?????##? 1,1,1,4").strip()

  assert solve(sample_input, 1) == 53


def test_sample_130():
  sample_input = textwrap.dedent("??.???????#??? 1,7,1").strip()

  assert solve(sample_input, 1) == 7


def test_sample_131():
  sample_input = textwrap.dedent(".#.??.?##???#.? 1,1,3,2,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_132():
  sample_input = textwrap.dedent("#??.??##??.?#?.#?#?? 3,4,1,4").strip()

  assert solve(sample_input, 1) == 3


def test_sample_133():
  sample_input = textwrap.dedent("???..?????????.# 2,1,3,1,1").strip()

  assert solve(sample_input, 1) == 20


def test_sample_134():
  sample_input = textwrap.dedent("??#.?????#?##.?#.# 2,6,2,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_135():
  sample_input = textwrap.dedent("?#?.?.#??#?? 1,6").strip()

  assert solve(sample_input, 1) == 1


def test_sample_136():
  sample_input = textwrap.dedent("?###????#?.? 6,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_137():
  sample_input = textwrap.dedent("?.?????????????.?? 1,1,1,1,4,1").strip()

  assert solve(sample_input, 1) == 88


def test_sample_138():
  sample_input = textwrap.dedent("????.?#?##??#??. 1,1,5,2").strip()

  assert solve(sample_input, 1) == 9


def test_sample_139():
  sample_input = textwrap.dedent("???????.????# 1,1,1,3").strip()

  assert solve(sample_input, 1) == 25


def test_sample_140():
  sample_input = textwrap.dedent("##???.????#???# 2,1,1,1,5").strip()

  assert solve(sample_input, 1) == 2


def test_sample_141():
  sample_input = textwrap.dedent(".#?##???####?.??#.?? 4,5,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_142():
  sample_input = textwrap.dedent("????????#?#?.?#?? 1,1,3,1,3").strip()

  assert solve(sample_input, 1) == 12


def test_sample_143():
  sample_input = textwrap.dedent("?.?????#?. 2,2").strip()

  assert solve(sample_input, 1) == 5


def test_sample_144():
  sample_input = textwrap.dedent("?#???????????#.????? 7,2,1,1,1").strip()

  assert solve(sample_input, 1) == 37


def test_sample_145():
  sample_input = textwrap.dedent("????????#..##. 1,2,2,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_146():
  sample_input = textwrap.dedent("#?#?##?#??. 3,5").strip()

  assert solve(sample_input, 1) == 1


def test_sample_147():
  sample_input = textwrap.dedent("???#????###????????. 17,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_148():
  sample_input = textwrap.dedent(".????#???## 1,3,4").strip()

  assert solve(sample_input, 1) == 1


def test_sample_149():
  sample_input = textwrap.dedent("??####??#??#?#?#?#?? 6,6,4").strip()

  assert solve(sample_input, 1) == 2


def test_sample_150():
  sample_input = textwrap.dedent("??????#????.?.?? 1,3,1,1,1").strip()

  assert solve(sample_input, 1) == 65


def test_sample_151():
  sample_input = textwrap.dedent("..?##?.?.?. 3,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_152():
  sample_input = textwrap.dedent(".???####?????#? 8,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_153():
  sample_input = textwrap.dedent(".???????#?..??.?# 1,3,1,2,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_154():
  sample_input = textwrap.dedent("??.?#?????? 1,2,2").strip()

  assert solve(sample_input, 1) == 15


def test_sample_155():
  sample_input = textwrap.dedent("??#???#..?#?????#??? 4,1,5,1,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_156():
  sample_input = textwrap.dedent("??#?...#?? 4,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_157():
  sample_input = textwrap.dedent("??????.#?#?##??.?? 2,7").strip()

  assert solve(sample_input, 1) == 5


def test_sample_158():
  sample_input = textwrap.dedent(".???????##???. 1,9").strip()

  assert solve(sample_input, 1) == 3


def test_sample_159():
  sample_input = textwrap.dedent("?..#.????#??#???#?? 1,3,9").strip()

  assert solve(sample_input, 1) == 1


def test_sample_160():
  sample_input = textwrap.dedent("?#??????????#???.#?? 4,3,1,1,3").strip()

  assert solve(sample_input, 1) == 18


def test_sample_161():
  sample_input = textwrap.dedent(".?????#???.??#?.?. 4,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_162():
  sample_input = textwrap.dedent("??#.?##?#??##??#?#? 1,1,12,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_163():
  sample_input = textwrap.dedent("?##??#??##???#.?.. 2,9").strip()

  assert solve(sample_input, 1) == 1


def test_sample_164():
  sample_input = textwrap.dedent("#??????#??? 3,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_165():
  sample_input = textwrap.dedent("##???.?#..#.?# 5,2,1,2").strip()

  assert solve(sample_input, 1) == 1


def test_sample_166():
  sample_input = textwrap.dedent("???.?.???# 2,1,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_167():
  sample_input = textwrap.dedent("?.?????.?? 2,2").strip()

  assert solve(sample_input, 1) == 5


def test_sample_168():
  sample_input = textwrap.dedent("???.?????#?.?????? 1,2,2").strip()

  assert solve(sample_input, 1) == 84


def test_sample_169():
  sample_input = textwrap.dedent(".#????#????.? 1,6").strip()

  assert solve(sample_input, 1) == 3


def test_sample_170():
  sample_input = textwrap.dedent("????.#.?#??????#???? 1,1,1,1,2,7").strip()

  assert solve(sample_input, 1) == 3


def test_sample_171():
  sample_input = textwrap.dedent("?.???.#.??##???#?? 1,1,1,1,8").strip()

  assert solve(sample_input, 1) == 7


def test_sample_172():
  sample_input = textwrap.dedent("??????.?#? 4,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_173():
  sample_input = textwrap.dedent("#??..?????#? 2,1,2,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_174():
  sample_input = textwrap.dedent("?##.#.????##?# 2,1,2,4").strip()

  assert solve(sample_input, 1) == 2


def test_sample_175():
  sample_input = textwrap.dedent("????????#???. 9,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_176():
  sample_input = textwrap.dedent("??..????.? 1,4").strip()

  assert solve(sample_input, 1) == 2


def test_sample_177():
  sample_input = textwrap.dedent("????#???#?.? 9,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_178():
  sample_input = textwrap.dedent("#???.??????? 3,1,2,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_179():
  sample_input = textwrap.dedent(".??????.?##??#. 6,3,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_180():
  sample_input = textwrap.dedent("#.?.?#????#??#? 1,2,1,2,2").strip()

  assert solve(sample_input, 1) == 5


def test_sample_181():
  sample_input = textwrap.dedent("##??##?.??? 6,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_182():
  sample_input = textwrap.dedent("?????.????#???? 1,1,6").strip()

  assert solve(sample_input, 1) == 39


def test_sample_183():
  sample_input = textwrap.dedent("#??.????????????#?#. 2,1,1,4,3").strip()

  assert solve(sample_input, 1) == 20


def test_sample_184():
  sample_input = textwrap.dedent("???#??..?????#?## 5,3,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_185():
  sample_input = textwrap.dedent("?##??????.??.? 4,4,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_186():
  sample_input = textwrap.dedent("???#?????#?.? 2,1,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_187():
  sample_input = textwrap.dedent(".?#?#????#?#?#? 5,6").strip()

  assert solve(sample_input, 1) == 4


def test_sample_188():
  sample_input = textwrap.dedent("?..?#??###???? 1,7").strip()

  assert solve(sample_input, 1) == 4


def test_sample_189():
  sample_input = textwrap.dedent("??#.???##.#? 2,4,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_190():
  sample_input = textwrap.dedent("#??????#.?##?#?##??? 1,2,3,8,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_191():
  sample_input = textwrap.dedent("?.?????????#?.? 2,6").strip()

  assert solve(sample_input, 1) == 5


def test_sample_192():
  sample_input = textwrap.dedent("??.????##??? 1,3,2,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_193():
  sample_input = textwrap.dedent("?#?#??#???#?#??? 10,4").strip()

  assert solve(sample_input, 1) == 1


def test_sample_194():
  sample_input = textwrap.dedent("#.?.???#.#??#?? 1,1,1,1,6").strip()

  assert solve(sample_input, 1) == 2


def test_sample_195():
  sample_input = textwrap.dedent("??##??.??? 3,1").strip()

  assert solve(sample_input, 1) == 7


def test_sample_196():
  sample_input = textwrap.dedent("?????.??#..?.#? 1,1,3,1,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_197():
  sample_input = textwrap.dedent("####???#????? 8,1,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_198():
  sample_input = textwrap.dedent("?###???#?.. 4,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_199():
  sample_input = textwrap.dedent("????.?????#?.???? 1,1,1,5,2").strip()

  assert solve(sample_input, 1) == 9


def test_sample_200():
  sample_input = textwrap.dedent("#????#.??? 4,1,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_201():
  sample_input = textwrap.dedent("??#??????.??#?. 7,1,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_202():
  sample_input = textwrap.dedent("??#?????##??? 1,8").strip()

  assert solve(sample_input, 1) == 3


def test_sample_203():
  sample_input = textwrap.dedent("..?#.?#???????. 2,2,2,1").strip()

  assert solve(sample_input, 1) == 9


def test_sample_204():
  sample_input = textwrap.dedent("??.???#???.? 1,1,2,1").strip()

  assert solve(sample_input, 1) == 18


def test_sample_205():
  sample_input = textwrap.dedent(".?.#?.?.??? 2,1,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_206():
  sample_input = textwrap.dedent("????##??.????##?##?? 5,9").strip()

  assert solve(sample_input, 1) == 9


def test_sample_207():
  sample_input = textwrap.dedent("?#???????..?? 2,3,2").strip()

  assert solve(sample_input, 1) == 8


def test_sample_208():
  sample_input = textwrap.dedent("?#???????.??#????#?? 1,1,1,1,8").strip()

  assert solve(sample_input, 1) == 22


def test_sample_209():
  sample_input = textwrap.dedent("#.?????#?.? 1,2,1").strip()

  assert solve(sample_input, 1) == 5


def test_sample_210():
  sample_input = textwrap.dedent("#?.??????????????? 1,1,1,4,1,1").strip()

  assert solve(sample_input, 1) == 56


def test_sample_211():
  sample_input = textwrap.dedent("??.#???#????#? 1,2,4,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_212():
  sample_input = textwrap.dedent(".#???.???.#???#.? 4,1,1,2,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_213():
  sample_input = textwrap.dedent("??????#???#?# 1,2,1,1").strip()

  assert solve(sample_input, 1) == 9


def test_sample_214():
  sample_input = textwrap.dedent("????##??###??????.?? 1,8,4,1").strip()

  assert solve(sample_input, 1) == 14


def test_sample_215():
  sample_input = textwrap.dedent("??#?????#?????????? 9,1,3").strip()

  assert solve(sample_input, 1) == 31


def test_sample_216():
  sample_input = textwrap.dedent(".##???.???????? 2,1,1,1").strip()

  assert solve(sample_input, 1) == 62


def test_sample_217():
  sample_input = textwrap.dedent("?#.???.??#????# 2,1,1,7").strip()

  assert solve(sample_input, 1) == 1


def test_sample_218():
  sample_input = textwrap.dedent(".?..?..??? 1,1,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_219():
  sample_input = textwrap.dedent("???.????.??#?? 3,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_220():
  sample_input = textwrap.dedent(".?#.???#????????? 2,6").strip()

  assert solve(sample_input, 1) == 4


def test_sample_221():
  sample_input = textwrap.dedent("????.?#?????????# 1,6,1,1,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_222():
  sample_input = textwrap.dedent("???#?.?#???????? 1,2,4,2,1").strip()

  assert solve(sample_input, 1) == 12


def test_sample_223():
  sample_input = textwrap.dedent("??##???#??#? 1,2,3,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_224():
  sample_input = textwrap.dedent("#?.?.#.???? 1,1,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_225():
  sample_input = textwrap.dedent("?#??#.?????? 1,2,4").strip()

  assert solve(sample_input, 1) == 3


def test_sample_226():
  sample_input = textwrap.dedent("??????.##?????.? 1,4,1").strip()

  assert solve(sample_input, 1) == 18


def test_sample_227():
  sample_input = textwrap.dedent("#????.???.#.???????. 1,1,3,1,3,1").strip()

  assert solve(sample_input, 1) == 18


def test_sample_228():
  sample_input = textwrap.dedent(".#?##?..?##?.??.?? 4,2").strip()

  assert solve(sample_input, 1) == 1


def test_sample_229():
  sample_input = textwrap.dedent(".#?###??#???#?? 9,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_230():
  sample_input = textwrap.dedent("#??.##?.?.?#????#. 3,3,1,3,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_231():
  sample_input = textwrap.dedent("?????##????? 3,2,1").strip()

  assert solve(sample_input, 1) == 9


def test_sample_232():
  sample_input = textwrap.dedent("??#??????#????. 3,7").strip()

  assert solve(sample_input, 1) == 9


def test_sample_233():
  sample_input = textwrap.dedent("????#.?#?? 1,1,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_234():
  sample_input = textwrap.dedent(".??.#?##?.?? 1,5").strip()

  assert solve(sample_input, 1) == 2


def test_sample_235():
  sample_input = textwrap.dedent("?#??.#..?????#??#??? 2,1,1,1,6,1").strip()

  assert solve(sample_input, 1) == 9


def test_sample_236():
  sample_input = textwrap.dedent("?#?.??#???#??? 1,3,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_237():
  sample_input = textwrap.dedent("????.?#.?????????? 4,1,1,1,1,1").strip()

  assert solve(sample_input, 1) == 35


def test_sample_238():
  sample_input = textwrap.dedent("?.#.??????.?.##. 1,1,6,1,2").strip()

  assert solve(sample_input, 1) == 1


def test_sample_239():
  sample_input = textwrap.dedent("????????#???#???? 1,5,3,1").strip()

  assert solve(sample_input, 1) == 36


def test_sample_240():
  sample_input = textwrap.dedent(".?.?#??.?#?? 1,3,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_241():
  sample_input = textwrap.dedent("??????????#??####?? 1,1,4,8").strip()

  assert solve(sample_input, 1) == 5


def test_sample_242():
  sample_input = textwrap.dedent("?#???..????# 1,1,4").strip()

  assert solve(sample_input, 1) == 2


def test_sample_243():
  sample_input = textwrap.dedent(".??###?.#..#???.?.? 5,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_244():
  sample_input = textwrap.dedent("??.?.?????.???????.. 1,3,4").strip()

  assert solve(sample_input, 1) == 40


def test_sample_245():
  sample_input = textwrap.dedent("..??????.???. 4,1").strip()

  assert solve(sample_input, 1) == 10


def test_sample_246():
  sample_input = textwrap.dedent("#????????####??????# 1,11,2").strip()

  assert solve(sample_input, 1) == 5


def test_sample_247():
  sample_input = textwrap.dedent("?#?.?.????? 1,1,2").strip()

  assert solve(sample_input, 1) == 7


def test_sample_248():
  sample_input = textwrap.dedent(".?.?#??###?????.?#?? 1,2,7,1,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_249():
  sample_input = textwrap.dedent("???#?.#???#????..? 1,3,2,6,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_250():
  sample_input = textwrap.dedent("?..???????.? 1,1,4,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_251():
  sample_input = textwrap.dedent(".??????.#?????????? 1,1,1,1,1,4").strip()

  assert solve(sample_input, 1) == 80


def test_sample_252():
  sample_input = textwrap.dedent("?.?#??#?#???? 1,5").strip()

  assert solve(sample_input, 1) == 2


def test_sample_253():
  sample_input = textwrap.dedent("???.????#????#### 1,1,11").strip()

  assert solve(sample_input, 1) == 4


def test_sample_254():
  sample_input = textwrap.dedent(".??#.?????#??#??? 1,1,2,6,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_255():
  sample_input = textwrap.dedent("?#.?????.#?? 2,1,2,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_256():
  sample_input = textwrap.dedent("???.???#.#. 2,3,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_257():
  sample_input = textwrap.dedent("?????.????.# 3,1,1").strip()

  assert solve(sample_input, 1) == 13


def test_sample_258():
  sample_input = textwrap.dedent(".?????..?????# 4,1,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_259():
  sample_input = textwrap.dedent(".??##??#?#?????#. 6,1,3").strip()

  assert solve(sample_input, 1) == 1


def test_sample_260():
  sample_input = textwrap.dedent("??#?#???.??????#### 5,1,7").strip()

  assert solve(sample_input, 1) == 9


def test_sample_261():
  sample_input = textwrap.dedent("???#??#??#??.? 1,1,6").strip()

  assert solve(sample_input, 1) == 4


def test_sample_262():
  sample_input = textwrap.dedent("??????.???? 1,1,3").strip()

  assert solve(sample_input, 1) == 20


def test_sample_263():
  sample_input = textwrap.dedent("???###?###?.#??#? 1,9,2,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_264():
  sample_input = textwrap.dedent("##??.###..??? 4,3,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_265():
  sample_input = textwrap.dedent("??.??.?????#? 1,1,4").strip()

  assert solve(sample_input, 1) == 20


def test_sample_266():
  sample_input = textwrap.dedent("?#????????? 2,1,2").strip()

  assert solve(sample_input, 1) == 25


def test_sample_267():
  sample_input = textwrap.dedent("#?.?????.#?.??#?. 1,2,2,1,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_268():
  sample_input = textwrap.dedent("?#???..#????????#? 4,11").strip()

  assert solve(sample_input, 1) == 2


def test_sample_269():
  sample_input = textwrap.dedent("?????????####?? 1,1,1,5").strip()

  assert solve(sample_input, 1) == 30


def test_sample_270():
  sample_input = textwrap.dedent("??.?????.?#??????. 3,3,2").strip()

  assert solve(sample_input, 1) == 15


def test_sample_271():
  sample_input = textwrap.dedent("????.?#?#????#??.?? 2,11").strip()

  assert solve(sample_input, 1) == 3


def test_sample_272():
  sample_input = textwrap.dedent("##.#.?#.???.?.? 2,1,2,1,1").strip()

  assert solve(sample_input, 1) == 8


def test_sample_273():
  sample_input = textwrap.dedent("??.??????.????? 2,2,1,1,3").strip()

  assert solve(sample_input, 1) == 9


def test_sample_274():
  sample_input = textwrap.dedent("#?#???.#??#? 1,2,5").strip()

  assert solve(sample_input, 1) == 1


def test_sample_275():
  sample_input = textwrap.dedent("??#?.????? 3,2,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_276():
  sample_input = textwrap.dedent("??.???#??. 1,2").strip()

  assert solve(sample_input, 1) == 7


def test_sample_277():
  sample_input = textwrap.dedent("????#??#?. 1,1,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_278():
  sample_input = textwrap.dedent("#?.???.????? 1,1,1,5").strip()

  assert solve(sample_input, 1) == 1


def test_sample_279():
  sample_input = textwrap.dedent("???????.#?#??#?#??? 2,1,1,1,1,4").strip()

  assert solve(sample_input, 1) == 18


def test_sample_280():
  sample_input = textwrap.dedent("??#????##.? 5,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_281():
  sample_input = textwrap.dedent("??#???#?..#???. 6,1,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_282():
  sample_input = textwrap.dedent("?.#?????#?.. 1,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_283():
  sample_input = textwrap.dedent(".??.??#????..???#? 2,5").strip()

  assert solve(sample_input, 1) == 2


def test_sample_284():
  sample_input = textwrap.dedent("?#?#????#?????#? 3,6,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_285():
  sample_input = textwrap.dedent("?###????.????##. 4,1,3").strip()

  assert solve(sample_input, 1) == 9


def test_sample_286():
  sample_input = textwrap.dedent("?.???????# 1,2,1").strip()

  assert solve(sample_input, 1) == 11


def test_sample_287():
  sample_input = textwrap.dedent(".??.??????#?..?## 1,6,2").strip()

  assert solve(sample_input, 1) == 5


def test_sample_288():
  sample_input = textwrap.dedent("#???#??#????..???.?? 9,1,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_289():
  sample_input = textwrap.dedent("#.???????????.???? 1,1,1,3,1,1").strip()

  assert solve(sample_input, 1) == 166


def test_sample_290():
  sample_input = textwrap.dedent("..??##??????##????# 3,11").strip()

  assert solve(sample_input, 1) == 2


def test_sample_291():
  sample_input = textwrap.dedent("?????.????????.?? 4,2,2,1").strip()

  assert solve(sample_input, 1) == 48


def test_sample_292():
  sample_input = textwrap.dedent("#..??.?#?? 1,1,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_293():
  sample_input = textwrap.dedent("????.???##???.#???? 1,1,1,6,1,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_294():
  sample_input = textwrap.dedent("??#?#??#??.???????# 1,8,2,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_295():
  sample_input = textwrap.dedent("??#.???#.?? 2,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_296():
  sample_input = textwrap.dedent("???#?#?.#????????##? 3,2,8").strip()

  assert solve(sample_input, 1) == 2


def test_sample_297():
  sample_input = textwrap.dedent("???#?.????#????? 4,6,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_298():
  sample_input = textwrap.dedent("??.??..????? 1,2,1,1").strip()

  assert solve(sample_input, 1) == 12


def test_sample_299():
  sample_input = textwrap.dedent("?.??#?#?????. 7,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_300():
  sample_input = textwrap.dedent("?.????#??#??#?#? 2,7").strip()

  assert solve(sample_input, 1) == 3


def test_sample_301():
  sample_input = textwrap.dedent(".?????????????#???? 3,1,4,1,1").strip()

  assert solve(sample_input, 1) == 46


def test_sample_302():
  sample_input = textwrap.dedent("????.????.? 1,3").strip()

  assert solve(sample_input, 1) == 8


def test_sample_303():
  sample_input = textwrap.dedent("??#..?????? 3,1,1").strip()

  assert solve(sample_input, 1) == 10


def test_sample_304():
  sample_input = textwrap.dedent(".?#...??????. 2,1,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_305():
  sample_input = textwrap.dedent("?????????????# 2,1,8").strip()

  assert solve(sample_input, 1) == 3


def test_sample_306():
  sample_input = textwrap.dedent("?????????? 1,1,5").strip()

  assert solve(sample_input, 1) == 4


def test_sample_307():
  sample_input = textwrap.dedent("??#?##??#?#?#?????? 6,2,1,1,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_308():
  sample_input = textwrap.dedent(".???#?????#. 4,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_309():
  sample_input = textwrap.dedent("?#.???#????###?#? 1,1,3,6").strip()

  assert solve(sample_input, 1) == 6


def test_sample_310():
  sample_input = textwrap.dedent("????#?#?#???.?.#?? 1,4,1,1,1,1").strip()

  assert solve(sample_input, 1) == 11


def test_sample_311():
  sample_input = textwrap.dedent("?#???###.??#?##? 2,1,3,6").strip()

  assert solve(sample_input, 1) == 2


def test_sample_312():
  sample_input = textwrap.dedent("?????????.#? 6,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_313():
  sample_input = textwrap.dedent("?????#???#????..# 4,1,4,2,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_314():
  sample_input = textwrap.dedent(".?.????.?????????? 1,2,7").strip()

  assert solve(sample_input, 1) == 21


def test_sample_315():
  sample_input = textwrap.dedent("#???????????? 1,1,2,5").strip()

  assert solve(sample_input, 1) == 4


def test_sample_316():
  sample_input = textwrap.dedent("???????????#.??.? 5,4").strip()

  assert solve(sample_input, 1) == 3


def test_sample_317():
  sample_input = textwrap.dedent("???##?#?#####???? 13,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_318():
  sample_input = textwrap.dedent("??.?..???.?? 1,1").strip()

  assert solve(sample_input, 1) == 24


def test_sample_319():
  sample_input = textwrap.dedent("???#?#?????? 8,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_320():
  sample_input = textwrap.dedent("?.??#?.#??? 2,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_321():
  sample_input = textwrap.dedent("#.?.??..#? 1,1,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_322():
  sample_input = textwrap.dedent("????????.??#???? 2,1,1,1,4").strip()

  assert solve(sample_input, 1) == 13


def test_sample_323():
  sample_input = textwrap.dedent("??#.??????????????? 1,3").strip()

  assert solve(sample_input, 1) == 13


def test_sample_324():
  sample_input = textwrap.dedent(".??##?.??.???##??#?. 4,8").strip()

  assert solve(sample_input, 1) == 4


def test_sample_325():
  sample_input = textwrap.dedent("?.???#????..???? 4,1").strip()

  assert solve(sample_input, 1) == 22


def test_sample_326():
  sample_input = textwrap.dedent("?#??????#?#. 1,3,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_327():
  sample_input = textwrap.dedent("#??####????.??? 11,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_328():
  sample_input = textwrap.dedent(".?#??????????????? 2,3,6").strip()

  assert solve(sample_input, 1) == 25


def test_sample_329():
  sample_input = textwrap.dedent("?#???#?#????#?.? 8,1,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_330():
  sample_input = textwrap.dedent("??.????.?.??#?#? 2,1,1,1,5").strip()

  assert solve(sample_input, 1) == 6


def test_sample_331():
  sample_input = textwrap.dedent("???#??.????#.. 4,2,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_332():
  sample_input = textwrap.dedent("???.????????. 3,1,2,1").strip()

  assert solve(sample_input, 1) == 10


def test_sample_333():
  sample_input = textwrap.dedent("#?#??.??#.????? 1,2,3,1,3").strip()

  assert solve(sample_input, 1) == 1


def test_sample_334():
  sample_input = textwrap.dedent("????#.???#?. 1,1,1,5").strip()

  assert solve(sample_input, 1) == 1


def test_sample_335():
  sample_input = textwrap.dedent("?????#???.?????. 8,2").strip()

  assert solve(sample_input, 1) == 8


def test_sample_336():
  sample_input = textwrap.dedent("??##??##??##??##? 11,4").strip()

  assert solve(sample_input, 1) == 1


def test_sample_337():
  sample_input = textwrap.dedent("??#.????#?? 2,5").strip()

  assert solve(sample_input, 1) == 3


def test_sample_338():
  sample_input = textwrap.dedent("??????????? 2,3").strip()

  assert solve(sample_input, 1) == 21


def test_sample_339():
  sample_input = textwrap.dedent("?????.#..? 1,1,1").strip()

  assert solve(sample_input, 1) == 11


def test_sample_340():
  sample_input = textwrap.dedent(".???#????#?????? 10,1").strip()

  assert solve(sample_input, 1) == 10


def test_sample_341():
  sample_input = textwrap.dedent("#???#?#???#????#???? 1,15,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_342():
  sample_input = textwrap.dedent("??????????##? 1,1,1,5").strip()

  assert solve(sample_input, 1) == 14


def test_sample_343():
  sample_input = textwrap.dedent("???.??##???.#..??#. 4,1,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_344():
  sample_input = textwrap.dedent(".?????.??##.? 1,1,1,4").strip()

  assert solve(sample_input, 1) == 1


def test_sample_345():
  sample_input = textwrap.dedent("??????##???..???#?? 3,5,1,2,1").strip()

  assert solve(sample_input, 1) == 8


def test_sample_346():
  sample_input = textwrap.dedent(".?#?#????.?.#?. 6,1,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_347():
  sample_input = textwrap.dedent("?????#?#?.#?? 1,4,1").strip()

  assert solve(sample_input, 1) == 7


def test_sample_348():
  sample_input = textwrap.dedent("???.??##?.?????? 3,5,1,1,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_349():
  sample_input = textwrap.dedent("?.????.????? 3,2,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_350():
  sample_input = textwrap.dedent("..??.?..#??##????#? 2,10").strip()

  assert solve(sample_input, 1) == 1


def test_sample_351():
  sample_input = textwrap.dedent("???..?????#?.??????? 1,2,5").strip()

  assert solve(sample_input, 1) == 39


def test_sample_352():
  sample_input = textwrap.dedent("?#???????????#?.? 9,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_353():
  sample_input = textwrap.dedent("..?##????##..# 2,1,2,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_354():
  sample_input = textwrap.dedent("???#??????#?.# 9,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_355():
  sample_input = textwrap.dedent("#?#???.??? 5,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_356():
  sample_input = textwrap.dedent("???..???.?.??????. 1,2,3,1").strip()

  assert solve(sample_input, 1) == 18


def test_sample_357():
  sample_input = textwrap.dedent(".#???.?.#??#?..?. 3,5").strip()

  assert solve(sample_input, 1) == 1


def test_sample_358():
  sample_input = textwrap.dedent("?#?#??###?. 4,4").strip()

  assert solve(sample_input, 1) == 3


def test_sample_359():
  sample_input = textwrap.dedent("????.?#???#? 2,3,2").strip()

  assert solve(sample_input, 1) == 9


def test_sample_360():
  sample_input = textwrap.dedent("?#?.#?.?..#? 3,1,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_361():
  sample_input = textwrap.dedent("???.??????.#??? 2,4,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_362():
  sample_input = textwrap.dedent(".##??????##?#????.#? 10,2,2").strip()

  assert solve(sample_input, 1) == 1


def test_sample_363():
  sample_input = textwrap.dedent("..??##??..??. 4,1").strip()

  assert solve(sample_input, 1) == 7


def test_sample_364():
  sample_input = textwrap.dedent("#.##????....##.??? 1,2,3,2,3").strip()

  assert solve(sample_input, 1) == 1


def test_sample_365():
  sample_input = textwrap.dedent("?.???#.?#.????? 2,2,4").strip()

  assert solve(sample_input, 1) == 2


def test_sample_366():
  sample_input = textwrap.dedent("???#???.??###? 3,6").strip()

  assert solve(sample_input, 1) == 3


def test_sample_367():
  sample_input = textwrap.dedent("?#..????..?##??.? 2,3,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_368():
  sample_input = textwrap.dedent("??#.???????????. 1,1,4,2,1").strip()

  assert solve(sample_input, 1) == 11


def test_sample_369():
  sample_input = textwrap.dedent(".##?????#???##?.???? 5,7,1").strip()

  assert solve(sample_input, 1) == 8


def test_sample_370():
  sample_input = textwrap.dedent("??.?????#???#?#?? 2,1,1,9").strip()

  assert solve(sample_input, 1) == 4


def test_sample_371():
  sample_input = textwrap.dedent("#?.??.?#.? 1,1,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_372():
  sample_input = textwrap.dedent("???..??????#?? 1,2,4").strip()

  assert solve(sample_input, 1) == 19


def test_sample_373():
  sample_input = textwrap.dedent(".#?#?#????.??#?.##?? 8,1,3").strip()

  assert solve(sample_input, 1) == 1


def test_sample_374():
  sample_input = textwrap.dedent("??????????.?? 6,1").strip()

  assert solve(sample_input, 1) == 16


def test_sample_375():
  sample_input = textwrap.dedent("?#????.?#.#??#?#.. 4,2,6").strip()

  assert solve(sample_input, 1) == 2


def test_sample_376():
  sample_input = textwrap.dedent(".????????.??.?? 4,1").strip()

  assert solve(sample_input, 1) == 26


def test_sample_377():
  sample_input = textwrap.dedent("???.#?#???????#... 6,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_378():
  sample_input = textwrap.dedent(".????.????? 1,5").strip()

  assert solve(sample_input, 1) == 4


def test_sample_379():
  sample_input = textwrap.dedent("?????????#. 1,5").strip()

  assert solve(sample_input, 1) == 4


def test_sample_380():
  sample_input = textwrap.dedent(".?..??##?.##?. 3,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_381():
  sample_input = textwrap.dedent("??.#?#?#?#????#???? 1,1,3,7,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_382():
  sample_input = textwrap.dedent("..??#?#???#??. 5,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_383():
  sample_input = textwrap.dedent("?..##????????? 1,5,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_384():
  sample_input = textwrap.dedent("?#?????#?? 1,4").strip()

  assert solve(sample_input, 1) == 3


def test_sample_385():
  sample_input = textwrap.dedent("#.???#??????#?. 1,4,5").strip()

  assert solve(sample_input, 1) == 5


def test_sample_386():
  sample_input = textwrap.dedent("?????##????.?.?? 1,8,1").strip()

  assert solve(sample_input, 1) == 9


def test_sample_387():
  sample_input = textwrap.dedent("???###?#??.??.?# 1,7,1,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_388():
  sample_input = textwrap.dedent("?#.??#??#????? 1,5").strip()

  assert solve(sample_input, 1) == 2


def test_sample_389():
  sample_input = textwrap.dedent("?#.???#????.???#?? 2,1,3,1,3").strip()

  assert solve(sample_input, 1) == 24


def test_sample_390():
  sample_input = textwrap.dedent("??#?.???##.??.????.? 4,2,3,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_391():
  sample_input = textwrap.dedent("??.??????#????#? 1,8").strip()

  assert solve(sample_input, 1) == 11


def test_sample_392():
  sample_input = textwrap.dedent("?#???.?????#?? 3,2,2").strip()

  assert solve(sample_input, 1) == 10


def test_sample_393():
  sample_input = textwrap.dedent(".#???????? 2,2").strip()

  assert solve(sample_input, 1) == 5


def test_sample_394():
  sample_input = textwrap.dedent("??.##.????????????? 2,2,3,1").strip()

  assert solve(sample_input, 1) == 101


def test_sample_395():
  sample_input = textwrap.dedent("#???????#?. 5,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_396():
  sample_input = textwrap.dedent("##.??.#?.??#?? 2,1,2,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_397():
  sample_input = textwrap.dedent("??????##??. 1,4").strip()

  assert solve(sample_input, 1) == 12


def test_sample_398():
  sample_input = textwrap.dedent("??.??##????? 1,7,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_399():
  sample_input = textwrap.dedent("???.?#??#??? 1,5").strip()

  assert solve(sample_input, 1) == 7


def test_sample_400():
  sample_input = textwrap.dedent("?#???.?????##?#?#?.# 3,3,2,3,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_401():
  sample_input = textwrap.dedent("?#?.????#? 2,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_402():
  sample_input = textwrap.dedent(".?#?#??.??#???? 4,6").strip()

  assert solve(sample_input, 1) == 4


def test_sample_403():
  sample_input = textwrap.dedent("?#..?######???? 1,10").strip()

  assert solve(sample_input, 1) == 2


def test_sample_404():
  sample_input = textwrap.dedent("??##??????? 2,5").strip()

  assert solve(sample_input, 1) == 2


def test_sample_405():
  sample_input = textwrap.dedent("???.????##..?..????? 2,2").strip()

  assert solve(sample_input, 1) == 8


def test_sample_406():
  sample_input = textwrap.dedent("??...##.????? 2,2,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_407():
  sample_input = textwrap.dedent("?#????#..#????#???? 6,10").strip()

  assert solve(sample_input, 1) == 1


def test_sample_408():
  sample_input = textwrap.dedent(".?##?????#??# 2,7").strip()

  assert solve(sample_input, 1) == 1


def test_sample_409():
  sample_input = textwrap.dedent("?????????#??#?#??#?? 2,10").strip()

  assert solve(sample_input, 1) == 13


def test_sample_410():
  sample_input = textwrap.dedent(".??##????#??.???.#?? 11,1,1,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_411():
  sample_input = textwrap.dedent("?#???.????# 2,5").strip()

  assert solve(sample_input, 1) == 2


def test_sample_412():
  sample_input = textwrap.dedent("???#?.??..???##???.? 5,1,2,2,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_413():
  sample_input = textwrap.dedent("???.??????????#? 1,1,1,4,2").strip()

  assert solve(sample_input, 1) == 31


def test_sample_414():
  sample_input = textwrap.dedent("????###????.??? 8,2").strip()

  assert solve(sample_input, 1) == 9


def test_sample_415():
  sample_input = textwrap.dedent("???.?#.??#??.??????. 1,3,2").strip()

  assert solve(sample_input, 1) == 15


def test_sample_416():
  sample_input = textwrap.dedent("??#???.#????#?? 2,2,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_417():
  sample_input = textwrap.dedent("#?#???#??#????.# 3,9,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_418():
  sample_input = textwrap.dedent(".??#????????#.?? 1,1,1,4,1").strip()

  assert solve(sample_input, 1) == 9


def test_sample_419():
  sample_input = textwrap.dedent("??#.????????#???#??? 1,3,1,3,1,1").strip()

  assert solve(sample_input, 1) == 21


def test_sample_420():
  sample_input = textwrap.dedent("??.?#??##?#???#??## 1,15").strip()

  assert solve(sample_input, 1) == 2


def test_sample_421():
  sample_input = textwrap.dedent("?????.?????#???#.??? 5,8,3").strip()

  assert solve(sample_input, 1) == 1


def test_sample_422():
  sample_input = textwrap.dedent(".?##????..?#?. 6,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_423():
  sample_input = textwrap.dedent("#????.??##????.# 1,1,6,1").strip()

  assert solve(sample_input, 1) == 10


def test_sample_424():
  sample_input = textwrap.dedent("?##???#??.??#. 3,4,1,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_425():
  sample_input = textwrap.dedent("???#.???#?.??????#.? 3,4,1,1,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_426():
  sample_input = textwrap.dedent("????????.# 7,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_427():
  sample_input = textwrap.dedent("?#???###?? 1,4,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_428():
  sample_input = textwrap.dedent("??.??#????#? 1,1,7").strip()

  assert solve(sample_input, 1) == 2


def test_sample_429():
  sample_input = textwrap.dedent("?#??????#..??.. 2,5,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_430():
  sample_input = textwrap.dedent(".??.?#????#?#.. 1,9").strip()

  assert solve(sample_input, 1) == 2


def test_sample_431():
  sample_input = textwrap.dedent("???..???#.??? 2,4").strip()

  assert solve(sample_input, 1) == 2


def test_sample_432():
  sample_input = textwrap.dedent("#??##??#.??? 1,2,2,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_433():
  sample_input = textwrap.dedent("..???.????? 2,1,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_434():
  sample_input = textwrap.dedent("???????.????##.##.? 4,1,4,2").strip()

  assert solve(sample_input, 1) == 7


def test_sample_435():
  sample_input = textwrap.dedent("??.??.?#.. 1,2,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_436():
  sample_input = textwrap.dedent("??#??#????##? 1,1,6").strip()

  assert solve(sample_input, 1) == 1


def test_sample_437():
  sample_input = textwrap.dedent("???##?###???# 1,8,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_438():
  sample_input = textwrap.dedent("?#????????.?.#?? 3,1,1,3").strip()

  assert solve(sample_input, 1) == 27


def test_sample_439():
  sample_input = textwrap.dedent(".?#?#??#?#.??.?? 9,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_440():
  sample_input = textwrap.dedent(".?...???.????# 1,1,5").strip()

  assert solve(sample_input, 1) == 4


def test_sample_441():
  sample_input = textwrap.dedent("...#?.#???#?#????? 1,8").strip()

  assert solve(sample_input, 1) == 1


def test_sample_442():
  sample_input = textwrap.dedent("#...?????#??#?#???#? 1,1,1,1,8").strip()

  assert solve(sample_input, 1) == 6


def test_sample_443():
  sample_input = textwrap.dedent(".??.??#?????????? 1,12").strip()

  assert solve(sample_input, 1) == 4


def test_sample_444():
  sample_input = textwrap.dedent("#????.?###?##???. 5,7,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_445():
  sample_input = textwrap.dedent("?#?.?#??????? 2,6").strip()

  assert solve(sample_input, 1) == 4


def test_sample_446():
  sample_input = textwrap.dedent("?#?#??????? 6,1").strip()

  assert solve(sample_input, 1) == 7


def test_sample_447():
  sample_input = textwrap.dedent("..???..?#??????.#? 3,3,2,1").strip()

  assert solve(sample_input, 1) == 5


def test_sample_448():
  sample_input = textwrap.dedent("????.???#?? 1,2,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_449():
  sample_input = textwrap.dedent("???##?##???#????? 5,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_450():
  sample_input = textwrap.dedent(".???..#?#? 1,1,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_451():
  sample_input = textwrap.dedent("?????#???#? 5,4").strip()

  assert solve(sample_input, 1) == 1


def test_sample_452():
  sample_input = textwrap.dedent("#?.?##?#???#??#??.# 2,2,1,7,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_453():
  sample_input = textwrap.dedent("?#?????.??#??#.?. 6,4").strip()

  assert solve(sample_input, 1) == 2


def test_sample_454():
  sample_input = textwrap.dedent("???#.???.????.?? 3,2,2,1,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_455():
  sample_input = textwrap.dedent(".??#?#??#??? 1,1,1,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_456():
  sample_input = textwrap.dedent("?.??#.?.??? 3,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_457():
  sample_input = textwrap.dedent(".?.#??????#????##?## 1,1,2,1,1,7").strip()

  assert solve(sample_input, 1) == 1


def test_sample_458():
  sample_input = textwrap.dedent(".????#???#???? 2,6,3").strip()

  assert solve(sample_input, 1) == 1


def test_sample_459():
  sample_input = textwrap.dedent("??##????????## 2,1,1,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_460():
  sample_input = textwrap.dedent(".????..??. 3,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_461():
  sample_input = textwrap.dedent("???#.?????###?.??#?? 2,1,1,3,4").strip()

  assert solve(sample_input, 1) == 14


def test_sample_462():
  sample_input = textwrap.dedent("?..???..?.????????#? 1,2,1,7,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_463():
  sample_input = textwrap.dedent("????????#?#? 1,5,3").strip()

  assert solve(sample_input, 1) == 1


def test_sample_464():
  sample_input = textwrap.dedent(".????????????? 6,2").strip()

  assert solve(sample_input, 1) == 15


def test_sample_465():
  sample_input = textwrap.dedent("???????##?#????.?#?? 1,5,2,1,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_466():
  sample_input = textwrap.dedent("??#?#.????#?? 5,2,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_467():
  sample_input = textwrap.dedent("??..#?????????. 1,4").strip()

  assert solve(sample_input, 1) == 7


def test_sample_468():
  sample_input = textwrap.dedent("??#.#???#???#? 2,7,2").strip()

  assert solve(sample_input, 1) == 1


def test_sample_469():
  sample_input = textwrap.dedent(".?.?.?????##?.?? 1,1,1,4,1").strip()

  assert solve(sample_input, 1) == 14


def test_sample_470():
  sample_input = textwrap.dedent(".?#???.?#. 4,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_471():
  sample_input = textwrap.dedent("??????#?.#??.?? 2,2,1,1,1").strip()

  assert solve(sample_input, 1) == 17


def test_sample_472():
  sample_input = textwrap.dedent(".??#?.?#??? 3,2,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_473():
  sample_input = textwrap.dedent("?##????##.??.??? 8,1,1").strip()

  assert solve(sample_input, 1) == 7


def test_sample_474():
  sample_input = textwrap.dedent("???#..??.##??????#? 2,1,1,9").strip()

  assert solve(sample_input, 1) == 2


def test_sample_475():
  sample_input = textwrap.dedent(".#???#??#? 2,5").strip()

  assert solve(sample_input, 1) == 2


def test_sample_476():
  sample_input = textwrap.dedent("???#.???#???##???? 2,1,5,2,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_477():
  sample_input = textwrap.dedent("?..#?????#????. 1,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_478():
  sample_input = textwrap.dedent(".??????#??. 1,1,1").strip()

  assert solve(sample_input, 1) == 11


def test_sample_479():
  sample_input = textwrap.dedent("?.??.?????#??#? 1,1,2,4").strip()

  assert solve(sample_input, 1) == 9


def test_sample_480():
  sample_input = textwrap.dedent("???.?#.#??????.??? 3,1,2,2,1,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_481():
  sample_input = textwrap.dedent("?????##?#??#????#.?? 1,13").strip()

  assert solve(sample_input, 1) == 3


def test_sample_482():
  sample_input = textwrap.dedent("..#????????.?? 2,4").strip()

  assert solve(sample_input, 1) == 3


def test_sample_483():
  sample_input = textwrap.dedent("?#??.?#?.?#??. 2,2,2").strip()

  assert solve(sample_input, 1) == 8


def test_sample_484():
  sample_input = textwrap.dedent("???##.????##? 4,7").strip()

  assert solve(sample_input, 1) == 1


def test_sample_485():
  sample_input = textwrap.dedent("?##?#?###?#.???.#??? 11,2,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_486():
  sample_input = textwrap.dedent("?.???????#? 1,5").strip()

  assert solve(sample_input, 1) == 7


def test_sample_487():
  sample_input = textwrap.dedent("??.?.???## 1,1,2").strip()

  assert solve(sample_input, 1) == 8


def test_sample_488():
  sample_input = textwrap.dedent("..#??#?#??##???#???# 1,4,9,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_489():
  sample_input = textwrap.dedent("?#??#????????## 3,1,1,5").strip()

  assert solve(sample_input, 1) == 3


def test_sample_490():
  sample_input = textwrap.dedent(".#?.??#????????# 1,8,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_491():
  sample_input = textwrap.dedent("#??????#???#?. 1,1,3,1").strip()

  assert solve(sample_input, 1) == 9


def test_sample_492():
  sample_input = textwrap.dedent(".?.???.?#??## 1,6").strip()

  assert solve(sample_input, 1) == 4


def test_sample_493():
  sample_input = textwrap.dedent("#?#?????#?#??#?..??? 1,1,3,1,3,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_494():
  sample_input = textwrap.dedent("##??#???.?#?? 7,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_495():
  sample_input = textwrap.dedent("..??#????.??##?#???. 5,8").strip()

  assert solve(sample_input, 1) == 6


def test_sample_496():
  sample_input = textwrap.dedent("??..#??????? 1,1,1,2").strip()

  assert solve(sample_input, 1) == 13


def test_sample_497():
  sample_input = textwrap.dedent("?????##?#.? 6,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_498():
  sample_input = textwrap.dedent("???#???#?#?.# 4,1,1,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_499():
  sample_input = textwrap.dedent("?.#???#.?#?#??.? 3,1,4").strip()

  assert solve(sample_input, 1) == 2


def test_sample_500():
  sample_input = textwrap.dedent("?.?#??.???.#..? 2,1,1,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_501():
  sample_input = textwrap.dedent("???#?#????.#????#? 1,2,5,1,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_502():
  sample_input = textwrap.dedent(".#.??##??#?## 1,9").strip()

  assert solve(sample_input, 1) == 1


def test_sample_503():
  sample_input = textwrap.dedent("???.????.???.? 4,3").strip()

  assert solve(sample_input, 1) == 1


def test_sample_504():
  sample_input = textwrap.dedent(".???#???##.?#? 1,3,2,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_505():
  sample_input = textwrap.dedent("...#??#?#?# 1,5").strip()

  assert solve(sample_input, 1) == 1


def test_sample_506():
  sample_input = textwrap.dedent("???#?#???.. 1,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_507():
  sample_input = textwrap.dedent("#?#???#??###. 1,5,4").strip()

  assert solve(sample_input, 1) == 1


def test_sample_508():
  sample_input = textwrap.dedent("#?????????##?????## 1,1,1,1,6,3").strip()

  assert solve(sample_input, 1) == 5


def test_sample_509():
  sample_input = textwrap.dedent("?.?#????#????###.? 8,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_510():
  sample_input = textwrap.dedent(".??#???????????? 6,1,3").strip()

  assert solve(sample_input, 1) == 19


def test_sample_511():
  sample_input = textwrap.dedent(".?...#.??#.#. 1,1,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_512():
  sample_input = textwrap.dedent(".#????????? 4,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_513():
  sample_input = textwrap.dedent("?????????##?.????? 8,3").strip()

  assert solve(sample_input, 1) == 7


def test_sample_514():
  sample_input = textwrap.dedent("?????#?.?.???.??? 2,1,3,2").strip()

  assert solve(sample_input, 1) == 10


def test_sample_515():
  sample_input = textwrap.dedent(".???#????#### 1,1,1,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_516():
  sample_input = textwrap.dedent(".?.#??#??##?##???.?? 1,1,9,1,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_517():
  sample_input = textwrap.dedent("?..#???#?#?.???.??. 1,8,1,1").strip()

  assert solve(sample_input, 1) == 7


def test_sample_518():
  sample_input = textwrap.dedent("??.??.????????? 1,1,4,1,1").strip()

  assert solve(sample_input, 1) == 16


def test_sample_519():
  sample_input = textwrap.dedent(".???#.#??.#.? 4,3,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_520():
  sample_input = textwrap.dedent("???#???.??? 1,2,1").strip()

  assert solve(sample_input, 1) == 16


def test_sample_521():
  sample_input = textwrap.dedent("?#???????..??#?#???? 5,7").strip()

  assert solve(sample_input, 1) == 6


def test_sample_522():
  sample_input = textwrap.dedent("??#???????#?#????#? 1,6,5,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_523():
  sample_input = textwrap.dedent("#???????????#.###? 1,2,1,1,2,4").strip()

  assert solve(sample_input, 1) == 10


def test_sample_524():
  sample_input = textwrap.dedent("?#???#?.#??.?# 6,1,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_525():
  sample_input = textwrap.dedent("#??????????.#?##?? 6,2,4").strip()

  assert solve(sample_input, 1) == 3


def test_sample_526():
  sample_input = textwrap.dedent("???????.?#????? 2,1,1,2,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_527():
  sample_input = textwrap.dedent("??#?##?#..?????#. 2,4,6").strip()

  assert solve(sample_input, 1) == 1


def test_sample_528():
  sample_input = textwrap.dedent("??????.??#??#? 3,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_529():
  sample_input = textwrap.dedent(".??...?????.? 1,2").strip()

  assert solve(sample_input, 1) == 11


def test_sample_530():
  sample_input = textwrap.dedent("??#????##????????# 1,1,8,1,1").strip()

  assert solve(sample_input, 1) == 7


def test_sample_531():
  sample_input = textwrap.dedent(".?#?????.? 1,1").strip()

  assert solve(sample_input, 1) == 5


def test_sample_532():
  sample_input = textwrap.dedent("???#?#????.???? 4,1,1").strip()

  assert solve(sample_input, 1) == 34


def test_sample_533():
  sample_input = textwrap.dedent("?.???.##?????# 1,8").strip()

  assert solve(sample_input, 1) == 4


def test_sample_534():
  sample_input = textwrap.dedent("??.#??#.???? 1,4,3").strip()

  assert solve(sample_input, 1) == 4


def test_sample_535():
  sample_input = textwrap.dedent("?.?#?????#. 1,5,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_536():
  sample_input = textwrap.dedent(".???.?.????? 3,1,2,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_537():
  sample_input = textwrap.dedent("???#?.#????..?#? 3,1,3,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_538():
  sample_input = textwrap.dedent("??????#??#?### 1,9").strip()

  assert solve(sample_input, 1) == 4


def test_sample_539():
  sample_input = textwrap.dedent("??????#??#???.#? 1,11,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_540():
  sample_input = textwrap.dedent("?#????#?#?#?.? 3,2,4").strip()

  assert solve(sample_input, 1) == 2


def test_sample_541():
  sample_input = textwrap.dedent("??#.????#??..?????.? 1,1,4,1,2,1").strip()

  assert solve(sample_input, 1) == 25


def test_sample_542():
  sample_input = textwrap.dedent("?.???.???#??###?.? 1,1,2,7").strip()

  assert solve(sample_input, 1) == 4


def test_sample_543():
  sample_input = textwrap.dedent("????..#?#???.?.#? 3,5,1,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_544():
  sample_input = textwrap.dedent("???.?#####.##???? 1,1,5,2,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_545():
  sample_input = textwrap.dedent("?#???##??#???? 1,1,8").strip()

  assert solve(sample_input, 1) == 1


def test_sample_546():
  sample_input = textwrap.dedent("???.?##?????.?#?#??? 6,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_547():
  sample_input = textwrap.dedent("????#..????.#?#.?#?? 4,4,1,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_548():
  sample_input = textwrap.dedent("?#?.#???.????????? 3,1,1,7,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_549():
  sample_input = textwrap.dedent("#??#??#?#..?????? 1,6,1,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_550():
  sample_input = textwrap.dedent("???#???.?#? 1,3,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_551():
  sample_input = textwrap.dedent("?#.?.?#???? 1,1,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_552():
  sample_input = textwrap.dedent(".#???#?.?.????#.??? 1,1,2,1,3,1").strip()

  assert solve(sample_input, 1) == 7


def test_sample_553():
  sample_input = textwrap.dedent("??.??####?.##???. 4,4").strip()

  assert solve(sample_input, 1) == 1


def test_sample_554():
  sample_input = textwrap.dedent("?#?.??????? 1,3").strip()

  assert solve(sample_input, 1) == 5


def test_sample_555():
  sample_input = textwrap.dedent(".???#?#?###????.## 11,1,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_556():
  sample_input = textwrap.dedent("?#???###????? 2,3,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_557():
  sample_input = textwrap.dedent(".#?#??##??#?.?????? 1,5,2,2,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_558():
  sample_input = textwrap.dedent(".##?#??#??????#??? 8,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_559():
  sample_input = textwrap.dedent("##?#?#????? 4,1,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_560():
  sample_input = textwrap.dedent("??.????.??#?#?#?#??? 1,9").strip()

  assert solve(sample_input, 1) == 19


def test_sample_561():
  sample_input = textwrap.dedent("????.#?.#??##.?#..#? 2,1,1,5,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_562():
  sample_input = textwrap.dedent("??.#?#???###. 3,5").strip()

  assert solve(sample_input, 1) == 1


def test_sample_563():
  sample_input = textwrap.dedent("#????#?#???.?? 3,6,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_564():
  sample_input = textwrap.dedent(".#??..??#. 3,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_565():
  sample_input = textwrap.dedent("???????.?#? 1,4,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_566():
  sample_input = textwrap.dedent("#???????#???#. 1,3,1,5").strip()

  assert solve(sample_input, 1) == 1


def test_sample_567():
  sample_input = textwrap.dedent("??###??#???? 7,1").strip()

  assert solve(sample_input, 1) == 5


def test_sample_568():
  sample_input = textwrap.dedent(".??#?###??.?#?##?? 9,1,3").strip()

  assert solve(sample_input, 1) == 1


def test_sample_569():
  sample_input = textwrap.dedent("#??#???#?????###??# 4,1,1,1,5,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_570():
  sample_input = textwrap.dedent("?#.?#.??#????#. 1,1,3,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_571():
  sample_input = textwrap.dedent(".##.????.??#?. 2,1,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_572():
  sample_input = textwrap.dedent("##.??#?????????..## 2,8,1,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_573():
  sample_input = textwrap.dedent("?.??#?.????. 2,3").strip()

  assert solve(sample_input, 1) == 4


def test_sample_574():
  sample_input = textwrap.dedent("?#????##?#.???##?? 2,5,1,2").strip()

  assert solve(sample_input, 1) == 5


def test_sample_575():
  sample_input = textwrap.dedent("#????#??#???#.# 1,10,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_576():
  sample_input = textwrap.dedent("???????..? 1,1,1").strip()

  assert solve(sample_input, 1) == 25


def test_sample_577():
  sample_input = textwrap.dedent(".??#??#??#?? 4,1,2,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_578():
  sample_input = textwrap.dedent("?????#???..?? 2,1").strip()

  assert solve(sample_input, 1) == 10


def test_sample_579():
  sample_input = textwrap.dedent(".#?..???###. 1,6").strip()

  assert solve(sample_input, 1) == 1


def test_sample_580():
  sample_input = textwrap.dedent("???#?.??.???. 3,1,1").strip()

  assert solve(sample_input, 1) == 14


def test_sample_581():
  sample_input = textwrap.dedent("?#????.#?.??.??.#. 2,2,2,2,1").strip()

  assert solve(sample_input, 1) == 8


def test_sample_582():
  sample_input = textwrap.dedent("?.??#.??????? 2,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_583():
  sample_input = textwrap.dedent("??#??????? 2,1,2").strip()

  assert solve(sample_input, 1) == 9


def test_sample_584():
  sample_input = textwrap.dedent("???.?##?.??????? 2,2,1,1,1").strip()

  assert solve(sample_input, 1) == 20


def test_sample_585():
  sample_input = textwrap.dedent("??.??#??#? 1,5").strip()

  assert solve(sample_input, 1) == 5


def test_sample_586():
  sample_input = textwrap.dedent("#????????#?.##? 1,1,2,1,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_587():
  sample_input = textwrap.dedent("#??.?.?#?????????? 1,1,1,4,1,1").strip()

  assert solve(sample_input, 1) == 33


def test_sample_588():
  sample_input = textwrap.dedent("???.?#?.?#?? 3,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_589():
  sample_input = textwrap.dedent("..??#??..?#?.??..?.? 1,3,1,1,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_590():
  sample_input = textwrap.dedent("??#??#??##??#???.??? 6,5,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_591():
  sample_input = textwrap.dedent("??????##????????#.# 2,7,2,1,1").strip()

  assert solve(sample_input, 1) == 10


def test_sample_592():
  sample_input = textwrap.dedent("?#?.????.???#?? 2,2,4").strip()

  assert solve(sample_input, 1) == 18


def test_sample_593():
  sample_input = textwrap.dedent("?#?#??????#????#?? 1,6,1,1,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_594():
  sample_input = textwrap.dedent("???.?????? 1,2,1").strip()

  assert solve(sample_input, 1) == 19


def test_sample_595():
  sample_input = textwrap.dedent("?????????###?#???? 1,9,5").strip()

  assert solve(sample_input, 1) == 2


def test_sample_596():
  sample_input = textwrap.dedent("??????##?#????# 1,5,1,4").strip()

  assert solve(sample_input, 1) == 2


def test_sample_597():
  sample_input = textwrap.dedent("?.?#?##?...#?? 5,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_598():
  sample_input = textwrap.dedent(".???#...?????#?? 2,1,7").strip()

  assert solve(sample_input, 1) == 2


def test_sample_599():
  sample_input = textwrap.dedent("???.??.?????.??? 3,1,2,1,1").strip()

  assert solve(sample_input, 1) == 29


def test_sample_600():
  sample_input = textwrap.dedent(".?#??????. 1,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_601():
  sample_input = textwrap.dedent("??????????#. 5,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_602():
  sample_input = textwrap.dedent("????#???##????#??#? 2,2,3,8").strip()

  assert solve(sample_input, 1) == 3


def test_sample_603():
  sample_input = textwrap.dedent("???#.????????##?# 1,1,1,5,1").strip()

  assert solve(sample_input, 1) == 11


def test_sample_604():
  sample_input = textwrap.dedent("??????#?##?? 2,7").strip()

  assert solve(sample_input, 1) == 6


def test_sample_605():
  sample_input = textwrap.dedent("?.?##???#??## 1,3,2,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_606():
  sample_input = textwrap.dedent("?.????.?#.. 1,2").strip()

  assert solve(sample_input, 1) == 5


def test_sample_607():
  sample_input = textwrap.dedent("?#.????.????. 2,3,3").strip()

  assert solve(sample_input, 1) == 4


def test_sample_608():
  sample_input = textwrap.dedent(".?##????????????. 3,1,2").strip()

  assert solve(sample_input, 1) == 64


def test_sample_609():
  sample_input = textwrap.dedent(".???.??#?.???#?# 2,2,1,3").strip()

  assert solve(sample_input, 1) == 8


def test_sample_610():
  sample_input = textwrap.dedent("?#?.?#??????????? 2,2,1,1,5").strip()

  assert solve(sample_input, 1) == 10


def test_sample_611():
  sample_input = textwrap.dedent("????#???#??????###?? 2,3,1,1,6,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_612():
  sample_input = textwrap.dedent("?#?##???#??#??. 4,2,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_613():
  sample_input = textwrap.dedent("??????.?#??.?? 1,1,3,1").strip()

  assert solve(sample_input, 1) == 40


def test_sample_614():
  sample_input = textwrap.dedent(".?????#####??###? 9,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_615():
  sample_input = textwrap.dedent(".?.???#?#.????.?## 1,4,3,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_616():
  sample_input = textwrap.dedent("???###.??????? 5,1,2").strip()

  assert solve(sample_input, 1) == 10


def test_sample_617():
  sample_input = textwrap.dedent("??#??.???. 4,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_618():
  sample_input = textwrap.dedent(".?.?.?##.??#? 1,3,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_619():
  sample_input = textwrap.dedent("???..?#??#?. 2,6").strip()

  assert solve(sample_input, 1) == 2


def test_sample_620():
  sample_input = textwrap.dedent("??.#??#????????.?? 1,5").strip()

  assert solve(sample_input, 1) == 4


def test_sample_621():
  sample_input = textwrap.dedent("??#.??##.?? 1,3").strip()

  assert solve(sample_input, 1) == 1


def test_sample_622():
  sample_input = textwrap.dedent("?#.?.?#?.?#####????. 2,1,2,7").strip()

  assert solve(sample_input, 1) == 4


def test_sample_623():
  sample_input = textwrap.dedent("???.????#?#??? 2,9").strip()

  assert solve(sample_input, 1) == 4


def test_sample_624():
  sample_input = textwrap.dedent("??????#?.# 1,1,1").strip()

  assert solve(sample_input, 1) == 5


def test_sample_625():
  sample_input = textwrap.dedent("???????????????????# 1,2,1,2,3,1").strip()

  assert solve(sample_input, 1) == 252


def test_sample_626():
  sample_input = textwrap.dedent("?.??.?????#??#??#?. 1,2,4,8").strip()

  assert solve(sample_input, 1) == 1


def test_sample_627():
  sample_input = textwrap.dedent("??#??????#?#??? 3,2,1,4").strip()

  assert solve(sample_input, 1) == 7


def test_sample_628():
  sample_input = textwrap.dedent(".????????.???????? 4,1,1,2,1").strip()

  assert solve(sample_input, 1) == 80


def test_sample_629():
  sample_input = textwrap.dedent("??????##?????????.?? 14,1").strip()

  assert solve(sample_input, 1) == 11


def test_sample_630():
  sample_input = textwrap.dedent(".????.???????? 1,7").strip()

  assert solve(sample_input, 1) == 8


def test_sample_631():
  sample_input = textwrap.dedent("??..?????##?.??#?? 2,7,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_632():
  sample_input = textwrap.dedent("?..#?..???? 2,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_633():
  sample_input = textwrap.dedent(".?.???.#???#?#????. 1,1,8").strip()

  assert solve(sample_input, 1) == 12


def test_sample_634():
  sample_input = textwrap.dedent("?????.?.????????? 1,1,8").strip()

  assert solve(sample_input, 1) == 22


def test_sample_635():
  sample_input = textwrap.dedent("??.??.??.#??? 1,2,1,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_636():
  sample_input = textwrap.dedent("???.?###???? 2,3,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_637():
  sample_input = textwrap.dedent("?#?????#???.????. 1,5,2").strip()

  assert solve(sample_input, 1) == 13


def test_sample_638():
  sample_input = textwrap.dedent(".????#??.?????#?. 4,4").strip()

  assert solve(sample_input, 1) == 6


def test_sample_639():
  sample_input = textwrap.dedent("???..?#?????.?. 2,3,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_640():
  sample_input = textwrap.dedent("?##?.??.?#?????#? 4,1,4,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_641():
  sample_input = textwrap.dedent("?????..#????##?? 1,1,1,6").strip()

  assert solve(sample_input, 1) == 12


def test_sample_642():
  sample_input = textwrap.dedent("?.??##???..?#?.???? 5,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_643():
  sample_input = textwrap.dedent(".????????#??????.?? 1,10,1").strip()

  assert solve(sample_input, 1) == 24


def test_sample_644():
  sample_input = textwrap.dedent(".#?.?????#??# 1,7").strip()

  assert solve(sample_input, 1) == 1


def test_sample_645():
  sample_input = textwrap.dedent("?##?##???.???#. 6,1,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_646():
  sample_input = textwrap.dedent("?#??.#.?????#?#?. 1,1,1,1,6").strip()

  assert solve(sample_input, 1) == 3


def test_sample_647():
  sample_input = textwrap.dedent("?#?###??.#??##?? 7,5,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_648():
  sample_input = textwrap.dedent(".??#??????#?.?#????? 10,5").strip()

  assert solve(sample_input, 1) == 4


def test_sample_649():
  sample_input = textwrap.dedent("?#.#??????????#???# 2,2,1,3,3,1").strip()

  assert solve(sample_input, 1) == 10


def test_sample_650():
  sample_input = textwrap.dedent("???????????? 2,1,1,4").strip()

  assert solve(sample_input, 1) == 5


def test_sample_651():
  sample_input = textwrap.dedent(".#?????##??#???# 1,5,1,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_652():
  sample_input = textwrap.dedent("??..?.??????.?????. 2,3").strip()

  assert solve(sample_input, 1) == 23


def test_sample_653():
  sample_input = textwrap.dedent("?#??.??????.#?#????? 2,3,3,1").strip()

  assert solve(sample_input, 1) == 32


def test_sample_654():
  sample_input = textwrap.dedent("???#.????##???? 1,8").strip()

  assert solve(sample_input, 1) == 3


def test_sample_655():
  sample_input = textwrap.dedent("???????#???#?#??. 1,1,8,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_656():
  sample_input = textwrap.dedent("??????.??? 5,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_657():
  sample_input = textwrap.dedent("?.?..??.#??#?#?? 1,1,1,7").strip()

  assert solve(sample_input, 1) == 2


def test_sample_658():
  sample_input = textwrap.dedent(".#??##??#??? 6,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_659():
  sample_input = textwrap.dedent(".?#.?...?? 2,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_660():
  sample_input = textwrap.dedent("??#?##?#?????#???? 14,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_661():
  sample_input = textwrap.dedent("..?#?.?#.????#?? 2,2,4").strip()

  assert solve(sample_input, 1) == 6


def test_sample_662():
  sample_input = textwrap.dedent(".???.????.????#?? 2,1,1,1,3").strip()

  assert solve(sample_input, 1) == 45


def test_sample_663():
  sample_input = textwrap.dedent("#.???????#??##???# 1,1,1,9,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_664():
  sample_input = textwrap.dedent("??.???#?.. 2,5").strip()

  assert solve(sample_input, 1) == 1


def test_sample_665():
  sample_input = textwrap.dedent("?#???#?.??????.???? 3,1,1,1,1,2").strip()

  assert solve(sample_input, 1) == 44


def test_sample_666():
  sample_input = textwrap.dedent(".??#.???.#?#? 1,1,2,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_667():
  sample_input = textwrap.dedent(".?#?.#???#. 2,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_668():
  sample_input = textwrap.dedent(".?##?##?.?#..???.#?? 7,2,3,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_669():
  sample_input = textwrap.dedent("?#????#??#??#.#.?. 1,9,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_670():
  sample_input = textwrap.dedent("??.????????????? 2,1,1,2,4").strip()

  assert solve(sample_input, 1) == 15


def test_sample_671():
  sample_input = textwrap.dedent("?.????????? 1,1,6").strip()

  assert solve(sample_input, 1) == 3


def test_sample_672():
  sample_input = textwrap.dedent("????.#?????#??? 1,1,1,2,2").strip()

  assert solve(sample_input, 1) == 20


def test_sample_673():
  sample_input = textwrap.dedent(".??#??.#??.??.?? 1,1,1,2,2").strip()

  assert solve(sample_input, 1) == 5


def test_sample_674():
  sample_input = textwrap.dedent("#????????#??# 1,1,3,1").strip()

  assert solve(sample_input, 1) == 9


def test_sample_675():
  sample_input = textwrap.dedent("???.?#??.##?? 3,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_676():
  sample_input = textwrap.dedent("?##?#####???. 8,2").strip()

  assert solve(sample_input, 1) == 1


def test_sample_677():
  sample_input = textwrap.dedent("????????????##???.?# 10,2,2,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_678():
  sample_input = textwrap.dedent("??.?#.??????.? 1,1,1").strip()

  assert solve(sample_input, 1) == 30


def test_sample_679():
  sample_input = textwrap.dedent("?????#.##???.?#??? 3,2,5,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_680():
  sample_input = textwrap.dedent("???.?#????#?.? 1,8").strip()

  assert solve(sample_input, 1) == 3


def test_sample_681():
  sample_input = textwrap.dedent("?.##?#???.#??.?.? 6,1,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_682():
  sample_input = textwrap.dedent("???.??#?#???##.?.?? 2,4,4,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_683():
  sample_input = textwrap.dedent(".#??##???#???? 6,4").strip()

  assert solve(sample_input, 1) == 2


def test_sample_684():
  sample_input = textwrap.dedent("??....???. 1,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_685():
  sample_input = textwrap.dedent("#??#??.?????? 5,1,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_686():
  sample_input = textwrap.dedent("??????.?#.??..??? 1,1,2,1,2").strip()

  assert solve(sample_input, 1) == 43


def test_sample_687():
  sample_input = textwrap.dedent("#??.????????.#?. 3,1,1,4,2").strip()

  assert solve(sample_input, 1) == 1


def test_sample_688():
  sample_input = textwrap.dedent("#?.??.????? 1,1,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_689():
  sample_input = textwrap.dedent("?##?.?#.?? 2,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_690():
  sample_input = textwrap.dedent("?.?.##????.?. 1,1,6,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_691():
  sample_input = textwrap.dedent("?????????? 1,1,1").strip()

  assert solve(sample_input, 1) == 56


def test_sample_692():
  sample_input = textwrap.dedent("#???.?#?#????????..? 4,9,1,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_693():
  sample_input = textwrap.dedent("????#???##??.? 6,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_694():
  sample_input = textwrap.dedent("?##?????.#???# 3,2,5").strip()

  assert solve(sample_input, 1) == 5


def test_sample_695():
  sample_input = textwrap.dedent("???#???#.? 2,1,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_696():
  sample_input = textwrap.dedent("?.??????##.???.. 3,2").strip()

  assert solve(sample_input, 1) == 5


def test_sample_697():
  sample_input = textwrap.dedent("?#?.?????? 1,1,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_698():
  sample_input = textwrap.dedent("???.?#?##???#???? 1,6,1,1").strip()

  assert solve(sample_input, 1) == 19


def test_sample_699():
  sample_input = textwrap.dedent("#?#.#.#..??.# 3,1,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_700():
  sample_input = textwrap.dedent(".??????????? 5,4").strip()

  assert solve(sample_input, 1) == 3


def test_sample_701():
  sample_input = textwrap.dedent("??#.?????##??? 3,2,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_702():
  sample_input = textwrap.dedent("????#?#???##???.??? 14,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_703():
  sample_input = textwrap.dedent("#.##????#?.#??.???? 1,7,1,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_704():
  sample_input = textwrap.dedent("???#????#??????? 4,6,2").strip()

  assert solve(sample_input, 1) == 10


def test_sample_705():
  sample_input = textwrap.dedent("?.##?#?.?????##? 2,1,7").strip()

  assert solve(sample_input, 1) == 2


def test_sample_706():
  sample_input = textwrap.dedent("??.????#?#?????.? 1,1,4,3").strip()

  assert solve(sample_input, 1) == 15


def test_sample_707():
  sample_input = textwrap.dedent("#.????.?#? 1,1,3").strip()

  assert solve(sample_input, 1) == 4


def test_sample_708():
  sample_input = textwrap.dedent(".?#????##???.???? 1,7,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_709():
  sample_input = textwrap.dedent(".#.?????#??##?# 1,11").strip()

  assert solve(sample_input, 1) == 1


def test_sample_710():
  sample_input = textwrap.dedent("??????#??.#? 1,1,1,2").strip()

  assert solve(sample_input, 1) == 11


def test_sample_711():
  sample_input = textwrap.dedent("??..#???.?? 2,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_712():
  sample_input = textwrap.dedent("??###??#???????.???# 12,1,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_713():
  sample_input = textwrap.dedent(".?#??#.#??????#??#?? 4,1,1,3,1,1").strip()

  assert solve(sample_input, 1) == 5


def test_sample_714():
  sample_input = textwrap.dedent("??#??.????? 3,1,1").strip()

  assert solve(sample_input, 1) == 23


def test_sample_715():
  sample_input = textwrap.dedent(".?..?????#????#?##?? 2,10").strip()

  assert solve(sample_input, 1) == 5


def test_sample_716():
  sample_input = textwrap.dedent("?????????##??. 1,1,5").strip()

  assert solve(sample_input, 1) == 31


def test_sample_717():
  sample_input = textwrap.dedent("?????#?#??#?????? 4,1,2,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_718():
  sample_input = textwrap.dedent("#????.???? 1,3,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_719():
  sample_input = textwrap.dedent("?.??#?????#?? 1,9").strip()

  assert solve(sample_input, 1) == 4


def test_sample_720():
  sample_input = textwrap.dedent("?...#.??##???? 1,1,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_721():
  sample_input = textwrap.dedent("?..?#.#????????.? 2,1,6,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_722():
  sample_input = textwrap.dedent("#?#??#?.??????#??# 1,1,2,4,3,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_723():
  sample_input = textwrap.dedent("????#?????.?.?? 1,5,1,1,1").strip()

  assert solve(sample_input, 1) == 8


def test_sample_724():
  sample_input = textwrap.dedent("????.??#?.#?.?? 4,1,1,2,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_725():
  sample_input = textwrap.dedent("?????????.?###? 7,4").strip()

  assert solve(sample_input, 1) == 6


def test_sample_726():
  sample_input = textwrap.dedent(".#?#?#.?.?.????? 3,1,1,1,2").strip()

  assert solve(sample_input, 1) == 10


def test_sample_727():
  sample_input = textwrap.dedent("???##.?.##? 2,2").strip()

  assert solve(sample_input, 1) == 1


def test_sample_728():
  sample_input = textwrap.dedent("?#.?#.?#???##? 1,1,2,3").strip()

  assert solve(sample_input, 1) == 4


def test_sample_729():
  sample_input = textwrap.dedent("?.????#???? 1,2,5").strip()

  assert solve(sample_input, 1) == 3


def test_sample_730():
  sample_input = textwrap.dedent("?.?##.??#???.???? 1,3,5,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_731():
  sample_input = textwrap.dedent("???..??##?? 2,4,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_732():
  sample_input = textwrap.dedent(".????.????. 2,4").strip()

  assert solve(sample_input, 1) == 3


def test_sample_733():
  sample_input = textwrap.dedent("????####..#???.??? 7,3,3").strip()

  assert solve(sample_input, 1) == 1


def test_sample_734():
  sample_input = textwrap.dedent("???#???.##?.??#?#? 1,1,1,3,5").strip()

  assert solve(sample_input, 1) == 8


def test_sample_735():
  sample_input = textwrap.dedent("??#??##?.? 1,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_736():
  sample_input = textwrap.dedent("??#??????? 2,2").strip()

  assert solve(sample_input, 1) == 9


def test_sample_737():
  sample_input = textwrap.dedent("#??..??????? 2,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_738():
  sample_input = textwrap.dedent("?.??.?.???#??#?##?#? 1,1,1,10").strip()

  assert solve(sample_input, 1) == 19


def test_sample_739():
  sample_input = textwrap.dedent("????.?#?.?#??#? 2,3,5").strip()

  assert solve(sample_input, 1) == 6


def test_sample_740():
  sample_input = textwrap.dedent("?????????????#.?? 5,1,1,4,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_741():
  sample_input = textwrap.dedent("?#?..?#.?.?? 2,2,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_742():
  sample_input = textwrap.dedent("..#.?????? 1,4").strip()

  assert solve(sample_input, 1) == 3


def test_sample_743():
  sample_input = textwrap.dedent("?.??##??????..??? 6,2").strip()

  assert solve(sample_input, 1) == 9


def test_sample_744():
  sample_input = textwrap.dedent("??????#???? 3,1,1").strip()

  assert solve(sample_input, 1) == 11


def test_sample_745():
  sample_input = textwrap.dedent(".?????????#???# 10,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_746():
  sample_input = textwrap.dedent("????#?.#.?.???? 1,2,1,1,1").strip()

  assert solve(sample_input, 1) == 35


def test_sample_747():
  sample_input = textwrap.dedent("?.#??.????#. 1,2,3,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_748():
  sample_input = textwrap.dedent("??.#????.??#?????#?? 1,1,1,9").strip()

  assert solve(sample_input, 1) == 26


def test_sample_749():
  sample_input = textwrap.dedent("???.????#..???. 1,1,5,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_750():
  sample_input = textwrap.dedent("#???????#. 1,2,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_751():
  sample_input = textwrap.dedent("??????#???#?##?#? 1,1,1,7").strip()

  assert solve(sample_input, 1) == 17


def test_sample_752():
  sample_input = textwrap.dedent("??.?###???.?? 1,4,1,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_753():
  sample_input = textwrap.dedent(".??#?#?..???#.??### 3,1,4,4").strip()

  assert solve(sample_input, 1) == 1


def test_sample_754():
  sample_input = textwrap.dedent(".?###???.??#... 6,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_755():
  sample_input = textwrap.dedent("?#?.??????#?###?#?? 2,7,7").strip()

  assert solve(sample_input, 1) == 2


def test_sample_756():
  sample_input = textwrap.dedent("?#??????.??????.. 7,1,1,1").strip()

  assert solve(sample_input, 1) == 8


def test_sample_757():
  sample_input = textwrap.dedent(".??????.??.???#?.# 1,1,1,2,2,1").strip()

  assert solve(sample_input, 1) == 32


def test_sample_758():
  sample_input = textwrap.dedent("???.??.#???? 1,1,1,1").strip()

  assert solve(sample_input, 1) == 28


def test_sample_759():
  sample_input = textwrap.dedent("???#???#??.?????? 1,1,4,2,1").strip()

  assert solve(sample_input, 1) == 24


def test_sample_760():
  sample_input = textwrap.dedent("#?#.??#?#???#??? 3,1,1,1,3").strip()

  assert solve(sample_input, 1) == 4


def test_sample_761():
  sample_input = textwrap.dedent("?#????????.#..????? 4,1,1,1,4").strip()

  assert solve(sample_input, 1) == 18


def test_sample_762():
  sample_input = textwrap.dedent("??..???.?.? 1,3,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_763():
  sample_input = textwrap.dedent(".????...??#????#.?. 2,1,1").strip()

  assert solve(sample_input, 1) == 8


def test_sample_764():
  sample_input = textwrap.dedent("?????#??????#???? 6,7").strip()

  assert solve(sample_input, 1) == 10


def test_sample_765():
  sample_input = textwrap.dedent("?.??#?#???? 1,5,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_766():
  sample_input = textwrap.dedent("?..??#.???? 3,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_767():
  sample_input = textwrap.dedent("???##???##??#? 1,2,5").strip()

  assert solve(sample_input, 1) == 2


def test_sample_768():
  sample_input = textwrap.dedent("?.????????.#??#?.? 1,8,1,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_769():
  sample_input = textwrap.dedent("#??#????###?.???.? 5,6,1,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_770():
  sample_input = textwrap.dedent("????#?#?#?#???.??# 13,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_771():
  sample_input = textwrap.dedent("???#?#??#?? 3,4").strip()

  assert solve(sample_input, 1) == 2


def test_sample_772():
  sample_input = textwrap.dedent("??..?#???#????..? 1,4").strip()

  assert solve(sample_input, 1) == 3


def test_sample_773():
  sample_input = textwrap.dedent("??#..?.????.???? 1,1,3,1,1").strip()

  assert solve(sample_input, 1) == 12


def test_sample_774():
  sample_input = textwrap.dedent("?#??..??.???????.? 3,1,2,2,1").strip()

  assert solve(sample_input, 1) == 30


def test_sample_775():
  sample_input = textwrap.dedent("?????#???? 2,3,1").strip()

  assert solve(sample_input, 1) == 10


def test_sample_776():
  sample_input = textwrap.dedent("????#?#???.?#.#?#??? 1,6,1,1,6").strip()

  assert solve(sample_input, 1) == 1


def test_sample_777():
  sample_input = textwrap.dedent("#?##?#?#??????. 4,1,1,4").strip()

  assert solve(sample_input, 1) == 2


def test_sample_778():
  sample_input = textwrap.dedent("#?#.???#??? 3,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_779():
  sample_input = textwrap.dedent(".??.??.???#?#.?.? 1,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_780():
  sample_input = textwrap.dedent("???#?????#?? 1,3,1,1").strip()

  assert solve(sample_input, 1) == 8


def test_sample_781():
  sample_input = textwrap.dedent(".???????#? 4,2").strip()

  assert solve(sample_input, 1) == 5


def test_sample_782():
  sample_input = textwrap.dedent("???#?????.?????.. 1,4,1,1,2").strip()

  assert solve(sample_input, 1) == 12


def test_sample_783():
  sample_input = textwrap.dedent("???????????#?# 2,1,5").strip()

  assert solve(sample_input, 1) == 15


def test_sample_784():
  sample_input = textwrap.dedent("?.???.??..????.?.. 2,2").strip()

  assert solve(sample_input, 1) == 11


def test_sample_785():
  sample_input = textwrap.dedent("???.?????#?.????? 1,1,1,4,3").strip()

  assert solve(sample_input, 1) == 9


def test_sample_786():
  sample_input = textwrap.dedent("??.??????#???.?? 2,1,1,4,1").strip()

  assert solve(sample_input, 1) == 21


def test_sample_787():
  sample_input = textwrap.dedent("??#??.#.?.?##?#??? 4,1,1,7").strip()

  assert solve(sample_input, 1) == 4


def test_sample_788():
  sample_input = textwrap.dedent("?#???#?.???#??.#??#? 6,3,4").strip()

  assert solve(sample_input, 1) == 6


def test_sample_789():
  sample_input = textwrap.dedent("??#?.?????????. 4,2,2,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_790():
  sample_input = textwrap.dedent("??#????...##? 5,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_791():
  sample_input = textwrap.dedent("?#???##.??.???#?#. 6,1,5").strip()

  assert solve(sample_input, 1) == 2


def test_sample_792():
  sample_input = textwrap.dedent("????????#???#??.? 3,10").strip()

  assert solve(sample_input, 1) == 3


def test_sample_793():
  sample_input = textwrap.dedent("???.?#??.???##? 2,2,4").strip()

  assert solve(sample_input, 1) == 8


def test_sample_794():
  sample_input = textwrap.dedent("?..?????## 1,6").strip()

  assert solve(sample_input, 1) == 1


def test_sample_795():
  sample_input = textwrap.dedent("#??#.#?##???#?? 1,2,1,3,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_796():
  sample_input = textwrap.dedent("?##.????##?.?##. 3,3,3,3").strip()

  assert solve(sample_input, 1) == 1


def test_sample_797():
  sample_input = textwrap.dedent("???.???..#??..?.?#? 2,1,1,1,1,2").strip()

  assert solve(sample_input, 1) == 20


def test_sample_798():
  sample_input = textwrap.dedent("?#?##????#? 1,8").strip()

  assert solve(sample_input, 1) == 1


def test_sample_799():
  sample_input = textwrap.dedent(".??#??#?##?## 1,1,8").strip()

  assert solve(sample_input, 1) == 1


def test_sample_800():
  sample_input = textwrap.dedent(".#??..????..#.????? 1,1,1,1,1,5").strip()

  assert solve(sample_input, 1) == 3


def test_sample_801():
  sample_input = textwrap.dedent("???????.?#??# 5,3,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_802():
  sample_input = textwrap.dedent("#???#...?? 5,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_803():
  sample_input = textwrap.dedent(".???###??????? 5,1").strip()

  assert solve(sample_input, 1) == 15


def test_sample_804():
  sample_input = textwrap.dedent("?#?.?#?..#?#?#???? 1,2,1,1,2,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_805():
  sample_input = textwrap.dedent("#??#???.?????.??? 6,3,1,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_806():
  sample_input = textwrap.dedent("????#??.?. 1,2,1").strip()

  assert solve(sample_input, 1) == 7


def test_sample_807():
  sample_input = textwrap.dedent("????.??#.?.???#??? 1,1,2,1,1,3").strip()

  assert solve(sample_input, 1) == 9


def test_sample_808():
  sample_input = textwrap.dedent("#.???????##?????? 1,10,1,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_809():
  sample_input = textwrap.dedent("?.??.???##???#.? 2,8").strip()

  assert solve(sample_input, 1) == 1


def test_sample_810():
  sample_input = textwrap.dedent("?.#???.??#?? 3,2,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_811():
  sample_input = textwrap.dedent("?#?.?#???. 2,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_812():
  sample_input = textwrap.dedent(".???.#?..?#???##???? 1,2,2,7").strip()

  assert solve(sample_input, 1) == 9


def test_sample_813():
  sample_input = textwrap.dedent("?#???????? 3,4").strip()

  assert solve(sample_input, 1) == 5


def test_sample_814():
  sample_input = textwrap.dedent("?#???.?#?? 1,2,4").strip()

  assert solve(sample_input, 1) == 1


def test_sample_815():
  sample_input = textwrap.dedent("?????#.??? 6,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_816():
  sample_input = textwrap.dedent("??.???.?#? 1,2,2").strip()

  assert solve(sample_input, 1) == 8


def test_sample_817():
  sample_input = textwrap.dedent("..#?????????#.?#?#?# 5,4,5").strip()

  assert solve(sample_input, 1) == 1


def test_sample_818():
  sample_input = textwrap.dedent("#????#??#???? 2,1,4").strip()

  assert solve(sample_input, 1) == 3


def test_sample_819():
  sample_input = textwrap.dedent("..??.???.???#??? 2,7").strip()

  assert solve(sample_input, 1) == 3


def test_sample_820():
  sample_input = textwrap.dedent("??#??..??.???.?? 5,1,1,1").strip()

  assert solve(sample_input, 1) == 16


def test_sample_821():
  sample_input = textwrap.dedent(".?#??#?#.?..#?#.? 7,3").strip()

  assert solve(sample_input, 1) == 1


def test_sample_822():
  sample_input = textwrap.dedent("...?#?#?????#.?#? 2,7,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_823():
  sample_input = textwrap.dedent("??..???.?????????.? 2,2,1,4").strip()

  assert solve(sample_input, 1) == 23


def test_sample_824():
  sample_input = textwrap.dedent("???.?#???.? 1,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_825():
  sample_input = textwrap.dedent("?#?#?.???##???# 3,5,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_826():
  sample_input = textwrap.dedent("##?#.?##?.#? 4,3,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_827():
  sample_input = textwrap.dedent(".?????##?# 1,5,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_828():
  sample_input = textwrap.dedent("?.???#??#?#?? 1,7").strip()

  assert solve(sample_input, 1) == 5


def test_sample_829():
  sample_input = textwrap.dedent(".????##??????.? 12,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_830():
  sample_input = textwrap.dedent("???????.?.? 1,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_831():
  sample_input = textwrap.dedent("?#.???##????..???#?. 2,6,1,4").strip()

  assert solve(sample_input, 1) == 6


def test_sample_832():
  sample_input = textwrap.dedent("#???##?#..?????. 1,5,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_833():
  sample_input = textwrap.dedent("#??##.???.????.? 1,3,1,1").strip()

  assert solve(sample_input, 1) == 23


def test_sample_834():
  sample_input = textwrap.dedent("?.????#..??#??? 3,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_835():
  sample_input = textwrap.dedent(".??????#??... 4,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_836():
  sample_input = textwrap.dedent(".???#.?.??? 2,1").strip()

  assert solve(sample_input, 1) == 5


def test_sample_837():
  sample_input = textwrap.dedent("?#??#??#?#????##?? 2,1,11").strip()

  assert solve(sample_input, 1) == 4


def test_sample_838():
  sample_input = textwrap.dedent(".?#???..?.??.... 3,1,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_839():
  sample_input = textwrap.dedent("???#??#??????#??? 1,2,2,3,4").strip()

  assert solve(sample_input, 1) == 6


def test_sample_840():
  sample_input = textwrap.dedent(".###?????###.???? 11,4").strip()

  assert solve(sample_input, 1) == 1


def test_sample_841():
  sample_input = textwrap.dedent("#?#?..#?#???#??????? 4,7,1,1").strip()

  assert solve(sample_input, 1) == 10


def test_sample_842():
  sample_input = textwrap.dedent("????????????#?.. 6,3").strip()

  assert solve(sample_input, 1) == 9


def test_sample_843():
  sample_input = textwrap.dedent(".#.??..????. 1,1,2,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_844():
  sample_input = textwrap.dedent("?.#??#?#?#?#.?? 1,8,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_845():
  sample_input = textwrap.dedent(".???#??##?????. 1,9").strip()

  assert solve(sample_input, 1) == 3


def test_sample_846():
  sample_input = textwrap.dedent("#???????#? 2,1,3").strip()

  assert solve(sample_input, 1) == 5


def test_sample_847():
  sample_input = textwrap.dedent("???#?#.?.?.???? 3,1,1,2").strip()

  assert solve(sample_input, 1) == 12


def test_sample_848():
  sample_input = textwrap.dedent(".##???#??.??.#???# 8,5").strip()

  assert solve(sample_input, 1) == 1


def test_sample_849():
  sample_input = textwrap.dedent("#?##??????????? 1,7,1").strip()

  assert solve(sample_input, 1) == 5


def test_sample_850():
  sample_input = textwrap.dedent("??????????.??.?#? 7,1,1,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_851():
  sample_input = textwrap.dedent("#????#????##?????? 13,1,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_852():
  sample_input = textwrap.dedent("#??#????.?.?.?? 1,6,1,1").strip()

  assert solve(sample_input, 1) == 5


def test_sample_853():
  sample_input = textwrap.dedent("?#??###???#? 1,8").strip()

  assert solve(sample_input, 1) == 2


def test_sample_854():
  sample_input = textwrap.dedent("?????#..?? 2,3,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_855():
  sample_input = textwrap.dedent(".??????.??????. 1,1,5").strip()

  assert solve(sample_input, 1) == 20


def test_sample_856():
  sample_input = textwrap.dedent("???.?..???. 2,1").strip()

  assert solve(sample_input, 1) == 8


def test_sample_857():
  sample_input = textwrap.dedent("???????#???##?#?? 3,2,5").strip()

  assert solve(sample_input, 1) == 14


def test_sample_858():
  sample_input = textwrap.dedent("??????##??# 1,3,1").strip()

  assert solve(sample_input, 1) == 9


def test_sample_859():
  sample_input = textwrap.dedent("#??..?#???. 3,5").strip()

  assert solve(sample_input, 1) == 1


def test_sample_860():
  sample_input = textwrap.dedent("??#??#??#?#???#????? 15,1").strip()

  assert solve(sample_input, 1) == 9


def test_sample_861():
  sample_input = textwrap.dedent("??.???.???###? 2,3").strip()

  assert solve(sample_input, 1) == 4


def test_sample_862():
  sample_input = textwrap.dedent("?????????.???#. 2,5,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_863():
  sample_input = textwrap.dedent(".???????..??#? 1,1,1,2").strip()

  assert solve(sample_input, 1) == 35


def test_sample_864():
  sample_input = textwrap.dedent("????#?#.?.???.?? 6,1,1,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_865():
  sample_input = textwrap.dedent("?.??????.?.## 1,4,1,2").strip()

  assert solve(sample_input, 1) == 5


def test_sample_866():
  sample_input = textwrap.dedent("?#??#?#?.##??#?##??? 1,3,11").strip()

  assert solve(sample_input, 1) == 1


def test_sample_867():
  sample_input = textwrap.dedent("????##???.. 1,2,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_868():
  sample_input = textwrap.dedent("????.?.????#????#?#? 3,1,1,1,1,3").strip()

  assert solve(sample_input, 1) == 18


def test_sample_869():
  sample_input = textwrap.dedent("???.?.????#??.? 1,6").strip()

  assert solve(sample_input, 1) == 8


def test_sample_870():
  sample_input = textwrap.dedent("??##??????# 6,1,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_871():
  sample_input = textwrap.dedent("??.?.????##?????. 2,1,2,2").strip()

  assert solve(sample_input, 1) == 14


def test_sample_872():
  sample_input = textwrap.dedent("???...??????? 2,1").strip()

  assert solve(sample_input, 1) == 24


def test_sample_873():
  sample_input = textwrap.dedent(".?????###???.????.. 9,1").strip()

  assert solve(sample_input, 1) == 13


def test_sample_874():
  sample_input = textwrap.dedent("??.?#?.?.?##. 1,3").strip()

  assert solve(sample_input, 1) == 1


def test_sample_875():
  sample_input = textwrap.dedent("??#???#.??.# 1,5,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_876():
  sample_input = textwrap.dedent("??.????????? 1,5").strip()

  assert solve(sample_input, 1) == 16


def test_sample_877():
  sample_input = textwrap.dedent("???#???.?.#??????.?# 6,1,1,3,1,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_878():
  sample_input = textwrap.dedent("?????#.???##??.?. 1,1,1,7,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_879():
  sample_input = textwrap.dedent("?.??#?#??#?..?#??. 1,4,2,2,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_880():
  sample_input = textwrap.dedent("????????#????#??.?. 2,10").strip()

  assert solve(sample_input, 1) == 9


def test_sample_881():
  sample_input = textwrap.dedent("????##???#???.???? 5,3,3").strip()

  assert solve(sample_input, 1) == 12


def test_sample_882():
  sample_input = textwrap.dedent("#.#.?##??#?????#? 1,1,7,1,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_883():
  sample_input = textwrap.dedent("#?????##??????? 1,1,6,1").strip()

  assert solve(sample_input, 1) == 16


def test_sample_884():
  sample_input = textwrap.dedent("#.??#?.??..#.??#..?? 1,4,1,1,3,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_885():
  sample_input = textwrap.dedent("#???#?#??#.?##? 1,5,1,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_886():
  sample_input = textwrap.dedent("#.?##???#.?.??#. 1,6,1,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_887():
  sample_input = textwrap.dedent("???.?.???? 1,1,1").strip()

  assert solve(sample_input, 1) == 29


def test_sample_888():
  sample_input = textwrap.dedent("?#?#???.?? 4,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_889():
  sample_input = textwrap.dedent("###?##?..???##?? 6,2").strip()

  assert solve(sample_input, 1) == 1


def test_sample_890():
  sample_input = textwrap.dedent("?.#.?#??####???#?. 1,8,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_891():
  sample_input = textwrap.dedent("#??.????#??? 1,1,3,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_892():
  sample_input = textwrap.dedent("#?#??..#????#?? 1,1,1,1,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_893():
  sample_input = textwrap.dedent(".???#?#???# 2,5,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_894():
  sample_input = textwrap.dedent("?#?##???.???? 4,1,1").strip()

  assert solve(sample_input, 1) == 11


def test_sample_895():
  sample_input = textwrap.dedent("?#?.???##??#??????? 2,8,1,1").strip()

  assert solve(sample_input, 1) == 40


def test_sample_896():
  sample_input = textwrap.dedent("?????.???????.??##?? 2,1,6,3").strip()

  assert solve(sample_input, 1) == 12


def test_sample_897():
  sample_input = textwrap.dedent("..????.#?#?? 2,4").strip()

  assert solve(sample_input, 1) == 3


def test_sample_898():
  sample_input = textwrap.dedent(".?#???????#.??? 1,1,2,1,1").strip()

  assert solve(sample_input, 1) == 13


def test_sample_899():
  sample_input = textwrap.dedent("??#?..#?#??..????? 2,4,4").strip()

  assert solve(sample_input, 1) == 4


def test_sample_900():
  sample_input = textwrap.dedent("??.?.?..?? 2,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_901():
  sample_input = textwrap.dedent("#??#???##??.??#? 5,5,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_902():
  sample_input = textwrap.dedent("???#????.???? 5,1,1").strip()

  assert solve(sample_input, 1) == 24


def test_sample_903():
  sample_input = textwrap.dedent("#???.??#?##?#.#..? 2,1,1,6,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_904():
  sample_input = textwrap.dedent(".?#?##????????.? 1,3,2,1").strip()

  assert solve(sample_input, 1) == 11


def test_sample_905():
  sample_input = textwrap.dedent(".#?#??.?.? 4,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_906():
  sample_input = textwrap.dedent("??.???#?????????? 1,11").strip()

  assert solve(sample_input, 1) == 11


def test_sample_907():
  sample_input = textwrap.dedent(".###????###????. 3,6,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_908():
  sample_input = textwrap.dedent("??#????.?##? 4,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_909():
  sample_input = textwrap.dedent("???.?###???# 1,8").strip()

  assert solve(sample_input, 1) == 3


def test_sample_910():
  sample_input = textwrap.dedent("???.???.#???#?.? 1,1,5,1").strip()

  assert solve(sample_input, 1) == 11


def test_sample_911():
  sample_input = textwrap.dedent("??##????????#?? 5,2,3").strip()

  assert solve(sample_input, 1) == 18


def test_sample_912():
  sample_input = textwrap.dedent("#?#?#????#?##..#???? 1,1,9,1,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_913():
  sample_input = textwrap.dedent("#??.##???.??? 1,2,1,1").strip()

  assert solve(sample_input, 1) == 7


def test_sample_914():
  sample_input = textwrap.dedent("?..#?????. 1,3,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_915():
  sample_input = textwrap.dedent(".???#?#??##????#??? 12,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_916():
  sample_input = textwrap.dedent("#??????.??#? 7,3").strip()

  assert solve(sample_input, 1) == 2


def test_sample_917():
  sample_input = textwrap.dedent("??#.?#?.#????#?.# 2,1,2,3,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_918():
  sample_input = textwrap.dedent("?#?.?.???????? 2,7").strip()

  assert solve(sample_input, 1) == 4


def test_sample_919():
  sample_input = textwrap.dedent("??.??#?#?.????????? 1,4,9").strip()

  assert solve(sample_input, 1) == 5


def test_sample_920():
  sample_input = textwrap.dedent(".??.???##? 2,1,2").strip()

  assert solve(sample_input, 1) == 2


def test_sample_921():
  sample_input = textwrap.dedent(".??????#.?.?????. 1,1,1,1").strip()

  assert solve(sample_input, 1) == 99


def test_sample_922():
  sample_input = textwrap.dedent("???#.???#???#..? 1,1,8,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_923():
  sample_input = textwrap.dedent(".????#???? 1,1,1").strip()

  assert solve(sample_input, 1) == 11


def test_sample_924():
  sample_input = textwrap.dedent("?#.??.??????????#.? 1,1,2,5,1").strip()

  assert solve(sample_input, 1) == 17


def test_sample_925():
  sample_input = textwrap.dedent("?.?.???.?. 1,1").strip()

  assert solve(sample_input, 1) == 13


def test_sample_926():
  sample_input = textwrap.dedent("???.?.#???????#?#?#. 1,1,1,7,1,3").strip()

  assert solve(sample_input, 1) == 1


def test_sample_927():
  sample_input = textwrap.dedent("??.?????#??## 1,1,1,2").strip()

  assert solve(sample_input, 1) == 11


def test_sample_928():
  sample_input = textwrap.dedent(".????????? 3,2").strip()

  assert solve(sample_input, 1) == 10


def test_sample_929():
  sample_input = textwrap.dedent("#?????????#????#. 6,4,2").strip()

  assert solve(sample_input, 1) == 3


def test_sample_930():
  sample_input = textwrap.dedent("#??.?##???.??? 1,3,1,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_931():
  sample_input = textwrap.dedent("??.???##?#? 4,2").strip()

  assert solve(sample_input, 1) == 1


def test_sample_932():
  sample_input = textwrap.dedent("?#.?????.?.??#?.?. 1,2,1,1,4,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_933():
  sample_input = textwrap.dedent("?????..??.?? 1,1,1,1").strip()

  assert solve(sample_input, 1) == 28


def test_sample_934():
  sample_input = textwrap.dedent("#???#???#???? 2,1,5").strip()

  assert solve(sample_input, 1) == 3


def test_sample_935():
  sample_input = textwrap.dedent("?.???..?????.?? 3,5").strip()

  assert solve(sample_input, 1) == 1


def test_sample_936():
  sample_input = textwrap.dedent("??#..#?????????? 3,1,2,3").strip()

  assert solve(sample_input, 1) == 10


def test_sample_937():
  sample_input = textwrap.dedent("#?????###???..?#? 1,1,4,1,1").strip()

  assert solve(sample_input, 1) == 7


def test_sample_938():
  sample_input = textwrap.dedent("?##?#?.#?#? 5,4").strip()

  assert solve(sample_input, 1) == 2


def test_sample_939():
  sample_input = textwrap.dedent("?##???#??..#??#? 9,1,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_940():
  sample_input = textwrap.dedent("???#???##??????. 4,4").strip()

  assert solve(sample_input, 1) == 6


def test_sample_941():
  sample_input = textwrap.dedent("??#???#??#.???#? 3,4,1,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_942():
  sample_input = textwrap.dedent("?#?#??.?##?#??#?. 5,8").strip()

  assert solve(sample_input, 1) == 4


def test_sample_943():
  sample_input = textwrap.dedent("?.???.?#???.????.. 1,1,5,3").strip()

  assert solve(sample_input, 1) == 8


def test_sample_944():
  sample_input = textwrap.dedent(".???.?.?#??? 2,1,1,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_945():
  sample_input = textwrap.dedent("###?.????.?????? 3,1,1,1,1").strip()

  assert solve(sample_input, 1) == 46


def test_sample_946():
  sample_input = textwrap.dedent("????#??#???.?##???? 2,2,2,5").strip()

  assert solve(sample_input, 1) == 10


def test_sample_947():
  sample_input = textwrap.dedent("???????#.?.?#? 1,4,1,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_948():
  sample_input = textwrap.dedent("???????##?##?????#. 11,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_949():
  sample_input = textwrap.dedent(".???#.?#?????### 1,2,1,1,5").strip()

  assert solve(sample_input, 1) == 1


def test_sample_950():
  sample_input = textwrap.dedent("??????#????#..?? 8,1,1").strip()

  assert solve(sample_input, 1) == 7


def test_sample_951():
  sample_input = textwrap.dedent("#?????#?..???.#? 8,2,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_952():
  sample_input = textwrap.dedent("???#???##???? 1,3,2,2").strip()

  assert solve(sample_input, 1) == 6


def test_sample_953():
  sample_input = textwrap.dedent("???????#????.??? 5,1,1,1").strip()

  assert solve(sample_input, 1) == 31


def test_sample_954():
  sample_input = textwrap.dedent("?##..???#?? 3,5").strip()

  assert solve(sample_input, 1) == 2


def test_sample_955():
  sample_input = textwrap.dedent(".??????#????.? 7,1").strip()

  assert solve(sample_input, 1) == 11


def test_sample_956():
  sample_input = textwrap.dedent("?#?#?#???.??#??.?? 8,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_957():
  sample_input = textwrap.dedent("?????##???#? 5,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_958():
  sample_input = textwrap.dedent("??#?.??????#.?? 3,2,1,2,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_959():
  sample_input = textwrap.dedent(".#?????.???..???..?. 5,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_960():
  sample_input = textwrap.dedent("????#??????? 5,1").strip()

  assert solve(sample_input, 1) == 20


def test_sample_961():
  sample_input = textwrap.dedent("?.?#??#?###?# 1,10").strip()

  assert solve(sample_input, 1) == 1


def test_sample_962():
  sample_input = textwrap.dedent("????#?????.#??..? 5,3").strip()

  assert solve(sample_input, 1) == 5


def test_sample_963():
  sample_input = textwrap.dedent("???#?#??.? 2,1,1").strip()

  assert solve(sample_input, 1) == 3


def test_sample_964():
  sample_input = textwrap.dedent(".????.???#??? 3,1,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_965():
  sample_input = textwrap.dedent("#?#?#????????. 1,1,1,6").strip()

  assert solve(sample_input, 1) == 2


def test_sample_966():
  sample_input = textwrap.dedent("#.?##?#???##??#???? 1,5,2,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_967():
  sample_input = textwrap.dedent("????.##??#???#??#? 1,9,2").strip()

  assert solve(sample_input, 1) == 8


def test_sample_968():
  sample_input = textwrap.dedent("???#?#?#?#?.?# 8,2,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_969():
  sample_input = textwrap.dedent("??#???#????#????#?.? 9,5,2").strip()

  assert solve(sample_input, 1) == 1


def test_sample_970():
  sample_input = textwrap.dedent("#.????????#?. 1,1,1,2").strip()

  assert solve(sample_input, 1) == 25


def test_sample_971():
  sample_input = textwrap.dedent("?????..????.???#?. 5,2,3").strip()

  assert solve(sample_input, 1) == 6


def test_sample_972():
  sample_input = textwrap.dedent("????.??.?#.? 1,1,1,1").strip()

  assert solve(sample_input, 1) == 17


def test_sample_973():
  sample_input = textwrap.dedent("???#??#?.??? 4,1").strip()

  assert solve(sample_input, 1) == 5


def test_sample_974():
  sample_input = textwrap.dedent("???#???#?#??#?????? 1,1,4,2,1,1").strip()

  assert solve(sample_input, 1) == 27


def test_sample_975():
  sample_input = textwrap.dedent(".?##??..?. 2,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_976():
  sample_input = textwrap.dedent("?#####?????#??.??? 13,2").strip()

  assert solve(sample_input, 1) == 4


def test_sample_977():
  sample_input = textwrap.dedent("???.#??#?#??#??. 1,1,7").strip()

  assert solve(sample_input, 1) == 6


def test_sample_978():
  sample_input = textwrap.dedent(".???#?????#?#??.?#?# 12,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_979():
  sample_input = textwrap.dedent("?...#...##. 1,2").strip()

  assert solve(sample_input, 1) == 1


def test_sample_980():
  sample_input = textwrap.dedent("?.#????????.#?.?.?? 5,2,1,1,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_981():
  sample_input = textwrap.dedent("?#???..#??? 3,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_982():
  sample_input = textwrap.dedent("??.#?????????????#?? 1,1,6,1,1,1").strip()

  assert solve(sample_input, 1) == 32


def test_sample_983():
  sample_input = textwrap.dedent("?.?..??#?..????? 1,1,4,1,3").strip()

  assert solve(sample_input, 1) == 1


def test_sample_984():
  sample_input = textwrap.dedent("???.??.?#??.#.? 3,1,2,1,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_985():
  sample_input = textwrap.dedent("?#?##??????#??? 1,2,3,3,1").strip()

  assert solve(sample_input, 1) == 1


def test_sample_986():
  sample_input = textwrap.dedent("?#???.?.?#??.?#? 3,1,3,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_987():
  sample_input = textwrap.dedent("##??.???.? 3,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_988():
  sample_input = textwrap.dedent(".?.??????? 1,3").strip()

  assert solve(sample_input, 1) == 11


def test_sample_989():
  sample_input = textwrap.dedent("?????#?#??.?????## 1,1,1,1,1,6").strip()

  assert solve(sample_input, 1) == 3


def test_sample_990():
  sample_input = textwrap.dedent("..????.??..?? 1,2,1,1").strip()

  assert solve(sample_input, 1) == 4


def test_sample_991():
  sample_input = textwrap.dedent("??#??.??#????? 4,4,1").strip()

  assert solve(sample_input, 1) == 12


def test_sample_992():
  sample_input = textwrap.dedent("??.??.???#?? 1,3").strip()

  assert solve(sample_input, 1) == 15


def test_sample_993():
  sample_input = textwrap.dedent("?????#?#???#? 1,1,3,1").strip()

  assert solve(sample_input, 1) == 7


def test_sample_994():
  sample_input = textwrap.dedent("??.?..##???? 1,3").strip()

  assert solve(sample_input, 1) == 3


def test_sample_995():
  sample_input = textwrap.dedent(".?.???.#?? 1,1,1").strip()

  assert solve(sample_input, 1) == 8


def test_sample_996():
  sample_input = textwrap.dedent("?#????##??##???.#??# 4,2,6,1,1").strip()

  assert solve(sample_input, 1) == 2


def test_sample_997():
  sample_input = textwrap.dedent("??.#?#?.???##...???? 1,4,4,3").strip()

  assert solve(sample_input, 1) == 4


def test_sample_998():
  sample_input = textwrap.dedent("??.?#???.??? 4,1").strip()

  assert solve(sample_input, 1) == 6


def test_sample_999():
  sample_input = textwrap.dedent("?#???#?.#???? 6,1,1").strip()

  assert solve(sample_input, 1) == 6
