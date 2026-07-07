"""
Simple collection of sorting and numeric utilities.

Includes:
- bubble_sort: basic bubble sort algorithm
- sort_numbers: built-in sorting wrapper
- sum_of_squares: sum of squares computation
"""

def bubble_sort(arr: list) -> list:
    """Basic bubble sort implementation that returns a sorted list."""
    # Refactored bubble sort: uses last-swap tracking to shrink the pass range.
    n = len(arr)
    while n > 1:
        last_swap = 0
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                last_swap = i
        n = last_swap
    return arr


def sort_numbers(arr: list) -> list:
    """Return a sorted copy of the given list."""
    return sorted(arr)


def sum_of_squares(numbers: list) -> float:
    """Return the sum of squares of the given numbers."""
    # Simplified implementation using a generator expression.
    return sum(x * x for x in numbers)


if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(sample))
    print(sum_of_squares(sample))