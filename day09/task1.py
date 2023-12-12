from commons.utils import read_input

oasis = read_input(day_number=9)
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

print(answer)
