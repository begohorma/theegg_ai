
import pytest
from conversor import decimal_to_binary

test_data = [
    (0, "0"),
    (1, "1"),
    (2, "10"),
    (3, "11"),
    (4, "100"),
    (5, "101"),
    (6,	"110"),
    (7,	"111"),
    (8,	"1000"),
    (9,	"1001"),
    (10, "1010"),
    (20, "10100"),
    (30, "11110"),
    (40, "101000"),
    (50, "110010"),
    (60, "111100"),
    (70, "1000110"),
    (80, "1010000"),
    (90, "1011010"),
    (100, "1100100"),
    (200, "11001000"),
    (300, "100101100"),
    (400, "110010000"),
    (500, "111110100"),
    (511, "111111111")
]


@pytest.mark.parametrize("num_dec,num_bin", test_data)
def test_decimal_to_binary(num_dec, num_bin):
    assert decimal_to_binary(num_dec) == num_bin
