import re

import numpy as np

from commons.utils import read_input


def turn_on(light, lights):
    lights[light[0]][light[1]] += 1
    return lights


def turn_off(light, lights):
    if lights[light[0]][light[1]] > 0:
        lights[light[0]][light[1]] -= 1
    return lights


def toggle(light, lights):
    lights[light[0]][light[1]] += 2
    return lights


COMMAND_MAP = {
    "turn on": turn_on,
    "turn off": turn_off,
    "toggle": toggle,
}


def solve(input_data):
    lights = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]

    for instruction in input_data:
        command, range_start, range_end = re.findall(r"(.+) (\d+\,\d+) through (\d+\,\d+)", instruction)[0]

        range_start = tuple(map(int, range_start.split(",")))
        range_end = tuple(map(int, range_end.split(",")))
        for row in range(range_start[0], range_end[0] + 1):
            for col in range(range_start[1], range_end[1] + 1):
                COMMAND_MAP[command](light=(row, col), lights=lights)

    lights = np.array(lights)
    return np.sum(lights)


if __name__ == "__main__":
    input_data = read_input(year=2015, day_number=6)
    print(solve(input_data))
