from gendiff.formatters.consts import NODE_TYPES


def get_indent(depth):
    return ' ' * (depth * 4 - 2)


def stringit(value, depth=0):
    """Turns value to string."""

    if isinstance(value, bool):
        return 'true' if value else 'false'

    if value is None:
        return 'null'

    if isinstance(value, dict):
        indent = get_indent(depth)
        current_indent = indent + (' ' * 6)
        lines = []
        for key, val in value.items():
            lines.append(f'{current_indent}{key}: {stringit(val, depth + 1)}')
        result = '\n'.join(lines)
        return f"{{\n{result}\n  {indent}}}"
    return value


def formatter(node, depth=0):  # noqa: C901
    """Return formatted data in the library's standart Stylish output."""

    children = node.get('children')
    indent = get_indent(depth)
    value = stringit(node.get('value'), depth)
    old_value = stringit(node.get('old_value'), depth)
    new_value = stringit(node.get('new_value'), depth)
    if node['type'] not in NODE_TYPES:
        raise ValueError(f"Invalid node type {node['type']}")
    if node['type'] == 'tree':
        lines = map(lambda child: formatter(child, depth + 1), children)
        result = '\n'.join(lines)
        if 'key' not in node:
            return f"{{\n{result}\n}}"
        else:
            return f"{indent}  {node['key']}: {{\n{result}\n  {indent}}}"
    if node['type'] == 'added':
        return f'{indent}+ {node["key"]}: {value}'
    if node['type'] == 'changed':
        line1 = f'{indent}- {node["key"]}: {old_value}\n'
        line2 = f'{indent}+ {node["key"]}: {new_value}'
        return line1 + line2
    if node['type'] == 'deleted':
        return f'{indent}- {node["key"]}: {value}'
    if node['type'] == 'unchanged':
        return f'{indent}  {node["key"]}: {value}'
    return f"{{\n{result}\n}}"
