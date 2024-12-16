import time
from advent_of_code_2024.topographic_map import TopographicMap

def part_one():
    start = time.monotonic()
    topo_map = TopographicMap("day-10.txt")
    print("Day 10 part 1:", topo_map.score(), f"in {time.monotonic() - start:.3f} seconds")

def part_two():
    start = time.monotonic()
    topo_map = TopographicMap("day-10.txt")
    print("Day 10 part 2:", topo_map.rating(), f"in {time.monotonic() - start:.3f} seconds")


if __name__ == "__main__":
    part_one()
    part_two()
