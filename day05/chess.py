import hashlib

PUZZLE_INPUT = "uqwqemis"
PASSWORD_LENGTH = 8
HASH_PREFIX = "00000"
PLACEHOLDER = "_"


def apply_md5_hash(puzzle_input, index):
    value_to_hash = puzzle_input + str(index)
    md5 = hashlib.md5(value_to_hash.encode())
    return md5.digest().hex()


def is_valid_hash(md5_hash):
    return md5_hash.startswith(HASH_PREFIX)


def is_password_incomplete(password_chars):
    for char in password_chars:
        if char == PLACEHOLDER:
            return True
    return False


def is_invalid_position_char(char):
    return not "0" <= char < "8"


def is_position_taken(password_chars, pos):
    return password_chars[pos] != PLACEHOLDER


def join_password_chars(password_chars):
    return "".join(password_chars)


def find_password_part1():
    index = -1
    password_chars = []
    while len(password_chars) < PASSWORD_LENGTH:
        index += 1
        md5_hash = apply_md5_hash(PUZZLE_INPUT, index)
        if is_valid_hash(md5_hash):
            password_chars.append(md5_hash[5])
    return join_password_chars(password_chars)


def find_password_part2():
    index = -1
    password_chars = list(PLACEHOLDER * 8)
    while is_password_incomplete(password_chars):
        index += 1
        md5_hash = apply_md5_hash(PUZZLE_INPUT, index)
        if is_valid_hash(md5_hash):
            if is_invalid_position_char(md5_hash[5]):
                continue
            pos = int(md5_hash[5])
            if is_position_taken(password_chars, pos):
                continue
            password_chars[pos] = md5_hash[6]
    return join_password_chars(password_chars)


def main():
    print("The password for part 1 is {}".format(find_password_part1()))
    print("The password for part 2 is {}".format(find_password_part2()))


if __name__ == '__main__':
    main()
