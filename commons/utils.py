import os
import re


def read_input(day_number):
    with open(os.path.join(f"day{day_number}", "input.txt"), "r", encoding="utf-8") as f:
        return f.read().splitlines()


def read_test_input(day_number):
    with open(os.path.join(f"day{day_number}", "test_input.txt"), "r", encoding="utf-8") as f:
        return f.read().splitlines()


def extract_numbers(text, type=int):
    return [type(val) for val in re.findall(r"(\d+)", text)]
