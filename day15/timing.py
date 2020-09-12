class Disc:

    def __init__(self, positions, current):
        self.positions = positions
        self.current = current

    def tick(self):
        self.current = (self.current + 1) % self.positions

    def capsule_falls_through(self, t):
        return (self.current + t) % self.positions == 0


def create_puzzle_input_part1():
    return [
        Disc(13, 10),
        Disc(17, 15),
        Disc(19, 17),
        Disc(7, 1),
        Disc(5, 0),
        Disc(3, 1)
    ]


def create_puzzle_input_part2():
    part2 = create_puzzle_input_part1()
    part2.append(Disc(11, 0))
    return part2


def button_push_results_in_capture(discs):
    timer = 1
    for disc in discs:
        if not disc.capsule_falls_through(timer):
            return False
        timer += 1
    return True


def tick(discs):
    for disc in discs:
        disc.tick()


def find_first_time(discs):
    t = 0
    while not button_push_results_in_capture(discs):
        tick(discs)
        t += 1
    return t


def main():
    part1 = find_first_time(create_puzzle_input_part1())
    print(f"First time for part 1: {part1}")
    part2 = find_first_time(create_puzzle_input_part2())
    print(f"First time for part 2: {part2}")


if __name__ == '__main__':
    main()
