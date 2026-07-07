import pytest

from main import bubble_sort, sort_numbers, sum_of_squares


@pytest.mark.parametrize(
    "input_list,expected",
    [
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ([3, 1, 2], [1, 2, 3]),
        ([5, 5, 2, 2, 1], [1, 2, 2, 5, 5]),
        ([], []),
        ([1], [1]),
    ],
)
def test_bubble_sort_returns_sorted_list(input_list, expected):
    result = bubble_sort(input_list)
    assert result == expected
    assert input_list == expected


def test_bubble_sort_inplace_returns_same_object():
    data = [4, 2, 3]
    result = bubble_sort(data)
    assert result is data
    assert result == [2, 3, 4]


@pytest.mark.parametrize(
    "input_list,expected",
    [
        ([5, 4, 1], [1, 4, 5]),
        ([], []),
        ([2, -1, 0], [-1, 0, 2]),
        ([3, 3, 1], [1, 3, 3]),
    ],
)
def test_sort_numbers_returns_sorted_copy(input_list, expected):
    original = list(input_list)
    result = sort_numbers(input_list)
    assert result == expected
    assert input_list == original


@pytest.mark.parametrize(
    "values,expected",
    [
        ([1, 2, 3], 14),
        ([], 0),
        ([0, -1, 1], 2),
        ([1.5, 2.5], 8.5),
    ],
)
def test_sum_of_squares(values, expected):
    assert sum_of_squares(values) == expected
