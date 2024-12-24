from typing import Any

from advent_of_code_2024.data_loaders import load_file_as_blocks


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
        return f"LogicInput({self.name}, {self.bit})"


class LogicGate:
    def __init__(
        self, input_0: LogicNode, input_1: LogicNode, output: LogicNode
    ) -> None:
        self.input_0 = input_0
        self.input_1 = input_1
        self.output = output

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
        self.gates = self.build_gates(connection_block.split("\n"))
        self.apply_initial_values(value_block.split("\n"))

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

    def evaluate(self) -> None:
        queue = list(self.gates)
        while queue:
            remaining = []
            for gate in queue:
                try:
                    gate.run()
                except TypeError:
                    remaining.append(gate)
            queue = remaining

    def output(self) -> int:
        z_names = sorted([name for name in self.nodes.keys() if name.startswith("z")])
        z_bits = [(shift, self.nodes[name].bit) for shift, name in enumerate(z_names)]
        return sum([bit << shift for shift, bit in z_bits])

    def run(self) -> int:
        self.evaluate()
        return self.output()
