from gendiff import generate_diff


def test_format_json():
    data_1 = 'tests/fixtures/stylish/file1.json'
    data_2 = 'tests/fixtures/stylish/file2.json'
    expected = 'tests/fixtures/json/expected_json.txt'
    diff = print(generate_diff(data_1, data_2, 'json'))
    assert diff == print(expected)