import json
import yaml
from yaml.loader import SafeLoader
import os


def get_path(file):
    f = os.path.abspath(file)
    return f


def get_extension(file):
    f = get_path(file)
    _, extension = os.path.splitext(f)
    return extension


def parsing_yaml(file):
    file_path = get_path(file)
    extension = get_extension(file_path)
    if extension == '.yml' or extension == '.yaml':
        with open(file) as file1:
            data = yaml.load(file1, Loader=SafeLoader)
            return data
    else:
        return False


def parsing_json(file):
    file_path = get_path(file)
    extension = get_extension(file_path)
    if extension == '.json':
        data = json.load(open(file_path))
        return data
    else:
        return False
