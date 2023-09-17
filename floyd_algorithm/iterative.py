import sys
import itertools

NO_PATH = sys.maxsize

def floyd(distance):
    """
    A simple implementation of Floyd's algorithm. (As per the PDF from University of Liverpool)
    """
    MAX_LENGTH = len(distance[0])

    for intermediate, start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        # Return all possible paths and find the minimum
        distance[start_node][end_node] = min(
            distance[start_node][end_node],
            distance[start_node][intermediate] + distance[intermediate][end_node]
        )
    # For testing and other usages, it's better to return the modified matrix
    return distance
