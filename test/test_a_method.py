import pytest

from src.static_method import SomeClass


def test_a_method_is_five():
    some_class = SomeClass(some_dependency=5)
    assert some_class.a_method() == "some_dependency is 5"


@pytest.mark.parametrize("some_dependency", [10, 2])
def test_a_method_is_not_five(some_dependency):
    some_class = SomeClass(some_dependency=some_dependency)
    assert some_class.a_method() == "some_dependency is not 5"
