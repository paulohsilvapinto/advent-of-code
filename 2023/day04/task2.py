import re
from collections import defaultdict

from commons.utils import read_input


def solve(input_data):
    games = input_data
    scratchcards_per_card = defaultdict(int)

    for game in games:
        card_number = int(game.split(":")[0].split()[1])
        scratchcards_per_card[card_number] += 1  # Original Card

        winning_numbers = re.findall(r"\:\s+(.*)\s+\|", game)[0].split()
        scratched_numbers = re.findall(r"\|\s+(.*)", game)[0].split()

        count_correct_numbers = 0
        for number in scratched_numbers:
            if number in winning_numbers:
                count_correct_numbers += 1
                scratchcards_per_card[card_number + count_correct_numbers] += (
                    1 * scratchcards_per_card[card_number]
                )  # Copy Cards

        response = sum(scratchcards_per_card.values())

    return response


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=3)
    print(solve(input_data))
