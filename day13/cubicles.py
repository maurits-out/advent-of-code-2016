PUZZLE_INPUT = 1358
START = (1, 1)
DESTINATION = (31, 39)
MAX_STEPS = 50


def is_open_space(x, y):
    n = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + PUZZLE_INPUT
    binary = "{0:b}".format(n)
    num_1s = sum(int(digit) for digit in binary)
    return num_1s % 2 == 0


def find_adjacent_open_spaces(x, y):
    adjacent_nodes = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
    return [node for node in adjacent_nodes if node >= (0, 0) and is_open_space(*node)]


def shortest_path():
    visited = set()
    queue = [(START, 0)]
    while len(queue) > 0:
        location, length = queue.pop(0)
        visited.add(location)
        if location == DESTINATION:
            return length
        for space in find_adjacent_open_spaces(*location):
            if space not in visited:
                queue.append((space, length + 1))
    return None


def count_locations():
    visited = set()
    queue = [(START, 1)]
    while len(queue) > 0:
        location, steps = queue.pop(0)
        visited.add(location)
        if steps == MAX_STEPS:
            continue
        for space in find_adjacent_open_spaces(*location):
            if space not in visited:
                queue.append((space, steps + 1))
    return len(visited)


def main():
    print("Fewest number of steps required (part 1): {}".format(shortest_path()))
    print("Number of locations (part 2): {}".format(count_locations()))


if __name__ == '__main__':
    main()
