from functools import lru_cache

from advent_of_code_2024.data_loaders import load_file_as_lines, load_file_as_string


class Towels:
    def __init__(self, patterns_file: str, designs_file: str) -> None:
        self.patterns = [
            p.strip() for p in load_file_as_string(patterns_file).split(",")
        ]
        self.designs = [d.strip() for d in load_file_as_lines(designs_file)]

    def count_combinations(self) -> int:
        return sum(self.combinations(design) for design in self.designs)

    def count_possible(self) -> int:
        return sum(self.combinations(design) > 0 for design in self.designs)

    @lru_cache(None)  # noqa: B019
    def combinations(self, design: str) -> int:
        if design == "":
            return 1
        return sum(
            self.combinations(design[len(pattern) :])
            for pattern in self.patterns
            if design.startswith(pattern)
        )
