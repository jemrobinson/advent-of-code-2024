from advent_of_code_2024.plant_regions import GardenPlot


def part_one():
    plot = GardenPlot("day-12.txt")
    print("Day 12 part 1:", plot.price())

def part_two():
    plot_2 = GardenPlot("day-12.txt")
    print("Day 12 part 2:", plot_2.price_discounted())


if __name__ == "__main__":
    part_one()
    part_two()
