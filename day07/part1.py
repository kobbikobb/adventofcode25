from _utils.text_utils import get_lines


def get_result_part_1(data: str):
    """Gets the result"""

    lines = get_lines(data)

    first = lines[0].index("S")
    hits: set[int] = {first}

    result = 0

    for l, line in enumerate(lines[1:]):

        if (l % 2) == 0:
            continue

        new_hits: set[int] = set()

        for h in hits:

            if line[h] == "^":
                if h > 0:
                    new_hits.add(h - 1)
                if h < len(line) - 1:
                    new_hits.add(h + 1)
                result += 1
            else:
                new_hits.add(h)

        hits = new_hits

    return result
