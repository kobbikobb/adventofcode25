import math
from itertools import combinations

from _utils.text_utils import get_lines


class Point:
    """A point in 3D space."""

    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other: object) -> bool:
        """Checks equality between two points."""
        if not isinstance(other, Point):
            return False
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    @classmethod
    def from_line(cls, line: str) -> "Point":
        """Creates a Point from a line of text."""
        points = line.split(",")
        if len(points) != 3:
            raise ValueError(f"Invalid line for Point: {line}")

        return cls(int(points[0]), int(points[1]), int(points[2]))

    def __str__(self):
        return f"{self.x},{self.y},{self.z}"


def distance(point1: Point, point2: Point) -> float:
    """Calculates the Euclidean distance between two 3D points."""
    x1, y1, z1 = point1.x, point1.y, point1.z
    x2, y2, z2 = point2.x, point2.y, point2.z

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def get_distances(points: list[Point]) -> list[tuple[Point, Point, float]]:
    """Gets all distances between points."""
    distances = [(p1, p2, distance(p1, p2)) for p1, p2 in combinations(points, 2)]
    return distances


def get_result_part_1(data: str, max_connected: int) -> int:
    """Gets the result"""

    lines = get_lines(data)
    points: list[Point] = [Point.from_line(line) for line in lines]

    distances = get_distances(points)
    distances.sort(key=lambda x: x[2])
    circuits: list[list[Point]] = []

    connected = 0

    for dist in distances:
        connected += 1
        d1, d2, l = dist

        # Find the circuits containing d1 and d2
        c1 = c2 = None
        for circuit in circuits:
            if d1 in circuit:
                c1 = circuit
            if d2 in circuit:
                c2 = circuit
            if c1 and c2:
                break

        # Already in the same circuit (use identity, not equality)
        if c1 is not None and c2 is not None and c1 is c2:
            if connected >= max_connected:
                break
            continue

        # If both are in different circuits, merge c2 into c1
        if c1 and c2:
            for point in c2:
                if point not in c1:
                    c1.append(point)
            circuits.remove(c2)

        # Only d1 is in a circuit → add d2
        elif c1:
            if d2 not in c1:
                c1.append(d2)

        # Only d2 is in a circuit → add d1
        elif c2:
            if d1 not in c2:
                c2.append(d1)

        # Neither in a circuit → create new
        else:
            circuits.append([d1, d2])

        if connected >= max_connected:
            break

    circuits.sort(key=len, reverse=True)

    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])
