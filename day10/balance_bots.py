import re


def read_lines_from_input():
    with open("input.txt", "r") as file:
        return file.readlines()


def create_initial_state(lines):
    state = {}
    for line in lines:
        match = re.match(r'value (\d+) goes to bot (\d+)', line)
        if match:
            chip = int(match.group(1))
            bot = int(match.group(2))
            assign_chip_to_bot(state, bot, chip)
    return state


def create_bot_instructions(lines):
    instructions = {}
    for line in lines:
        match = re.match(r'bot (\d+) gives (.+)', line)
        if match:
            bot = int(match.group(1))
            instructions[bot] = match.group(2)
    return instructions


def find_bot_for_part1(state):
    for bot in state:
        chips = state[bot]
        if 61 in chips and 17 in chips:
            return bot
    return None


def find_bot_with_two_chips(state):
    for bot in state:
        if len(state[bot]) == 2:
            return bot
    return None


def extract_low_and_high(chips):
    if chips[0] < chips[1]:
        return chips[0], chips[1]
    return chips[1], chips[0]


def assign_chip_to_bot(state, bot, chip):
    if bot in state:
        state[bot].append(chip)
    else:
        state[bot] = [chip]


def apply_instruction(state, bot, instruction, output):
    low, high = extract_low_and_high(state[bot])
    assign_low(instruction, low, output, state)
    assign_high(instruction, high, output, state)
    del state[bot]


def assign_high(instruction, high, output, state):
    match = re.match(r'.+high to bot (\d+)', instruction)
    if match:
        assign_chip_to_bot(state, int(match.group(1)), high)
        return
    match = re.match(r'.+high to output (\d+)', instruction)
    output_bin = int(match.group(1))
    output[output_bin] = high


def assign_low(instruction, low, output, state):
    match = re.match(r'low to bot (\d+)', instruction)
    if match:
        assign_chip_to_bot(state, int(match.group(1)), low)
        return
    match = re.match(r'low to output (\d+)', instruction)
    output_bin = int(match.group(1))
    output[output_bin] = low


def part1(state, instructions):
    result = None
    output = {}
    while result is None:
        bot = find_bot_with_two_chips(state)
        apply_instruction(state, bot, instructions[bot], output)
        result = find_bot_for_part1(state)
    return result


def part2(state, instructions):
    output = {}
    while True:
        bot = find_bot_with_two_chips(state)
        if bot is None:
            break
        apply_instruction(state, bot, instructions[bot], output)
    return output[0] * output[1] * output[2]


def main():
    lines = read_lines_from_input()
    instructions = create_bot_instructions(lines)
    state = create_initial_state(lines)
    print("Number of the bot (part 1): {}".format(part1(state, instructions)))
    print("Multiplying chip values in outputs 0, 1, and 2 (part 2): {}".format(part2(state, instructions)))


if __name__ == '__main__':
    main()
