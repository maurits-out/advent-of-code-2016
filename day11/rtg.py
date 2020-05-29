from itertools import accumulate


def min_steps(num_components_per_floor):
    # Moving n items one floor up takes at least 2 * (n - 1) - 1 steps. First move all components from floor 0 to
    # floor 1, then move all components from floor 1 to floor 2, etc.
    return sum(2 * (n - 1) - 1 for n in accumulate(num_components_per_floor))


def main():
    print("Minimum number of steps required (part 1): {}".format(min_steps([4, 5, 1])))
    print("Minimum number of steps required (part 2): {}".format(min_steps([8, 5, 1])))


if __name__ == '__main__':
    main()
