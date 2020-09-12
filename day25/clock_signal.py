def evaluate(expression, registers):
    if "a" <= expression <= "d":
        return registers[expression]
    return int(expression)


def copy(registers, arguments):
    value = evaluate(arguments[0], registers)
    register = arguments[1]
    registers[register] = value


def update(registers, arguments, delta):
    register = arguments[0]
    registers[register] = registers[register] + delta


def jump(registers, arguments):
    value = evaluate(arguments[0], registers)
    if value == 0:
        return 1
    return evaluate(arguments[1], registers)


def out(registers, arguments):
    print(evaluate(arguments[0], registers))


def execute(instructions, registers):
    pc = 0
    while pc < len(instructions):
        components = instructions[pc].split()
        instruction, arguments = components[0], components[1:]
        if instruction == "cpy":
            copy(registers, arguments)
            pc += 1
        elif instruction == "inc":
            update(registers, arguments, 1)
            pc += 1
        elif instruction == "dec":
            update(registers, arguments, -1)
            pc += 1
        elif instruction == "out":
            out(registers, arguments)
            pc += 1
        else:
            pc += jump(registers, arguments)


def part1(instructions):
    registers = {"a": 192, "b": 0, "c": 0, "d": 0}
    execute(instructions, registers)


def read_instructions():
    with open("input.txt", "r") as file:
        return file.read().splitlines()


def main():
    instructions = read_instructions()
    # binary representation of 192 + 2538 is 0101010101010
    registers = {"a": 192, "b": 0, "c": 0, "d": 0}
    execute(instructions, registers)


if __name__ == '__main__':
    main()
