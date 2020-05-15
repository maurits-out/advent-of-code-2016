import re

SCREEN_WIDTH = 50
SCREEN_HEIGHT = 6


def read_input():
    with open("input.txt", "r") as file:
        return file.readlines()


def create_screen():
    return [[0] * SCREEN_WIDTH for _ in range(SCREEN_HEIGHT)]


def screen_value_to_char(value):
    if value == 0:
        return " "
    return "#"


def print_row(row):
    result = [screen_value_to_char(value) for value in row]
    print("".join(result))


def print_screen(screen):
    for row in screen:
        print_row(row)


def count_pixels_lit(screen):
    row_counts = [sum(row) for row in screen]
    return sum(row_counts)


def apply_rect(screen, width, height):
    for row in range(height):
        for column in range(width):
            screen[row][column] = 1


def apply_rotate_row(screen, row, num_pixels):
    for _ in range(num_pixels):
        last = screen[row][SCREEN_WIDTH - 1]
        for column in range(SCREEN_WIDTH - 1, 0, -1):
            screen[row][column] = screen[row][column - 1]
        screen[row][0] = last


def apply_rotate_column(screen, column, num_pixels):
    for _ in range(num_pixels):
        last = screen[SCREEN_HEIGHT - 1][column]
        for row in range(SCREEN_HEIGHT - 1, 0, -1):
            screen[row][column] = screen[row - 1][column]
        screen[0][column] = last


def apply_operation(screen, operation):
    match = re.match(r'rect (\d+)x(\d+)', operation)
    if match:
        apply_rect(screen, int(match.group(1)), int(match.group(2)))
        return
    match = re.match(r'rotate row y=(\d+) by (\d+)', operation)
    if match:
        apply_rotate_row(screen, int(match.group(1)), int(match.group(2)))
        return
    match = re.match(r'rotate column x=(\d+) by (\d+)', operation)
    apply_rotate_column(screen, int(match.group(1)), int(match.group(2)))


def apply_operations(operations):
    screen = create_screen()
    for operation in operations:
        apply_operation(screen, operation)
    return screen


def main():
    operations = read_input()
    screen = apply_operations(operations)
    print("Number of pixels lit: {}".format(count_pixels_lit(screen)))
    print("Display:")
    print_screen(screen)


if __name__ == '__main__':
    main()
