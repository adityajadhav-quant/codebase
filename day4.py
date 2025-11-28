"""
PROBLEM:
You rolled the dice several times. You remember N results (array A).
There are F rolls missing, and the arithmetic mean of ALL rolls equals M.

We must reconstruct any valid list of F integers (each between 1 and 6)
representing the missing dice rolls.

-----------------------------------------------
Let:
- known_sum = sum(A)
- total_rolls = N + F
- target_total_sum = M * total_rolls
- missing_sum = target_total_sum - known_sum

We must split missing_sum into F dice values in [1..6].

Valid range for total missing sum:
    minimum_possible = 1*F
    maximum_possible = 6*F

If missing_sum is outside this range → impossible → return [0].

Otherwise:
- Start assigning missing dice as 1
- Increase each value up to 6 until the total sum matches missing_sum

Return any valid list of size F.

-----------------------------------------------
Return:
- a list of F integers (1..6), OR
- [0] if no valid solution exists
"""

def solution(A, F, M):
    known_sum = sum(A)
    total_rolls = len(A) + F
    target_total_sum = M * total_rolls
    required_missing_sum = target_total_sum - known_sum

    # The missing sum must fit within F dice values (each 1..6)
    min_possible = F * 1
    max_possible = F * 6

    # If a required sum is impossible → no solution
    if not (min_possible <= required_missing_sum <= max_possible):
        return [0]

    # Build the answer starting with all dice set to 1
    missing_rolls = [1] * F
    remaining_sum = required_missing_sum - F  # we already placed F ones

    # Distribute remaining_sum by increasing dice values up to 6
    idx = 0
    while remaining_sum > 0 and idx < F:
        addable = min(5, remaining_sum)  # max we can add to a '1' is +5 (to reach 6)
        missing_rolls[idx] += addable
        remaining_sum -= addable
        idx += 1

    return missing_rolls


print(solution([3, 2, 4, 3], 2, 4)) # [6, 6]
print(solution([1, 2, 3, 4], 6, 6)) # [0]
print(solution([6, 1], 1, 1)) # [0]

