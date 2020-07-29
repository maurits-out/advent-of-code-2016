INPUT = 3014603


class Elf:
    def __init__(self, position):
        self.position = position
        self.presents = 1
        self.next = None


def create_circle():
    first = Elf(1)
    current = first
    for position in range(2, INPUT + 1):
        current.next = Elf(position)
        current = current.next
    current.next = first
    return first


def part1():
    current = create_circle()
    while current.next != current:
        current.presents = current.presents + current.next.presents
        current.next = current.next.next
        current = current.next
    return current.position


result = part1()
print(f"Part 1: elf {result} gets all the presents.")

