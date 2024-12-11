import enum
from collections.abc import Sequence
from itertools import product


class Operator(enum.StrEnum):
    PLUS = "+"
    TIMES = "*"


class Calibration:
    def __init__(self, line: str) -> None:
        output, inputs = line.strip().split(":")
        self.inputs = list(map(int, inputs.strip().split(" ")))
        self.output = int(output)
        self.operators = list(Operator)

    def evaluate(self, start: int, operations: Sequence[tuple[Operator, int]]) -> int:
        total = start
        for operation in operations:
            if operation[0] == Operator.PLUS:
                total += operation[1]
            if operation[0] == Operator.TIMES:
                total *= operation[1]
        return total

    def is_valid(self) -> bool:
        for operators in product(self.operators, repeat=len(self.inputs) - 1):
            operations: list[tuple[Operator, int]] = list(
                zip(operators, self.inputs[1:], strict=True)  # type: ignore[arg-type]
            )
            if self.evaluate(self.inputs[0], operations) == self.output:
                return True
        return False
