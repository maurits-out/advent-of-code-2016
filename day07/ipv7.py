ABBA_LENGTH = 4


def is_letter(char):
    return "a" <= char <= "z"


def has_abba(ip, index):
    if ip[index] != ip[index + 3]:
        return False
    if ip[index + 1] != ip[index + 2]:
        return False
    if ip[index] == ip[index + 1]:
        return False
    return is_letter(ip[index]) and is_letter(ip[index + 1])


def start_hypernet_sequence(ip, index):
    return ip[index] == "["


def end_hypernet_sequence(ip, index):
    return ip[index] == "]"


def supports_tls(ip):
    index = 0
    abba_found = False
    in_hypernet_sequence = False
    while index < len(ip) - ABBA_LENGTH:
        if start_hypernet_sequence(ip, index):
            in_hypernet_sequence = True
        elif end_hypernet_sequence(ip, index):
            in_hypernet_sequence = False
        elif has_abba(ip, index):
            if in_hypernet_sequence:
                break
            else:
                abba_found = True
        index += 1
    return abba_found and index == len(ip) - ABBA_LENGTH


def count_tls(ips):
    count = 0
    for ip in ips:
        if supports_tls(ip):
            count += 1
    return count


def read_input():
    with open("input.txt", "r") as file:
        return file.readlines()


def main():
    ips = read_input()
    print("Number of IPs supporting TLS: {}".format(count_tls(ips)))


if __name__ == '__main__':
    main()
