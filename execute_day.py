import sys
from importlib import import_module

from commons.utils import read_input

year = sys.argv[1]
day = sys.argv[2].zfill(2)
task = sys.argv[3]

module = import_module(f"{year}.day{day}.task{task}")
solution = module.solve(read_input(year, day))

print(f"Advent of Code {year} - day {day} - part {task} - solution: {solution}")
