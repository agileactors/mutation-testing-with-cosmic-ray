import pytest

from src.multiply import multiply


@pytest.mark.parametrize(
    "number_1, number_2, expected_result",
    [(0, 11, 0), (2, 0.5, 1), (0.5, 0.25, 0.125), (-1, -2, 2), (-20, 12, -240)]
)
def test_multiply(number_1, number_2, expected_result):
    assert multiply(number_1, number_2) == expected_result