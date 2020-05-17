def parse_marker(marker):
    separator = marker.find("x")
    return int(marker[:separator]), int(marker[separator + 1:])


def decompressed_length(contents, recurse):
    idx, length = 0, 0
    while idx < len(contents):
        if contents[idx] == "(":
            idx_closing = contents.find(")", idx)
            subsequence_length, repeat = parse_marker(contents[idx + 1:idx_closing])
            idx = idx_closing + subsequence_length + 1
            if recurse:
                length += repeat * decompressed_length(contents[idx_closing + 1:idx], recurse)
            else:
                length += repeat * subsequence_length
        else:
            length += 1
            idx += 1
    return length


def read_input():
    with open("input.txt", "r") as file:
        return file.read().strip()


def main():
    contents = read_input()
    length_part1 = decompressed_length(contents, False)
    print("Decompressed length of the file (part 1): {}".format(length_part1))
    length_part2 = decompressed_length(contents, True)
    print("Decompressed length of the file (part 2): {}".format(length_part2))


if __name__ == '__main__':
    main()
