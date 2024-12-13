from advent_of_code_2024.claw_machine import get_claw_machines


def part_one():
    machines = get_claw_machines("day-13.txt")
    solutions = [machine.solve() for machine in machines]
    prizes = list(filter(None, solutions))
    print("Day 13 part 1:", sum([prize[2] for prize in prizes]))

def part_two():
    pass

if __name__ == "__main__":
    part_one()
    part_two()
