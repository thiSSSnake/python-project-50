def to_string(value):

    """
    The same as the 'stringit' function,
    but instead of full nested data, [complex value] is returned.
    """

    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, int):
        return value
    return f"'{value}'"


def formatter_plain(tree, path=''):
    """Return formatted data in Plain output."""
    result = []
    for node in tree:
        node_type = node['type']
        value = to_string(node.get('value'))
        old_value = to_string(node.get('old_value'))
        new_value = to_string(node.get('new_value'))
        curr_path = f'{path}{node.get("key")}'
        if node_type == 'tree':
            children = node["children"]
            lines = formatter_plain(children, f"{curr_path}.")
            result.append(lines)
        elif node_type == 'added':
            result.append(f"Property '{curr_path}' was added with value: {value}")  # noqa: E501
        elif node_type == 'deleted':
            result.append(f"Property '{curr_path}' was removed")
        elif node_type == 'changed':
            result.append(f"Property '{curr_path}' was updated. From {old_value} to {new_value}")  # noqa: E501
    return '\n'.join(result)
