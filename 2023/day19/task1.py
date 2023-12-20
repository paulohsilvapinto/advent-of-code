import re
from dataclasses import dataclass
from typing import Callable
from typing import List

from commons.utils import read_input


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

        # print(f"Rule = {part_parameter}, {comparison_operand}, {comparison_value}, {response_if_true}")
        rules.append(Rule(part_parameter, COMPARISON_MAP[comparison_operand], comparison_value, response_if_true))

    rules[-1].default = default_value
    WORKFLOWS[workflow_name] = Workflow(workflow_name, rules)


def create_workflows(input_data: list):
    while True:
        workflow_description = input_data.pop(0)
        if not workflow_description:
            return

        create_workflow(workflow_description)


def create_parts(input_data):
    parts = []
    for part_description in input_data:
        parameters = part_description[1:-1].split(",")
        parameters.sort(key=lambda p: PARAMETERS_SORT_ORDER.index(p[0]))
        parts.append(Part(*[int(val[2:]) for val in parameters]))

    return parts


def process_parts(parts, starting_workflow="in"):
    processed_parts = []
    for part in parts:
        processed_parts.append(WORKFLOWS[starting_workflow].process(part))

    return processed_parts


def get_answer(processed_parts):
    answer = 0
    for part in processed_parts:
        if part.accepted:
            answer += part.x + part.m + part.a + part.s

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
PARAMETERS_SORT_ORDER = "xmas"


def solve(input_data):
    create_workflows(input_data)
    parts = create_parts(input_data)
    processed_parts = process_parts(parts)

    return get_answer(processed_parts)


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=19)
    print(solve(input_data))
