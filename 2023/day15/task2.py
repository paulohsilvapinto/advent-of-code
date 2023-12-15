from collections import defaultdict

from commons.utils import read_input


def default_box():
    return {
        "lenses": [],
        "focal_length": [],
    }


def hash_algorithm(string):
    hash_val = 0
    for char in string:
        ascii_val = ord(char)
        hash_val += ascii_val
        hash_val *= 17
        hash_val = hash_val % 256

    return hash_val


def add_replace_lens(boxes, box_number, lens_name, focal_length):
    if lens_name in boxes[box_number]["lenses"]:
        lens_position = boxes[box_number]["lenses"].index(lens_name)
        boxes[box_number]["lenses"][lens_position] = lens_name
        boxes[box_number]["focal_length"][lens_position] = focal_length
    else:
        boxes[box_number]["lenses"].append(lens_name)
        boxes[box_number]["focal_length"].append(focal_length)

    return boxes


def remove_lens(boxes, box_number, lens_name):
    if lens_name in boxes[box_number]["lenses"]:
        lens_position = boxes[box_number]["lenses"].index(lens_name)
        boxes[box_number]["lenses"].pop(lens_position)
        boxes[box_number]["focal_length"].pop(lens_position)

    return boxes


def calculate_focusing_power(boxes):
    focusing_power = 0
    for box_number, box_content in boxes.items():
        for lens_idx in range(len(box_content["lenses"])):
            focusing_power += (box_number + 1) * (lens_idx + 1) * (box_content["focal_length"][lens_idx])

    return focusing_power


def solve(input_data):
    boxes = defaultdict(default_box)
    for instruction in input_data[0].split(","):
        if "=" in instruction:
            lens_name, focal_length = instruction.split("=")
            focal_length = int(focal_length)

            box_number = hash_algorithm(lens_name)
            boxes = add_replace_lens(boxes, box_number, lens_name, focal_length)

        elif "-" in instruction:
            lens_name = instruction[:-1]

            box_number = hash_algorithm(lens_name)
            boxes = remove_lens(boxes, box_number, lens_name)

    return calculate_focusing_power(boxes)


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=15)
    print(solve(input_data))
