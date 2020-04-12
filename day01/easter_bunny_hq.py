from enum import Enum, auto

class Heading(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

def turn_left(heading):
    if heading == Heading.NORTH:
        return Heading.WEST
    if heading == Heading.WEST:
        return Heading.SOUTH
    if heading == Heading.SOUTH:
        return Heading.EAST
    return Heading.NORTH

def turn_right(heading):
    if heading == Heading.NORTH:
        return Heading.EAST
    if heading == Heading.EAST:
        return Heading.SOUTH
    if heading ==Heading.SOUTH:
        return Heading.WEST
    return Heading.NORTH

def turn(heading, direction):
    if direction == "R":
        return turn_right(heading)
    return turn_left(heading)

def get_direction(instruction):
    return instruction[0:1]

def get_number_of_blocks(instruction):
    return int(instruction[1:])

def get_delta_row(heading):
    if heading == Heading.NORTH:
        return -1
    if heading == Heading.SOUTH:
        return 1
    return 0

def get_delta_column(heading):
    if heading == Heading.WEST:
        return -1
    if heading == Heading.EAST:
        return 1
    return 0

def move_blocks(current_row, current_column, heading, number_of_blocks):
    delta_row = get_delta_row(heading)
    delta_column = get_delta_column(heading)
    locations = []
    for _ in range(number_of_blocks):
        current_row += delta_row
        current_column += delta_column
        locations.append((current_row, current_column))
    return locations

def follow_instructions(instructions):
    locations = [(0,0)]
    heading = Heading.NORTH
    for instruction in instructions:
        heading = turn(heading, get_direction(instruction))
        current_location = locations[-1]
        number_of_blocks = get_number_of_blocks(instruction)
        locations = locations + move_blocks(*current_location, heading, number_of_blocks)
    return locations

def distance(row, column):
    return abs(row) + abs(column)

def find_location_for_part1(locations):
    return locations[-1]

def find_location_for_part2(locations):
    visited = set()
    for location in locations:
        if location in visited:
            return location
        visited.add(location)
    return None

input = "R5, R4, R2, L3, R1, R1, L4, L5, R3, L1, L1, R4, L2, R1, R4, R4, L2, L2, R4, L4, R1, R3, L3, L1, L2, R1, R5, L5, L1, L1, R3, R5, L1, R4, L5, R5, R1, L185, R4, L1, R51, R3, L2, R78, R1, L4, R188, R1, L5, R5, R2, R3, L5, R3, R4, L1, R2, R2, L4, L4, L5, R5, R4, L4, R2, L5, R2, L1, L4, R4, L4, R2, L3, L4, R2, L3, R3, R2, L2, L3, R4, R3, R1, L4, L2, L5, R4, R4, L1, R1, L5, L1, R3, R1, L2, R1, R1, R3, L4, L1, L3, R2, R4, R2, L2, R1, L5, R3, L3, R3, L1, R4, L3, L3, R4, L2, L1, L3, R2, R3, L2, L1, R4, L3, L5, L2, L4, R1, L4, L4, R3, R5, L4, L1, L1, R4, L2, R5, R1, R1, R2, R1, R5, L1, L3, L5, R2"
locations = follow_instructions(input.split(", "))

distance_part1 = distance(*find_location_for_part1(locations))
print("Easter Bunny HQ is {} blocks away (part 1).".format(distance_part1))

distance_part2 = distance(*find_location_for_part2(locations))
print("Easter Bunny HQ is {} blocks away (part 2).".format(distance_part2))
