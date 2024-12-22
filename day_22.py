import time

from advent_of_code_2024.banana_market import BananaMarket


def part_one():
    start = time.monotonic()
    market = BananaMarket("day-22.txt")
    print("Day 22 part 1:", market.sum_buyer_secrets(), f"in {time.monotonic() - start:.3f} seconds")


def part_two():
    start = time.monotonic()
    market = BananaMarket("day-22.txt")
    print("Day 22 part 2:", market.most_bananas(), f"in {time.monotonic() - start:.3f} seconds")

if __name__ == "__main__":
    part_one()
    part_two()
