import time
from advent_of_code_2024.plant_regions import GardenPlot


def part_one():
    start = time.monotonic()
    plot = GardenPlot("day-12.txt")
    print("Day 12 part 1:", plot.price(), f"in {time.monotonic() - start:.3f} seconds")

def part_two():
    start = time.monotonic()
    plot_2 = GardenPlot("day-12.txt")
    print("Day 12 part 2:", plot_2.price_discounted(), f"in {time.monotonic() - start:.3f} seconds")


if __name__ == "__main__":
    part_one()
    part_two()
