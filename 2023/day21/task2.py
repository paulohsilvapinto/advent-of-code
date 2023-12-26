from collections import namedtuple
from math import ceil

from commons.utils import get_matrix_tuple_from_input
from commons.utils import read_input

Point = namedtuple("Point", ["x", "y"])


def get_starting_position(matrix, where="S"):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == where:
                return Point(i, j)


def translate_position(position, max_height, max_width):
    new_x = position.x % max_height
    new_y = position.y % max_width

    return Point(new_x, new_y)


def get_neighbours(matrix, current_position, max_height, max_width):
    neighbours = []
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbour = Point(current_position.x + i, current_position.y + j)
        remapped_point = translate_position(neighbour, max_height, max_width)

        if matrix[remapped_point.x][remapped_point.y] in [".", "S"]:
            neighbours.append(neighbour)

    return neighbours


def get_positions_after_n_steps(garden, max_height, max_width, steps):
    even_positions = set()
    odd_positions = set()
    current_pointer = next_pointer = even_positions

    unprocessed = [get_starting_position(garden)]

    for step in range(steps):
        if step % 2 == 0:
            current_pointer = even_positions
            next_pointer = odd_positions
        else:
            current_pointer = odd_positions
            next_pointer = even_positions

        for p in unprocessed:
            current_pointer.add(p)

        temp_unprocessed = []
        for position in unprocessed:
            temp_unprocessed += get_neighbours(garden, position, max_height, max_width)
        unprocessed = set([val for val in temp_unprocessed if val not in next_pointer])

    for val in unprocessed:
        next_pointer.add(val)
    return next_pointer


def get_quadratic_equation_coeffiecients(garden, max_height, max_width, steps=26_501_365):
    quadratic_sequence = [
        len(get_positions_after_n_steps(garden, max_height, max_width, ((steps % max_height) + i * max_height)))
        for i in range(5)
    ]
    first_diff_sequence = [quadratic_sequence[i] - quadratic_sequence[i - 1] for i in range(1, len(quadratic_sequence))]
    second_diff_sequence = [
        first_diff_sequence[i] - first_diff_sequence[i - 1] for i in range(1, len(first_diff_sequence))
    ]

    # Quadratic equation coefficients
    a = second_diff_sequence[0] // 2
    b = first_diff_sequence[0] - 3 * a
    c = quadratic_sequence[0] - b - a

    return a, b, c


def get_quadratic_nth_element(a, b, c, n):
    return a * n**2 + b * n + c


def solve(input_data):
    garden = get_matrix_tuple_from_input(input_data)
    max_height = len(garden)
    max_width = len(garden[0])

    steps = 26_501_365

    return get_quadratic_nth_element(
        *get_quadratic_equation_coeffiecients(garden, max_height, max_width),
        n=ceil(steps / max_height),
    )


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=21)
    print(solve(input_data))
