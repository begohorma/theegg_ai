import pytest
from sort_algorithms import quick_sort_simple_version


@pytest.fixture()
def unordered_list():
    unordered_list = [3, 56, 33, 874, 123, 66, 1000, 23, 45, 56, 65]
    return unordered_list


def test_quick_sort_simple_version(unordered_list):
    output = quick_sort_simple_version(unordered_list)
    assert output == [3, 23, 33, 45, 56, 56, 65, 66, 123, 874, 1000]
