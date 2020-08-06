from collections import namedtuple


def read_ranges():
    ip_range_tuple = namedtuple('ip_range_tuple', 'low high')
    ip_ranges = []
    with open("input.txt", "r") as file:
        for line in file:
            parts = line.split("-")
            ip_ranges.append(ip_range_tuple(int(parts[0]), int(parts[1])))
    return ip_ranges


def find_ip_range_containing(ip, ip_ranges):
    return next((ip_range for ip_range in ip_ranges if ip_range.low <= ip <= ip_range.high), None)


def find_lowest_valued_ip_available(ip_ranges):
    candidate = 0
    while True:
        ip_range = find_ip_range_containing(candidate, ip_ranges)
        if ip_range is None:
            return candidate
        candidate = ip_range.high + 1


def main():
    ip_ranges = read_ranges()

    part1 = find_lowest_valued_ip_available(ip_ranges)
    print(f"Lowest-valued IP that is available (part 1): {part1}")


if __name__ == '__main__':
    main()
