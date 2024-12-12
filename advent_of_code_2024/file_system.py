from .data_loaders import load_file_as_string


class Block:
    pass


class File(Block):
    def __init__(self, id_: int) -> None:
        self.id_ = id_


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

    def compact(self) -> list[Block]:
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

    def checksum(self) -> int:
        disk_map = self.compact()
        return sum(
            [
                (idx * block.id_)
                for idx, block in enumerate(disk_map)
                if isinstance(block, File)
            ]
        )
