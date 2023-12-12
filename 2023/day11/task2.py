from itertools import combinations

from commons.utils import read_input


def identify_expanded_universe_rows_cols(universe):
    rows_to_expand = []
    cols_to_expand = []

    for row_idx, row in enumerate(universe):
        if all([space_element == "." for space_element in row]):
            rows_to_expand.append(row_idx)

    for col_idx in range(len(universe[0])):
        if all([row[col_idx] == "." for row in universe]):
            cols_to_expand.append(col_idx)

    return rows_to_expand, cols_to_expand


def identify_galaxies(universe):
    galaxies_positions = []

    for row_idx, row in enumerate(universe):
        for col_idx, col in enumerate(row):
            if col == "#":
                galaxies_positions.append((row_idx, col_idx))

    return galaxies_positions


def update_galaxies_positions(galaxies_positions, rows_to_expand, cols_to_expand):
    for position_idx, position in enumerate(galaxies_positions):
        adjusted_row_position = position[0]
        adjusted_col_position = position[1]

        for row_to_expand in rows_to_expand:
            if position[0] > row_to_expand:
                adjusted_row_position += 1_000_000 - 1

        for col_to_expand in cols_to_expand:
            if position[1] > col_to_expand:
                adjusted_col_position += 1_000_000 - 1

        galaxies_positions[position_idx] = (adjusted_row_position, adjusted_col_position)

    return galaxies_positions


def calculate_distance(point_a, point_b):
    x_distance = abs(point_a[0] - point_b[0])
    y_distance = abs(point_a[1] - point_b[1])

    return x_distance + y_distance


def solve(input_data):
    universe = [row for row in input_data]
    rows_to_expand, cols_to_expand = identify_expanded_universe_rows_cols(universe)

    galaxies_positions = identify_galaxies(universe)
    galaxies_positions = update_galaxies_positions(galaxies_positions, rows_to_expand, cols_to_expand)

    galaxies_pairs = list(combinations(galaxies_positions, 2))
    distances = [calculate_distance(pair[0], pair[1]) for pair in galaxies_pairs]
    total_distance = sum(distances)

    return total_distance


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=11)
    print(solve(input_data))
