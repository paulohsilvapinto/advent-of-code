import re
import sys

from commons.utils import read_input

print(sys.path)

games = read_input(day_number=4)
response = 0

for game in games:
    winning_numbers = re.findall(r"\:\s+(.*)\s+\|", game)[0].split()
    scratched_numbers = re.findall(r"\|\s+(.*)", game)[0].split()

    count_correct_numbers = 0
    for number in scratched_numbers:
        if number in winning_numbers:
            count_correct_numbers += 1

    response += 2 ** (count_correct_numbers - 1) if count_correct_numbers else 0

print(response)
