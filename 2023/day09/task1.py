from commons.utils import read_input


def solve(input_data):
    oasis = input_data
    answer = 0
    # print(oasis)

    for oasis_line in oasis:
        # print(oasis_line)
        sequence = [int(number) for number in oasis_line.split()]
        last_numbers = [sequence[-1]]

        # print(sequence)
        # print(last_numbers)

        while not all(number == 0 for number in sequence):
            new_sequence = []

            for i in range(0, len(sequence) - 1):
                new_sequence.append(sequence[i + 1] - sequence[i])

            last_numbers.append(new_sequence[-1])
            sequence = new_sequence
            # print(sequence)

        answer += sum(last_numbers)

    return answer


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=9)
    print(solve(input_data))
