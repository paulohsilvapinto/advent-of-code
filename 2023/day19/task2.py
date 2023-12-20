import re
from collections import namedtuple
from copy import deepcopy
from dataclasses import dataclass
from math import prod
from typing import Callable
from typing import List

from commons.utils import read_input


ParameterBoundaries = namedtuple("ParameterBoundaries", ["low", "high"])


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int
    accepted: bool = None


@dataclass
class Rule:
    part_parameter: str
    comparison_operand: str
    comparer: Callable
    comparison_value: int
    target_if_true: str
    default: str = None

    def apply_rule(self, part):
        parameter = getattr(part, self.part_parameter)
        if self.comparer(parameter, self.comparison_value):
            return self.target_if_true
        else:
            return self.default


@dataclass
class Workflow:
    name: str
    rules: List[Rule]

    def process(self, part):
        for rule in self.rules:
            rule_response = rule.apply_rule(part)
            if rule_response in ACCEPTED_MAP:
                part.accepted = ACCEPTED_MAP[rule_response]
                return part
            elif rule_response:
                return WORKFLOWS[rule_response].process(part)
            else:
                pass  # to the next rule in the workflow


def create_workflow(description: str):
    workflow_name = description[: description.index("{")]
    rules_description = re.findall(r"([xmas][<>]\d+:[A-z]+)", description)
    default_value = description[description.rfind(",") + 1 : -1]

    rules = []
    for rule in rules_description:
        part_parameter = rule[0]
        comparison_operand = rule[1]
        colon_idx = rule.find(":")
        comparison_value = int(rule[2:colon_idx])
        response_if_true = rule[colon_idx + 1 :]

        rules.append(
            Rule(
                part_parameter,
                comparison_operand,
                COMPARISON_MAP[comparison_operand],
                comparison_value,
                response_if_true,
            ),
        )

    rules[-1].default = default_value
    WORKFLOWS[workflow_name] = Workflow(workflow_name, rules)


def create_workflows(input_data: list):
    while True:
        workflow_description = input_data.pop(0)
        if not workflow_description:
            return

        create_workflow(workflow_description)


def find_parts_boundaries(generic_part, parts, current_workflow="in"):
    if current_workflow in ACCEPTED_MAP:
        generic_part.accepted = ACCEPTED_MAP[current_workflow]
        parts.append(generic_part)
        return parts

    for rule in WORKFLOWS[current_workflow].rules:
        current_boundaries = getattr(generic_part, rule.part_parameter)
        if rule.comparison_operand == "<":
            if rule.comparer(current_boundaries.low, rule.comparison_value):
                new_part = deepcopy(generic_part)
                setattr(
                    new_part,
                    rule.part_parameter,
                    ParameterBoundaries(current_boundaries.low, rule.comparison_value - 1),
                )

                parts = find_parts_boundaries(new_part, parts, rule.target_if_true)

            if current_boundaries.high >= rule.comparison_value:
                setattr(
                    generic_part,
                    rule.part_parameter,
                    ParameterBoundaries(rule.comparison_value, current_boundaries.high),
                )
        else:
            if rule.comparer(current_boundaries.high, rule.comparison_value):
                new_part = deepcopy(generic_part)
                setattr(
                    new_part,
                    rule.part_parameter,
                    ParameterBoundaries(rule.comparison_value + 1, current_boundaries.high),
                )

                parts = find_parts_boundaries(new_part, parts, rule.target_if_true)

            if current_boundaries.low <= rule.comparison_value:
                setattr(
                    generic_part,
                    rule.part_parameter,
                    ParameterBoundaries(current_boundaries.low, rule.comparison_value),
                )

        if rule.default:
            parts = find_parts_boundaries(generic_part, parts, rule.default)

    return parts


def get_answer(processed_parts):
    answer = 0
    for part in processed_parts:
        if part.accepted:
            answer += prod([getattr(part, parameter).high - getattr(part, parameter).low + 1 for parameter in "xmas"])
    return answer


def less_than(a, b):
    return a < b


def greater_than(a, b):
    return a > b


COMPARISON_MAP = {
    "<": less_than,
    ">": greater_than,
}

ACCEPTED_MAP = {
    "A": True,
    "R": False,
}

WORKFLOWS = {}


def solve(input_data):
    create_workflows(input_data)
    parts = find_parts_boundaries(Part(*[ParameterBoundaries(1, 4000) for _ in range(4)]), list())
    # print(parts)
    return get_answer(parts)


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=19)
    print(solve(input_data))
