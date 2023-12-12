import re

from commons.utils import read_input


def solve(input_data):
    calibration_doc = input_data

    calibration_total = 0
    for line in calibration_doc:
        digits = re.findall(r"\d", line)
        calibration_number = digits[0] + digits[-1]
        calibration_total += int(calibration_number)

    return calibration_total


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=1)
    print(solve(input_data))
