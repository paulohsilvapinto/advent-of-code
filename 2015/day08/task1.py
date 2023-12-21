import re

from commons.utils import read_input


def solve(input_data):
    answer = 0
    for word in input_data:
        len_code = len(word)

        word = word[1:-1]
        word = word.replace("\\\\", "\\").replace('\\"', '"')
        hexas = list(re.findall(r"\\x[A-f0-9]{2}", word))

        for hexa in hexas:
            word = word.replace(hexa, bytes.fromhex(hexa[2:]).decode("ISO-8859-1"))

        len_word = len(word)
        answer += len_code - len_word

    return answer


if __name__ == "__main__":
    input_data = read_input(year=2015, day_number=8)
    print(solve(input_data))
