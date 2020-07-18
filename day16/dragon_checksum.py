PUZZLE_INPUT = "11100010111110100"


def apply_dragon_curve(a):
    return a + [0] + [1 - v for v in reversed(a)]


def fill_disk(disk_length):
    a = [ord(ch) - ord("1") + 1 for ch in PUZZLE_INPUT]
    while len(a) < disk_length:
        a = apply_dragon_curve(a)
    return a[:disk_length]


def generate_checksum(a):
    return [1 if a[i] == a[i + 1] else 0 for i in range(0, len(a), 2)]


def convert_to_string(a):
    return "".join(chr(ord("0") + v) for v in a)


def generate_checksum_of_even_length(disk_length):
    disk = fill_disk(disk_length)
    checksum = generate_checksum(disk)
    while len(checksum) % 2 == 0:
        checksum = generate_checksum(checksum)
    return convert_to_string(checksum)


print("Checksum of part 1: {}".format(generate_checksum_of_even_length(272)))
print("Checksum of part 2: {}".format(generate_checksum_of_even_length(35651584)))
