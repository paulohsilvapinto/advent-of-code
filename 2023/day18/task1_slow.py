import re
from collections import deque

from commons.utils import read_input


MOVE_MAP = {
    "R": [0, 1],
    "L": [0, -1],
    "U": [-1, 0],
    "D": [1, 0],
}


def move_drill(lagoon_edges, movement_directions, current_position, direction, amount):
    movement = MOVE_MAP[direction]

    for _ in range(amount):
        current_position = (current_position[0] + movement[0], current_position[1] + movement[1])
        lagoon_edges.append(current_position)
        movement_directions.append(direction)

    return current_position


def normalize_edges(lagoon_edges):
    min_height = max_height = min_width = max_width = 0

    for point in lagoon_edges:
        min_height = min(min_height, point[0])
        max_height = max(max_height, point[0])
        min_width = min(min_width, point[1])
        max_width = max(max_width, point[1])

    if min_height >= 0 and min_width >= 0:
        return

    for idx, point in enumerate(lagoon_edges):
        if min_height != 0:
            adjusted_x = point[0] - min_height
        else:
            adjusted_x = point[0]

        if min_width != 0:
            adjusted_y = point[1] - min_width
        else:
            adjusted_y = point[1]

        lagoon_edges[idx] = (adjusted_x, adjusted_y)


def get_max_dimensions(lagoon_edges):
    max_height = max_width = 0

    for point in lagoon_edges:
        max_height = max(max_height, point[0])
        max_width = max(max_width, point[1])

    return max_height, max_width


def create_grid(max_height, max_width, lagoon_edges):
    grid = []

    for _ in range(max_height + 1):
        grid.append(["." for _ in range(max_width + 1)])

    for point in lagoon_edges:
        grid[point[0]][point[1]] = "#"

    return grid


def are_valid_coordinates(coordinates, max_row_id, max_col_id):
    if coordinates[0] >= 0 and coordinates[0] < max_row_id and coordinates[1] >= 0 and coordinates[1] < max_col_id:
        return True
    return False


def is_loop_clockwise(grid, movement_directions, lagoon_edges):
    for row_idx, row in enumerate(grid):
        if all([val == "." for val in row]):
            continue

        for col_idx, grid_val in enumerate(row):
            if grid_val != ".":
                if movement_directions[lagoon_edges.index((row_idx, col_idx))] in ["R", "U"]:
                    return True
                elif movement_directions[lagoon_edges.index((row_idx, col_idx))] in ["L", "D"]:
                    return False


def get_coordinate_to_check_inside(direction, coordinates, flag_loop_clockwise):
    coordinate_offset = 1 if flag_loop_clockwise else -1
    if direction == "U":
        return (coordinates[0], coordinates[1] + coordinate_offset)
    elif direction == "D":
        return (coordinates[0], coordinates[1] - coordinate_offset)
    elif direction == "L":
        return (coordinates[0] - coordinate_offset, coordinates[1])
    elif direction == "R":
        return (coordinates[0] + coordinate_offset, coordinates[1])


def mark_inside_grid_per_coordinate(
    grid,
    current_details,
    previous_details,
    flag_loop_clockwise,
    max_row_id,
    max_col_id,
):
    queue = deque([])
    visited = []

    current_coordinate, current_direction = current_details
    queue.append(get_coordinate_to_check_inside(current_direction, current_coordinate, flag_loop_clockwise))

    if previous_details:
        # handle corners
        previous_coordinate, previous_direction = previous_details
        if previous_direction != current_direction:
            queue.append(get_coordinate_to_check_inside(current_direction, previous_coordinate, flag_loop_clockwise))

    while queue:
        coordinates = queue.popleft()
        if not are_valid_coordinates(coordinates, max_row_id, max_col_id):
            continue
        if coordinates not in visited:
            if grid[coordinates[0]][coordinates[1]] == ".":
                grid[coordinates[0]][coordinates[1]] = "#"

                queue.extend(
                    [
                        (coordinates[0] - 1, coordinates[1]),
                        (coordinates[0] + 1, coordinates[1]),
                        (coordinates[0], coordinates[1] - 1),
                        (coordinates[0], coordinates[1] + 1),
                    ],
                )

            visited.append(coordinates)

    return grid


def mark_inside_elements(grid, lagoon_edges, movement_directions, max_row_id, max_col_id):
    previous_details = None
    flag_loop_clockwise = is_loop_clockwise(grid, movement_directions, lagoon_edges)
    for current_details in zip(lagoon_edges, movement_directions):
        if previous_details:
            grid = mark_inside_grid_per_coordinate(
                grid,
                current_details,
                previous_details,
                flag_loop_clockwise,
                max_row_id,
                max_col_id,
            )
        else:
            grid = mark_inside_grid_per_coordinate(
                grid,
                current_details,
                None,
                flag_loop_clockwise,
                max_row_id,
                max_col_id,
            )
        previous_details = current_details

    return grid


def count_inside_elements(grid):
    count_inside = 0
    for idx, row in enumerate(grid):
        for char in row:
            if char == "#":
                count_inside += 1
        print(f"Row: {idx} - Area: {count_inside}")
    return count_inside


def solve(input_data):
    current_position = (0, 0)
    lagoon_edges = []
    movement_directions = []

    for instruction in input_data:
        direction, amount = re.findall(r"^([RLUD]) (\d+) \(#.+\)$", instruction)[0]
        amount = int(amount)

        current_position = move_drill(lagoon_edges, movement_directions, current_position, direction, amount)

    normalize_edges(lagoon_edges)
    max_height, max_width = get_max_dimensions(lagoon_edges)
    grid = create_grid(max_height, max_width, lagoon_edges)
    grid = mark_inside_elements(grid, lagoon_edges, movement_directions, max_height + 1, max_width + 1)

    return count_inside_elements(grid)


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=18)
    print(solve(input_data))
