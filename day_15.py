import time

from advent_of_code_2024.warehouse import LargeWarehouse, Warehouse


def part_one():
    start = time.monotonic()
    warehouse = Warehouse("day-15-moves.txt", "day-15-warehouse.txt")
    print("Day 15 part 1:", warehouse.score_gps(), f"in {time.monotonic() - start:.3f} seconds")

def part_two():
    start = time.monotonic()
    warehouse = LargeWarehouse("day-15-moves.txt", "day-15-warehouse.txt")
    print("Day 15 part 2:", warehouse.score_gps(), f"in {time.monotonic() - start:.3f} seconds")

if __name__ == "__main__":
    part_one()
    part_two()
