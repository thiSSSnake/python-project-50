import pytest
from gendiff import generate_diff


@pytest.mark.parametrize('input1, input2, expected, format', [
    (
        'tests/fixtures/nested_file1.json',
        'tests/fixtures/nested_file2.json',
        'tests/fixtures/expected_stylish',
        'stylish'
    ),
    (
        'tests/fixtures/nested_file1.yaml',
        'tests/fixtures/nested_file2.yaml',
        'tests/fixtures/expected_stylish',
        'stylish'
    )
])
def test_stylish(input1, input2, expected, format):
    diff = generate_diff(input1, input2, format)
    assert print(diff) == print(expected)
