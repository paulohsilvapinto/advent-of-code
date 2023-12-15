from commons.utils import read_input


def hash_algorithm(string):
    hash_val = 0
    for char in string:
        ascii_val = ord(char)
        hash_val += ascii_val
        hash_val *= 17
        hash_val = hash_val % 256

    return hash_val


def solve(input_data):
    hash_total = 0
    for string in input_data[0].split(","):
        hash_total += hash_algorithm(string)

    return hash_total


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=15)
    print(solve(input_data))
