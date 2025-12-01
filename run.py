#!/usr/bin/env python3
import sys
import os
import subprocess


def run_day(day):
    day_str = f"day{day:02d}"
    solution_path = os.path.join(day_str, "solution.py")

    if not os.path.exists(solution_path):
        print(f"Error: {solution_path} does not exist")
        return 1

    print(f"Running {day_str}...")
    print("-" * 40)

    result = subprocess.run(
        [sys.executable, "solution.py"],
        cwd=day_str
    )

    return result.returncode


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 run.py <day>")
        print("Example: python3 run.py 1")
        sys.exit(1)

    try:
        day = int(sys.argv[1])
        if day < 1 or day > 25:
            print("Error: Day must be between 1 and 25")
            sys.exit(1)
    except ValueError:
        print("Error: Day must be a number")
        sys.exit(1)

    sys.exit(run_day(day))
