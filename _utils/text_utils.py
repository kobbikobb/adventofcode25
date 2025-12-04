def read_input_data(filename: str):
    """Parse the input file and return the data."""
    with open(filename, "r") as f:
        return f.read().strip()


def get_lines(data: str):
    """Get lines"""
    return data.split("\n")


def get_comma_separated(data: str):
    """Get comma separated"""
    return data.split(",")
