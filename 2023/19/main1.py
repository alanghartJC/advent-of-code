import re
from typing import Dict, List
from pprint import pprint, pformat


def solve(input_str: str):
  print("")
  workflows_section, ratings_section = input_str.split("\n\n")

  workflow_re = re.compile(r'([^{]+)\{(.*?)\}')

  workflows: Dict[str, list] = dict()
  workflows["A"] = ["A"]
  workflows["R"] = ["R"]

  for line in workflows_section.splitlines():
    match = workflow_re.search(line)
    workflow_name, workflow_contents = match.groups()
    wf_steps = workflow_contents.split(",")
    workflows[workflow_name] = wf_steps

  pprint(workflows)

  ratings: List[Dict[str, int]] = []
  for ratings_line in ratings_section.splitlines():
    ratings_line = ratings_line[1:-1]
    ratings_strs = ratings_line.split(",")
    ratings_dict = {}
    for rating in ratings_strs:
      k, v = rating.split("=")
      ratings_dict[k] = int(v)
    ratings.append(ratings_dict)

  pprint(ratings)

  output = 0
  accepted = []
  rejected = []

  comparers = {
    "<": lambda a,b: a < b,
    ">": lambda a,b: a > b,
  }
  for rating in ratings:
    cur_wf = workflows["in"]
    part_score = sum(rating.values())
    while cur_wf is not None:
      for rule in cur_wf:
        if rule == "A":
          accepted.append(rating)
          output += part_score
          cur_wf = None
          break
        if rule == "R":
          rejected.append(rating)
          cur_wf = None
          break
        if rule in workflows:
          cur_wf = workflows[rule]
          break
        cmp_str, dest = rule.split(":")
        attribute = cmp_str[0]
        comparer = comparers[cmp_str[1]]
        cmp_val = int(cmp_str[2:])
        if attribute in rating:
          if comparer(rating[attribute], cmp_val):
            cur_wf = workflows[dest]
            break

  print("Accepted:")
  pprint(accepted)

  print("Rejected:")
  pprint(rejected)

  return output





def main():
  with open("./input.txt", "r") as f:
    input_str = f.read()
  result = solve(input_str)
  print(result)

if __name__ == "__main__":
  main()
