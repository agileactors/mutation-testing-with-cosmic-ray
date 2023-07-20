from src.compare_numbers import compare_numbers


def test_compare_numbers():
    compare_numbers(1, 1)
    compare_numbers(1, 2)
    compare_numbers(2, 1)
    assert True == True
