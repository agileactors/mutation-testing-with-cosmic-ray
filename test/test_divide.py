import pytest as pytest

from src.divide import divide


@pytest.mark.parametrize(
    "number_1, number_2, expected_result",
    [(10, 5, 2), (1, 2, 0.5), (0, 10, 0), (-11, -22, 0.5), (-10, 2, -5)],
)
def test_divide(number_1, number_2, expected_result):
    assert divide(number_1, number_2) == expected_result


def test_divide_zero_denominator():
    with pytest.raises(ZeroDivisionError) as e:
        divide(1, 0)

    assert str(e.value) == "division by zero"
