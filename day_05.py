import time

from advent_of_code_2024.print_queue import PrintQueue

def part_one():
    start = time.monotonic()
    queue = PrintQueue(rules_file="day-5.rules.csv", updates_file="day-5.updates.csv")
    print("Day 5 part 1:", queue.score_ordered_updates(), f"in {time.monotonic() - start:.3f} seconds")

def part_two():
    start = time.monotonic()
    queue = PrintQueue(rules_file="day-5.rules.csv", updates_file="day-5.updates.csv")
    print("Day 5 part 2:", queue.score_unordered_updates(), f"in {time.monotonic() - start:.3f} seconds")


if __name__ == "__main__":
    part_one()
    part_two()