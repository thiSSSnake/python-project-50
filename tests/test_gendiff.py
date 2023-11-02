from gendiff import generate_diff


def test_stylish_json(get_files_json, get_expected_res_stylish):
    file_1, file_2 = get_files_json
    expected = get_expected_res_stylish
    diff = print(generate_diff(file_1, file_2, 'stylish'))
    assert diff == print(expected)


def test_stylish_yml(get_files_yaml, get_expected_res_stylish):
    file_1, file_2 = get_files_yaml
    expected = get_expected_res_stylish
    diff = print(generate_diff(file_1, file_2, 'stylish'))
    assert diff == print(expected)


def test_plain_json(get_files_json, get_expected_res_plain):
    file_1, file_2 = get_files_json
    expected = get_expected_res_plain
    diff = print(generate_diff(file_1, file_2, 'plain'))
    assert diff == print(expected)


def test_plain_yml(get_files_yaml, get_expected_res_plain):
    file_1, file_2 = get_files_yaml
    expected = get_expected_res_plain
    diff = print(generate_diff(file_1, file_2, 'plain'))
    assert diff == print(expected)


def test_format_json(get_files_json, get_result_json_format):
    file_1, file_2 = get_files_json
    result = get_result_json_format
    diff = print(generate_diff(file_1, file_2, 'json'))
    assert diff == print(result)