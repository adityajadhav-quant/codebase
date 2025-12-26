# Find the largest integer X such that X appears exactly X times in the array.
# Examples:
# A = [3, 8, 2, 3, 3, 2] → 3 (3 appears 3 times)
# A = [7, 1, 2, 8, 2] → 2 (2 appears 2 times)
# A = [3, 1, 4, 1, 5] → 0 (no such X)

from collections import Counter

def find_largest_x_appearing_x_times(A):
    """
    Finds the largest integer X that appears exactly X times in the list A.

    Args:
        A (list of int): The input list of integers.

    Returns:
        int: The largest X where frequency of X equals X, or 0 if none exists.
    """
    if not A:
        return 0

    frequency_map = Counter(A)
    valid_numbers = [number for number, freq in frequency_map.items() if number == freq]

    if not valid_numbers:
        return 0

    return max(valid_numbers)
