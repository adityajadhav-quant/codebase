from find_largest_x_appearing_x_times import find_largest_x_appearing_x_times
from binary_search_target import binary_search_target
from check_independence_and_compute_stats import check_independence_and_compute_stats
from reconstruct_missing_dice_rolls import reconstruct_missing_dice_rolls
from compare_nested_dicts import compare_nested_dicts
import pandas as pd


class TestFindLargestX:
    def test_example_1(self):
        assert find_largest_x_appearing_x_times([3, 8, 2, 3, 3, 2]) == 3

    def test_example_2(self):
        assert find_largest_x_appearing_x_times([7, 1, 2, 8, 2]) == 2

    def test_example_3(self):
        assert find_largest_x_appearing_x_times([3, 1, 4, 1, 5]) == 0

    def test_five_appears_five_times(self):
        assert find_largest_x_appearing_x_times([5, 5, 5, 5, 5]) == 5

    def test_empty_list(self):
        assert find_largest_x_appearing_x_times([]) == 0

    def test_one_appears_once(self):
        assert find_largest_x_appearing_x_times([1]) == 1

    def test_two_appears_twice(self):
        assert find_largest_x_appearing_x_times([2, 2]) == 2

    def test_four_appears_four_times(self):
        assert find_largest_x_appearing_x_times([4, 4, 4, 4]) == 4


class TestBinarySearchTarget:
    def test_found_at_middle(self):
        assert binary_search_target([1, 2, 5, 9, 9], 5) == 2

    def test_found_at_start(self):
        assert binary_search_target([1, 2, 5, 9, 9], 1) == 0

    def test_found_at_end(self):
        assert binary_search_target([1, 2, 5, 9, 9], 9) in [3, 4]

    def test_not_found(self):
        assert binary_search_target([1, 2, 5, 9, 9], 7) == -1

    def test_empty_list(self):
        assert binary_search_target([], 10) == -1

    def test_negative_numbers(self):
        assert binary_search_target([-10, -3, 0, 4, 8], -3) == 1

    def test_positive_found(self):
        assert binary_search_target([-10, -3, 0, 4, 8], 8) == 4


class TestCheckIndependence:
    def test_not_independent(self):
        table1 = pd.DataFrame({
            "X": [0, 0, 1, 1],
            "Y": [1, 2, 1, 2],
            "pr": [0.3, 0.25, 0.15, 0.3]
        })
        result = check_independence_and_compute_stats(table1)
        assert result["are_independent"] == False
        # Add assertions for cov and corr if needed

    def test_independent(self):
        table2 = pd.DataFrame({
            "X": [0, 0, 1, 1],
            "Y": [0, 1, 0, 1],
            "pr": [0.2, 0.3, 0.2, 0.3]
        })
        result = check_independence_and_compute_stats(table2)
        assert result["are_independent"] == True

    def test_perfect_correlation(self):
        table3 = pd.DataFrame({
            "X": [0, 1, 2],
            "Y": [0, 1, 2],
            "pr": [0.2, 0.5, 0.3]
        })
        result = check_independence_and_compute_stats(table3)
        assert result["are_independent"] == False  # Assuming not independent


class TestReconstructDice:
    def test_valid_case(self):
        result = reconstruct_missing_dice_rolls([3, 2, 4, 3], 2, 4)
        assert len(result) == 2
        assert all(1 <= r <= 6 for r in result)
        # Check mean
        total = sum([3, 2, 4, 3] + result)
        assert abs(total / 6 - 4) < 1e-6

    def test_impossible_case(self):
        assert reconstruct_missing_dice_rolls([1, 2, 3, 4], 6, 6) == [0]

    def test_another_impossible(self):
        assert reconstruct_missing_dice_rolls([6, 1], 1, 1) == [0]


class TestCompareNestedDicts:
    def test_simple_equal(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 1, 'b': 2}
        assert compare_nested_dicts(d1, d2) == True

    def test_simple_unequal(self):
        d1 = {'a': 1, 'b': 2}
        d3 = {'a': 1, 'b': 3}
        assert compare_nested_dicts(d1, d3) == False

    def test_nested_equal(self):
        d4 = {'a': 1, 'b': {'x': 10, 'y': 20}}
        d5 = {'a': 1, 'b': {'x': 10, 'y': 20}}
        assert compare_nested_dicts(d4, d5) == True

    def test_nested_unequal(self):
        d4 = {'a': 1, 'b': {'x': 10, 'y': 20}}
        d6 = {'a': 1, 'b': {'x': 10, 'y': 21}}
        assert compare_nested_dicts(d4, d6) == False

    def test_different_structure(self):
        d4 = {'a': 1, 'b': {'x': 10, 'y': 20}}
        d7 = {'a': 1, 'b': {'x': 10}}
        assert compare_nested_dicts(d4, d7) == False
