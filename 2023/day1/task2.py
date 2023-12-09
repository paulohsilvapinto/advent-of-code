import re

NUMBER_MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

written_numbers_search_str = "|".join(NUMBER_MAPPING.keys())

with open("2023\\day1\\day1_input.txt", "r", encoding="utf-8") as f:
    calibration_doc = f.readlines()

calibration_total = 0
for line in calibration_doc:
    digits = re.findall(f"\d|{written_numbers_search_str}", line.lower())
    calibration_number = NUMBER_MAPPING.get(digits[0], digits[0]) + NUMBER_MAPPING.get(digits[-1], digits[-1])
    calibration_total += int(calibration_number)

print(calibration_total)