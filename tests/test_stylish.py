from gendiff import generate_diff


def test_stylish_json():
    file_1 = 'tests/fixtures/stylish/file1.json'
    file_2 = 'tests/fixtures/stylish/file2.json'
    nested_file_1 = 'tests/fixtures/stylish/nested_file1.json'
    nested_file_2 = 'tests/fixtures/stylish/nested_file2.json'
    expected_1 = 'tests/fixtures/stylish/expected_plain.txt'
    expected_2 = 'tests/fixtures/stylish/expected_nested.txt'
    diff = print(generate_diff(file_1, file_2, 'stylish'))
    diff_2 = print(generate_diff(nested_file_1, nested_file_2, 'stylish'))
    assert diff == print(expected_1)
    assert diff_2 == print(expected_2)


def test_stylish_yml():
    file_1 = 'tests/fixtures/stylish/file1.yml'
    file_2 = 'tests/fixtures/stylish/file2.yml'
    nested_file_1 = 'tests/fixtures/stylish/nested_file1.yml'
    nested_file_2 = 'tests/fixtures/stylish/nested_file2.yml'
    expected_1 = 'tests/fixtures/stylish/expected_plain.txt'
    expected_2 = 'tests/fixtures/stylish/expected_nested.txt'
    diff = print(generate_diff(file_1, file_2, 'stylish'))
    diff_2 = print(generate_diff(nested_file_1, nested_file_2, 'stylish'))
    assert diff == print(expected_1)
    assert diff_2 == print(expected_2)