import sys
import timeit
import psutil
from floyd_algorithm.iterative import floyd

# Define a symbolic representation for absent paths in the graph matrix.
NO_PATH = sys.maxsize

# A representative adjacency matrix for a weighted graph.
# Elements indicate the direct path weight between nodes.
# A value of `NO_PATH` denotes that no direct path exists.
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]


def test_performance_iterative():
    """
    Evaluate the performance of the iterative Floyd algorithm as a
    method used by perf_comparison.py.

    This function gauges the efficiency of the Floyd algorithm
    implemented iteratively by measuring time, memory, and CPU usage
    before and after its execution. It provides insights into the
    computational cost associated with the algorithm on the predefined graph.

    Returns:
    - float: Time taken for the algorithm's execution in seconds.
    - int: Amount of memory utilized (in bytes) during the algorithm's execution.
    - float: CPU percentage usage during the algorithm's execution.
    """

    # Capture memory utilization prior to algorithm execution.
    memory_before = psutil.virtual_memory().used

    # Assess CPU utilization before execution. The interval denotes
    # the duration for which CPU usage is computed.
    cpu_before = psutil.cpu_percent(interval=1)

    # Time the algorithm's execution to assess its efficiency.
    time_taken = timeit.timeit(lambda: floyd(graph), number=1)

    # Measure memory consumption post-algorithm execution.
    memory_after = psutil.virtual_memory().used

    # Evaluate CPU utilization after the execution completes.
    cpu_after = psutil.cpu_percent(interval=1)

    # Compute the difference in metrics before and after to derive the exact usage.
    memory_used = memory_after - memory_before
    cpu_used = cpu_after - cpu_before

    return time_taken, memory_used, cpu_used
