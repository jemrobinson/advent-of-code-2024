from advent_of_code_2024.topographic_map import TopographicMap

def part_one():
    topo_map = TopographicMap("day-10.txt")
    print("Day 10 part 1:", topo_map.score())

def part_two():
    topo_map = TopographicMap("day-10.txt")
    print("Day 10 part 2:", topo_map.rating())


if __name__ == "__main__":
    part_one()
    part_two()
