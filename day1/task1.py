import re
from commons.utils import read_input

calibration_doc = read_input(day_number=1)

calibration_total = 0
for line in calibration_doc:
    digits = re.findall(r"\d", line)
    calibration_number = digits[0] + digits[-1]
    calibration_total += int(calibration_number)

print(calibration_total)