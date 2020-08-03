from math import log2, pow


def part1(puzzle_input):
    """
    The first part of the puzzle corresponds to the Josephus problem (https://en.wikipedia.org/wiki/Josephus_problem)
    with k = 2. The elf receiving all the presents can be computed using 2 * i + 1 where input = 2 ^ m + i
    (0 <= i < 2^m).
    """
    m = int(log2(puzzle_input))
    i = puzzle_input - int(pow(2, m))
    return 2 * i + 1


result = part1(3014603)
print(f"Part 1: elf {result} gets all the presents.")
