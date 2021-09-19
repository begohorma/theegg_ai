import pytest

from aux_functions import *


@pytest.fixture()
def numbers():
    numbers = [5, 16, 2, 5, 57, 5, 2]
    return numbers


def test_get_list_elements_sum(numbers):
    assert get_list_elements_sum(numbers) == 92


def test_get_elements_frequency(numbers):
    assert get_elements_frequency(numbers) == [(5, 3), (16, 1), (2, 2), (57, 1)]
