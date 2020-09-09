from collections import namedtuple
from itertools import permutations

NUM_MARKERS = 8

state_tuple = namedtuple('state_tuple', 'position steps')


def read_maze():
    with open('input.txt', 'r') as file:
        return file.read().splitlines()


def find_marker(maze, marker):
    return next((r, c) for r in range(len(maze)) for c in range(len(maze[r])) if maze[r][c] == marker)


def create_initial_state(maze, marker):
    position = find_marker(maze, marker)
    return state_tuple(position, 0)


def get_adjacent_positions(position):
    (row, column) = position
    return [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]


def is_allowed(maze, position):
    (row, column) = position
    return maze[row][column] != '#'


def is_end_state(maze, state, to_marker):
    (row, column) = state.position
    return maze[row][column] == to_marker


def find_shortest_path(maze, from_marker, to_marker):
    initial_state = create_initial_state(maze, from_marker)
    queue = [initial_state]
    visited = {initial_state.position}
    while True:
        state = queue.pop(0)
        if is_end_state(maze, state, to_marker):
            return state.steps
        for position in find_next_positions(maze, state, visited):
            visited.update([position])
            queue.append(state_tuple(position, state.steps + 1))


def find_next_positions(maze, state, visited):
    return [position for position in get_adjacent_positions(state.position) if
            position not in visited and is_allowed(maze, position)]


def create_distance_table(maze):
    distance_table = [[0] * NUM_MARKERS for _ in range(NUM_MARKERS)]
    for from_marker in range(NUM_MARKERS):
        for to_marker in range(from_marker + 1, NUM_MARKERS):
            steps = find_shortest_path(maze, str(from_marker), str(to_marker))
            distance_table[from_marker][to_marker] = steps
            distance_table[to_marker][from_marker] = steps
    return distance_table


def generate_routes():
    markers = [number for number in range(1, NUM_MARKERS)]
    return list(permutations(markers))


def count_steps_part1(route, distance_table):
    return distance_table[0][route[0]] + \
           sum(distance_table[route[i]][route[i + 1]] for i in range(NUM_MARKERS - 2))


def count_steps_part2(route, distance_table):
    return count_steps_part1(route, distance_table) + distance_table[route[NUM_MARKERS - 2]][0]


def count_minimum_number_of_steps(distance_table, routes, count_steps_function):
    steps = (count_steps_function(route, distance_table) for route in routes)
    return min(steps)


def main():
    maze = read_maze()
    distance_table = create_distance_table(maze)
    routes = generate_routes()
    part1 = count_minimum_number_of_steps(distance_table, routes, count_steps_part1)
    print(f"Minimum number of steps (part 1): {part1}")
    part2 = count_minimum_number_of_steps(distance_table, routes, count_steps_part2)
    print(f"Minimum number of steps (part 2): {part2}")


if __name__ == '__main__':
    main()
