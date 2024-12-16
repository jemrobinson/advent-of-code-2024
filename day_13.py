import time
from advent_of_code_2024.claw_machine import get_claw_machines


def part_one():
    start = time.monotonic()
    machines = get_claw_machines("day-13.txt")
    solutions = [machine.solve(use_brute_force=True) for machine in machines]
    prizes = list(filter(None, solutions))
    print("Day 13 part 1:", sum([prize[2] for prize in prizes]), f"in {time.monotonic() - start:.3f} seconds")

def part_two():
    start = time.monotonic()
    machines = get_claw_machines("day-13.txt", offset=10000000000000)
    solutions = [machine.solve() for machine in machines]
    prizes = list(filter(None, solutions))
    print("Day 13 part 2:", sum([prize[2] for prize in prizes]), f"in {time.monotonic() - start:.3f} seconds")

if __name__ == "__main__":
    part_one()
    part_two()
