from collections import defaultdict
from collections import namedtuple
from math import prod

from commons.utils import extract_numbers
from commons.utils import read_input

Race = namedtuple("Race", ["time", "record_distance"])


def calculate_distance(time_holding, time_available):
    return time_holding * (time_available - time_holding)


races = read_input(year=2023, day_number=6)
races_times = extract_numbers(races[0])
races_distances = extract_numbers(races[1])
races = [Race(time, distance) for time, distance in zip(races_times, races_distances)]

ways_to_beat = defaultdict(int)
for race_id, race in enumerate(races):
    # print(race)
    for time_holding in range(0, race.time):
        if calculate_distance(time_holding, time_available=race.time) > race.record_distance:
            ways_to_beat[race_id] += 1

print(prod(ways_to_beat.values()))
