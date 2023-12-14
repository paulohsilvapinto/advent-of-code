from commons.utils import read_input


def validate_first_condition(string):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_counter = len([char for char in string if char in vowels])

    if vowel_counter >= 3:
        return True
    return False


def validate_second_condition(string):
    for idx in range(len(string) - 1):
        if string[idx] == string[idx + 1]:
            return True
    return False


def validate_third_condition(string):
    for chars in ["ab", "cd", "pq", "xy"]:
        if chars in string:
            return False
    return True


def is_nice(string):
    return validate_first_condition(string) and validate_second_condition(string) and validate_third_condition(string)


def solve(input_data):
    answer = 0

    for string in input_data:
        answer += 1 if is_nice(string.lower()) else 0

    return answer


if __name__ == "__main__":
    input_data = read_input(year=2015, day_number=5)
    print(solve(input_data))
