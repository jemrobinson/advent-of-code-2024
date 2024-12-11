import logging
from collections.abc import Sequence

logger = logging.getLogger(__name__)


def evaluate_update(update: Sequence[int], rules: Sequence[tuple[int, int]]) -> bool:
    for rule in rules:
        try:
            idx_first = update.index(rule[0])
            idx_second = update.index(rule[1])
            if idx_second < idx_first:
                logger.error(
                    f"Discarding {update} as {rule[0]} is not before {rule[1]}"
                )
                return False
        except ValueError:
            logger.debug(f"Ignoring {rule} as it does not apply to {update}")
            continue
    return True


def middle_page(update: Sequence[int]) -> int:
    if len(update) % 2 == 0:
        msg = f"No middle page for update of length {len(update)}"
        raise ValueError(msg)
    return update[len(update) // 2]
