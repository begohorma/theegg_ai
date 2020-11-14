import pytest
from biologo import find_common_sequence, find_occurrences, check_new_candidate

test_data_secuences = [
    ("ctgactga", "actgagc", "actga"),  # 8 - 7 fin- inicio
    ("cgtaattgcgat", "cgtacagtagc", "cgta"),  # 12 - 11  inicio - inicio
    ("ctgggccttgaggaaaactg", "gtaccagtactgatagt", "actg"),  # 20  - 17 fin medio
    ("aacgt", "cgt", "cgt"),  # 5 - 3 fin-fin
    ("a", "a", "a"),
    ("a", "c", "")
]

test_data_occurrences = [
    ("c", "ctgactga", [0, 4]),
    ("t", "ctgactga", [1, 5]),
    ("a", "ctgactga", [3, 7]),
    ("g", "ctgactga", [2, 6])

]

test_data_candidate = [
    ("c", "ctga", "ctga"),
    ("", "a", "a"),
    ("a", " ", "a"),
    ("ctga", "actga", "actga")
]


@pytest.mark.parametrize("seq1, seq2, common_seq", test_data_secuences)
def test_find_common_sequence(seq1, seq2, common_seq):
    assert find_common_sequence(seq1, seq2) == common_seq


@pytest.mark.parametrize("car,  string, indices", test_data_occurrences)
def test_find_occurrences(car, string, indices):
    assert find_occurrences(car, string) == indices


@pytest.mark.parametrize("candidate, new_candidate, final_candidate", test_data_candidate)
def test_check_new_candidate(candidate, new_candidate, final_candidate):
    assert check_new_candidate(candidate, new_candidate) == final_candidate
