from advent_of_code_2024.data_loaders import load_file_as_lines


class ThreeBitComputer:
    def __init__(self, filename: str) -> None:
        for line in load_file_as_lines(filename):
            if "A" in line:
                self.register_a = self.register_a_init = int(line.split()[-1])
            if "B" in line:
                self.register_b = self.register_b_init = int(line.split()[-1])
            if "C" in line:
                self.register_c = self.register_c_init = int(line.split()[-1])
            if "P" in line:
                self.program = [int(d) for d in line.split()[1].split(",")]
        self.program_length = len(self.program)

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

    def find_characteristic(self) -> int:
        # Looking at the result for first few thousand values of A shows a characteristic k
        # .. digit 0 changes on every step,
        # .. digit 1 changes on every k-th step
        # .. digit 2 changes on every k^2-th step
        # .. digit 3 changes on every k^3-th step
        # => digit n is changed every k^n-th step
        k, current_length = 0, 1
        while True:
            new_length = len(self.run_with_register_a(k))
            if new_length > current_length:
                return k
            current_length = new_length
            k += 1

    def find_register_a(self) -> int:
        k = self.find_characteristic()  # find digit-increasing characteristic
        current_a = k ** (self.program_length - 1)  # smallest A with correct length
        while True:
            output = self.run_with_register_a(current_a)
            if len(output) != self.program_length:
                msg = f"Output length {len(output)} does not match program length {self.program_length}"
                raise ValueError(msg)
            matches = [
                d_output == d_program
                for d_output, d_program in zip(output, self.program, strict=False)
            ]
            if all(matches):
                break
            last_incorrect_digit = self.program_length - matches[::-1].index(False)
            # Move to the next time this digit changes
            step_size = k ** (last_incorrect_digit - 1)
            current_a = step_size * (current_a // step_size + 1)
        return int(current_a)

    def run(self) -> list[int]:
        # Setup
        instruction_ptr = 0
        output = []
        # Loop until the instruction pointer moves out of the program
        while instruction_ptr < self.program_length:
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

    def run_with_register_a(self, register_a: int) -> list[int]:
        self.register_a = register_a
        self.register_b = self.register_b_init
        self.register_c = self.register_c_init
        return self.run()
