from math import floor

from commons.utils import extract_numbers
from commons.utils import read_input


def calculate_distance(time_holding, time_available):
    return time_holding * (time_available - time_holding)


def get_list_middle_index(input_list):
    if len(input_list) % 2 == 0:
        return floor(len(input_list) // 2)
    else:
        return len(input_list) // 2


def find_min_time_win(time_range, race_time, record_distance):
    if len(time_range) == 1:
        return time_range[0]

    elif len(time_range) == 2:
        if calculate_distance(time_range[0], race_time) > record_distance:
            return time_range[0]
        else:
            return time_range[1]

    middle_idx = get_list_middle_index(time_range)
    if calculate_distance(time_range[middle_idx], race_time) > record_distance:
        return find_min_time_win(time_range[0 : (middle_idx + 1)], race_time, record_distance)
    else:
        return find_min_time_win(time_range[(middle_idx + 1) :], race_time, record_distance)


def find_max_time_win(time_range, race_time, record_distance):
    if len(time_range) == 1:
        return time_range[0]
    elif len(time_range) == 2:
        if calculate_distance(time_range[1], race_time) > record_distance:
            return time_range[1]
        else:
            return time_range[0]

    middle_idx = get_list_middle_index(time_range)
    if calculate_distance(time_range[middle_idx], race_time) > record_distance:
        return find_max_time_win(time_range[middle_idx:], race_time, record_distance)
    else:
        return find_max_time_win(time_range[0:middle_idx], race_time, record_distance)


races = read_input(year=2023, day_number=6)
race_time = int("".join(extract_numbers(races[0], type=str)))
race_distance = int("".join(extract_numbers(races[1], type=str)))

min_hold_to_win = find_min_time_win([i for i in range(0, race_time)], race_time, race_distance)
max_hold_to_win = find_max_time_win([i for i in range(0, race_time)], race_time, race_distance)

print(max_hold_to_win - min_hold_to_win + 1)
