from commons.utils import read_input


def solve(input_data):
    oasis = input_data
    answer = 0

    for oasis_line in oasis:
        sequence = [int(number) for number in oasis_line.split()]
        first_numbers = [sequence[0]]

        while not all(number == 0 for number in sequence):
            new_sequence = []

            for i in range(0, len(sequence) - 1):
                new_sequence.append(sequence[i + 1] - sequence[i])

            first_numbers.append(new_sequence[0])
            sequence = new_sequence

        first_numbers.reverse()
        initial_number = 0
        for number in first_numbers:
            initial_number = number - initial_number

        answer += initial_number

    return answer


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=9)
    print(solve(input_data))
