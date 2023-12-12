from collections import deque

from commons.utils import read_input


def get_maze():
    return [[char for char in line] for line in read_input(year=2023, day_number=10)]


def print_maze():
    for row in maze:
        print("".join(row))


def find_starting_coordinate():
    for row_idx, row in enumerate(maze):
        if "S" in row:
            return (row_idx, row.index("S"))


def move_down(current_coordinate):
    return (current_coordinate[0] + 1, current_coordinate[1]), "down"


def move_up(current_coordinate):
    return (current_coordinate[0] - 1, current_coordinate[1]), "up"


def move_left(current_coordinate):
    return (current_coordinate[0], current_coordinate[1] - 1), "left"


def move_right(current_coordinate):
    return (current_coordinate[0], current_coordinate[1] + 1), "right"


def find_path_after_start(maze, starting_coordinate):
    if starting_coordinate[1] + 1 < MAX_COL_ID and maze[starting_coordinate[0]][starting_coordinate[1] + 1] in [
        "-",
        "J",
        "7",
    ]:
        return move_right(starting_coordinate)
    elif starting_coordinate[1] - 1 >= 0 and maze[starting_coordinate[0]][starting_coordinate[1] - 1] in [
        "-",
        "L",
        "F",
    ]:
        return move_left(starting_coordinate)
    elif starting_coordinate[0] - 1 >= 0 and maze[starting_coordinate[0] - 1][starting_coordinate[1]] in [
        "|",
        "7",
        "F",
    ]:
        return move_up(starting_coordinate)
    else:
        return move_down(starting_coordinate)


def get_next_position(current_pipe, current_direction, current_coordinate):
    pipe_movement_map = {
        "|": {
            "up": move_up,
            "down": move_down,
        },
        "-": {
            "left": move_left,
            "right": move_right,
        },
        "L": {
            "down": move_right,
            "left": move_up,
        },
        "J": {
            "down": move_left,
            "right": move_up,
        },
        "7": {
            "right": move_down,
            "up": move_left,
        },
        "F": {
            "up": move_right,
            "left": move_down,
        },
    }

    return pipe_movement_map[current_pipe][current_direction](current_coordinate)


def find_maze_loop():
    starting_coordinate = find_starting_coordinate()
    current_coordinate, current_direction = find_path_after_start(maze, starting_coordinate)
    loop_coordinates = [starting_coordinate, current_coordinate]
    loop_directions = [current_direction, current_direction]

    while current_coordinate != starting_coordinate:
        current_pipe = maze[current_coordinate[0]][current_coordinate[1]]
        current_coordinate, current_direction = get_next_position(current_pipe, current_direction, current_coordinate)
        loop_coordinates.append(current_coordinate)
        loop_directions.append(current_direction)

    return loop_coordinates, loop_directions


def are_valid_coordinates(coordinates):
    if coordinates[0] >= 0 and coordinates[0] < MAX_ROW_ID and coordinates[1] >= 0 and coordinates[1] < MAX_COL_ID:
        return True
    return False


def remove_pipes_not_used():
    for row_idx in range(MAX_ROW_ID):
        for col_idx in range(MAX_COL_ID):
            if (row_idx, col_idx) not in loop_coordinates:
                maze[row_idx][col_idx] = "."


def is_loop_clockwise():
    for row_idx, row in enumerate(maze):
        if all([val == "." for val in row]):
            continue

        for col_idx, maze_val in enumerate(row):
            if maze_val != ".":
                if loop_directions[loop_coordinates.index((row_idx, col_idx))] == "right":
                    return True
                elif loop_directions[loop_coordinates.index((row_idx, col_idx))] == "left":
                    return False


def get_coordinate_to_check_inside(direction, coordinates):
    coordinate_offset = 1 if flag_loop_clockwise else -1
    if direction == "up":
        return (coordinates[0], coordinates[1] + coordinate_offset)
    elif direction == "down":
        return (coordinates[0], coordinates[1] - coordinate_offset)
    elif direction == "left":
        return (coordinates[0] - coordinate_offset, coordinates[1])
    elif direction == "right":
        return (coordinates[0] + coordinate_offset, coordinates[1])


def mark_inside_maze_per_coordinate(
    current_details,
    previous_details,
):
    queue = deque([])
    visited = []

    current_coordinate, current_direction = current_details
    queue.append(get_coordinate_to_check_inside(current_direction, current_coordinate))

    if previous_details:
        # handle corners
        previous_coordinate, previous_direction = previous_details
        if previous_direction != current_direction:
            queue.append(get_coordinate_to_check_inside(current_direction, previous_coordinate))

    while queue:
        coordinates = queue.popleft()
        if not are_valid_coordinates(coordinates):
            continue
        if coordinates not in visited:
            if maze[coordinates[0]][coordinates[1]] == ".":
                maze[coordinates[0]][coordinates[1]] = "I"

                queue.extend(
                    [
                        (coordinates[0] - 1, coordinates[1]),
                        (coordinates[0] + 1, coordinates[1]),
                        (coordinates[0], coordinates[1] - 1),
                        (coordinates[0], coordinates[1] + 1),
                    ],
                )

            visited.append(coordinates)


def mark_inside_elements():
    previous_details = None
    for current_details in zip(loop_coordinates, loop_directions):
        if previous_details:
            mark_inside_maze_per_coordinate(
                current_details,
                previous_details,
            )
        else:
            mark_inside_maze_per_coordinate(
                current_details,
                None,
            )
        previous_details = current_details


def count_inside_elements():
    count_inside = 0
    for row in maze:
        for char in row:
            if char == "I":
                count_inside += 1
    return count_inside


maze = get_maze()
MAX_ROW_ID = len(maze)
MAX_COL_ID = len(maze[0])

loop_coordinates, loop_directions = find_maze_loop()
remove_pipes_not_used()
flag_loop_clockwise = is_loop_clockwise()
mark_inside_elements()

# print_maze()
print(count_inside_elements())
