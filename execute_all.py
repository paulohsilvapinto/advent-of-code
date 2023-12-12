import os
import re
import sys
from importlib import import_module

from commons.utils import read_input

try:
    years_dir = [os.path.join(".", year_dir) for year_dir in sys.argv[1].split(",")]
except Exception:
    years_dir = [os.path.join(".", year_dir) for year_dir in os.listdir(".") if re.match(r"\d{4}", year_dir)]

days_dir = [
    os.path.join(year_dir, day_dir)
    for year_dir in years_dir
    for day_dir in os.listdir(year_dir)
    if day_dir.startswith("day")
]
task_file_paths = [
    os.path.join(day_dir, task_file)
    for day_dir in days_dir
    for task_file in os.listdir(day_dir)
    if task_file.startswith("task")
]

print("Solutions are:\n")

previous_year = None
for task_file_path in task_file_paths:
    module_path = task_file_path[2:].replace("\\", ".").replace(".py", "")

    year, day, file_name = module_path.split(".")
    day = day[-2:]  # Remove string "day"
    if previous_year and previous_year != year:
        print()

    module = import_module(module_path)
    solution = module.solve(read_input(year, day))

    previous_year = year

    print(f"Advent of Code {year} - day {day} - part {file_name[4]} - solution: {solution}")
