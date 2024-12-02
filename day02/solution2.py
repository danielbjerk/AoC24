num_safe = 0
with open("day02\input1.txt", "r") as fp:
    for report in fp:
        levels = [int(l) for l in report.split(" ")]
        increases = [levels[i] - levels[i - 1] for i in range(1, len(levels))]
        signs = [1 if l >= 0 else -1 for l in increases]
        if not sum(signs) >= len(increases) - 1 or not sum(signs) <= len(increases) + 1:
            continue
        func = (lambda i: 4 > i >= 1) if all(positive) else (lambda i: -4 < i <= -1)
        if not all([func(i) for i in increases]):
            continue
        num_safe += 1
print(num_safe)
