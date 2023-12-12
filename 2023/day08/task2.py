import re
from math import lcm

from commons.utils import read_input

nodes = {}
data = read_input(year=2023, day_number=8)

instructions = data[0]
nodes_definition = data[2:]

for node in nodes_definition:
    node_name, node_connections = node.split(" = ")
    node_connections = re.findall(r"([A-z]+)", node_connections)
    nodes[node_name] = node_connections
# print(nodes)

starting_locations = [node for node in nodes if node.endswith("A")]

steps_per_starting_location = []
for starting_location in starting_locations:
    steps = 0
    current_location = starting_location

    while not current_location.endswith("Z"):
        for instruction in instructions:
            if current_location.endswith("Z"):
                break

            if instruction == "L":
                current_location = nodes[current_location][0]
            else:
                current_location = nodes[current_location][1]

            # print(f"{steps} - {current_locations}")
            steps += 1

    steps_per_starting_location.append(steps)

steps_for_convergence = lcm(*steps_per_starting_location)  # Least Common Multiple

print(steps_for_convergence)
