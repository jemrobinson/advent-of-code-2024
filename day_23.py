import time

from advent_of_code_2024.lan_party import LanParty


def part_one():
    start = time.monotonic()
    party = LanParty("day-23.txt")
    print("Day 23 part 1:", party.count_triples_with_ts(), f"in {time.monotonic() - start:.3f} seconds")


def part_two():
    pass

if __name__ == "__main__":
    part_one()
    part_two()
