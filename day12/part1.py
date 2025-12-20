from dataclasses import dataclass

from _utils.text_utils import get_lines


@dataclass
class Shape:
    """A shape"""

    def __init__(self, size_x, size_y):
        self.grid: list[list[bool]] = [
            [False for _ in range(size_x)] for _ in range(size_y)
        ]

    def rows(self) -> int:
        """Gets the number of rows"""
        return len(self.grid)

    def cols(self) -> int:
        """Gets the number of columns"""
        return len(self.grid[0]) if self.rows() > 0 else 0

    def get_number_of_filled_cells(self) -> int:
        """Gets the number of filled cells"""

        count: int = 0

        for row in self.grid:
            for cell in row:
                if cell:
                    count += 1

        return count


@dataclass
class Region:
    """The region"""

    size_x: int
    size_y: int
    shape_index_quantaties: list[int]

    def is_successful(self, shapes: list[Shape]) -> bool:
        """Checks if the region is successful"""

        total_number_of_cells: int = self.size_x * self.size_y
        target_number_of_cells: int = 0

        for shape_index, target_quantity in enumerate(self.shape_index_quantaties):

            shape: Shape = shapes[shape_index]

            target_number_of_cells += (
                shape.get_number_of_filled_cells() * target_quantity
            )

            if target_number_of_cells > total_number_of_cells:
                return False

        print(
            f"Region size: {total_number_of_cells}, target cells: {target_number_of_cells }"
        )

        return target_number_of_cells * 1.3 <= total_number_of_cells


@dataclass
class ShapeGrid:
    """The shape grid"""

    shape: Shape

    index_x: int = 0
    index_y: int = 0

    def __init__(self, size_x, size_y):
        self.grid: list[list[bool]] = [
            [False for _ in range(size_x)] for _ in range(size_y)
        ]


@dataclass
class Presents:
    """The presents"""

    shapes: list[Shape]
    regions: list[Region]

    def get_num_successful_regions(self) -> int:
        """Gets the number of successful regions"""
        return sum(1 for region in self.regions if region.is_successful(self.shapes))


def get_shapes_from_lines(lines: list[str]) -> list[Shape]:
    """Gets the shapes from lines"""

    shapes: list[Shape] = []
    shape_index: int = -1
    row_index: int = 0

    for line in lines:

        if not line.strip():
            continue

        if line.find("x") > 0:
            break

        if line.find(":") > 0:
            shape_index += 1
            row_index = 0
            shapes.append(Shape(0, 0))
            shapes[shape_index].grid = []
            continue

        shapes[shape_index].grid.append([])

        for char in line:
            shapes[shape_index].grid[row_index].append(char == "#")

        row_index += 1

    return shapes


def get_regions_from_lines(lines: list[str]) -> list[Region]:
    """Gets the regions from lines"""

    regions: list[Region] = []

    for line in lines:
        if "x" in line and ":" in line:
            size, shapes_str = line.split(":")
            size_x_str, size_y_str = size.split("x")

            regions.append(
                Region(
                    size_x=int(size_x_str),
                    size_y=int(size_y_str),
                    shape_index_quantaties=[int(count) for count in shapes_str.split()],
                )
            )

    return regions


def get_presents_from_lines(lines: list[str]) -> Presents:
    """Gets the presents from lines"""

    return Presents(
        shapes=get_shapes_from_lines(lines), regions=get_regions_from_lines(lines)
    )


def get_result_part_1(data: str) -> int:
    """Gets the result"""

    lines: list[str] = get_lines(data)
    presents: Presents = get_presents_from_lines(lines)

    return presents.get_num_successful_regions()
