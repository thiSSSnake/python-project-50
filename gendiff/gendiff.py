from gendiff.parsing import get_content
from gendiff.tree import gen_diff
from gendiff.formatters import formatting


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """
    Returning the difference
    between two JSON/YML files in one of several formats.
    """

    data_1 = get_content(file_path1)
    data_2 = get_content(file_path2)
    tree = gen_diff(data_1, data_2)
    diff = formatting(tree, format_name)
    return diff
