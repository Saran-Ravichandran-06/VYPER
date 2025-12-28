# Helper functions
def flatten_2d_list(matrix):
    """
    Converts 2D grid into 1D list.
    Useful for debugging or analytics.
    """
    return [cell for row in matrix for cell in row]


def count_symbol(grid, symbol):
    """
    Counts occurrences of a symbol in the grid.
    """
    count = 0
    for row in grid:
        count += row.count(symbol)
    return count
