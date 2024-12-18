num_safe = 0
with open("day02\input1.txt", "r") as fp:
    for report in fp:
        levels = [int(l) for l in report.split(" ")]
        increases = [levels[i] - levels[i - 1] for i in range(1, len(levels))]
        positive = [l >= 0 for l in increases]
        if not all(positive) and any(positive):
            continue
        func = (lambda i: 4 > i >= 1) if all(positive) else (lambda i: -4 < i <= -1)
        if not all([func(i) for i in increases]):
            continue
        num_safe += 1
print(num_safe)
