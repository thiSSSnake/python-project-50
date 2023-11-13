import pytest
from gendiff import generate_diff
from correct_outputs import JSON


@pytest.mark.parametrize('input1, input2, expected', [
    (
        'tests/fixtures/nested_file1.json',
        'tests/fixtures/nested_file2.json',
        JSON
    ),
    (
        'tests/fixtures/nested_file1.yaml',
        'tests/fixtures/nested_file2.yaml',
        JSON
    )
])
def test_json(input1, input2, expected):
    diff = generate_diff(input1, input2, 'json')
    assert diff == expected
