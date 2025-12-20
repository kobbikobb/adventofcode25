from dataclasses import dataclass

from _utils.text_utils import get_lines


@dataclass
class Shape:
    """A shape"""

    grid: list[list[bool]]

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

    def get_rotated_shape(self) -> "Shape":
        """Gets the rotated shape"""

        rotated_shape: Shape = Shape(size_x=self.rows(), size_y=self.cols())

        for row_index, row in enumerate(self.grid):
            for col_index, cell in enumerate(row):
                rotated_shape.grid[col_index][self.rows() - 1 - row_index] = cell

        return rotated_shape

    def get_flipped_shape(self) -> "Shape":
        """Gets the flipped shape"""

        flipped_shape: Shape = Shape(size_x=self.rows(), size_y=self.cols())

        for row_index, row in enumerate(self.grid):
            for col_index, cell in enumerate(row):
                flipped_shape.grid[row_index][self.cols() - 1 - col_index] = cell

        return flipped_shape


@dataclass
class Region:
    """The region"""

    size_x: int
    size_y: int
    shape_index_quantaties: list[int]

    def is_successful(self, shapes: list[Shape]) -> bool:
        """Checks if the region is successful"""

        grid: ShapeGrid = ShapeGrid(self.size_x, self.size_y)

        for shape_index, target_quantity in enumerate(self.shape_index_quantaties):

            shape: Shape = shapes[shape_index]

            for _ in range(target_quantity):

                if grid.can_place_shape(shape):
                    grid.place_shape(shape)
                    grid.index_x += shape.cols()
                    grid.index_y += shape.rows()
                    continue

                rotated: Shape = shape.get_rotated_shape()
                if grid.can_place_shape(rotated):
                    grid.place_shape(rotated)
                    grid.index_x += rotated.cols()
                    grid.index_y += rotated.rows()
                    continue

                flipped: Shape = shape.get_flipped_shape()
                if grid.can_place_shape(flipped):
                    grid.place_shape(flipped)
                    grid.index_x += flipped.cols()
                    grid.index_y += flipped.rows()
                    continue

                return False

        return True


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

    def can_place_shape(self, shape: Shape) -> bool:
        """Checks if it can place shape in the grid"""

        for row_index, row in enumerate(shape.grid):
            for col_index, cell in enumerate(row):
                if cell:
                    grid_row = self.index_y + row_index
                    grid_col = self.index_x + col_index

                    if (
                        grid_row >= len(self.grid)
                        or grid_col >= len(self.grid[grid_row])
                        or self.grid[grid_row][grid_col]
                    ):
                        return False
        return True

    def place_shape(self, shape: Shape):
        """Places the shape on the grid"""

        for row_index, row in enumerate(shape.grid):
            for col_index, cell in enumerate(row):
                if cell:
                    grid_row = self.index_y + row_index
                    grid_col = self.index_x + col_index

                    if self.grid[grid_row][grid_col]:
                        raise ValueError("Cannot place shape here.")
                    self.grid[grid_row][grid_col] = True


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

        if line.find("x") > 0:
            break

        if line.find(":") > 0:
            shape_index += 1
            row_index = 0
            shapes.append(Shape(0, 0))
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
        x: int = line.find("x")
        if x > 0:
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
