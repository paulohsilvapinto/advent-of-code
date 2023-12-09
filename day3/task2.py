from collections import namedtuple

from commons.utils import read_input

response = 0
number_builder = ""
MatrixPosition = namedtuple("MatrixPosition", ["row", "column"])
NumberAdjacencies = namedtuple("NumberAdjacencies", ["number_value", "adjacent_positions"])
number_adjacencies_list = []
gears = []


def get_adjacent_points(engine_schematic_matrix, start_position, end_position):
    # print(start_position)
    # print(end_position)
    adjacent_positions = []
    for row_search_idx in range(
        max(0, start_position.row - 1),
        min(len(engine_schematic_matrix), end_position.row + 2),
    ):
        for col_search_idx in range(
            max(0, start_position.column - 1),
            min(len(engine_schematic_matrix[0]), end_position.column + 2),
        ):
            if start_position.row == row_search_idx and start_position.column <= col_search_idx <= end_position.column:
                pass
            else:
                adjacent_positions.append(MatrixPosition(row_search_idx, col_search_idx))
    # print(adjacent_positions)
    return adjacent_positions


engine_schematic = read_input(day_number=3)
engine_schematic_matrix = [[char for char in row] for row in engine_schematic]

for row_idx, row_val in enumerate(engine_schematic_matrix):
    for col_idx, col_val in enumerate(engine_schematic_matrix[row_idx]):
        if col_val.isnumeric():
            if not number_builder:
                start_position = MatrixPosition(row_idx, col_idx)
            number_builder += col_val
        else:
            if number_builder:
                end_position = MatrixPosition(row_idx, col_idx - 1)
                current_number = int(number_builder)
                number_builder = ""
                number_adjacencies_list.append(
                    NumberAdjacencies(
                        current_number,
                        get_adjacent_points(engine_schematic_matrix, start_position, end_position),
                    ),
                )
                # print(current_number, end=", ")

            if col_val == "*":
                gears.append(MatrixPosition(row_idx, col_idx))

for gear in gears:
    numbers_in_gear = []
    for number_adjacency in number_adjacencies_list:
        if gear in number_adjacency.adjacent_positions:
            numbers_in_gear.append(number_adjacency.number_value)

    if len(numbers_in_gear) == 2:
        # print(numbers_in_gear)
        response += numbers_in_gear[0] * numbers_in_gear[1]

print(response)
