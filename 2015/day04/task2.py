from hashlib import md5

from commons.utils import read_input


def solve(input_data):
    input_data = input_data[0]
    md5_hash = ""
    ans = 0

    while not md5_hash.startswith("000000"):
        ans += 1
        md5_hash = md5(f"{input_data}{ans}".encode("utf-8")).hexdigest()

    return ans


if __name__ == "__main__":
    input_data = read_input(year=2015, day_number=4)
    print(solve(input_data))
