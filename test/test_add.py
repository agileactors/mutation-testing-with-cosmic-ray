import pytest

from src.add import add


@pytest.mark.parametrize(
    "number_1, number_2, expected_result",
    [(10, 5, 15), (1, 0.252, 1.252), (-1, 10, 9), (11111, -320, 10791), (-0.25, -0.135, -0.385)],
)
def test_add(number_1, number_2, expected_result):
    assert add(number_1, number_2) == expected_result
