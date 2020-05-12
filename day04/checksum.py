CODE_POINT_A = ord("a")
CHECKSUM_LENGTH = 5
NUM_LETTERS = 26


def reconstruct_checksum(letters):
    count_by_letter = {}
    for letter in letters:
        count_by_letter[letter] = count_by_letter.get(letter, 0) + 1
    sorted_letters = sorted(count_by_letter, key=lambda l: (-count_by_letter[l], l))
    return "".join(sorted_letters)[:CHECKSUM_LENGTH]


def extract_supplied_checksum(last_segment):
    opening = last_segment.find("[")
    closing = last_segment.find("]")
    return last_segment[opening + 1:closing]


def is_real_room(line):
    segments = line.split("-")
    reconstructed_checksum = reconstruct_checksum("".join(segments[:-1]))
    supplied_checksum = extract_supplied_checksum(segments[-1])
    return supplied_checksum == reconstructed_checksum


def extract_sector_id(line):
    segments = line.split("-")
    last_segment = segments[-1]
    opening = last_segment.find("[")
    return int(last_segment[:opening])


def find_real_rooms(lines):
    real_rooms = filter(lambda line: is_real_room(line), lines)
    return list(real_rooms)


def sum_of_sector_ids(lines_of_real_rooms):
    sector_ids = map(lambda line: extract_sector_id(line), lines_of_real_rooms)
    return sum(sector_ids)


def decrypt_char(char, sector_id):
    n = (ord(char) - CODE_POINT_A + sector_id) % NUM_LETTERS
    return chr(CODE_POINT_A + n)


def decrypt_segment(segment, sector_id):
    result = map(lambda char: decrypt_char(char, sector_id), segment)
    return "".join(result)


def decrypt(segments, sector_id):
    result = map(lambda s: decrypt_segment(s, sector_id), segments)
    return " ".join(result)


def find_sector_id(lines_of_real_rooms):
    for line in lines_of_real_rooms:
        segments = line.split("-")
        sector_id = extract_sector_id(segments[-1])
        decrypted = decrypt(segments[:-1], sector_id)
        if decrypted == "northpole object storage":
            return sector_id
    return None


def read_lines():
    with open("input.txt", "r") as file:
        return file.readlines()


def main():
    lines_of_real_rooms = find_real_rooms(read_lines())
    print("Sum of sector IDs of real rooms: {}".format(sum_of_sector_ids(lines_of_real_rooms)))
    print("Sector ID of room containing North Pole objects: {}".format(find_sector_id(lines_of_real_rooms)))


if __name__ == '__main__':
    main()
