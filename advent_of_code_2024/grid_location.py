from collections.abc import Sequence


class GridLocation:
    def __init__(self, location: Sequence[int]) -> None:
        self.pos_0 = int(location[0])
        self.pos_1 = int(location[1])

    def __add__(self, other: "GridLocation") -> "GridLocation":
        return GridLocation([self.pos_0 + other.pos_0, self.pos_1 + other.pos_1])

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GridLocation):
            return False
        if self.as_tuple() == other.as_tuple():
            return True
        return False

    def __hash__(self) -> int:
        return hash(self.as_tuple())

    def __mul__(self, other: object) -> "GridLocation":
        return self.__rmul__(other)

    def __rmul__(self, other: object) -> "GridLocation":
        if not isinstance(other, int):
            raise NotImplementedError
        return GridLocation([self.pos_0 * other, self.pos_1 * other])

    def __str__(self) -> str:
        return f"GridLocation({self.pos_0}, {self.pos_1})"

    def __sub__(self, other: "GridLocation") -> "GridLocation":
        return GridLocation([self.pos_0 - other.pos_0, self.pos_1 - other.pos_1])

    def adjacent(self, other: "GridLocation") -> bool:
        return abs(self.pos_0 - other.pos_0) + abs(self.pos_1 - other.pos_1) == 1

    def as_tuple(self) -> tuple[int, int]:
        return (self.pos_0, self.pos_1)

    def in_bounds(self, max_0: int, max_1: int) -> bool:
        return (0 <= self.pos_0 <= max_0) and (0 <= self.pos_1 <= max_1)
