from advent_of_code_2024.claw_machine import get_claw_machines


def test_part_one():
    machines = get_claw_machines("day-13.test.txt")
    solutions = [machine.solve(use_brute_force=True) for machine in machines]
    prizes = list(filter(None, solutions))
    assert sum([prize[2] for prize in prizes]) == 480


def test_part_two():
    machines = get_claw_machines("day-13.test.txt", offset=10000000000000)
    solutions = [machine.solve() for machine in machines]
    prizes = list(filter(None, solutions))
    assert sum([prize[2] for prize in prizes]) == 875318608908
