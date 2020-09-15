import pytest
from recursion import factorial, binary_search, binary_sum
from math import factorial as math_factorial


@pytest.mark.parametrize("n", [0, 1, 2, 3, 10, 59])
def test_factorial(n):
    assert math_factorial(n) == factorial(n)


@pytest.mark.parametrize("array,target,result", [
    ([1, 2, 5, 6, 7], 1, 0),
    ([1, 2, 5, 6, 7], 6, 3),
    ([1, 2, 5, 6, 7], -3, None),
    ([], 0, None),
])
def test_binary_search(array, target, result):
    assert result == binary_search(array, target)


@pytest.mark.parametrize("array", [
    [1, 2, 4],
    [1],
    [10, -9, 4, 1],
    []
])
def test_binary_sum(array):
    assert sum(array) == binary_sum(array)
