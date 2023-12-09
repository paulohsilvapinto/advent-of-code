import re

with open("2023\\day1\\day1_input.txt", "r", encoding="utf-8") as f:
    calibration_doc = f.readlines()

calibration_total = 0
for line in calibration_doc:
    digits = re.findall("\d", line)
    calibration_number = digits[0] + digits[-1]
    calibration_total += int(calibration_number)

print(calibration_total)