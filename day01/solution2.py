count_first = {}
count_second = {}
with open("day01\input1.txt", "r") as fp:
    for line in fp:
        first, second = line.split("   ")
        first, second = int(first), int(second)
        count_first[first] = count_first.get(first, 0) + 1
        count_second[second] = count_second.get(second, 0) + 1
        # TODO: total be calculated in this loop?

total = 0
for first, num_instances_first in count_first.items():
    num_instances_second = count_second.get(first, 0)
    total += (first * num_instances_second) * num_instances_first
print(total)
