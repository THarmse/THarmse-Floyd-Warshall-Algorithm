import unittest
from floyd_algorithm import iterative
import sys

# Define a constant to represent the absence of a path.
NO_PATH = sys.maxsize

# Sample graph matrix with distances. If no direct path exists between two nodes, it's denoted by `NO_PATH`.
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]
MAX_LENGTH = len(graph[0])  # Capture the size of the graph matrix for potential further tests.


class TestIterativeFloyd(unittest.TestCase):
    """
    Unit tests for the Floyd's iterative algorithm. (Test of the Original algorithm shared
    by University of Liverpool.

    This suite of tests checks the correctness of the Floyd's algorithm
    implemented in an iterative manner. The tests focus on verifying the
    shortest paths obtained from the algorithm.
    """

    def test_floyd(self):
        """
        Test the iterative Floyd algorithm for a given graph.

        This test case checks if the algorithm successfully computes the
        shortest paths between all pairs of nodes, comparing it with an
        expected result.
        """

        # Expected result matrix after Floyd's algorithm.
        expected = [
            [0, 7, 12, 8],
            [NO_PATH, 0, 5, 7],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]

        # Run the algorithm.
        result = iterative.floyd(graph)

        # Assert if the result matches the expected matrix.
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
