from commons.utils import read_input


def validate_first_condition(string):
    for pair_start_idx in range(len(string) - 1):
        pair = string[pair_start_idx : pair_start_idx + 2]

        pair_counter = 0
        skip_next_idx = False
        for search_idx in range(pair_start_idx, len(string) - 1):
            if skip_next_idx:
                skip_next_idx = False
                continue
            else:
                search_pair = string[search_idx : search_idx + 2]
                if pair == search_pair:
                    pair_counter += 1
                    skip_next_idx = True

            if pair_counter >= 2:
                return True

    return False


def validate_second_condition(string):
    for idx in range(len(string) - 2):
        if string[idx] == string[idx + 2]:
            return True
    return False


def is_nice(string):
    return validate_first_condition(string) and validate_second_condition(string)


def solve(input_data):
    answer = 0

    for string in input_data:
        string = string
        answer += 1 if is_nice(string.lower()) else 0

    return answer


if __name__ == "__main__":
    input_data = read_input(year=2015, day_number=5)
    print(solve(input_data))
