from dataclasses import dataclass

import pulp

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

    num_buttons = len(machine.buttons)

    problem = pulp.LpProblem("MinimizeButtonPresses", pulp.LpMinimize)

    x_variable = [
        pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(num_buttons)
    ]

    problem += pulp.lpSum(x_variable), "TotalPresses"

    for i, target in enumerate(machine.joltages):
        problem += (
            pulp.lpSum(
                x_variable[j] for j, btn in enumerate(machine.buttons) if i in btn
            )
            == target,
            f"Counter{i}",
        )

    problem.solve(pulp.PULP_CBC_CMD(msg=0))  # silent solver

    total_presses = sum(int(pulp.value(var)) for var in x_variable)

    return total_presses


def get_result_part_2(data: str) -> int:
    """Gets the result"""

    lines: list[str] = get_lines(data)
    machines: list[Machine] = get_machines(lines)

    return sum(calculate_machine(machine) for machine in machines)
