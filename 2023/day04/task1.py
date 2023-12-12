import re

from commons.utils import read_input


def solve(input_data):
    games = input_data
    answer = 0

    for game in games:
        winning_numbers = re.findall(r"\:\s+(.*)\s+\|", game)[0].split()
        scratched_numbers = re.findall(r"\|\s+(.*)", game)[0].split()

        count_correct_numbers = 0
        for number in scratched_numbers:
            if number in winning_numbers:
                count_correct_numbers += 1

        answer += 2 ** (count_correct_numbers - 1) if count_correct_numbers else 0

    return answer


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=4)
    print(solve(input_data))
