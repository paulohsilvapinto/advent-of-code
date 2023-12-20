import re

from commons.utils import read_input


MOVE_MAP = {
    "R": [0, 1],
    "L": [0, -1],
    "U": [-1, 0],
    "D": [1, 0],
}


def move_drill(lagoon_edges, current_position, direction, amount):
    movement = MOVE_MAP[direction]

    for _ in range(amount):
        current_position = (current_position[0] + movement[0], current_position[1] + movement[1])
        lagoon_edges.append(current_position)

    return current_position


def normalize_points(points):
    min_height = min_width = 0

    for point in points:
        min_height = min(min_height, point[0])
        min_width = min(min_width, point[1])

    for idx, point in enumerate(points):
        adjusted_x = point[0] - min_height
        adjusted_y = point[1] - min_width

        points[idx] = (adjusted_x, adjusted_y)


def get_max_dimensions(lagoon_edges):
    max_height = max_width = 0

    for point in lagoon_edges:
        max_height = max(max_height, point[0])
        max_width = max(max_width, point[1])

    return max_height, max_width


def create_grid(lagoon_edges):
    grid = []
    max_height, max_width = get_max_dimensions(lagoon_edges)

    for _ in range(max_height + 1):
        grid.append(["." for _ in range(max_width + 1)])

    for point in lagoon_edges:
        grid[point[0]][point[1]] = "#"

    for row in grid:
        print("".join(row))

    return grid


def calculate_area(lagoon_edges):
    # read rows from top to bottom
    # ignore isolated points (non consecutive) as they do not increase or decrease the inside_points.
    area = 0
    inside_points = set()
    is_consecutive_points = False
    consecutive_points = None
    current_row = 0

    for idx, current_point in enumerate(lagoon_edges[:-1]):
        next_point = lagoon_edges[idx + 1]
        y = current_point[1]

        if current_point[0] != current_row:
            # changed row
            current_row = current_point[0]
            area += len(inside_points)
            # print(f"Row: {current_row} - Count: {len(inside_points)} - Area {area}")

        if current_point[0] == current_row:
            if current_point[1] == next_point[1] - 1:
                if not is_consecutive_points:
                    # create consecutive set
                    is_consecutive_points = True
                    consecutive_points = [y]
                else:
                    # add middle elements of the consecutive set
                    consecutive_points.append(y)
            elif is_consecutive_points:
                # add last element of the consecutive set
                consecutive_points.append(y)
                is_consecutive_points = False

        if not is_consecutive_points and consecutive_points:
            # handle consecutive points after set is completed
            if all([val in inside_points for val in consecutive_points]):
                # if true, then it is a closing edge
                if consecutive_points[0] - 1 in inside_points and consecutive_points[-1] + 1 in inside_points:
                    # closing downwards
                    for val in consecutive_points[1:-1]:
                        area += 1
                        inside_points.discard(val)
                elif consecutive_points[0] - 1 in inside_points:
                    # closing to the left
                    for val in consecutive_points[1:]:
                        area += 1
                        inside_points.discard(val)
                elif consecutive_points[-1] + 1 in inside_points:
                    # closing to the right
                    for val in consecutive_points[:-1]:
                        area += 1
                        inside_points.discard(val)
                else:
                    # closing upwards
                    for val in consecutive_points:
                        area += 1
                        inside_points.discard(val)
            else:
                # opening edges
                for val in consecutive_points:
                    inside_points.add(val)

            consecutive_points = None

    area += len(inside_points)

    return area


def solve(input_data):
    current_position = (0, 0)
    lagoon_edges = [current_position]

    for instruction in input_data:
        direction, amount = re.findall(r"^([RLUD]) (\d+) \(#.+\)$", instruction)[0]
        amount = int(amount)

        current_position = move_drill(lagoon_edges, current_position, direction, amount)

    # normalize_points(lagoon_edges)
    lagoon_edges.sort()
    # create_grid(lagoon_edges)

    return calculate_area(lagoon_edges)


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=18)
    print(solve(input_data))
