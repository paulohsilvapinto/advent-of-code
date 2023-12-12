from commons.utils import read_input

BASEMENT = -1
MOVEMENT_MAP = {
    "(": 1,
    ")": -1,
}


def solve(input_data):
    movements = input_data[0]

    floor = 0
    to_basement_position = None
    for movement_idx, movement in enumerate(movements):
        floor += MOVEMENT_MAP[movement]

        if floor == BASEMENT:
            to_basement_position = movement_idx + 1
            break

    return to_basement_position


if __name__ == "__main__":
    input_data = read_input(year=2015, day_number=1)
    print(solve(input_data))
