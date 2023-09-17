from perf_iterative import test_performance_iterative
from perf_recursion import test_performance_recursion


def main():
    """
    Evaluate and compare the performance of the iterative and recursive implementations of the Floyd algorithm.

    This function triggers performance tests for both the iterative and recursive versions
    of the Floyd algorithm. It subsequently prints the duration, memory consumption, and CPU usage
    associated with each implementation, facilitating a comprehensive comparison.
    """

    # Capture performance metrics for the iterative approach.
    iterative_time, iterative_memory, iterative_cpu = test_performance_iterative()

    # Capture performance metrics for the recursive approach.
    recursive_time, recursive_memory, recursive_cpu = test_performance_recursion()

    # Display the performance results for the iterative approach.
    print(f"Iterative Time: {iterative_time:.6f} seconds")
    print(f"Iterative Memory Used: {iterative_memory / (1024 ** 2):.2f} MB")
    print(f"Iterative CPU Used: {iterative_cpu:.2f}%")
    print("-" * 50)

    # Display the performance results for the recursive approach.
    print(f"Recursion Time: {recursive_time:.6f} seconds")
    print(f"Recursion Memory Used: {recursive_memory / (1024 ** 2):.2f} MB")
    print(f"Recursion CPU Used: {recursive_cpu:.2f}%")


if __name__ == "__main__":
    # If the script is invoked as the main module, initiate the performance evaluation.
    main()
