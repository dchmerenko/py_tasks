#!/usr/bin/env python3

# Calculating armstrong numbers list.
#
# Armstrong number example:
#
#   1**3 + 5**3 + 3**3 == 153
#   where power 3 is length of a number

import time
import sys
from functools import lru_cache


def pow_with_no_cache(base, exp):
    return pow(base, exp)


cache = {}

def pow_with_cache_manual(base, exp):
    if (base, exp) in cache:
        return cache[(base, exp)]
    result = pow(base, exp)
    cache[(base, exp)] = result
    return result


@lru_cache
def pow_with_cache(base, exp):
    return pow(base, exp)


def armstrong(digits, exp, pow_function):
    return sum(pow_function(digit, exp) for digit in digits)


def run(pow_function):
    start_time = time.time()

    max_n = 1_000

    if len(sys.argv) > 1:
        max_n = int(sys.argv[1])

    armstrong_numbers = []
    for n in range(max_n):
        digits = [int(n) for n in str(n)]
        exp = len(str(n))
        candidate = armstrong(digits, exp, pow_function)
        if candidate == n:
            armstrong_numbers.append(candidate)

    total_time = time.time() - start_time

    print(f"\nPow function: {pow_function.__name__}\n")
    print(armstrong_numbers)
    print(f"Execution time: {total_time}")


def main():
    print("\nCalculating armstrong numbers list.")

    for pow_function in [pow_with_no_cache, pow_with_cache_manual, pow_with_cache]:
        run(pow_function)

    print(pow_with_cache.cache_info())


if __name__ == '__main__':
    main()

