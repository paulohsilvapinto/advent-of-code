import re

from commons.utils import read_input

AVAILABLE_CUBES = {"red": 12, "green": 13, "blue": 14}


games_doc = read_input(day_number=2)

game_id_regex = r"^game (\d+):"
cubes_distribution_regex = r"(\d+\s[a-z]+)+"
response = 0

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
        response += game_id

print(response)
