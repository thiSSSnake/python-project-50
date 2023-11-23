import json
import yaml
import os


def get_extension(file_name):
    '''Get extension of file(.json or .yaml/.yml)'''
    return os.path.splitext(file_name)[1]


def get_content(file_name):
    '''Get content from file.'''
    extension = get_extension(file_name)
    with open(file_name) as file:
        data = file.read()
    return parse_files(data, extension)


def parse_files(file_data, file_format):
    """Getting a parsed JSON or YAML file.
    First arg -- content from file
    Second arg -- .extension of file"""
    if file_format in ('.yml', '.yaml'):
        return yaml.load(file_data, Loader=yaml.SafeLoader)
    elif file_format == '.json':
        return json.loads(file_data)

    raise ValueError(f"Unsupported file extension: {file_format}.")
