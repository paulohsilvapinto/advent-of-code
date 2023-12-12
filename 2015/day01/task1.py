from collections import Counter

from commons.utils import read_input


def solve(input_data):
    movements = input_data[0]

    movements_counter = Counter(movements)
    floor = movements_counter["("] - movements_counter[")"]

    return floor


if __name__ == "__main__":
    input_data = read_input(year=2015, day_number=1)
    print(solve(input_data))
