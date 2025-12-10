import math
from itertools import combinations


class Point:
    """A point in 3D space."""

    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other: "Point") -> float:
        """Calculates the Euclidean distance between two 3D points."""

        x1, y1, z1 = self.x, self.y, self.z
        x2, y2, z2 = other.x, other.y, other.z

        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    @classmethod
    def from_line(cls, line: str) -> "Point":
        """Creates a Point from a line of text."""
        points = line.split(",")
        if len(points) != 3:
            raise ValueError(f"Invalid line for Point: {line}")

        return cls(int(points[0]), int(points[1]), int(points[2]))

    def __str__(self):
        return f"{self.x},{self.y},{self.z}"

    def __eq__(self, other: object) -> bool:
        """Checks equality between two points."""
        if not isinstance(other, Point):
            return False
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))


def get_distances(points: list[Point]) -> list[tuple[Point, Point, float]]:
    """Gets all distances between points."""
    distances = [(p1, p2, p1.distance(p2)) for p1, p2 in combinations(points, 2)]

    return distances
