def is_valid_triangle(line):
    sides = line.split()
    side1 = int(sides[0])
    side2 = int(sides[1])
    side3 = int(sides[2])
    return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1


def main():
    count = 0
    with open("input.txt", "r") as file:
        for line in file:
            if is_valid_triangle(line):
                count += 1
    print("Number of possible triangles (part 1): {}".format(count))


if __name__ == '__main__':
    main()
