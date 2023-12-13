import math


def change_making(denominations, target):
    cache = {}

    def sub_problem(i, t):
        if (i, t) in cache:
            return cache[(i, t)]

        val = denominations[i]

        if val > t:
            choice_take = math.inf
        elif val == t:
            choice_take = 1
        else:
            choice_take = 1 + sub_problem(i, t - val)

        if i == 0:
            choice_leave = math.inf
        else:
            choice_leave = sub_problem(i - 1, t)

        optimal = min(choice_take, choice_leave)
        cache[(i, t)] = optimal
        return optimal

    return sub_problem(len(denominations) - 1, target)


if __name__ == '__main__':
    print('change_making([1, 5, 12, 19], 16) = ' f'{change_making([1, 5, 12, 19], 16)}')
    print('change_making([25, 16, 5, 1], 33) = ' f'{change_making([25, 16, 5, 1], 33)}')
