from commons.utils import read_input


def solve(input_data):
    answer = 0
    for word in input_data:
        len_code = len(word)

        encoded = word.replace("\\", "\\\\").replace('"', '\\"')
        encoded = '"' + encoded + '"'
        print(f"{word=} - {encoded=}")
        len_encoded = len(encoded)

        answer += len_encoded - len_code

    return answer


if __name__ == "__main__":
    input_data = read_input(year=2015, day_number=8)
    print(solve(input_data))
