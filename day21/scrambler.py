import re
from itertools import permutations


def swap_position(string, pos1, pos2):
    result = []
    for pos in range(0, len(string)):
        if pos == pos1:
            result.append(string[pos2])
        elif pos == pos2:
            result.append(string[pos1])
        else:
            result.append(string[pos])
    return "".join(result)


def swap_letter(string, letter1, letter2):
    result = []
    for letter in string:
        if letter == letter1:
            result.append(letter2)
        elif letter == letter2:
            result.append(letter1)
        else:
            result.append(letter)
    return "".join(result)


def reverse_positions(string, start, end):
    return string[:start] + string[start:end + 1][::-1] + string[end + 1:]


def rotate_left(string, steps):
    index = steps % len(string)
    return string[index:] + string[:index]


def rotate_right(string, steps):
    index = len(string) - (steps % len(string))
    return string[index:] + string[:index]


def rotate_based_on_position_of_letter(string, letter):
    index = string.index(letter)
    steps = 1 + index
    if index >= 4:
        steps += 1
    return rotate_right(string, steps)


def move(string, pos1, pos2):
    char = string[pos1]
    without_char = string[:pos1] + string[pos1 + 1:]
    return without_char[:pos2] + char + without_char[pos2:]


def read_operations_from_input():
    with open("input.txt", "r") as file:
        return file.readlines()


def apply(string, operation):
    match = re.match(r'rotate right (\d+) steps?', operation)
    if match:
        return rotate_right(string, int(match.group(1)))
    match = re.match(r'rotate left (\d+) steps?', operation)
    if match:
        return rotate_left(string, int(match.group(1)))
    match = re.match(r'swap letter (\w) with letter (\w)', operation)
    if match:
        return swap_letter(string, match.group(1), match.group(2))
    match = re.match(r'move position (\d+) to position (\d+)', operation)
    if match:
        return move(string, int(match.group(1)), int(match.group(2)))
    match = re.match(r'swap position (\d+) with position (\d+)', operation)
    if match:
        return swap_position(string, int(match.group(1)), int(match.group(2)))
    match = re.match(r'rotate based on position of letter (\w)', operation)
    if match:
        return rotate_based_on_position_of_letter(string, match.group(1))
    match = re.match(r'reverse positions (\d+) through (\d+)', operation)
    return reverse_positions(string, int(match.group(1)), int(match.group(2)))


def scramble(password, operations):
    scrambled = password
    for operation in operations:
        scrambled = apply(scrambled, operation)
    return scrambled


def unscramble(scrambled, operations):
    candidates = ("".join(perm) for perm in permutations(scrambled))
    return next(candidate for candidate in candidates if scramble(candidate, operations) == scrambled)


def main():
    operations = read_operations_from_input()

    scrambled = scramble("abcdefgh", operations)
    print(f"Scrambled password (part 1): {scrambled}")

    unscrambled = unscramble("fbgdceah", operations)
    print(f"Unscrambled version (part 2): {unscrambled}")


if __name__ == '__main__':
    main()
