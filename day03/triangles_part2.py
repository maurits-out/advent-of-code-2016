def read_lines():
    with open("input.txt", "r") as file:
        return file.readlines()


def count_valid_triangles(lines):
    count = 0
    for column_number in range(3):
        column = extract_column(lines, column_number)
        count += count_valid_triangles_in_column(column)
    return count


def extract_column(lines, column_number):
    column = []
    for line in lines:
        values = line.split()
        column.append(int(values[column_number]))
    return column


def count_valid_triangles_in_column(column):
    count = 0
    for row in range(0, len(column) - 2, 3):
        if is_valid_triangle(column[row], column[row + 1], column[row + 2]):
            count += 1
    return count


def is_valid_triangle(side1, side2, side3):
    return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1


def main():
    lines = read_lines()
    count = count_valid_triangles(lines)
    print("Number of possible triangles (part 2): {}".format(count))


if __name__ == '__main__':
    main()
