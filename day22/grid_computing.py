import re
from collections import namedtuple

GRID_WIDTH = 35
GRID_HEIGHT = 25


def read_input():
    with open("input.txt") as file:
        return file.readlines()


def create_grid(lines):
    grid = [[None] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    node_tuple = namedtuple('node_tuple', 'used available')
    for line in lines:
        match = re.match(r'/dev/grid/node-x(\d+)-y(\d+) +\d+T +(\d+)T +(\d+)T +\d+%', line)
        if match:
            column = int(match.group(1))
            row = int(match.group(2))
            node = node_tuple(int(match.group(3)), int(match.group(4)))
            grid[row][column] = node
    return grid


def extract_all_nodes(grid):
    return [grid[row][column] for row in range(GRID_HEIGHT) for column in range(GRID_WIDTH)]


def count_viable_pairs(grid):
    nodes = extract_all_nodes(grid)
    pairs = [1 for node1 in nodes for node2 in nodes if node1 != node2 and 0 < node1.used <= node2.available]
    return len(pairs)


def node_to_char(node):
    if node.used > 100:
        return '#'
    elif node.used == 0:
        return '_'
    return '.'


def print_grid(grid):
    for row in range(GRID_HEIGHT):
        s = [node_to_char(node) for node in grid[row]]
        print(" ".join(s))


def main():
    lines = read_input()
    grid = create_grid(lines)
    print_grid(grid)
    count = count_viable_pairs(grid)
    print(f'The number of viable pairs is (part 1): {count}')


if __name__ == '__main__':
    main()
