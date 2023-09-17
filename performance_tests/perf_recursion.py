import sys
import timeit
import psutil
from floyd_algorithm.recursion import floyds_recursive_approach

# A symbolic constant representing the absence of a direct path in the graph matrix.
NO_PATH = sys.maxsize

# Define the adjacency matrix for a given graph.
# Matrix entries represent direct weights between nodes.
# The special value `NO_PATH` indicates the lack of a direct connection.
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]


def test_performance_recursion():
    """
    Assess the performance of Floyd's recursive algorithm implementation
    as a method used by perf_comparison.py.

    This function benchmarks the recursive approach of the Floyd algorithm
    by capturing the time, memory, and CPU overhead during its run. It helps
    in gauging the computational and memory footprints when processing the given graph.

    Returns:
    - float: Duration in seconds taken by the algorithm.
    - int: Memory consumption (in bytes) during the algorithm's operation.
    - float: Percentage of CPU usage during the algorithm's run.
    """

    # Record the memory usage before initiating the algorithm.
    memory_before = psutil.virtual_memory().used

    # Log the CPU utilization preceding the algorithm's execution.
    # The interval parameter denotes the time span for computing the CPU percentage.
    cpu_before = psutil.cpu_percent(interval=1)

    # Determine the elapsed time while running the recursive Floyd algorithm.
    time_taken = timeit.timeit(lambda: floyds_recursive_approach(graph), number=1)

    # Fetch memory stats post algorithm execution.
    memory_after = psutil.virtual_memory().used

    # Register the CPU consumption following the algorithm's conclusion.
    cpu_after = psutil.cpu_percent(interval=1)

    # Compute the net memory and CPU usage during the algorithm's lifecycle.
    memory_used = memory_after - memory_before
    cpu_used = cpu_after - cpu_before

    return time_taken, memory_used, cpu_used
