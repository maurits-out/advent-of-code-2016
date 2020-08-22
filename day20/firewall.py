from collections import namedtuple
from operator import attrgetter

NUM_IP_ADDRESSES = 4294967296


def read_blocked_ip_ranges():
    ip_range_tuple = namedtuple('ip_range_tuple', 'low high')
    ip_ranges = []
    with open("input.txt", "r") as file:
        for line in file:
            parts = line.split("-")
            ip_range = ip_range_tuple(int(parts[0]), int(parts[1]))
            ip_ranges.append(ip_range)
    return ip_ranges


def sort_ip_ranges(ip_ranges):
    return sorted(ip_ranges, key=attrgetter('low'))


def find_lowest_valued_ip_available(blocked_ip_ranges):
    candidate = 0
    for ip_range in blocked_ip_ranges:
        if ip_range.low > candidate:
            break
        candidate = ip_range.high + 1
    return candidate


def count_allowed_addresses(blocked_ip_ranges):
    count = NUM_IP_ADDRESSES
    highest = -1
    for ip_range in blocked_ip_ranges:
        if ip_range.high > highest:
            if ip_range.low > highest:
                count -= ip_range.high - ip_range.low + 1
            else:
                count -= ip_range.high - highest
            highest = ip_range.high
    return count


def main():
    blocked_ip_ranges = sort_ip_ranges(read_blocked_ip_ranges())
    part1 = find_lowest_valued_ip_available(blocked_ip_ranges)
    print(f"Lowest-valued IP that is available (part 1): {part1}")
    part2 = count_allowed_addresses(blocked_ip_ranges)
    print(f"Number of allowed IP addresses (part 2): {part2}")


if __name__ == '__main__':
    main()
