from _utils.text_utils import get_lines
from day08.point import Point, get_distances


def get_result_part_2(data: str) -> int:
    """Gets the result"""

    lines = get_lines(data)
    points: list[Point] = [Point.from_line(line) for line in lines]

    distances = get_distances(points)
    distances.sort(key=lambda x: x[2])
    circuits: list[list[Point]] = []
    last_connected: tuple[Point, Point]

    for dist in distances:
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
            continue

        # If both are in different circuits, merge c2 into c1
        if c1 and c2:

            last_connected = (d1, d2)

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

    print(len(circuits))
    print(last_connected[0])
    print(last_connected[1])

    return last_connected[0].x * last_connected[1].x
