import os
import re


def read_input(year, day_number):
    day = str(day_number).zfill(2)
    with open(os.path.join(f"{year}", f"day{day}", "input.txt"), "r", encoding="utf-8") as f:
        return f.read().splitlines()


def extract_numbers(text, type=int):
    return [type(val) for val in re.findall(r"(\d+)", text)]


def get_matrixes_from_input(input_data):
    matrixes = []

    matrix_builder = []
    for row in input_data:
        if row:
            matrix_builder.append([val for val in row])
        else:
            matrixes.append(matrix_builder)
            matrix_builder = []

    if matrix_builder:
        matrixes.append(matrix_builder)

    return matrixes


def get_matrix_from_input(input_data):
    matrix = []
    for row in input_data:
        matrix.append([val for val in row])

    return matrix


def get_matrix_tuple_from_input(input_data):
    return tuple([tuple([val for val in row]) for row in input_data])


def ares_matrixes_equal(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        return False
    return all(
        [
            all([matrix_a[row_idx][col_idx] == matrix_b[row_idx][col_idx]])
            for col_idx in range(len(matrix_a[0]))
            for row_idx in range(len(matrix_a))
        ],
    )


def list_matrix_to_tuple(matrix):
    return tuple([tuple([val for val in row]) for row in matrix])


def tuple_matrix_to_list(matrix):
    return list([list([val for val in row]) for row in matrix])
