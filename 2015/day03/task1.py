from commons.utils import read_input


def move(current_position, direction):
    DIRECTION_MAP = {
        "^": (current_position[0] - 1, current_position[1]),
        ">": (current_position[0], current_position[1] + 1),
        "v": (current_position[0] + 1, current_position[1]),
        "<": (current_position[0], current_position[1] - 1),
    }

    return DIRECTION_MAP[direction]


def solve(input_data):
    directions = input_data[0]
    current_position = (0, 0)
    visited_houses = set()

    visited_houses.add(current_position)

    for direction in directions:
        current_position = move(current_position, direction)
        visited_houses.add(current_position)

    return len(visited_houses)


if __name__ == "__main__":
    input_data = read_input(year=2015, day_number=3)
    print(solve(input_data))
