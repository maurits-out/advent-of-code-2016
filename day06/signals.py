LEAST_FREQUENT_FACTOR = 1
MOST_FREQUENT_FACTOR = -1
MESSAGE_LENGTH = 8


def find_character(messages, position, factor):
    char_count = {}
    for message in messages:
        current_char = message[position]
        char_count[current_char] = char_count.get(current_char, 0) + 1
    sorted_chars = sorted(char_count, key=lambda char: factor * char_count[char])
    return sorted_chars[0]


def reconstruct_correct_message(messages, factor):
    result = map(lambda pos: find_character(messages, pos, factor), range(MESSAGE_LENGTH))
    return "".join(result)


def read_input():
    with open("input.txt", "r") as file:
        return file.readlines()


def main():
    messages = read_input()
    print("The message for part 1: {}".format(reconstruct_correct_message(messages, MOST_FREQUENT_FACTOR)))
    print("The message for part 2: {}".format(reconstruct_correct_message(messages, LEAST_FREQUENT_FACTOR)))


if __name__ == '__main__':
    main()
