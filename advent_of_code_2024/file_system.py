from itertools import groupby

from advent_of_code_2024.data_loaders import load_file_as_string


class Block:
    pass


class File(Block):
    def __init__(self, id_: int) -> None:
        self.id_ = id_

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, File):
            return False
        if self.id_ == other.id_:
            return True
        return False

    def __hash__(self) -> int:
        return hash(self.id_)


class Empty(Block):
    pass


class FileSystem:
    def __init__(self, filename: str) -> None:
        self.disk_map = load_file_as_string(filename)

    def expand_map(self) -> list[Block]:
        is_file = True
        file_id = 0
        output: list[Block] = []
        for char in self.disk_map:
            if is_file:
                for _ in range(int(char)):
                    output.append(File(file_id))
                file_id += 1
                is_file = False
            else:
                for _ in range(int(char)):
                    output.append(Empty())
                is_file = True
        return output

    def compact_aggressive(self) -> list[Block]:
        disk_map = self.expand_map()
        while True:
            # Find last file and first empty
            idx_file, last_file_block = next(
                (len(disk_map) - idx - 1, block)
                for idx, block in enumerate(disk_map[::-1])
                if isinstance(block, File)
            )
            idx_empty, first_empty_block = next(
                (idx, block)
                for idx, block in enumerate(disk_map)
                if isinstance(block, Empty)
            )
            # If the last file block is earlier than the first empty block we can terminate
            if idx_file < idx_empty:
                break
            # Swap blocks
            disk_map[idx_empty] = last_file_block
            disk_map[idx_file] = first_empty_block
        return disk_map

    def compact_conservative(self) -> list[Block]:
        disk_map = self.expand_map()
        if not isinstance(disk_map[-1], File):
            raise ValueError
        file_id = disk_map[-1].id_
        while file_id >= 0:
            # Find location of last file
            file_end, file_block = next(
                (len(disk_map) - idx - 1, block)
                for idx, block in enumerate(disk_map[::-1])
                if isinstance(block, File) and block.id_ == file_id
            )
            file_start = file_end
            while (
                isinstance(disk_map[file_start - 1], File)
                and disk_map[file_start - 1] == file_block
            ):
                file_start -= 1
            file_size = file_end - file_start + 1

            # Find location of all empty blocks and group them into sequences
            empty_positions = [
                idx for idx, block in enumerate(disk_map) if isinstance(block, Empty)
            ]
            empty_sequences = [
                (len(group), group[0][1])
                for group in [
                    list(g)
                    for _, g in groupby(
                        enumerate(empty_positions), lambda x: x[1] - x[0]
                    )
                ]
            ]

            # Move into an empty block if a large enough one exists to the left
            try:
                _, first_empty_start = next(
                    sequence for sequence in empty_sequences if sequence[0] >= file_size
                )
                if first_empty_start > file_start:
                    raise ValueError
                # Swap file with empty space
                disk_map[first_empty_start : first_empty_start + file_size] = disk_map[
                    file_start : file_start + file_size
                ]
                disk_map[file_start : file_start + file_size] = [Empty()] * file_size
            except (StopIteration, ValueError):
                pass
            # Check next file
            file_id -= 1
        return disk_map

    def checksum(self, strategy: str = "aggressive") -> int:
        if strategy == "aggressive":
            disk_map = self.compact_aggressive()
        elif strategy == "conservative":
            disk_map = self.compact_conservative()
        return sum(
            [
                (idx * block.id_)
                for idx, block in enumerate(disk_map)
                if isinstance(block, File)
            ]
        )
