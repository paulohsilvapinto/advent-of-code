from dataclasses import dataclass
from functools import lru_cache
from uuid import uuid4

from commons.utils import get_matrix_tuple_from_input
from commons.utils import read_input


@dataclass
class Position:
    x: int
    y: int


@dataclass
class LightBeam:
    position: Position
    direction: str
    id: str

    def __hash__(self):
        return hash((self.position.x, self.position.y, self.direction))


def get_allowed_starting_positions(layout):
    starting_points = []
    for r in range(len(layout)):
        for c in range(len(layout[0])):
            if r == c and r == 0:
                starting_points.append(LightBeam(Position(r, c), "right", uuid4()))
                starting_points.append(LightBeam(Position(r, c), "down", uuid4()))
            elif r == 0 and c == len(layout[0]) - 1:
                starting_points.append(LightBeam(Position(r, c), "left", uuid4()))
                starting_points.append(LightBeam(Position(r, c), "down", uuid4()))
            elif r == len(layout) - 1 and c == 0:
                starting_points.append(LightBeam(Position(r, c), "right", uuid4()))
                starting_points.append(LightBeam(Position(r, c), "up", uuid4()))
            elif r == len(layout) - 1 and c == len(layout[0]) - 1:
                starting_points.append(LightBeam(Position(r, c), "left", uuid4()))
                starting_points.append(LightBeam(Position(r, c), "up", uuid4()))
            else:
                if r == 0:
                    starting_points.append(LightBeam(Position(r, c), "down", uuid4()))
                elif r == len(layout) - 1:
                    starting_points.append(LightBeam(Position(r, c), "up", uuid4()))
                if c == 0:
                    starting_points.append(LightBeam(Position(r, c), "right", uuid4()))
                elif c == len(layout) - 1:
                    starting_points.append(LightBeam(Position(r, c), "left", uuid4()))

    return starting_points


def validate_position(p: Position, layout):
    if 0 <= p.x < len(layout):
        if 0 <= p.y < len(layout[0]):
            return True
    return False


def move(light_beam: LightBeam, layout):
    if light_beam.direction == "up":
        light_beam.position.x -= 1
    elif light_beam.direction == "down":
        light_beam.position.x += 1
    elif light_beam.direction == "left":
        light_beam.position.y -= 1
    elif light_beam.direction == "right":
        light_beam.position.y += 1

    if validate_position(light_beam.position, layout):
        return light_beam
    return None


def handle_mirror(light_beam, mirror):
    direction = light_beam.direction

    if mirror == "\\":
        if direction == "right":
            light_beam.direction = "down"
        elif direction == "up":
            light_beam.direction = "left"
        elif direction == "left":
            light_beam.direction = "up"
        else:
            light_beam.direction = "right"

    elif mirror == "/":
        if direction == "right":
            light_beam.direction = "up"
        elif direction == "up":
            light_beam.direction = "right"
        elif direction == "left":
            light_beam.direction = "down"
        else:
            light_beam.direction = "left"

    return light_beam


def handle_splitter(light_beam, splitter, layout):
    if light_beam.direction in ["left", "right"]:
        if splitter == "-":
            return light_beam
        elif splitter == "|":
            handle_light_beam(LightBeam(Position(light_beam.position.x, light_beam.position.y), "up", uuid4()), layout)
            handle_light_beam(
                LightBeam(Position(light_beam.position.x, light_beam.position.y), "down", uuid4()),
                layout,
            )
            return None

    elif light_beam.direction in ["up", "down"]:
        if splitter == "-":
            handle_light_beam(
                LightBeam(Position(light_beam.position.x, light_beam.position.y), "left", uuid4()),
                layout,
            )
            handle_light_beam(
                LightBeam(Position(light_beam.position.x, light_beam.position.y), "right", uuid4()),
                layout,
            )
            return None
        elif splitter == "|":
            return light_beam


@lru_cache(maxsize=512)
def handle_light_beam(light_beam, layout):
    while True:
        if light_beam:
            obstacle = layout[light_beam.position.x][light_beam.position.y]
            if obstacle in MIRRORS:
                light_beam = handle_mirror(light_beam, obstacle)
            elif obstacle in SPLITTERS:
                light_beam = handle_splitter(light_beam, obstacle, layout)

        if light_beam:
            light_tracker = (light_beam.position.x, light_beam.position.y, light_beam.direction)
            if light_tracker in LIGHT_POSITIONS:
                light_beam = None
            else:
                LIGHT_POSITIONS.append(light_tracker)
                light_beam = move(light_beam, layout)
        else:
            return


def draw_energized(energized, layout):
    energized_matrix = [["." for _ in layout[0]] for _ in layout]
    for tracker in energized:
        energized_matrix[tracker[0]][tracker[1]] = "#"

    for row in energized_matrix:
        print("".join(row))


MIRRORS = ["/", "\\"]
SPLITTERS = ["-", "|"]
LIGHT_POSITIONS = []


def solve(input_data):
    global LIGHT_POSITIONS
    layout = get_matrix_tuple_from_input(input_data)
    max_energized = 0

    starting_points = get_allowed_starting_positions(layout)
    for idx, starting_light_beam in enumerate(starting_points):
        if idx % 25 == 0 or idx == 0:
            print(f"Remaining points to test: {len(starting_points) - idx}")
        handle_light_beam(starting_light_beam, layout)
        energized = set([(tracker[0], tracker[1]) for tracker in LIGHT_POSITIONS])
        # draw_energized(energized, layout)
        max_energized = max(max_energized, len(energized))
        LIGHT_POSITIONS = []

    return max_energized


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=16)
    print(solve(input_data))
