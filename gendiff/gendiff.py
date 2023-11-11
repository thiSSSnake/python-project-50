import os
from gendiff.parsing import parse_files
from gendiff.tree import make_tree
from gendiff.formatters.stylish import formatter
from gendiff.formatters.plain import formatter_plain
from gendiff.formatters.format_js import format_js


def get_extension(file: str):
    """Get extension of file path (string value)."""

    f = file
    _, extension = os.path.splitext(f)
    return extension


def get_file_data(file: str):
    """Get file data."""

    file_extension = get_extension(file)
    file_data = parse_files(file, file_extension)
    return file_data


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """
    Returning the difference
    between two JSON/YML files in one of several formats.
    """

    data_1 = dict(get_file_data(file_path1))
    data_2 = dict(get_file_data(file_path2))
    diff = make_tree(data_1, data_2)
    if format_name == 'stylish':
        result = formatter(diff)
        return result
    if format_name == 'plain':
        result = formatter_plain(diff)
        return result
    if format_name == 'json':
        result = format_js(diff)
        return result
