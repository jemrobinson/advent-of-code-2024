#! /usr/bin/env python
from advent_of_code_2024.data_loaders import load_print_queue_rules, load_print_queue_updates
from advent_of_code_2024.print_queue import evaluate_update, middle_page, sort_update

def part_one():
    rules = load_print_queue_rules("day-5.rules.csv")
    updates = load_print_queue_updates("day-5.updates.csv")
    print(sum([middle_page(update) for update in updates if evaluate_update(update, rules)]))

def part_two():
    rules = load_print_queue_rules("day-5.rules.csv")
    updates = load_print_queue_updates("day-5.updates.csv")
    print(sum(
        middle_page(sort_update(update, rules))
        for update in updates
        if not evaluate_update(update, rules)
    ))


if __name__ == "__main__":
    part_one()
    part_two()