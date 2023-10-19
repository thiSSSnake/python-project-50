import pytest 
from gendiff import generate_diff


def test_json():
    file_1 = 'tests/fixtures/plain/file1.json'
    file_2 = 'tests/fixtures/plain/file2.json'
    expected = 'tests/fixtures/plain/expected.txt'
    diff = print(generate_diff(file_1, file_2))
    assert diff == print(expected)


def test_yaml():
    file_1 = 'tests/fixtures/plain/file1.yml'
    file_2 = 'tests/fixtures/plain/file2.yml'
    expected = 'tests/fixtures/plain/expected.txt'
    diff = print(generate_diff(file_1, file_2))
    assert diff == print(expected)