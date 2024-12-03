import re

with open("day03/input1.txt") as fp:
    input_string = "".join(fp.readlines())

matches = [m[4:-1].split(",") for m in re.findall("mul\([0-9]+,[0-9]+\)", input_string)]
print(sum([int(first) * int(second) for [first, second] in matches]))
