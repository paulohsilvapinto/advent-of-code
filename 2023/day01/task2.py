import re

from commons.utils import read_input

NUMBER_MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
WRITTEN_NUMBERS_SEARCH_STR = "|".join(NUMBER_MAPPING.keys())


def solve(input_data):
    calibration_doc = read_input(year=2023, day_number=1)

    calibration_total = 0
    for line in calibration_doc:
        digits = re.findall(rf"\d|{WRITTEN_NUMBERS_SEARCH_STR}", line.lower())
        calibration_number = NUMBER_MAPPING.get(digits[0], digits[0]) + NUMBER_MAPPING.get(digits[-1], digits[-1])
        calibration_total += int(calibration_number)

    return calibration_total


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=1)
    print(solve(input_data))
