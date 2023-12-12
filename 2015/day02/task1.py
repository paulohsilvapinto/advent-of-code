from commons.utils import read_input


def solve(input_data):
    presents = input_data
    answer = 0

    for present in presents:
        l, w, h = list(map(int, present.split("x")))
        dimensions = [l * w, w * h, h * l]
        dimensions.sort()

        smallest_side = dimensions[0]
        paper_sqft = sum([2 * d for d in dimensions]) + smallest_side

        answer += paper_sqft

    return answer


if __name__ == "__main__":
    input_data = read_input(year=2015, day_number=2)
    print(solve(input_data))
