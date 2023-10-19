from gendiff.parsing import parsing_json, parsing_yaml
import itertools


def sort_keys(dict):
    new_dict = {}
    sorted_keys = sorted(dict.keys())
    for key in sorted_keys:
        new_dict[key] = dict[key]
    return new_dict


def stringify(value, replacer=' ', space_count=1):
    def inner_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value).lower()
        deep_indent_size = depth + space_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f"{deep_indent}{key}: {inner_(val, deep_indent_size)}")
        result = itertools.chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)
    return inner_(value, 0)


def get_diff(data_1, data_2):
    result = {}
    for key, _ in (data_1 | data_2).items():
        if key in data_1 and key in data_2:
            if data_1.get(key) == data_2.get(key):
                result[f"  {key}"] = data_1.get(key)
            else:
                result[f"- {key}"] = data_1.get(key)
                result[f"+ {key}"] = data_2.get(key)
        elif key in data_1 and key not in data_2:
            result[f"- {key}"] = data_1.get(key)
        elif key in data_2 and key not in data_1:
            result[f"+ {key}"] = data_2.get(key)
    return result


def generate_diff(file1, file2):
    if not parsing_yaml(file1, file2):
        f1, f2 = parsing_json(file1, file2)
    else:
        f1, f2 = parsing_yaml(file1, file2)
    data_1 = sort_keys(f1)
    data_2 = sort_keys(f2)
    result = get_diff(data_1, data_2)
    string = stringify(result, replacer=' ', space_count=2)
    return string
