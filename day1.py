"""
Find the largest integer X such that X appears exactly X times in the array.

Examples: 
A = [3, 8, 2, 3, 3, 2] → 3 
A = [7, 1, 2, 8, 2] → 2
A = [3, 1, 4, 1, 5] → 0
"""

A = [7, 1, 2, 8, 2]

def solution(A):
  freq = {}
  # count the frequency of each number
  for x in A:
    if x in freq:
      freq[x] += 1
    else:
      freq[x] = 1
  # find the largest number whose freq equals to number
  answer = 0
  for x in freq:
    if freq[x] == x:
      answer = max(answer, x)
  return answer


def solution_opt(A):
  from collections import Counter

  frequency_map = Counter(A)
  valid_numbers = [number for number, freq in frequency_map.items() if number == freq]

  if not valid_numbers:
    return 0

  return max(valid_numbers)


# Test cases
print(solution([3, 8, 2, 3, 3, 2]))   # Expected output: 3
print(solution([7, 1, 2, 8, 2]))      # Expected output: 2
print(solution([3, 1, 4, 1, 5]))      # Expected output: 0
print(solution([5, 5, 5, 5, 5]))      # Expected output: 5
print(solution([]))                   # Expected output: 0
print(solution([1]))                  # Expected output: 1
print(solution([2, 2, 2]))            # Expected output: 0
print(solution([4, 4, 4, 4]))         # Expected output: 4
print(solution([1, 2, 2, 3, 3, 3]))   # Expected output: 3

print(solution_opt([3, 8, 2, 3, 3, 2]))   # Expected output: 3
print(solution_opt([7, 1, 2, 8, 2]))      # Expected output: 2
print(solution_opt([3, 1, 4, 1, 5]))      # Expected output: 0
print(solution_opt([5, 5, 5, 5, 5]))      # Expected output: 5
print(solution_opt([]))                   # Expected output: 0
print(solution_opt([1]))                  # Expected output: 1
print(solution_opt([2, 2, 2]))            # Expected output: 0
print(solution_opt([4, 4, 4, 4]))         # Expected output: 4
print(solution_opt([1, 2, 2, 3, 3, 3]))   # Expected output: 3
