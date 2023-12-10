import re

from commons.utils import read_input

nodes = {}
data = read_input(day_number=8)

instructions = data[0]
nodes_definition = data[2:]

for node in nodes_definition:
    node_name, node_connections = node.split(" = ")
    node_connections = re.findall(r"([A-z]+)", node_connections)
    nodes[node_name] = node_connections

current_location = "AAA"
steps = 0
while current_location != "ZZZ":
    for instruction in instructions:
        if current_location == "ZZZ":
            break

        if instruction == "L":
            current_location = nodes[current_location][0]
        else:
            current_location = nodes[current_location][1]

        steps += 1

print(steps)
