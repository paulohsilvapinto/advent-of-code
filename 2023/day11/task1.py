from itertools import combinations

from commons.utils import read_input


def expand_universe(universe):
    row_expanded_universe = []

    for row in universe:
        row_expanded_universe.append(row)
        if all([space_element == "." for space_element in row]):
            row_expanded_universe.append(row)

    col_expanded_universe = []
    cols_to_expand = []
    for col_idx in range(len(row_expanded_universe[0])):
        if all([row[col_idx] == "." for row in row_expanded_universe]):
            cols_to_expand.append(col_idx)

    # print(cols_to_expand)

    for row in row_expanded_universe:
        row_col_expanded = ""
        start_position = 0
        for col_to_expand in cols_to_expand:
            row_col_expanded += row[start_position : col_to_expand + 1] + row[col_to_expand]
            # print(row_col_expanded)
            start_position = col_to_expand + 1

        # print(start_position)

        if start_position <= len(row) - 1:
            row_col_expanded += row[start_position:]

        col_expanded_universe.append(row_col_expanded)

    return col_expanded_universe


def identify_galaxies():
    galaxies_positions = []

    for row_idx, row in enumerate(universe):
        for col_idx, col in enumerate(row):
            if col == "#":
                galaxies_positions.append((row_idx, col_idx))

    return galaxies_positions


def calculate_distance(point_a, point_b):
    x_distance = abs(point_a[0] - point_b[0])
    y_distance = abs(point_a[1] - point_b[1])

    return x_distance + y_distance


universe = [row for row in read_input(year=2023, day_number=11)]
universe = expand_universe(universe)

# for row in universe:
#     print(row)
galaxies_positions = identify_galaxies()
# print(universe)
# print(galaxies_positions)
galaxies_pairs = list(combinations(galaxies_positions, 2))
distances = [calculate_distance(pair[0], pair[1]) for pair in galaxies_pairs]
total_distance = sum(distances)
print(total_distance)
