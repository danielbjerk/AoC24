def unsafe_indexes(levels):
    increases = [levels[i] - levels[i - 1] for i in range(1, len(levels))]
    same_signs = [i >= 0 for i in increases]
    if sum(same_signs) < len(same_signs) // 2:
        same_signs = [not s for s in same_signs]  # Decreasing
    small = [4 > abs(i) >= 1 for i in increases]
    crosscheck = [one and two for one, two in zip(same_signs, small)]
    unsafe_indexes = [idx for idx, safe in enumerate(crosscheck) if not safe]
    return unsafe_indexes


num_safe = 0
with open("day02\input1.txt", "r") as fp:
    for report in fp:
        levels = [int(l) for l in report.split(" ")]
        idxs = unsafe_indexes(levels)
        if len(idxs) > 1:
            continue
        elif len(idxs) == 0:
            num_safe += 1
            continue
        else:
            single_idxs = idxs[0]
            if single_idxs != 0:
                l1 = levels[:]
                l1.pop(single_idxs - 1)
                if len(unsafe_indexes(l1)) == 0:
                    num_safe += 1
                    continue
            if single_idxs != len(levels):
                l2 = levels[:]
                l2.pop(single_idxs + 1)
                if len(unsafe_indexes(l2)) == 0:
                    num_safe += 1
                    continue

        # ! If the single problem is of too high increase, since we at this point know that only one
        # level is a problem, then we can safely remove the level to the left of too high increase without
        # causing further magnitude errors.
        # TODO: But this can create increase errors?

        # Similarily, if the problem is a single wrong sign, we can safely remove the level to the right
        # of the increase, since we know the one to the right of that again at most is -1 + 3 away from the level
        # left of the increase, thus not creating more magnitude errors.
        # TODO: But this can create increase errors?


print(num_safe)
