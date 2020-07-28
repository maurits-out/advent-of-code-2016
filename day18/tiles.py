INPUT = ".^^..^...^..^^.^^^.^^^.^^^^^^.^.^^^^.^^.^^^^^^.^...^......^...^^^..^^^.....^^^^^^^^^....^^...^^^^..^"


def is_trap(left, center, right):
    return (left == "^" and center == "^" and right == ".") or\
           (left == "." and center == "^" and right == "^") or\
           (left == "^" and center == "." and right == ".") or\
           (left == "." and center == "." and right == "^")


def get_tile_in_next_row(extended_row, tile_index):
    if is_trap(extended_row[tile_index - 1], extended_row[tile_index], extended_row[tile_index + 1]):
        return "^"
    return "."


def construct_next_row(row):
    extended_row = ["."] + row + ["."]
    return [get_tile_in_next_row(extended_row, tile_index) for tile_index in range(1, len(extended_row) - 1)]


def count_safe_tiles_in_row(row):
    return len([ch for ch in row if ch == "."])


def count_safe_tiles(row_count):
    current = list(INPUT)
    num_safe_tiles = count_safe_tiles_in_row(current)
    for _ in range(row_count - 1):
        next_row = construct_next_row(current)
        num_safe_tiles += count_safe_tiles_in_row(next_row)
        current = next_row
    return num_safe_tiles


part1 = count_safe_tiles(40)
print(f"Number of safe tiles (part 1): {part1}")

part2 = count_safe_tiles(400000)
print(f"Number of safe tiles (part 2): {part2}")
