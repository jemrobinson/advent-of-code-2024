from advent_of_code_2024.data_loaders import load_file_as_blocks


class Lock:
    def __init__(self, block: str) -> None:
        self.teeth = [0, 0, 0, 0, 0]
        for idx_row, line in enumerate(block.split("\n")):
            for idx_col, char in enumerate(line):
                if char == "#":
                    self.teeth[idx_col] = idx_row


class Key:
    def __init__(self, block: str) -> None:
        self.teeth = [0, 0, 0, 0, 0]
        for idx_row, line in enumerate(block.split("\n")):
            for idx_col, char in enumerate(line):
                if char == ".":
                    self.teeth[idx_col] = 5 - idx_row


class LockKeyMatcher:
    def __init__(self, filename: str) -> None:
        self.locks: list[Lock] = []
        self.keys: list[Key] = []
        self.block_size = 6
        for block in load_file_as_blocks(filename):
            if block.startswith("#"):
                self.locks.append(Lock(block))
            else:
                self.keys.append(Key(block))

    def unique_pairs(self) -> int:
        return len(
            [
                True
                for lock in self.locks
                for key in self.keys
                if all(
                    sum(teeth) < self.block_size
                    for teeth in zip(lock.teeth, key.teeth, strict=True)
                )
            ]
        )
