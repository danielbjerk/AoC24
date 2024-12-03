import re

with open("day03/input1.txt") as fp:
    input_string = "".join(fp.readlines())

split = re.split("do(n't)?\(\)", input_string)
parts = [split[0]] + [
    split[i + 1] for i in range(1, len(split) - 1, 2) if split[i] != "n't"
]
combined_string = "".join(parts)
matches = [
    m[4:-1].split(",") for m in re.findall("mul\([0-9]+,[0-9]+\)", combined_string)
]
print(sum([int(first) * int(second) for [first, second] in matches]))
