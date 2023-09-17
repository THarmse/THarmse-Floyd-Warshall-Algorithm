# Floyd Warshall Algorithm - Recursive & Iterative Implementation

This project contains Python implementations of the Floyd Warshall algorithm. It provides both iterative and recursive methods to determine the shortest paths between all pairs of vertices in a given weighted directed graph.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Unit Tests](#unit-tests)
- [Performance Testing](#performance-testing)
- [License](#license)

## Installation

1. Clone the repository:
\```
git clone https://github.com/THarmse/THarmse-Floyd-Warshall-Algorithm.git
\```
2. Navigate to the cloned directory:
\```
cd THarmse-Floyd-Warshall-Algorithm
\```
3. Install required packages:
\```
pip install -r requirements.txt
\```

## Usage

There are main scripts associated with the Floyd Warshall algorithm in this project:

- `iterative.py` - Contains the iterative implementation of the algorithm. (as referenced by University of Liverpool)
- `recursion.py` - Contains the recursive implementation of the algorithm.

To run any of the scripts, use:
\```
python <script_name>.py
\```

## Directory Structure
.
├── floyd_algorithm/
│   ├── __init__.py
│   ├── iterative.py
│   └── recursion.py
├── performance_tests/
│   ├── __init__.py
│   ├── perf_comparison.py
│   ├── perf_iterative.py
│   └── perf_recursion.py
├── unit_tests/
│   ├── __init__.py
│   ├── test_iterative.py
│   └── test_recursion.py
├── LICENSE
├── README.md
└── requirements.txt

## Unit Tests

To ensure the accuracy and reliability of both the iterative and recursive implementations, unit tests have been included:

- `test_iterative.py` - Contains unit tests for the iterative approach.
- `test_recursion.py` - Contains unit tests for the recursive approach.

To run the unit tests:
\```
python -m unittest <test_script_name>.py
\```

## Performance Testing

Each performance test script will provide metrics such as execution time, CPU percentage, and memory usage for its respective algorithm implementation. The comparison script offers insights into which method is more efficient under certain circumstances:

- `perf_iterative.py` - Performance testing for the iterative approach as used by perf_comparison.py.
- `perf_recursion.py` - Performance testing for the recursive approach as used by perf_comparison.py.
- `perf_comparison.py` - Compares the performance of both methods.

## License

This project is open-source. (MIT License) 
