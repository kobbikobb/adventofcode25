import math

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

    @classmethod
    def from_line(cls, line: str) -> "Point":
        """Creates a Point from a line of text."""
        points = line.split(",")
        if len(points) != 3:
            raise ValueError(f"Invalid line for Point: {line}")

        cls.x = int(points[0])
        cls.y = int(points[1])
        cls.z = int(points[2])

        return cls(cls.x, cls.y, cls.z)

    def __str__(self):
        return f"{self.x},{self.y},{self.z}"


def distance(point1: Point, point2: Point) -> float:
    """Calculates the Euclidean distance between two 3D points."""
    x1, y1, z1 = point1.x, point1.y, point1.z
    x2, y2, z2 = point2.x, point2.y, point2.z

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


# arse points.
#
# uild list of all pairwise distances.
#
# ort by distance.
#
# se Union–Find:
#
# tart with 20 components of size 1.
#
# rocess edges until you have performed 10 merges.
#
# ount component sizes.
#
# ultiply the largest 3.


def get_result_part_1(data: str, max_connected: int = 10) -> int:
    """Gets the result"""

    lines = get_lines(data)
    points: list[Point] = [Point.from_line(line) for line in lines]

    distances: list[tuple[Point, Point, float]] = []

    for point in points:
        for other in points:
            if point != other:
                dist = distance(point, other)
                distances.append((point, other, dist))

    distances.sort(key=lambda x: x[2])
    circuts: list[list[Point]] = []

    connected = 0

    for dist in distances:

        for circut in circuts:

            if dist[0] in circut:
                circut.append(dist[1])
                connected += 1
                break
            if dist[1] in circut:
                circut.append(dist[0])
                connected += 1
                break

        circuts.append([dist[0], dist[1]])

        if connected >= max_connected:
            break

    result = 0

    for circut in circuts:
        result += len(circut)

    return result
