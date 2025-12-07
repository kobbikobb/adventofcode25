from _utils.text_utils import get_lines


def get_result_part_1(data: str):
    """Gets the result"""

    lines = get_lines(data)

    first = lines[0].index("S")
    hits: Set[int] = {first}

    result = 0

    for i, line in enumerate(lines[1:]):

        if (i % 2) == 0:
            continue

        print(line)
        print(hits)

        new_hits: Set[int] = set()

        for i in hits:

            if line[i] == "^":
                if i > 0:
                    new_hits.add(i - 1)
                if i < len(line) - 1:
                    new_hits.add(i + 1)
                result += 1
            else:
                new_hits.add(i)

        hits = new_hits

        print(result)

    return result
