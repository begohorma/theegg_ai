import pytest
from search_algorithms import linear_search, binary_search


@pytest.fixture()
def unordered_list():
    unordered_list = [3, 56, 33, 874, 123, 66, 1000, 23, 45, 56, 65]
    return unordered_list


@pytest.fixture()
def ordered_list():
    ordered_list = [3, 23, 33, 45, 56, 56, 65, 66, 123, 874, 1000]
    return ordered_list


def test_linear_search_not_found(unordered_list):
    output = linear_search(unordered_list, 875)
    assert output == 11


def test_linear_search_found_first_position(unordered_list):
    output = linear_search(unordered_list, 3)
    assert output == 1


def test_linear_search_found_last_position(unordered_list):
    output = linear_search(unordered_list, 65)
    assert output == 11


def test_linear_search_found_mid_position(unordered_list):
    output = linear_search(unordered_list, 66)
    assert output == 6


def test_binary_search_not_found(ordered_list):
    output = binary_search(ordered_list, 875)
    assert output == 4


def test_binary_search_found_first_position(ordered_list):
    output = binary_search(ordered_list, 3)
    assert output == 3


def test_binary_search_found_last_position(ordered_list):
    output = binary_search(ordered_list, 1000)
    assert output == 4


def test_binary_search_found_mid_position(ordered_list):
    output = binary_search(ordered_list, 56)
    assert output == 1
