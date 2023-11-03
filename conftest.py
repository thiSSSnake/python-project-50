import pytest


@pytest.fixture
def get_files_json():
    """Return JSON files."""

    file_1 = 'tests/fixtures/files/nested_file1.json'
    file_2 = 'tests/fixtures/files/nested_file2.json'
    return file_1, file_2


@pytest.fixture
def get_files_yaml():
    """Return YAML files."""

    file_1 = 'tests/fixtures/files/nested_file1.yaml'
    file_2 = 'tests/fixtures/files/nested_file2.yaml'
    return file_1, file_2


@pytest.fixture()
def get_expected_res_stylish():
    """Return expected result for default format - stylish."""

    file = 'tests/fixtures/stylish/expected_nested'
    return file


@pytest.fixture
def get_expected_res_plain():
    """Return expected result for plain format."""

    file = 'tests/fixtures/plain/expected.txt'
    return file


@pytest.fixture()
def get_result_json_format():
    """Return JSON-String"""

    result = 'tests/fixtures/json/expected_json.txt'
    return result
