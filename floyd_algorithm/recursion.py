import sys


def floyds_recursive_approach(distance, current_row=0, current_col=0, intermediate=0):
    """
    Execute the Floyd-Warshall algorithm recursively to find shortest paths.

    The Floyd-Warshall algorithm determines the shortest paths between all pairs
    of vertices in a weighted graph. This recursive approach offers a unique twist
    on the traditional iterative version of the algorithm.

    Parameters:
    - distance (list of list of int): Represents the graph's weight matrix.
    - current_row (int, optional): Currently processing row. Defaults to 0.
    - current_col (int, optional): Currently processing column. Defaults to 0.
    - intermediate (int, optional): Currently processing intermediate vertex. Defaults to 0.

    Returns:
    - list of list of int: Matrix showcasing shortest path weights between nodes.
    """

    # Obtain the size of the matrix.
    matrix_size = len(distance)

    # Base case: if all intermediate nodes are processed, return the resultant matrix.
    if intermediate == matrix_size:
        return distance

    # Case: diagonal elements should be 0 as the distance between a node to itself is zero.
    if current_row == current_col:
        distance[current_row][current_col] = 0
    else:
        # Update distance between current_row and current_col if a shorter path is found
        # via the intermediate node.
        distance[current_row][current_col] = min(
            distance[current_row][current_col],
            distance[current_row][intermediate] + distance[intermediate][current_col]
        )

    # Recursion magic: traverse through the matrix rows and columns.
    if current_col + 1 < matrix_size:
        return floyds_recursive_approach(distance, current_row, current_col + 1, intermediate)
    elif current_row + 1 < matrix_size:
        return floyds_recursive_approach(distance, current_row + 1, 0, intermediate)
    else:
        # Move on to the next intermediate node once all matrix elements for the current one are processed.
        return floyds_recursive_approach(distance, 0, 0, intermediate + 1)
