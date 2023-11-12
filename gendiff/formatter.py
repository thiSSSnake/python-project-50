from gendiff.formatters import format_stylish, formatter_plain, format_js


def formatting(tree: dict, format_name='stylish') -> str:

    formats = {
        'stylish': format_stylish,
        'plain': formatter_plain,
        'json': format_js
    }
    if format_name in formats:
        return formats[format_name](tree)

    raise ValueError(f'Unknown format: {format_name}')
