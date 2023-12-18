from dataclasses import dataclass
from uuid import uuid4

from commons.utils import get_matrix_from_input
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
    layout = get_matrix_from_input(input_data)
    starting_light_beam = LightBeam(Position(0, 0), "right", uuid4())

    handle_light_beam(starting_light_beam, layout)
    energized = set([(tracker[0], tracker[1]) for tracker in LIGHT_POSITIONS])
    draw_energized(energized, layout)

    return len(energized)


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=16)
    print(solve(input_data))
