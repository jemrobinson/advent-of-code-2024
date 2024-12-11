import enum
from collections.abc import Sequence
from itertools import product


class Operator(enum.StrEnum):
    PLUS = "+"
    TIMES = "*"
    CONCATENATE = "||"


class Calibration:
    def __init__(self, line: str, operators: list[Operator]) -> None:
        output, inputs = line.strip().split(":")
        self.inputs = list(map(int, inputs.strip().split(" ")))
        self.output = int(output)
        self.operators = operators

    def evaluate(self, start: int, operations: Sequence[tuple[Operator, int]]) -> int:
        total = start
        for operation in operations:
            if operation[0] == Operator.PLUS:
                total += operation[1]
            if operation[0] == Operator.TIMES:
                total *= operation[1]
            if operation[0] == Operator.CONCATENATE:
                total = int(str(total) + str(operation[1]))
        return total

    def is_valid(self) -> bool:
        for operators in product(self.operators, repeat=len(self.inputs) - 1):
            operations: list[tuple[Operator, int]] = list(
                zip(operators, self.inputs[1:], strict=True)
            )
            if self.evaluate(self.inputs[0], operations) == self.output:
                return True
        return False


class CalibrationSimple(Calibration):
    def __init__(self, line: str):
        super().__init__(line, operators=[Operator.PLUS, Operator.TIMES])


class CalibrationFull(Calibration):
    def __init__(self, line: str):
        super().__init__(
            line, operators=[Operator.PLUS, Operator.TIMES, Operator.CONCATENATE]
        )
