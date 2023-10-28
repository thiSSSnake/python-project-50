from gendiff.parsing import parsing_json, parsing_yaml
from gendiff.tree import make_tree
from gendiff.stylish import format


def generate_diff(file1, file2):
    data_1 = parsing_json(file1)
    data_2 = parsing_json(file2)
    if not data_1:
        data_1 = parsing_yaml(file1)
    if not data_2:
        data_2 = parsing_yaml(file2)
    diff = make_tree(data_1, data_2)
    result = format(diff)
    return result
