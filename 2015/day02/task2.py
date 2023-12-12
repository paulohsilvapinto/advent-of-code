from math import prod

from commons.utils import read_input


def solve(input_data):
    presents = input_data
    answer = 0

    for present in presents:
        dimensions = list(map(int, present.split("x")))
        dimensions.sort()

        ribbon_present = 2 * (dimensions[0] + dimensions[1])
        ribbon_bow = prod(dimensions)

        answer += ribbon_bow + ribbon_present

    return answer


if __name__ == "__main__":
    input_data = read_input(year=2015, day_number=2)
    print(solve(input_data))
