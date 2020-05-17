def marker_start(char):
    return char == "("


def decompressed_length_part1(contents):
    idx, length, value, subsequence_length = 0, 0, 0, 0
    parsing_number = False
    while idx < len(contents):
        if parsing_number and "0" <= contents[idx] <= "9":
            value = value * 10 + int(contents[idx])
        elif parsing_number and contents[idx] == "x":
            subsequence_length = value
            value = 0
        elif parsing_number and contents[idx] == ")":
            length += subsequence_length * value
            idx += subsequence_length
            parsing_number = False
        elif contents[idx] == "(":
            value = 0
            parsing_number = True
        else:
            length += 1
        idx += 1
    return length


def read_input():
    with open("input.txt", "r") as file:
        return file.read().strip()


def main():
    contents = read_input()
    print("Decompressed length of the file: {}".format(decompressed_length_part1(contents)))


if __name__ == '__main__':
    main()
