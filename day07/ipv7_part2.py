def is_letter(char):
    return "a" <= char <= "z"


def has_pattern(ip, pos):
    if ip[pos] != ip[pos + 2]:
        return False
    if ip[pos] == ip[pos + 1]:
        return False
    return is_letter(ip[pos]) and is_letter(ip[pos + 1])


def start_hypernet_sequence(ip, pos):
    return ip[pos] == "["


def end_hypernet_sequence(ip, pos):
    return ip[pos] == "]"


def find_abas_and_babs(ip):
    abas = []
    babs = []
    in_hypernet_sequence = False
    for pos in range(len(ip) - 3):
        if start_hypernet_sequence(ip, pos):
            in_hypernet_sequence = True
        elif end_hypernet_sequence(ip, pos):
            in_hypernet_sequence = False
        elif has_pattern(ip, pos):
            value = ip[pos:pos + 3]
            if in_hypernet_sequence:
                babs.append(value)
            else:
                abas.append(value)
    return abas, babs


def convert_aba_to_bab(aba):
    return aba[1] + aba[0] + aba[1]


def supports_ssl(ip):
    abas, babs = find_abas_and_babs(ip)
    matching = filter(lambda aba: convert_aba_to_bab(aba) in babs, abas)
    return len(list(matching)) > 0


def count_ssl(ips):
    ssl_ips = filter(lambda ip: supports_ssl(ip), ips)
    return len(list(ssl_ips))


def read_input():
    with open("input.txt", "r") as file:
        return file.readlines()


def main():
    ips = read_input()
    print("Number of IPs supporting SSL: {}".format(count_ssl(ips)))


if __name__ == '__main__':
    main()
