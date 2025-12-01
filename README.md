# Advent of Code 2025

Solutions for Advent of Code 2025 in Python 3.

## Setup

Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run a solution:
```bash
python3 run.py <day>
```

Run tests for a specific day:
```bash
pytest dayXX -v
```

Run all tests:
```bash
pytest
```

## New Day

Copy templates and add your input:
```bash
cp template.py dayXX/solution.py
cp _test_template.py dayXX/test_solution.py
touch dayXX/input.txt
```
