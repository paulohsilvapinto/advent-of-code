from collections import namedtuple

from commons.utils import read_input


def check_is_engine_part(engine_schematic_matrix, number_start_position, number_end_position):
    for row_search_idx in range(
        max(0, number_start_position.row - 1),
        min(len(engine_schematic_matrix), number_end_position.row + 2),
    ):
        for col_search_idx in range(
            max(0, number_start_position.column - 1),
            min(len(engine_schematic_matrix[0]), number_end_position.column + 2),
        ):
            schematic_char = engine_schematic_matrix[row_search_idx][col_search_idx]
            if (
                number_start_position.row == row_search_idx
                and number_start_position.column <= col_search_idx <= number_end_position.column
            ):
                pass
            else:
                if schematic_char not in ["."] and not schematic_char.isnumeric():
                    # print(f"char {repr(schematic_char)} on {row_search_idx}, {col_search_idx}")
                    return True
    return False


engine_schematic = read_input(year=2023, day_number=3)
engine_schematic_matrix = [[char for char in row] for row in engine_schematic]

MatrixPosition = namedtuple("MatrixPosition", ["row", "column"])
response = 0
number_builder = ""

for row_idx, row_val in enumerate(engine_schematic_matrix):
    for col_idx, col_val in enumerate(engine_schematic_matrix[row_idx]):
        if col_val.isnumeric():
            if not number_builder:
                start_position = MatrixPosition(row_idx, col_idx)
            number_builder += col_val

        if not col_val.isnumeric() or col_idx == len(engine_schematic_matrix[row_idx]) - 1:
            if number_builder:
                end_position = MatrixPosition(row_idx, col_idx - 1)
                current_number = int(number_builder)
                number_builder = ""

                # print(f"searching for {current_number} start_position {start_position}, end_position {end_position}, from row {max(0, start_position[0] - 1)} to row {min(len(engine_schematic_matrix), end_position[0] + 2)}, from col {max(0, start_position[1] - 1)} to col {min(len(engine_schematic_matrix[0]), end_position[1] + 2)}")
                if check_is_engine_part(engine_schematic_matrix, start_position, end_position):
                    # print(current_number)
                    response += current_number

print(response)
