import pytest
from gendiff import generate_diff
from correct_outputs import PLAIN


@pytest.mark.parametrize('input1, input2, expected', [
    (
        'tests/fixtures/nested_file1.json',
        'tests/fixtures/nested_file2.json',
        PLAIN
    ),
    (
        'tests/fixtures/nested_file1.yaml',
        'tests/fixtures/nested_file2.yaml',
        PLAIN
    )
])
def test_plain(input1, input2, expected):
    diff = generate_diff(input1, input2, 'plain')
    assert diff == expected
