from gendiff.parsing import open_file
from gendiff.tree import make_tree
from gendiff.formatters import formatting


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """
    Returning the difference
    between two JSON/YML files in one of several formats.
    """

    data_1 = open_file(file_path1)
    data_2 = open_file(file_path2)
    tree = make_tree(data_1, data_2)
    diff = formatting(tree, format_name)
    return diff
