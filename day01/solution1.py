first = []
second = []
with open("day01\input1.txt", "r") as fp:
    for line in fp:
        line = line.split("   ")
        first.append(int(line[0]))
        second.append(int(line[1]))

first.sort()
second.sort()
total = 0
for one, two in zip(first, second):
    total += max(one - two, two - one)
print(total)
