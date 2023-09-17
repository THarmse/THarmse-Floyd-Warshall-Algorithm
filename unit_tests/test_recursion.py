import unittest
from floyd_algorithm import recursion
import sys

# Define a constant to denote the absence of a direct path between nodes.
NO_PATH = sys.maxsize

# Sample adjacency matrix of the graph, where distances between nodes are given.
# The value `NO_PATH` signifies no direct link between nodes.
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]
MAX_LENGTH = len(graph[0])  # Extract the dimension of the graph matrix for potential further tests or verifications.


class TestRecursiveFloyd(unittest.TestCase):
    """
    Unit tests for Floyd's recursive algorithm sa rewritten from Iterative algorithm.

    This test suite aims to validate the correctness of the Floyd's algorithm
    implemented using a recursive approach. The central focus is ensuring that
    the calculated shortest paths align with the expected outcomes.
    """

    def test_floyds_recursive_approach(self):
        """
        Verify the recursive Floyd algorithm on a predefined graph.

        The test ensures that the algorithm accurately identifies the
        shortest paths between all pairs of nodes and matches the provided
        expected result.
        """

        # Expected shortest-path matrix after applying Floyd's recursive algorithm.
        expected = [
            [0, 7, 12, 8],
            [NO_PATH, 0, 5, 7],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]

        # Execute the algorithm.
        result = recursion.floyds_recursive_approach(graph)

        # Confirm that the algorithm's output matches the expected matrix.
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
