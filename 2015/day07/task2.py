from commons.utils import read_input

WIRES = {}
OPERATIONS = {}


def convert_parameter(parameter):
    if parameter.isnumeric():
        return int(parameter)
    return calculate_wire(parameter)


def calculate_wire(wire):
    if wire in WIRES:
        return WIRES[wire]

    instruction = OPERATIONS[wire]

    if len(instruction) == 1:
        param = convert_parameter(OPERATIONS[wire][0])
        WIRES[wire] = param

    elif "NOT" in instruction:
        param = convert_parameter(OPERATIONS[wire][1])
        WIRES[wire] = param ^ 0xFFFF  # unsigned complement

    else:
        param1 = convert_parameter(OPERATIONS[wire][0])
        param2 = convert_parameter(OPERATIONS[wire][2])

        if "AND" in instruction:
            WIRES[wire] = param1 & param2

        elif "OR" in instruction:
            WIRES[wire] = param1 | param2

        elif "LSHIFT" in instruction:
            WIRES[wire] = param1 << param2

        elif "RSHIFT" in instruction:
            WIRES[wire] = param1 >> param2

    return WIRES[wire]


def parse_input(input_data):
    for line in input_data:
        instruction, to_wire = line.split(" -> ")
        instruction = instruction.split()

        OPERATIONS[to_wire] = instruction


def solve(input_data):
    parse_input(input_data)

    OPERATIONS["b"] = ["46065"]

    for wire in OPERATIONS:
        calculate_wire(wire)

    return WIRES["a"]


if __name__ == "__main__":
    input_data = read_input(year=2015, day_number=7)
    print(solve(input_data))
