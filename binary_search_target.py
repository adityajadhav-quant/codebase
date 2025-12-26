# ------------------------------------------------------------
# Problem Explanation:
# You are given a sorted list of integers (numbers) and a target value.
# Your task is to return ANY index where target occurs in numbers.
# If target does not exist in numbers, return -1.
# ------------------------------------------------------------

def binary_search_target(numbers, target):
    """
    Performs binary search to find any index of the target in a sorted list.

    Args:
        numbers (list of int): A sorted list of integers.
        target (int): The value to search for.

    Returns:
        int: Any index where target is found, or -1 if not found.
    """
    length = len(numbers)
    if length == 0:
        return -1

    left = 0
    right = length - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1
