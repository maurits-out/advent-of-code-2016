import hashlib

PUZZLE_INPUT = "ihaygndm"


def create_md5_hash(index):
    value_to_hash = PUZZLE_INPUT + str(index)
    md5 = hashlib.md5(value_to_hash.encode())
    return md5.digest().hex()


def find_first_character_in_row_of_three(md5):
    for i in range(len(md5) - 2):
        current = md5[i]
        if current == md5[i + 1] and current == md5[i + 2]:
            return current
    return None


def contains_character_five_times_in_a_row(md5, character):
    return character * 5 in md5


def init_md5_cache():
    md5_cache = {}
    for index in range(1000):
        md5_cache[index] = create_md5_hash(index)
    return md5_cache


def is_key(index, md5_cache):
    character = find_first_character_in_row_of_three(md5_cache[index])
    if character is None:
        return False
    for i in range(index, index + 1000):
        if contains_character_five_times_in_a_row(md5_cache[i + 1], character):
            return True
    return False


def find_index_of_64th_key():
    index = -1
    num_keys_found = 0
    md5_cache = init_md5_cache()
    while num_keys_found < 64:
        index += 1
        md5_cache[index + 1000] = create_md5_hash(index + 1000)
        if is_key(index, md5_cache):
            num_keys_found += 1
        del md5_cache[index]
    return index


def main():
    print("Index of 64th key is: {}".format(find_index_of_64th_key()))


if __name__ == '__main__':
    main()