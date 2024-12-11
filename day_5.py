#! /usr/bin/env python
import logging
from advent_of_code_2024.data_loaders import load_print_queue_rules, load_print_queue_updates
from advent_of_code_2024.print_queue import evaluate_update, middle_page

def part_one():
    rules = load_print_queue_rules("day-5.rules.csv")
    updates = load_print_queue_updates("day-5.updates.csv")
    print(sum([middle_page(update) for update in updates if evaluate_update(update, rules)]))

def part_two():
    pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format=r"[%(levelname)8s] %(message)s")
    part_one()
    part_two()