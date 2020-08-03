from math import log2, pow

"""
This puzzle corresponds to the Josephus problem (https://en.wikipedia.org/wiki/Josephus_problem).
Part 1 can be solved using k = 2. The elf receiving all the presents can be computed using 2 * i + 1 where
INPUT = 2 ^ m + i  (0 <= i < 2^m).
"""

INPUT = 3014603


def part1():
    m = int(log2(INPUT))
    i = INPUT - int(pow(2, m))
    return 2 * i + 1


result = part1()
print(f"Part 1: elf {result} gets all the presents.")

