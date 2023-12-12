import os
import re


def read_input(day_number, test_input=False):
    file_name = "test_input.txt" if test_input else "input.txt"
    day = str(day_number).zfill(2)
    with open(os.path.join(f"day{day}", file_name), "r", encoding="utf-8") as f:
        return f.read().splitlines()


def extract_numbers(text, type=int):
    return [type(val) for val in re.findall(r"(\d+)", text)]
