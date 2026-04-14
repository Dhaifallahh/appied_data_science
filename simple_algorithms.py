"""Simple algorithm examples for learning Python.

This file shows beginner-friendly implementations of common algorithms.
"""


def linear_search(items, target):
    """Return index of target using linear search, or -1 if not found."""
    for index, value in enumerate(items):
        if value == target:
            return index
    return -1


def binary_search(sorted_items, target):
    """Return index of target in a sorted list using binary search, else -1."""
    left = 0
    right = len(sorted_items) - 1

    while left <= right:
        middle = (left + right) // 2

        if sorted_items[middle] == target:
            return middle
        if sorted_items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def bubble_sort(items):
    """Return a new list sorted in ascending order using bubble sort."""
    result = items[:]  # copy the list so we do not change the original
    n = len(result)

    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:  # optimization: stop early if already sorted
            break

    return result


def factorial(n):
    """Return n! (factorial) for non-negative integers."""
    if n < 0:
        raise ValueError("factorial is only defined for n >= 0")

    result = 1
    for number in range(2, n + 1):
        result *= number
    return result


def fibonacci(n):
    """Return first n Fibonacci numbers as a list."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


if __name__ == "__main__":
    sample_numbers = [7, 2, 9, 1, 5]
    sorted_numbers = bubble_sort(sample_numbers)

    print("Original:", sample_numbers)
    print("Bubble sort:", sorted_numbers)
    print("Linear search (9):", linear_search(sample_numbers, 9))
    print("Binary search (5):", binary_search(sorted_numbers, 5))
    print("Factorial (5):", factorial(5))
    print("Fibonacci (10):", fibonacci(10))
