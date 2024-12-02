num_safe = 0
with open("day02\input1.txt", "r") as fp:
    for report in fp:
        levels = [int(l) for l in report.split(" ")]
        increases = [levels[i] - levels[i - 1] for i in range(1, len(levels))]
        same_signs = [i >= 0 for i in increases]
        if sum(same_signs) < len(same_signs) // 2:
            same_signs = [not s for s in same_signs]  # Decreasing
        small = [4 > abs(i) >= 1 for i in increases]
        crosscheck = [one and two for one, two in zip(same_signs, small)]

        num_unsafe = len(crosscheck) - sum(crosscheck)
        if num_unsafe > 1:
            continue
        num_safe += 1
        # ! If the single problem is of too high increase, since we at this point know that only one
        # level is a problem, then we can safely remove the level to the left of too high increase without
        # causing further magnitude errors.
        # TODO: But this can create increase errors?

        # Similarily, if the problem is a single wrong sign, we can safely remove the level to the right
        # of the increase, since we know the one to the right of that again at most is -1 + 3 away from the level
        # left of the increase, thus not creating more magnitude errors.
        # TODO: But this can create increase errors?


print(num_safe)
