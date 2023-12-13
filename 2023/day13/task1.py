from numpy import transpose

from commons.utils import read_input


def parse_input(input_data):
    pattern_matrixes = []

    matrix_builder = []
    for pattern_row in input_data:
        if pattern_row:
            matrix_builder.append([val for val in pattern_row])
        else:
            pattern_matrixes.append(matrix_builder)
            matrix_builder = []

    if matrix_builder:
        pattern_matrixes.append(matrix_builder)

    return pattern_matrixes


def are_rows_mirroring(pattern, current_row_idx, row_length):
    offset = 0

    while current_row_idx - offset >= 0 and current_row_idx + offset + 1 <= len(pattern) - 1:
        row_comparison = [
            pattern[current_row_idx - offset][col_idx] == pattern[current_row_idx + offset + 1][col_idx]
            for col_idx in range(row_length)
        ]

        if all(row_comparison):
            offset += 1
        else:
            return False

    return True


def get_reflection_line_position(pattern, reflection_type):
    if reflection_type == "vertical":
        pattern = transpose(pattern)

    record_len = len(pattern[0])
    for i in range(0, len(pattern) - 1):
        if are_rows_mirroring(pattern, i, record_len):
            # print(f"Pattern type: {reflection_type}, Position: {i + 1}")
            return i + 1

    return None


def calculate_answer(horizontal_reflex_indexes, vertical_reflex_indexes):
    return sum(vertical_reflex_indexes) + sum(horizontal_reflex_indexes) * 100


def solve(input_data):
    pattern_matrixes = parse_input(input_data)

    horizontal_reflex_indexes = []
    vertical_reflex_indexes = []
    for pattern_matrix in pattern_matrixes:
        h_reflex_idx = get_reflection_line_position(pattern_matrix, "horizontal")
        if h_reflex_idx is not None:
            horizontal_reflex_indexes.append(h_reflex_idx)
            continue

        v_reflex_idx = get_reflection_line_position(pattern_matrix, "vertical")
        if v_reflex_idx is not None:
            vertical_reflex_indexes.append(v_reflex_idx)

    return calculate_answer(horizontal_reflex_indexes, vertical_reflex_indexes)


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=13)
    print(solve(input_data))
