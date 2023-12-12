import re

from commons.utils import read_input

AVAILABLE_CUBES = {"red": 12, "green": 13, "blue": 14}


def solve(input_data):
    games_doc = input_data

    game_id_regex = r"^game (\d+):"
    cubes_distribution_regex = r"(\d+\s[a-z]+)+"
    answer = 0

    for game_line in games_doc:
        game_line = game_line.lower()
        game_id = int(re.findall(game_id_regex, game_line)[0])
        cubes_distribution = re.findall(cubes_distribution_regex, game_line)
        is_game_possible = True
        for cube in cubes_distribution:
            cube_qty, cube_color = cube.split()
            if AVAILABLE_CUBES.get(cube_color, 0) < int(cube_qty):
                is_game_possible = False

        if is_game_possible:
            # print(game_id)
            answer += game_id

    return answer


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=2)
    print(solve(input_data))
