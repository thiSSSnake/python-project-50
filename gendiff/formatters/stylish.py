def get_indent(depth):
    return ' ' * (depth * 4 + 2)


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


def formatter(data, depth=0):  # noqa: C901
    result = '{\n'
    indent = '  '
    for i in range(depth):
        indent += '    '
    for node in data:
        node_type = node['type']
        key = node['key']
        value = stringit(node.get('value'), depth)
        old_value = stringit(node.get('old_value'), depth)
        new_value = stringit(node.get('new_value'), depth)
        if node_type == 'tree':
            children = node['children']
            result += f"{indent}  {key}: {formatter(children, depth + 1)}\n"
        elif node_type == 'added':
            result += f"{indent}+ {key}: {value}\n"
        elif node_type == 'changed':
            result += f"{indent}- {key}: {old_value}\n"
            result += f"{indent}+ {key}: {new_value}\n"
        elif node_type == 'deleted':
            result += f"{indent}- {key}: {value}\n"
        elif node_type == 'unchanged':
            result += f"{indent}  {key}: {value}\n"
        else:
            raise ValueError(f"Invalid node type: {node_type}")
    result += indent[:-2] + "}"
    return result
