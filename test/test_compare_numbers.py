import pytest as pytest

from src.compare_numbers import compare_numbers


@pytest.mark.parametrize(
    "number_1, number_2, expected_result",
    [
        (10, 5, "greater than"),
        (1, 2, "less than"),
        (0, 10, "less than"),
        (-11, -22, "greater than"),
        (-10, 2, "less than"),
        (0, 0, "equal to"),
        (-0.5, -0.5, "equal to")
    ]
)
def test_compare_numbers(number_1, number_2, expected_result):
    assert compare_numbers(number_1, number_2) == f"{number_1} is {expected_result} {number_2}"
