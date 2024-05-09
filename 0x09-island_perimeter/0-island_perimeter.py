#!/usr/bin/python3
"""
Module calculates the perimeter of a single island in a grid.
"""
def island_perimeter(grid):
    """
    Calculates the perimeter of an island represented by a grid.

    Args:
        grid: A 2D grid representing the island.

    Returns:
        int: The perimeter of the island.

    """
    perimeter = 0

    if not isinstance(grid, list):
        return 0

    rows = len(grid)
    for i, row in enumerate(grid):
        cols = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue

            # Check for edges around the cell
            top_edge = (i == 0 or grid[i - 1][j] == 0)
            right_edge = (j == cols - 1 or row[j + 1] == 0)
            bottom_edge = (i == rows - 1 or grid[i + 1][j] == 0)
            left_edge = (j == 0 or row[j - 1] == 0)

            # Increment perimeter based on edges
            perimeter += top_edge + right_edge + bottom_edge + left_edge

    return perimeter