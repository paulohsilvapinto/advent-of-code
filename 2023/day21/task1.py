from collections import namedtuple

from commons.utils import get_matrix_from_input
from commons.utils import read_input

Point = namedtuple("Point", ["x", "y"])


def get_starting_position(matrix, where="S"):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == where:
                return Point(i, j)


def get_neighbours(matrix, current_position, max_height, max_width):
    neighbours = []
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbour = Point(current_position.x + i, current_position.y + j)
        # validate garden limits
        if 0 <= neighbour.x < max_height and 0 <= neighbour.y < max_width:
            # validate garden plots
            if matrix[neighbour.x][neighbour.y] in [".", "S"]:
                neighbours.append(neighbour)
    # print(f"{current_position=} - {neighbours=}")
    return neighbours


def get_positions_after_n_steps(garden, max_height, max_width, steps):
    current_positions = set()
    current_positions.add(get_starting_position(garden))

    for _ in range(steps):
        temp = []
        for position in current_positions:
            temp += get_neighbours(garden, position, max_height, max_width)
        current_positions = set(temp)

    return current_positions


def solve(input_data):
    garden = get_matrix_from_input(input_data)
    max_height = len(garden)
    max_width = len(garden[0])

    return len(get_positions_after_n_steps(garden, max_height, max_width, 64))


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=21)
    print(solve(input_data))
