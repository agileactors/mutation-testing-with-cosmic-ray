import pytest

from src.substract import subtract


@pytest.mark.parametrize(
    "number_1, number_2, expected_result",
    [(0, 11, -11), (2, 0.5, 1.5), (0.5, 0.25, 0.25), (-1, -2, 1), (-20, 12, -32)]
)
def test_subtract(number_1, number_2, expected_result):
    assert subtract(number_1, number_2) == expected_result