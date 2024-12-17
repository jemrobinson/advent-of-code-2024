from advent_of_code_2024.data_loaders import load_file_as_lines


class ThreeBitComputer:
    def __init__(self, filename: str) -> None:
        for line in load_file_as_lines(filename):
            if "A" in line:
                self.register_a = int(line.split()[-1])
            if "B" in line:
                self.register_b = int(line.split()[-1])
            if "C" in line:
                self.register_c = int(line.split()[-1])
            if "P" in line:
                self.program = [int(d) for d in line.split()[1].split(",")]

    def combo(self, operand: int) -> int:
        if 0 <= operand <= 3:  # noqa: PLR2004
            return operand
        if operand == 4:  # noqa: PLR2004
            return self.register_a
        if operand == 5:  # noqa: PLR2004
            return self.register_b
        if operand == 6:  # noqa: PLR2004
            return self.register_b
        msg = f"Combo operand {operand} is invalid"
        raise ValueError(msg)

    def run(self) -> list[int]:
        instruction_ptr = 0
        program_length = len(self.program)
        output = []
        while instruction_ptr < program_length:
            opcode = self.program[instruction_ptr]
            operand = self.program[instruction_ptr + 1]
            instruction_ptr += 2
            match opcode:
                case 0:  # adv
                    self.register_a = self.register_a // (2 ** self.combo(operand))
                case 1:  # bxl
                    self.register_b = self.register_b ^ operand
                case 2:  # bst
                    self.register_b = self.combo(operand) % 8
                case 3:  # jnz
                    if self.register_a:
                        instruction_ptr = operand
                case 4:  # bxc
                    self.register_b = self.register_b ^ self.register_c
                case 5:  # out
                    output.append(self.combo(operand) % 8)
                case 6:  # bdv
                    self.register_b = self.register_a // (2 ** self.combo(operand))
                case 7:  # cdv
                    self.register_c = self.register_a // (2 ** self.combo(operand))
        return output
