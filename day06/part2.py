import re

from _utils.text_utils import get_lines


def calculate(symbol: str, numbers: list[int]) -> int:
    if symbol == "+":
        return sum(numbers)
    elif symbol == "*":
        result = 1
        for number in numbers:
            result *= number
        return result
    else:
        raise ValueError(f"Unknown symbol: {symbol}")


def get_cephalopod_numbers(column: list[str]) -> list[int]:
    numbers = []

    longest = max(len(s) for s in column)

    for i in range(longest):

        new: str = ""
        for number in column:
            if len(number) > i:
                digit: str = number[i]
                if digit != " ":
                    new += digit

        if len(new) > 0:
            numbers.append(int(new))

    return numbers


def get_result_part_2(data: str):
    """Gets the result"""

    lines = get_lines(data)
    last_line = lines[len(lines) - 1]

    symbols: list[tuple[str, int]] = []

    for i, c in enumerate(last_line):
        if c != " ":
            symbols.append((c, i))

    columns: list[list[str]] = []

    for i in range(0, len(lines) - 1):
        line = lines[i]

        for j in range(len(symbols)):
            if len(columns) <= j:
                columns.append([])

            s1 = symbols[j][1]

            if(j >= len(symbols) - 1):
                columns[j].append(line[s1:])
            else:
                s2 = symbols[j + 1][1]
                columns[j].append(line[s1: s2-1])

    result = 0
    for i, column in enumerate(columns):
        new_numbers = get_cephalopod_numbers(column)
        result += calculate(symbols[i][0], new_numbers)

    return result
