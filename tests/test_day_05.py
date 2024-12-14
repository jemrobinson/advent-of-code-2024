from advent_of_code_2024.print_queue import (
    evaluate_update,
    load_print_queue_rules,
    load_print_queue_updates,
    middle_page,
    sort_update,
)


def test_part_one():
    rules = load_print_queue_rules("day-5.rules.test.csv")
    updates = load_print_queue_updates("day-5.updates.test.csv")
    assert (
        sum(
            [
                middle_page(update)
                for update in updates
                if evaluate_update(update, rules)
            ]
        )
        == 143
    )


def test_part_two():
    rules = load_print_queue_rules("day-5.rules.test.csv")
    updates = load_print_queue_updates("day-5.updates.test.csv")
    assert (
        sum(
            middle_page(sort_update(update, rules))
            for update in updates
            if not evaluate_update(update, rules)
        )
        == 123
    )
