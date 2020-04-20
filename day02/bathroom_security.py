def bathroom_code(keypad, instructions, initial_location):
    current_location = initial_location
    code = ""
    for instruction in instructions:
        for char in instruction:
            next_location = get_next_location(char, *current_location)
            if is_valid(keypad, *next_location):
                current_location = next_location
        code = code + keypad[current_location[0]][current_location[1]]
    return code


def get_next_location(char, row, column):
    if char == "U":
        return row - 1, column
    if char == "L":
        return row, column - 1
    if char == "R":
        return row, column + 1
    return row + 1, column


def is_valid(keypad, row, column):
    return is_in_keypad(keypad, row, column) and is_button(keypad, row, column)


def is_button(keypad, row, column):
    return keypad[row][column] != " "


def is_in_keypad(keypad, row, column):
    return row in range(len(keypad)) and column in range(len(keypad[row]))


def part1(instructions):
    keypad = ["123", "456", "789"]
    initial_location = (1, 1)
    return bathroom_code(keypad, instructions, initial_location)


def part2(instructions):
    keypad = ["  1  ", " 234 ", "56789", " ABC ", "  D  "]
    initial_location = (2, 0)
    return bathroom_code(keypad, instructions, initial_location)


def main():
    instructions = []
    with open("input.txt", "r") as file:
        for line in file:
            instructions.append(line.strip())
    print("The bathroom code for part 1 is: {}".format(part1(instructions)))
    print("The bathroom code for part 2 is: {}".format(part2(instructions)))


if __name__ == '__main__':
    main()
