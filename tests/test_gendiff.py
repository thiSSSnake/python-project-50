import pytest 
from gendiff import generate_diff


def test_gendiff():
    file_1 = 'tests/fixtures/file1.json'
    file_2 = 'tests/fixtures/file2.json'
    expected = 'tests/fixtures/expected.txt'
    diff = print(generate_diff(file_1, file_2))
    assert diff == print(expected)