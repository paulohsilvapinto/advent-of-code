import heapq
from collections import defaultdict
from collections import namedtuple
from dataclasses import dataclass
from math import inf as INFINITY

from commons.utils import get_matrix_from_input
from commons.utils import read_input


DIRECTION_MAP = {
    "vertical": ["up", "down"],
    "horizontal": ["left", "right"],
}

DIRECTION_CHANGER = {
    "vertical": "horizontal",
    "horizontal": "vertical",
}

DIRECTION_OFFSET_MAP = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

Point = namedtuple("Point", ["x", "y"])


@dataclass
class Node:
    coordinates: Point
    from_direction: str
    to_direction: str

    def __hash__(self):
        return hash((self.coordinates, self.from_direction, self.to_direction))

    def __eq__(self, other):
        return (self.coordinates, self.to_direction) == (other.coordinates, other.to_direction)

    def __lt__(self, other):
        return (self.coordinates, self.to_direction) < (other.coordinates, other.to_direction)


def validate_position(point: Point, max_height, max_width):
    if 0 <= point.x < max_height and 0 <= point.y < max_width:
        return True
    return False


def get_starting_nodes(starting_coordinates: Point):
    starting_nodes = []

    starting_nodes.append(Node(starting_coordinates, "horizontal", "vertical"))
    starting_nodes.append(Node(starting_coordinates, "vertical", "horizontal"))

    return starting_nodes


def get_neighbours(city_blocks, max_height, max_width, from_node):
    original_direction = from_node.to_direction
    new_direction = DIRECTION_CHANGER[original_direction]

    # print(f"From: {from_node.coordinates} - {from_node.to_direction}")
    # print("To:", end=" ")

    for direction in DIRECTION_MAP[original_direction]:
        weight = 0
        offset = DIRECTION_OFFSET_MAP[direction]
        new_point = from_node.coordinates

        for _ in range(3):
            new_point = Point(new_point.x + offset[0], new_point.y + offset[1])
            if validate_position(new_point, max_height, max_width):
                weight += city_blocks[new_point.x][new_point.y]
                new_node = Node(new_point, original_direction, new_direction)
                yield ((new_node, weight))
                # print(f"{new_node.coordinates},", end=" ")
            else:
                break

    # print("\n")


def djikstra_alghoritm(city_blocks, max_height, max_width, starting_coordinates, destination_coordinates):
    nodes_visited = set()
    to_visit_queue = []
    distance_map = defaultdict(lambda: INFINITY)

    starting_nodes = get_starting_nodes(starting_coordinates)
    starting_weight = 0
    for node in starting_nodes:
        to_visit_queue.append((starting_weight, node))

    while to_visit_queue:
        distance, node = heapq.heappop(to_visit_queue)

        if node.coordinates == destination_coordinates:
            return distance

        if node in nodes_visited:
            continue
        else:
            nodes_visited.add(node)

            for neighbour_node, weight in get_neighbours(city_blocks, max_height, max_width, node):
                new_distance = distance + weight

                if new_distance < distance_map[neighbour_node]:
                    distance_map[neighbour_node] = new_distance
                    heapq.heappush(to_visit_queue, (new_distance, neighbour_node))

    print("Destination path is unreachable.")
    return None


def solve(input_data):
    city_blocks = [list(map(int, row)) for row in get_matrix_from_input(input_data)]

    max_height = len(city_blocks)
    max_width = len(city_blocks[0])

    starting_coordinates = Point(0, 0)
    destination_coordinates = Point(max_height - 1, max_width - 1)

    min_distance = djikstra_alghoritm(city_blocks, max_height, max_width, starting_coordinates, destination_coordinates)

    return min_distance


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=17)
    print(solve(input_data))
