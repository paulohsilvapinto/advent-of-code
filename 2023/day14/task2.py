import numpy as np

from commons.utils import get_matrix_from_input
from commons.utils import list_matrix_to_tuple
from commons.utils import read_input


def roll(matrix, roll_direction="left"):
    if roll_direction == "right":
        row_idxs = range(len(matrix) - 1, -1, -1)
        col_idxs = range(len(matrix[0]) - 2, -1, -1)
        comparer_offset = 1
    elif roll_direction == "left":
        row_idxs = range(0, len(matrix))
        col_idxs = range(1, len(matrix[0]))
        comparer_offset = -1
    else:
        raise ValueError("Roll direction must be either 'left' or 'right'.")

    moving = True
    while moving:
        moving = False
        for row_idx in row_idxs:
            for col_idx in col_idxs:
                if matrix[row_idx][col_idx] == "O" and matrix[row_idx][col_idx + comparer_offset] == ".":
                    matrix[row_idx][col_idx] = "."
                    matrix[row_idx][col_idx + comparer_offset] = "O"
                    moving = True

    return matrix


def roll_north(matrix):
    matrix = np.transpose(matrix)
    matrix = roll(matrix)
    return np.transpose(matrix)


def roll_west(matrix):
    return roll(matrix)


def roll_south(matrix):
    matrix = np.transpose(matrix)
    matrix = roll(matrix, roll_direction="right")
    return np.transpose(matrix)


def roll_east(matrix):
    return roll(matrix, roll_direction="right")


def roll_cycle(matrix):
    matrix = roll_north(matrix)
    matrix = roll_west(matrix)
    matrix = roll_south(matrix)
    return roll_east(matrix)


def roll_cycles(matrix, cycles):
    cache = []
    for i in range(cycles):
        # print(f"Cycle: {i}")
        matrix = roll_cycle(matrix)
        t_matrix = list_matrix_to_tuple(matrix)

        if t_matrix in cache:
            loop_start = cache.index(t_matrix)
            loop_end = i - 1
            # print(f"Loop found from cycle {loop_start} to {loop_end}")

            remaining_cycles = cycles - (i + 1)
            loop_length = loop_end - loop_start + 1

            return np.array(cache[(remaining_cycles % loop_length) + loop_start])
        else:
            cache.append(t_matrix)

    return matrix


def calculate_load(matrix):
    num_rows = len(matrix)
    load = 0

    for row_idx, row in enumerate(matrix):
        load += np.count_nonzero(row == "O") * (num_rows - row_idx)

    return load


def solve(input_data):
    platform = get_matrix_from_input(input_data)
    tilted_platform = roll_cycles(platform, cycles=1_000_000_000)
    return calculate_load(tilted_platform)


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=14)
    print(solve(input_data))
