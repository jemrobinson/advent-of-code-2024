from copy import deepcopy
from functools import reduce
from operator import iadd
from typing import Any

from advent_of_code_2024.data_loaders import load_file_as_blocks


class SwapError(Exception):
    pass


class LogicNode:
    def __init__(self, name: str) -> None:
        self.name = name
        self.bit_: int | None = None

    @property
    def bit(self) -> int:
        if self.bit_ is None:
            raise TypeError
        return self.bit_

    def __repr__(self) -> str:
        return f"LogicNode({self.name}, {self.bit_})"


class LogicGate:
    def __init__(
        self, input_0: LogicNode, input_1: LogicNode, output: LogicNode
    ) -> None:
        self.input_0 = input_0
        self.input_1 = input_1
        self.output = output

    def is_for_inputs(self, name_0: str, name_1: str) -> bool:
        return {self.input_0.name, self.input_1.name} == {name_0, name_1}

    def run(self) -> None:
        raise NotImplementedError


class AndGate(LogicGate):
    def __init__(self, *args: Any) -> None:
        super().__init__(*args)

    def __repr__(self) -> str:
        return f"AndGate({self.input_0} AND {self.input_1} -> {self.output})"

    def run(self) -> None:
        self.output.bit_ = self.input_0.bit & self.input_1.bit


class OrGate(LogicGate):
    def __init__(self, *args: Any) -> None:
        super().__init__(*args)

    def __repr__(self) -> str:
        return f"OrGate({self.input_0} OR {self.input_1} -> {self.output})"

    def run(self) -> None:
        self.output.bit_ = self.input_0.bit | self.input_1.bit


class XorGate(LogicGate):
    def __init__(self, *args: Any) -> None:
        super().__init__(*args)

    def __repr__(self) -> str:
        return f"XorGate({self.input_0} XOR {self.input_1} -> {self.output})"

    def run(self) -> None:
        self.output.bit_ = self.input_0.bit ^ self.input_1.bit


class Computer:
    def __init__(self, filename: str) -> None:
        value_block, connection_block = load_file_as_blocks(filename)
        self.nodes = self.build_nodes(connection_block.split("\n"))
        self.gates_initial = self.build_gates(connection_block.split("\n"))
        self.gates: list[LogicGate] = list(self.gates_initial)
        self.apply_initial_values(value_block.split("\n"))
        self.swaps: list[tuple[LogicNode, LogicNode]] = []

    def apply_initial_values(self, input_lines: list[str]) -> None:
        for input_line in input_lines:
            name, value = input_line.split(": ")
            self.nodes[name].bit_ = int(value)

    def build_nodes(self, input_lines: list[str]) -> dict[str, LogicNode]:
        names = set()
        for input_line in input_lines:
            elems = input_line.split(" ")
            names.update({elems[0], elems[2], elems[4]})
        return {name: LogicNode(name) for name in names}

    def build_gates(self, input_lines: list[str]) -> list[LogicGate]:
        gates: list[LogicGate] = []
        for input_line in input_lines:
            elems = input_line.split(" ")
            input_0 = self.nodes[elems[0]]
            input_1 = self.nodes[elems[2]]
            output = self.nodes[elems[4]]
            match elems[1]:
                case "AND":
                    gates.append(AndGate(input_0, input_1, output))
                case "OR":
                    gates.append(OrGate(input_0, input_1, output))
                case "XOR":
                    gates.append(XorGate(input_0, input_1, output))
        return gates

    def calculate_swaps(self, max_swaps: int = 4) -> str:
        """
        An n-bit adder consists of an initial half-adder then n-1 full-adders
        Each half-adder is and XOR and an AND
        Each full-adder needs two half-adders and an OR

        See e.g. https://www.101computing.net/binary-additions-using-logic-gates/
        """
        for _ in range(max_swaps):
            try:
                self.find_next_swap()
            except SwapError:
                pass
        return ",".join(
            sorted(reduce(iadd, [(swap[0].name, swap[1].name) for swap in self.swaps]))
        )

    def evaluate(self) -> None:
        """Evaluate all the gates in order"""
        queue = list(self.gates)
        while queue:
            remaining = []
            for gate in queue:
                try:
                    gate.run()
                except TypeError:
                    remaining.append(gate)
            queue = remaining

    def find_gate(self, name_0: str, name_1: str, kind: type[LogicGate]) -> LogicGate:
        """Find a gate given its inputs"""
        for gate in self.gates:
            if gate.is_for_inputs(name_0, name_1) and isinstance(gate, kind):
                return gate
        raise ValueError

    def find_next_swap(self) -> None:
        """
        An n-bit adder consists of an initial half-adder then n-1 full-adders
        Each half-adder is and XOR and an AND
        Each full-adder needs two half-adders and an OR

        See e.g. https://www.101computing.net/binary-additions-using-logic-gates/
        """
        n_bits_output = len(
            [name for name in self.nodes.keys() if name.startswith("z")]
        )
        n_bits_input = n_bits_output - 1
        last_carry = None
        for idx_bit in range(n_bits_input):
            name_x, name_y, name_z = (
                f"x{idx_bit:02d}",
                f"y{idx_bit:02d}",
                f"z{idx_bit:02d}",
            )
            # Check that sum and carry operations exist for the first half-adder
            sum_0 = self.find_gate(name_x, name_y, XorGate)
            carry_0 = self.find_gate(name_x, name_y, AndGate)
            if last_carry:
                # Get the second half-adder
                try:
                    sum_1 = self.find_gate(
                        sum_0.output.name, last_carry.output.name, XorGate
                    )
                    carry_1 = self.find_gate(
                        sum_0.output.name, last_carry.output.name, AndGate
                    )
                except ValueError:
                    # An error indicates that the sum/carry from the previous half-adder must have been switched
                    self.swap(sum_0, carry_0)
                # Get the OR
                try:
                    adder_or = self.find_gate(
                        carry_0.output.name, carry_1.output.name, OrGate
                    )
                except ValueError:
                    # An error indicates one of the half-adder carries must have been switched
                    if carry_0.output.name == name_z:
                        self.swap(carry_0, sum_1)
                    if carry_1.output.name == name_z:
                        self.swap(carry_1, sum_1)
                # The sum is the sum of the second half-adder
                # The carry is the output of the or
                current_sum = sum_1
                last_carry = adder_or
            else:
                # The sum is the sum of the half-adder
                # The carry is the carry of the half-adder
                current_sum = sum_0
                last_carry = carry_0

            # Check if the output sum goes to the correct z-bit
            # An error indicates this sum is swapped with the gate currently writing here
            if current_sum.output.name != name_z:
                z_output = next(
                    gate for gate in self.gates if gate.output.name == name_z
                )
                self.swap(z_output, current_sum)

    def output(self) -> int:
        self.evaluate()
        z_names = sorted([name for name in self.nodes.keys() if name.startswith("z")])
        z_bits = [(shift, self.nodes[name].bit) for shift, name in enumerate(z_names)]
        return sum([bit << shift for shift, bit in z_bits])

    def swap(self, gate_0: LogicGate, gate_1: LogicGate) -> None:
        self.swaps.append((gate_0.output, gate_1.output))
        self.gates = []
        for gate_initial in self.gates_initial:
            gate = deepcopy(gate_initial)
            for swap_0, swap_1 in self.swaps:
                if gate.output.name == swap_0.name:
                    gate.output = swap_1
                elif gate.output.name == swap_1.name:
                    gate.output = swap_0
            self.gates.append(gate)
        raise SwapError
