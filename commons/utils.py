import os
import re


def read_input(year, day_number):
    day = str(day_number).zfill(2)
    with open(os.path.join(f"{year}", f"day{day}", "input.txt"), "r", encoding="utf-8") as f:
        return f.read().splitlines()


def extract_numbers(text, type=int):
    return [type(val) for val in re.findall(r"(\d+)", text)]
