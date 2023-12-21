from collections import defaultdict
from collections import deque
from collections import namedtuple
from dataclasses import dataclass
from enum import Flag
from math import prod
from typing import List

from commons.utils import read_input

WireConnection = namedtuple("WireConnection", ["module", "received_from", "signal"])


class Signal(Flag):
    LOW = False
    HIGH = True


@dataclass
class GenericCircuitModule:
    identifier: str
    input_signals: dict
    output_modules: List[str]
    output_signal: int = Signal.LOW

    def receive_signal(self, input_signal, from_module):
        self.input_signals[from_module] = input_signal
        return self.process_signal(input_signal)

    def process_signal(self, _):
        raise NotImplementedError


@dataclass
class FlipFlopModule(GenericCircuitModule):
    def process_signal(self, input_signal):
        if input_signal == Signal.LOW:
            self.output_signal = ~self.output_signal
            return self.output_signal
        return None


@dataclass
class ConjunctionModule(GenericCircuitModule):
    def process_signal(self, _):
        if all([signal == Signal.HIGH for signal in self.input_signals.values()]):
            self.output_signal = Signal.LOW
        else:
            self.output_signal = Signal.HIGH

        return self.output_signal


@dataclass
class BroadcastModule(GenericCircuitModule):
    def process_signal(self, input_signal):
        self.output_signal = input_signal
        return self.output_signal


@dataclass
class OutputModule(BroadcastModule):
    # output signal is equal to input signal
    # but there are no connections to any output module
    pass


def default_circuit_definition():
    return {
        "type": OutputModule,
        "inputs": [],
        "outputs": [],
    }


def create_circuit_definition(input_data):
    circuit_definition = defaultdict(default_circuit_definition)

    for module_definition in input_data:
        module_name, outputs = module_definition.split(" -> ")
        module_type = MODULE_MAP[module_name[0]]
        outputs = outputs.split(", ")

        if module_name not in ["broadcaster", "output"]:
            module_name = module_name[1:]

        circuit_definition[module_name]["type"] = module_type
        for output in outputs:
            # map outputs
            if output not in circuit_definition[module_name]["outputs"]:
                circuit_definition[module_name]["outputs"].append(output)

            # update inputs of related modules
            if module_name not in circuit_definition[output]["inputs"]:
                circuit_definition[output]["inputs"].append(module_name)

    return circuit_definition


def create_circuit(circuit_definition):
    circuit = {}

    for module_name, definition in circuit_definition.items():
        inputs_as_low = {module_name: Signal.LOW for module_name in definition["inputs"]}
        circuit[module_name] = definition["type"](module_name, inputs_as_low, definition["outputs"])

    return circuit


def press_button(circuit, processed_signals_counter):
    execution_queue = deque([WireConnection("broadcaster", "button", Signal.LOW)])

    while execution_queue:
        current_module, from_module, input_signal = execution_queue.popleft()
        processed_signals_counter[input_signal] += 1
        output_signal = circuit[current_module].receive_signal(input_signal, from_module)

        if output_signal is not None:
            for output_module in circuit[current_module].output_modules:
                execution_queue.append(WireConnection(output_module, current_module, output_signal))

    return processed_signals_counter


def press_button_n_times(circuit, n=1000):
    processed_signals_counter = defaultdict(int)

    for _ in range(n):
        processed_signals_counter = press_button(circuit, processed_signals_counter)

    return processed_signals_counter


MODULE_MAP = {
    "%": FlipFlopModule,
    "&": ConjunctionModule,
    "b": BroadcastModule,
    "o": OutputModule,
}


def solve(input_data):
    circuit = create_circuit(create_circuit_definition(input_data))
    signals_counter = press_button_n_times(circuit, n=1000)

    return prod([count for count in signals_counter.values()])


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=20)
    print(solve(input_data))
