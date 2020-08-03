def create_circle(puzzle_input):
    circle = []
    for elf in range(puzzle_input):
        circle.append(elf + 1)
    circle[puzzle_input - 1] = 0
    return circle


def part2(puzzle_input):
    """
    For the second part we first create the circle of all elves as an array, where the i-th element contains the index
    of the elf next to elf i.Then we compute the index of the elf before the elf that sits across the first elf.
    The we repeatedly check if the number of remaining elves if even or odd. If odd then we delete the next elf or the
    elf next to the next elf until one elf remains.
    """
    circle = create_circle(puzzle_input)
    elf = int(puzzle_input / 2) - 1
    remaining = puzzle_input
    while remaining > 1:
        if remaining % 2 == 0:
            elf = circle[elf]
        circle[elf] = circle[circle[elf]]
        remaining -= 1
    return elf + 1


result = part2(3014603)
print(f"Part 2: elf {result} gets all the presents.")
