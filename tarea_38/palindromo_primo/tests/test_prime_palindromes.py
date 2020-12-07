import pytest
from prime_palindromes import is_prime, is_palindrome, get_smallest_prime_palindrome

test_data_valid_prime = [2, 3, 7, 19, 29, 37, 53, 67, 79, 89, 97, 999359]

test_data_invalid_prime = [4, 8, 26, 42, 72, 254, 492, 507, 828, 945]


@pytest.mark.parametrize("num", test_data_valid_prime)
def test_correct_is_prime(num):
    output = is_prime(num)
    assert output is True


@pytest.mark.parametrize("num", test_data_invalid_prime)
def test_incorrect_is_prime(num):
    output = is_prime(num)
    assert output is False


test_data_valid_palindrome = [11, 22, 101, 5665, 1003001, 7765677]

test_data_invalid_palindrome = [28, 201, 5467, 124321]


@pytest.mark.parametrize("num", test_data_valid_palindrome)
def test_correct_is_palindrome(num):
    output = is_palindrome(num)
    assert output is True


@pytest.mark.parametrize("num", test_data_invalid_palindrome)
def test_incorrect_is_palindrome(num):
    output = is_palindrome(num)
    assert output is False

test_data = [
    (31, 101),
    (456789, 1003001)
]

@pytest.mark.parametrize("num, small_prime_palindrome",test_data)
def test_get_smallest_prime_palindrome(num, small_prime_palindrome):
    assert get_smallest_prime_palindrome(num)  == small_prime_palindrome