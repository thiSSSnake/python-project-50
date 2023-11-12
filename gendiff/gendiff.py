import os
from gendiff.parsing import parse_files
from gendiff.tree import make_tree
from gendiff.formatters import formatting


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
    tree = make_tree(data_1, data_2)
    diff = formatting(tree, format_name)
    return diff
