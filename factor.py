from math import sqrt
import time


def factors(n):
    factors_cand = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors_cand.add(x)
            factors_cand.add(n // x)

    return sorted(factors_cand)


def clean_up(result):
    result = list(result)
    result = result[1:len(result) - 1]
    if not result:
        return

    for i in range(0, len(result)):
        result[i] = format(result[i], ",")

    return result
