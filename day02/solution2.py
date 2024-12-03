def is_safe(levels):
    increases = [levels[i] - levels[i - 1] for i in range(1, len(levels))]
    if all([4 > i >= 1 for i in increases]) or all([-4 < i <= -1 for i in increases]):
        return True
    return False


num_safe = 0
with open("day02\input1.txt", "r") as fp:
    for report in fp:
        levels = [int(l) for l in report.split(" ")]
        safe = is_safe(levels)
        if safe:
            num_safe += 1
            continue
        else:
            for i in range(len(levels)):
                levels_dampened = levels.copy()
                levels_dampened.pop(i)
                if is_safe(levels_dampened):
                    num_safe += 1
                    break

        # ! If the single problem is of too high increase, since we at this point know that only one
        # level is a problem, then we can safely remove the level to the left of too high increase without
        # causing further magnitude errors.
        # TODO: But this can create increase errors?

        # Similarily, if the problem is a single wrong sign, we can safely remove the level to the right
        # of the increase, since we know the one to the right of that again at most is -1 + 3 away from the level
        # left of the increase, thus not creating more magnitude errors.
        # TODO: But this can create increase errors?


print(num_safe)
