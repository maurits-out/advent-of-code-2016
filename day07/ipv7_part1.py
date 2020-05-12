ABBA_LENGTH = 4


def is_letter(char):
    return "a" <= char <= "z"


def has_abba(ip, pos):
    if ip[pos] != ip[pos + 3]:
        return False
    if ip[pos + 1] != ip[pos + 2]:
        return False
    if ip[pos] == ip[pos + 1]:
        return False
    return is_letter(ip[pos]) and is_letter(ip[pos + 1])


def start_hypernet_sequence(ip, pos):
    return ip[pos] == "["


def end_hypernet_sequence(ip, pos):
    return ip[pos] == "]"


def supports_tls(ip):
    abba_found = False
    in_hypernet_sequence = False
    for pos in range(len(ip) - ABBA_LENGTH):
        if start_hypernet_sequence(ip, pos):
            in_hypernet_sequence = True
        elif end_hypernet_sequence(ip, pos):
            in_hypernet_sequence = False
        elif has_abba(ip, pos):
            if in_hypernet_sequence:
                return False
            abba_found = True
    return abba_found


def count_tls(ips):
    tls_ips = filter(lambda ip: supports_tls(ip), ips)
    return len(list(tls_ips))


def read_input():
    with open("input.txt", "r") as file:
        return file.readlines()


def main():
    ips = read_input()
    print("Number of IPs supporting TLS: {}".format(count_tls(ips)))


if __name__ == '__main__':
    main()
