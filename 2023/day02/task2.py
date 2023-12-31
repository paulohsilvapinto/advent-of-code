import re
from collections import defaultdict

from commons.utils import read_input


def solve(input_data):
    games_doc = input_data
    cubes_distribution_regex = r"(\d+\s[a-z]+)+"
    response = 0

    for game_line in games_doc:
        cubes_distribution = re.findall(cubes_distribution_regex, game_line.lower())
        min_cubes = defaultdict(int)
        for cube in cubes_distribution:
            cube_qty, cube_color = cube.split()
            min_cubes[cube_color] = max(min_cubes[cube_color], int(cube_qty))

        response += min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]

    return response


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=2)
    print(solve(input_data))
