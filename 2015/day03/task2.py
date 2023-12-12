from commons.utils import read_input


def move(current_position, direction):
    DIRECTION_MAP = {
        "^": (current_position[0] - 1, current_position[1]),
        ">": (current_position[0], current_position[1] + 1),
        "v": (current_position[0] + 1, current_position[1]),
        "<": (current_position[0], current_position[1] - 1),
    }

    return DIRECTION_MAP[direction]


def turn_generator():
    turn_order = ["santa", "robo"]
    while True:
        for active in turn_order:
            yield active


def solve(input_data):
    directions = input_data[0]
    santa_position = robo_position = (0, 0)
    turn_order = turn_generator()

    visited_houses = set()
    visited_houses.add(santa_position)

    for direction in directions:
        if next(turn_order) == "santa":
            santa_position = move(santa_position, direction)
            visited_houses.add(santa_position)
        else:
            robo_position = move(robo_position, direction)
            visited_houses.add(robo_position)

    return len(visited_houses)


if __name__ == "__main__":
    input_data = read_input(year=2015, day_number=3)
    print(solve(input_data))
