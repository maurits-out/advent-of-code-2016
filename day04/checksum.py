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


def is_real_room(segments):
    reconstructed_checksum = reconstruct_checksum("".join(segments[:-1]))
    supplied_checksum = extract_supplied_checksum(segments[-1])
    return supplied_checksum == reconstructed_checksum


def extract_sector_id(last_segment):
    opening = last_segment.find("[")
    return int(last_segment[:opening])


def find_real_rooms(lines):
    real_rooms = []
    for line in lines:
        segments = line.split("-")
        if is_real_room(segments):
            real_rooms.append(line)
    return real_rooms


def sum_of_sector_ids(lines_of_real_rooms):
    sum_of_ids = 0
    for line in lines_of_real_rooms:
        segments = line.split("-")
        sum_of_ids += extract_sector_id(segments[-1])
    return sum_of_ids


def decrypt_segment(segment, sector_id):
    result = ""
    for char in segment:
        n = (ord(char) - CODE_POINT_A + sector_id) % NUM_LETTERS
        result += chr(CODE_POINT_A + n)
    return result


def decrypt(segments, sector_id):
    result = []
    for segment in segments:
        result.append(decrypt_segment(segment, sector_id))
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
