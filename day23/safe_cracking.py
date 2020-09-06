def is_register(expression):
    return "a" <= expression <= "d"


def evaluate(expression, registers):
    if is_register(expression):
        return registers[expression]
    return int(expression)


def copy(registers, arguments):
    value = evaluate(arguments[0], registers)
    expression = arguments[1]
    if is_register(expression):
        registers[expression] = value


def update(registers, arguments, delta):
    expression = arguments[0]
    if is_register(expression):
        registers[expression] += delta


def jump(registers, arguments):
    value = evaluate(arguments[0], registers)
    if value == 0:
        return 1
    return evaluate(arguments[1], registers)


def toggle_two_arg_command(command):
    if command == "jnz":
        return "cpy"
    return "jnz"


def toggle_one_arg_command(command):
    if command == "inc":
        return "dec"
    return "inc"


def toggle_instruction(instruction):
    components = instruction.split()
    command, arguments = components[0], components[1:]
    if len(arguments) == 1:
        command = toggle_one_arg_command(command)
    else:
        command = toggle_two_arg_command(command)
    return "{} {}".format(command, " ".join(arguments))


def toggle(registers, arguments, instructions, pc):
    value = evaluate(arguments[0], registers)
    index = pc + value
    if 0 <= index < len(instructions):
        instructions[index] = toggle_instruction(instructions[index])


def execute(instructions, registers):
    pc = 0
    while pc < len(instructions):
        if pc in [5, 21]:
            # to speed up for part 2
            registers['a'] += registers['c'] * registers['d']
            pc += 5
            continue
        components = instructions[pc].split()
        command, arguments = components[0], components[1:]
        if command == "cpy":
            copy(registers, arguments)
            pc += 1
        elif command == "inc":
            update(registers, arguments, 1)
            pc += 1
        elif command == "dec":
            update(registers, arguments, -1)
            pc += 1
        elif command == "tgl":
            toggle(registers, arguments, instructions, pc)
            pc += 1
        else:
            pc += jump(registers, arguments)


def read_instructions():
    with open("input.txt", "r") as file:
        return file.read().splitlines()


def run(a):
    instructions = read_instructions()
    registers = {'a': a, 'b': 0, 'c': 0, 'd': 0}
    execute(instructions, registers)
    return registers['a']


def main():
    print(f"Value of register 'a' (part 1): {run(7)}")
    print(f"Value of register 'a' (part 2): {run(12)}")


if __name__ == '__main__':
    main()
