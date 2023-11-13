import pytest
from gendiff import generate_diff
from correct_outputs import STYLISH


@pytest.mark.parametrize('input1, input2, expected', [
    (
        'tests/fixtures/nested_file1.json',
        'tests/fixtures/nested_file2.json',
        STYLISH
    ),
    (
        'tests/fixtures/nested_file1.yaml',
        'tests/fixtures/nested_file2.yaml',
        STYLISH
    )
])
def test_stylish(input1, input2, expected):
    diff = generate_diff(input1, input2, 'stylish')
    assert diff == expected
