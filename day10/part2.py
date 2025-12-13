from dataclasses import dataclass
from itertools import combinations, combinations_with_replacement

from _utils.text_utils import get_lines


@dataclass
class Machine:
    """State machine"""

    lights: list[bool]
    buttons: list[list[int]]
    joltages: list[int]


def get_between(source: str, start: str, end: str) -> str:
    """Gets the string between two substrings"""

    start_index: int = source.index(start)
    end_index: int = source.rindex(end)

    return source[start_index + 1 : end_index]


def get_machines(lines: list[str]) -> list[Machine]:
    """Gets the machines from the lines"""

    machines: list[Machine] = []

    for line in lines:
        lights_str = get_between(line, "[", "]")
        buttons_strs = get_between(line, "(", ")").split(") (")
        joltages_str = get_between(line, "{", "}")

        lights = [c == "#" for c in lights_str]
        buttons = [[int(num) for num in btn_str.split(",")] for btn_str in buttons_strs]
        joltages = [int(joltage_str) for joltage_str in joltages_str.split(",")]

        machines.append(Machine(lights, buttons, joltages))

    return machines


def calculate_machine(machine: Machine) -> int:
    """Calculates the result for a single machine"""

    for i in range(1, sum(machine.joltages) + 1):

        combos = list(combinations_with_replacement(machine.buttons, i))

        for combo in combos:
            to_match: list[int] = [0] * len(machine.joltages)

            for buttons in combo:
                for idx in buttons:
                    to_match[idx] = to_match[idx] + 1

            if to_match == machine.joltages:
                print(f"Found match with {i} buttons")
                return i

    return 0


def get_result_part_2(data: str) -> int:
    """Gets the result"""

    lines: list[str] = get_lines(data)
    machines: list[Machine] = get_machines(lines)

    return sum(calculate_machine(machine) for machine in machines)
