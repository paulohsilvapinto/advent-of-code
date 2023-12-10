import os
import re


def read_input(day_number):
    with open(os.path.join(f"day{day_number}", "input.txt"), "r", encoding="utf-8") as f:
        return f.readlines()


def read_test_input(day_number):
    with open(os.path.join(f"day{day_number}", "input.txt"), "r", encoding="utf-8") as f:
        return f.readlines()


def extract_numbers(text, type=int):
    return [type(val) for val in re.findall(r"(\d+)", text)]
