# ------------------------------------------------------------
# Problem Explanation:
# You are given a sorted list of integers (A) and a target value (X).
# Your task is to return ANY index where X occurs in A.
# If X does not exist in A, return -1.
# ------------------------------------------------------------

def solution(numbers, target):
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


# ------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------

print(solution([1, 2, 5, 9, 9], 5))        # Expected: 2
print(solution([1, 2, 5, 9, 9], 1))        # Expected: 0
print(solution([1, 2, 5, 9, 9], 9))        # Expected: 3 or 4
print(solution([1, 2, 5, 9, 9], 7))        # Expected: -1
print(solution([], 10))                    # Expected: -1
print(solution([-10, -3, 0, 4, 8], -3))    # Expected: 1
print(solution([-10, -3, 0, 4, 8], 8))     # Expected: 4
