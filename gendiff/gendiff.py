from gendiff.parsing import parsing_json, parsing_yaml
from gendiff.tree import make_tree
from gendiff.formatters.stylish import format
from gendiff.formatters.plain import plain_format
from gendiff.formatters.format_js import format_js


def generate_diff(file1, file2, format_name='stylish'):
    """
    Returning the difference
    between two JSON/YML files in one of several formats.
    """

    data_1 = parsing_json(file1)
    data_2 = parsing_json(file2)
    if not data_1:
        data_1 = parsing_yaml(file1)
    if not data_2:
        data_2 = parsing_yaml(file2)
    diff = make_tree(data_1, data_2)
    if format_name == 'stylish':
        result = format(diff)
        return result
    if format_name == 'plain':
        result = plain_format(diff)
        return result
    if format_name == 'json':
        result = format_js(diff)
        return result
