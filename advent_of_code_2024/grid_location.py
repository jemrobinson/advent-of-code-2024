from collections.abc import Sequence


class GridLocation:
    """Location in a rectangular grid.

    Co-ordinates:
    - (0,0) in the north-west corner.
    - Increasing pos_0 moves south
    - Increasing pos_1 moves east
    """

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

    def north(self) -> "GridLocation":
        return self + GridLocation((-1, 0))

    def northeast(self) -> "GridLocation":
        return self + GridLocation((-1, 1))

    def east(self) -> "GridLocation":
        return self + GridLocation((0, 1))

    def southeast(self) -> "GridLocation":
        return self + GridLocation((1, 1))

    def south(self) -> "GridLocation":
        return self + GridLocation((1, 0))

    def southwest(self) -> "GridLocation":
        return self + GridLocation((1, -1))

    def west(self) -> "GridLocation":
        return self + GridLocation((0, -1))

    def northwest(self) -> "GridLocation":
        return self + GridLocation((-1, -1))
