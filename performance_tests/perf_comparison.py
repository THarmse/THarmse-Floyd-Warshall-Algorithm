from performance_tests.perf_iterative import test_performance_iterative
from performance_tests.perf_recursion import test_performance_recursion

def print_difference(iterative_value, recursive_value, metric_name, primary_unit, secondary_unit=None):
    """
    Print the difference between the iterative and recursive values for a given metric.
    """
    difference = recursive_value - iterative_value

    # For time, switch to microseconds if the difference is below 1 ms.
    if metric_name == "time" and abs(difference) < 0.001 and secondary_unit:
        difference *= 1e6  # Convert to microseconds
        unit = secondary_unit
    else:
        unit = primary_unit

    if difference > 0:
        print(f"Recursion uses {difference:.2f} {unit} more {metric_name} than Iterative.")
    elif difference < 0:
        print(f"Iterative uses {-difference:.2f} {unit} more {metric_name} than Recursion.")
    else:
        print(f"Both Iterative and Recursion use the same {metric_name}.")

def main():
    """
    Evaluate and compare the performance of the iterative and recursive implementations of the Floyd algorithm.
    This function triggers performance tests for both the iterative and recursive versions
    of the Floyd algorithm. It subsequently prints the duration, memory consumption, and CPU usage
    associated with each implementation, facilitating a comprehensive comparison.
    """

    # Capture performance metrics for the iterative approach.
    iterative_time, iterative_memory, iterative_cpu = test_performance_iterative()

    # Convert memory usage to MB for consistency
    iterative_memory_MB = iterative_memory / (1024 ** 2)

    # Capture performance metrics for the recursive approach.
    recursive_time, recursive_memory, recursive_cpu = test_performance_recursion()

    # Convert memory usage to MB for consistency
    recursive_memory_MB = recursive_memory / (1024 ** 2)

    # Display the performance results for the iterative approach.
    print(f"Iterative Time: {iterative_time:.6f} seconds")
    print(f"Iterative Memory Used: {iterative_memory_MB:.2f} MB")
    print(f"Iterative CPU Used: {iterative_cpu:.2f}%")
    print("-" * 50)

    # Display the performance results for the recursive approach.
    print(f"Recursion Time: {recursive_time:.6f} seconds")
    print(f"Recursion Memory Used: {recursive_memory_MB:.2f} MB")
    print(f"Recursion CPU Used: {recursive_cpu:.2f}%")

    # Add comparisons to show the differences
    print("\nPerformance Differences:")
    print_difference(iterative_time, recursive_time, "time", "seconds", "µs")
    print_difference(iterative_memory_MB, recursive_memory_MB, "memory", "MB")
    print_difference(iterative_cpu, recursive_cpu, "CPU usage", "%")

if __name__ == "__main__":
    # If the script is invoked as the main module, initiate the performance evaluation.
    main()
