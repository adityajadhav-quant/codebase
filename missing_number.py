# ============================================================
#  FIND THE MISSING NUMBER IN A LIST
#  Problem: Numbers start at 1 and go till n (e.g. 1 to 10)
#           One number is missing. Find it.
#  Input  : lst = [1, 2, 3, 4, 5, 6, 8, 9, 10]
#  Answer : 7
# ============================================================

lst = [1, 2, 3, 4, 5, 6, 8, 9, 10]


# ─────────────────────────────────────────────────────────────
# APPROACH 1 — MATH FORMULA   Best 
# Concept  : Arithmetic series → sum of 1..n = n*(n+1)/2
# Time     : O(n)   — one pass to sum the list
# Space    : O(1)   — no extra data structure
# ─────────────────────────────────────────────────────────────

def find_missing_math(lst):
    n = max(lst)                    # largest number tells us the full range
    expected_sum = n * (n + 1) // 2 # sum of 1+2+3+...+n using formula
    actual_sum   = sum(lst)         # actual sum of the given list
    return expected_sum - actual_sum # the gap is exactly the missing number

print("Approach 1 - Math formula     :", find_missing_math(lst))   # 7


# ─────────────────────────────────────────────────────────────
# APPROACH 2 — XOR BIT TRICK
# Concept  : x ^ x = 0  (same number XORed cancels out)
#            x ^ 0 = x  (XOR with 0 keeps the number)
#            XOR all 1..n then XOR all list elements
#            → paired numbers cancel, only missing one survives
# Time     : O(n)   — two passes
# Space    : O(1)   — just one variable
# Why use  : Works even when sum overflows (important in C/Java)
# ─────────────────────────────────────────────────────────────

def find_missing_xor(lst):
    n = max(lst)

    xor_result = 0

    # XOR every number in the full range 1..n
    for i in range(1, n + 1):
        xor_result ^= i             # e.g. 1^2^3^4^5^6^7^8^9^10

    # XOR every number in the given list
    for x in lst:
        xor_result ^= x             # e.g. ^1^2^3^4^5^6^8^9^10

    # All numbers that appear in both cancel out (x^x=0)
    # Only the missing number remains (it was XORed once, never cancelled)
    return xor_result

print("Approach 2 - XOR bit trick    :", find_missing_xor(lst))    # 7


# ─────────────────────────────────────────────────────────────
# APPROACH 3 — SET DIFFERENCE
# Concept  : Convert both ranges to sets.
#            Set subtraction gives elements in one but not the other.
# Time     : O(n)   — set creation and difference are O(n)
# Space    : O(n)   — storing the full range as a set
# Bonus    : Naturally handles MULTIPLE missing numbers!
# ─────────────────────────────────────────────────────────────

def find_missing_set(lst):
    n        = max(lst)
    full_set = set(range(1, n + 1)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    lst_set  = set(lst)             # {1, 2, 3, 4, 5, 6, 8, 9, 10}
    return full_set - lst_set       # {7}  ← elements in full but not in list

print("Approach 3 - Set difference   :", find_missing_set(lst))    # {7}

# Bonus demo: works for multiple missing values too
lst_multi = [1, 3, 5, 7, 9]
n_multi   = max(lst_multi)
print("  Multi-missing example       :", set(range(1, n_multi+1)) - set(lst_multi))
# → {2, 4, 6, 8}


# ─────────────────────────────────────────────────────────────
# APPROACH 4 — SORT + LINEAR SCAN
# Concept  : After sorting, index i should hold value i+1.
#            First mismatch reveals the missing number.
#            Uses enumerate() to walk index and value together.
# Time     : O(n log n)  — dominated by the sort step
# Space    : O(1)        — sorted() can sort in-place; scan uses no extras
# ─────────────────────────────────────────────────────────────

def find_missing_sort_scan(lst):
    sorted_lst = sorted(lst)        # sort first so positions are predictable

    # enumerate gives (index, value) pairs: (0,1), (1,2), (2,3) ...
    for index, value in enumerate(sorted_lst):
        expected = index + 1        # at index 0 we expect 1, at index 1 we expect 2 …
        if value != expected:
            return expected         # first position where they don't match → missing

    return None                     # no missing number found

print("Approach 4 - Sort + scan      :", find_missing_sort_scan(lst))  # 7


# ─────────────────────────────────────────────────────────────
# APPROACH 4B — SORT + ZIP SCAN (cleaner version)
# Concept  : zip() walks two sequences in parallel.
#            Pair up range(1,n+1) with sorted list and find first divergence.
# ─────────────────────────────────────────────────────────────

def find_missing_zip(lst):
    n = max(lst)
    # zip stops at the shorter sequence, so range is one longer → catches last gap
    for expected, actual in zip(range(1, n + 1), sorted(lst)):
        if expected != actual:
            return expected
    return n + 1                    # edge case: missing number is n itself

print("Approach 4b - zip scan        :", find_missing_zip(lst))     # 7


# ─────────────────────────────────────────────────────────────
# APPROACH 5 — BINARY SEARCH  ⭐ Best when list is already sorted
# Concept  : In a sorted list with no missing number, lst[i] == i+1.
#            Once a number is missing, lst[i] > i+1 for all positions after it.
#            Binary search on this boolean property → O(log n)
# Time     : O(log n)  — if list is already sorted
# Space    : O(1)      — only two pointers
# ─────────────────────────────────────────────────────────────

def find_missing_binary_search(lst):
    # This assumes the list is already sorted!
    lo, hi = 0, len(lst) - 1

    while lo < hi:
        mid = (lo + hi) // 2       # integer division gives the middle index

        if lst[mid] == mid + 1:
            # No gap on the LEFT half (values match their positions)
            # Missing number must be on the RIGHT half
            lo = mid + 1
        else:
            # A gap exists somewhere in the LEFT half (or at mid itself)
            hi = mid

    # lo == hi now. Two cases:
    # • lst[lo] != lo+1 → gap is AT this position → missing = lo + 1
    # • lst[lo] == lo+1 → everything checked was fine → missing = lo + 2
    if lst[lo] != lo + 1:
        return lo + 1
    return lo + 2

print("Approach 5 - Binary search    :", find_missing_binary_search(lst))  # 7


# ─────────────────────────────────────────────────────────────
# APPROACH 6 — PYTHONIC ONE-LINERS
# Concept  : Python has powerful built-ins and generator expressions.
#            next() with a generator is lazy — stops at first match.
# ─────────────────────────────────────────────────────────────

def find_missing_oneliner(lst):
    n = max(lst)

    # --- 6A: List comprehension ---
    # Builds a list of all numbers in range that are NOT in the list
    # O(n) time, O(n) space
    missing_all = [i for i in range(1, n + 1) if i not in set(lst)]
    print("  6A list comprehension       :", missing_all)

    # --- 6B: filter() with lambda ---
    # filter() lazily applies the condition; list() forces evaluation
    # O(n) time, O(n) space
    lst_set = set(lst)
    missing_filter = list(filter(lambda x: x not in lst_set, range(1, n + 1)))
    print("  6B filter + lambda          :", missing_filter)

    # --- 6C: next() with generator ⭐ most efficient one-liner ---
    # Generator is LAZY — evaluates one at a time and stops immediately on first hit
    # No need to build the full list; stops as soon as it finds the first missing number
    # O(k) time where k = position of missing number, O(1) space
    missing_next = next(i for i in range(1, n + 1) if i not in lst_set)
    print("  6C next() + generator       :", missing_next)

    return missing_next

print("Approach 6 - One-liners:")
find_missing_oneliner(lst)


# ─────────────────────────────────────────────────────────────
# APPROACH 7 — DICTIONARY / HASH MAP (FREQUENCY COUNT)
# Concept  : Count frequency of each number using a dict.
#            Any number in 1..n with count 0 is missing.
#            Same idea as a set but shows dict usage.
# Time     : O(n)   — one pass to build dict, one pass to scan
# Space    : O(n)   — storing counts
# ─────────────────────────────────────────────────────────────

def find_missing_dict(lst):
    n = max(lst)

    # Build frequency map: {number: count}
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1   # .get(key, default) avoids KeyError

    # Scan 1..n and find the number with no entry in freq map
    for i in range(1, n + 1):
        if freq.get(i, 0) == 0:            # 0 means it never appeared
            return i

    return None

print("Approach 7 - Dictionary       :", find_missing_dict(lst))    # 7


# ─────────────────────────────────────────────────────────────
# APPROACH 8 — USING Counter (from collections)
# Concept  : collections.Counter auto-builds a frequency map.
#            Very Pythonic way to count occurrences.
# Time     : O(n)
# Space    : O(n)
# ─────────────────────────────────────────────────────────────

from collections import Counter

def find_missing_counter(lst):
    n       = max(lst)
    counts  = Counter(lst)          # Counter({1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 8:1, 9:1, 10:1})

    # Counter returns 0 for missing keys (unlike plain dict)
    for i in range(1, n + 1):
        if counts[i] == 0:          # this key was never in lst
            return i

    return None

print("Approach 8 - Counter          :", find_missing_counter(lst)) # 7


# ─────────────────────────────────────────────────────────────
# APPROACH 9 — NUMPY (for data science workflows)
# Concept  : NumPy's setdiff1d finds values in array A not in array B.
#            Vectorized C-level operations — very fast on large datasets.
# Time     : O(n log n)  — numpy uses sorted sets internally
# Space    : O(n)
# ─────────────────────────────────────────────────────────────

try:
    import numpy as np

    def find_missing_numpy(lst):
        n        = max(lst)
        full_arr = np.arange(1, n + 1)      # array([1, 2, 3, ..., 10])
        lst_arr  = np.array(lst)
        missing  = np.setdiff1d(full_arr, lst_arr)  # values in full not in lst
        return missing                               # array([7])

    print("Approach 9 - NumPy            :", find_missing_numpy(lst))  # [7]

except ImportError:
    print("Approach 9 - NumPy            : (numpy not installed, skipping)")


# ─────────────────────────────────────────────────────────────
# SUMMARY TABLE
# ─────────────────────────────────────────────────────────────
#
#  Approach              Time        Space   Notes
#  ─────────────────     ────────    ─────   ────────────────────────────────
#  1. Math formula       O(n)        O(1)    Best overall. Interview gold standard.
#  2. XOR bit trick      O(n)        O(1)    Best when overflow is a concern.
#  3. Set difference     O(n)        O(n)    Handles multiple missing values.
#  4. Sort + scan        O(n log n)  O(1)    Easy to understand; teaches enumerate/zip.
#  5. Binary search      O(log n)    O(1)    Best IF list is already sorted.
#  6. One-liners         O(n)        O(1/n)  Most Pythonic. next() stops early.
#  7. Dictionary         O(n)        O(n)    Teaches dict/hashmap usage.
#  8. Counter            O(n)        O(n)    Pythonic dict; auto-handles missing keys.
#  9. NumPy              O(n log n)  O(n)    Best for large arrays in data science.
#
# ─────────────────────────────────────────────────────────────
# KEY PYTHON CONCEPTS COVERED IN THIS FILE:
#   • Arithmetic formula          — n*(n+1)//2
#   • XOR / bit manipulation      — ^=, a^a=0, a^0=a
#   • Sets and set operations     — set(), difference (-)
#   • Sorting                     — sorted(), in-place sort()
#   • enumerate()                 — iterate with index and value
#   • zip()                       — iterate two sequences together
#   • Binary search               — lo/hi/mid pointer pattern
#   • List comprehensions         — [x for x in ... if ...]
#   • Generator expressions       — (x for x in ... if ...)
#   • next()                      — lazy evaluation, stops at first match
#   • filter() + lambda           — functional style filtering
#   • Dictionary / hash map       — {}, .get(key, default)
#   • Counter                     — collections.Counter
#   • NumPy arrays                — np.arange, np.setdiff1d
# ─────────────────────────────────────────────────────────────
