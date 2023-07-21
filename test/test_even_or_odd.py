import pytest

from src.even_or_odd import even_or_odd


@pytest.mark.parametrize(
    "number, expected_result",
    [(0, "Even"), (2, "Even"), (5, "Odd"), (15, "Odd"), (-2, "Even"), (-5, "Odd")]
)
def test_even_or_odd(number, expected_result):
    assert even_or_odd(number) == expected_result


@pytest.mark.parametrize("number", [1.5, 0.5])
def test_even_or_odd_float(number):
    with pytest.raises(ValueError) as e:
        even_or_odd(number)

    assert str(e.value) == "Number must be an integer"
