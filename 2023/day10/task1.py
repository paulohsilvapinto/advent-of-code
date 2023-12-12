from commons.utils import read_input


def get_maze():
    return [[char for char in line] for line in read_input(year=2023, day_number=10)]


def find_starting_coordinate(maze):
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
    if starting_coordinate[1] + 1 < len(maze[0]) and maze[starting_coordinate[0]][starting_coordinate[1] + 1] in [
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


def get_next_position(current_direction, current_coordinate):
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


maze = get_maze()
starting_coordinate = find_starting_coordinate(maze)

# print(maze)
# print(starting_coordinate)

current_coordinate, current_direction = find_path_after_start(maze, starting_coordinate)
steps = 1
while current_coordinate != starting_coordinate:
    current_pipe = maze[current_coordinate[0]][current_coordinate[1]]
    # print(current_pipe)
    current_coordinate, current_direction = get_next_position(current_direction, current_coordinate)
    steps += 1

farthest_from_start = steps // 2 if steps % 2 == 0 else steps // 2 + 1
print(farthest_from_start)
