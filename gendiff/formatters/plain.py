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


def formatter_plain(node, path=''):
    """Return formatted data in Plain output."""

    children = node.get('children')
    value = to_string(node.get('value'))
    old_value = to_string(node.get('old_value'))
    new_value = to_string(node.get('new_value'))
    cur_path = f'{path}{node.get("key")}'
    if node['type'] == 'root':
        lines = map(lambda child: formatter_plain(child, path), children)
        result = '\n'.join(filter(bool, lines))
        return result
    if node['type'] == 'nested':
        lines = map(lambda child: formatter_plain(child, f"{cur_path}."), children)  # noqa: E501
        result = '\n'.join(filter(bool, lines))
        return result
    if node['type'] == 'added':
        return f"Property '{cur_path}' was added with value: {value}"
    if node['type'] == 'deleted':
        return f"Property '{cur_path}' was removed"
    if node['type'] == 'changed':
        return f"Property '{cur_path}' was updated. From {old_value} to {new_value}"  # noqa: E501


def plain_format(data):
    return formatter_plain(data)
