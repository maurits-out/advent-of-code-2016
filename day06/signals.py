def find_character(messages, position, factor):
    char_count = {}
    for message in messages:
        current_char = message[position]
        char_count[current_char] = char_count.get(current_char, 0) + 1
    sorted_chars = sorted(char_count, key=lambda ch: factor * char_count[ch])
    return sorted_chars[0]


def reconstruct_correct_message(messages, factor):
    result = []
    for pos in range(0, 8):
        result.append(find_character(messages, pos, factor))
    return "".join(result)


def read_input():
    with open("input.txt", "r") as file:
        return file.readlines()


def main():
    messages = read_input()
    print("The message for part 1: {}".format(reconstruct_correct_message(messages, -1)))
    print("The message for part 2: {}".format(reconstruct_correct_message(messages, 1)))


if __name__ == '__main__':
    main()
