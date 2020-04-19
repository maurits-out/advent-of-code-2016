def bathroom_code(keypad, instructions, initial_location):
    current_location = initial_location
    code = ""
    for instruction in instructions:
        for char in instruction:
            next_location = get_next_location(char, current_location)
            if is_valid(keypad, next_location):
                current_location = next_location
        code = code + keypad[current_location[0]][current_location[1]]
    return code

def get_next_location(char, location):
    if char == "U":
        return (location[0] - 1, location[1])
    if char == "L":
        return (location[0], location[1] - 1)
    if char == "R":
        return (location[0], location[1] + 1)
    return (location[0] + 1, location[1])

def is_valid(keypad, location):
    return location[0] in range(len(keypad)) and location[1] in range(len(keypad[location[0]])) and keypad[location[0]][location[1]] != " "

def part1(instructions):
    keypad = ["123", "456", "789"]
    return bathroom_code(keypad, instructions, (1, 1))

def part2(instructions):
    keypad = ["  1  ", " 234 ", "56789", " ABC ", "  D  "]
    return bathroom_code(keypad, instructions, (2, 0))

instructions = []
with open("day02/input.txt", "r") as file:
    for line in file:
        instructions.append(line.strip())
print("The bathroom code for part 1 is: {}".format(part1(instructions)))
print("The bathroom code for part 2 is: {}".format(part2(instructions)))