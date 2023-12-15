import numpy as np

from commons.utils import get_matrix_from_input
from commons.utils import read_input


def left_roll(matrix):
    moving = True
    while moving:
        moving = False
        for row_idx in range(len(matrix)):
            for col_idx, col in enumerate(matrix[row_idx]):
                if col_idx == 0:
                    continue
                elif col == "O" and matrix[row_idx][col_idx - 1] == ".":
                    matrix[row_idx][col_idx] = "."
                    matrix[row_idx][col_idx - 1] = "O"
                    moving = True

    return matrix


def calculate_load(matrix):
    num_rows = len(matrix)
    load = 0

    for row_idx, row in enumerate(matrix):
        load += np.count_nonzero(row == "O") * (num_rows - row_idx)

    return load


def roll_to_north(matrix):
    matrix = np.transpose(matrix)
    matrix = left_roll(matrix)
    return np.transpose(matrix)


def solve(input_data):
    platform = get_matrix_from_input(input_data)
    platform = roll_to_north(platform)

    return calculate_load(platform)


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=14)
    print(solve(input_data))
