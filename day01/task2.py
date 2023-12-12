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

written_numbers_search_str = "|".join(NUMBER_MAPPING.keys())
calibration_doc = read_input(day_number=1)

calibration_total = 0
for line in calibration_doc:
    digits = re.findall(rf"\d|{written_numbers_search_str}", line.lower())
    calibration_number = NUMBER_MAPPING.get(digits[0], digits[0]) + NUMBER_MAPPING.get(digits[-1], digits[-1])
    calibration_total += int(calibration_number)

print(calibration_total)
