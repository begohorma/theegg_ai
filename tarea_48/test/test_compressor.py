import pytest
from compressor import Compressor

test_data_compress = [
    ("ababababababababababababababab", [(0, 0, 'a'), (0, 0, 'b'), (2, 2, 'a'), (4, 4, 'b'), (10, 10, 'a'), (8, 8, 'b')]),
    ("abracadabraarray abracadabra", [(0, 0, 'a'), (0, 0, 'b'), (0, 0, 'r'), (3, 1, 'c'), (2, 1, 'd'), (7, 4, 'a'), (3, 1, 'r'), (3, 1, 'y'), (0, 0, ' '), (17, 10, 'a')]),
    ("abcdabcdabcdabcdabcdabcdabcdab", [(0, 0, 'a'), (0, 0, 'b'), (0, 0, 'c'), (0, 0, 'd'), (4, 4, 'a'), (8, 8, 'b'), (12, 11, 'b')]),
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", [(0, 0, 'a'), (1, 1, 'a'), (3, 3, 'a'), (7, 7, 'a'), (15, 15, 'a'), (31, 31, 'a'), (7, 7, 'a')]),
    ("abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",[(0, 0, 'a'), (0, 0, 'b'), (0, 0, 'c'), (0, 0, 'd'), (4, 4, 'a'), (8, 8, 'b'), (16, 16, 'c'), (32, 32, 'd'), (68, 68, 'a'), (136, 136, 'b'), (28, 25, 'd')])
]

test_data_decompress = [
    ([(0, 0, 'a'), (0, 0, 'b'), (2, 2, 'a'), (4, 4, 'b'), (10, 10, 'a'), (8, 8, 'b')], "ababababababababababababababab"),
    ([(0, 0, 'a'), (0, 0, 'b'), (0, 0, 'r'), (3, 1, 'c'), (2, 1, 'd'), (7, 4, 'a'), (3, 1, 'r'), (3, 1, 'y'), (0, 0, ' '), (17, 10, 'a')],"abracadabraarray abracadabra"),
    ([(0, 0, 'a'), (0, 0, 'b'), (0, 0, 'c'), (0, 0, 'd'), (4, 4, 'a'), (8, 8, 'b'), (12, 11, 'b')],"abcdabcdabcdabcdabcdabcdabcdab"),
    ([(0, 0, 'a'), (1, 1, 'a'), (3, 3, 'a'), (7, 7, 'a'), (15, 15, 'a'), (31, 31, 'a'), (7, 7, 'a')],"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"),
    ([(0, 0, 'a'), (0, 0, 'b'), (0, 0, 'c'), (0, 0, 'd'), (4, 4, 'a'), (8, 8, 'b'), (16, 16, 'c'), (32, 32, 'd'), (68, 68, 'a'), (136, 136, 'b'), (28, 25, 'd')],"abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd")
]


@pytest.mark.parametrize("original_text, compressed_text", test_data_compress)
def test_compress_default_window_and_buffer_size(original_text, compressed_text):
    c = Compressor()
    assert c.compress(original_text) == compressed_text


@pytest.mark.parametrize("compressed_text, decompressed_text", test_data_decompress)
def test_descompress(compressed_text, decompressed_text):
    c = Compressor()
    assert c.decompress(compressed_text) == decompressed_text
