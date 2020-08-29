import re
from collections import namedtuple

GRID_WIDTH = 35
GRID_HEIGHT = 25


def read_input():
    with open("input.txt") as file:
        return file.readlines()


def create_grid(lines):
    grid = [[None] * GRID_HEIGHT for _ in range(GRID_WIDTH)]
    node_tuple = namedtuple('node_tuple', 'size used available')
    for line in lines:
        match = re.match(r'/dev/grid/node-x(\d+)-y(\d+) +(\d+)T +(\d+)T +(\d+)T +\d+%', line)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            node = node_tuple(int(match.group(3)), int(match.group(4)), int(match.group(5)))
            grid[x][y] = node
    return grid


def extract_all_nodes(grid):
    return [grid[x][y] for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)]


def count_viable_pairs(grid):
    nodes = extract_all_nodes(grid)
    pairs = [1 for node1 in nodes for node2 in nodes if node1 != node2 and 0 < node1.used <= node2.available]
    return len(pairs)


def main():
    lines = read_input()
    grid = create_grid(lines)
    viable_pairs_count = count_viable_pairs(grid)
    print(f'The number of viable pairs is (part 1): {viable_pairs_count}')


if __name__ == '__main__':
    main()
