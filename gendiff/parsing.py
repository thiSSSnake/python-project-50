import json
import yaml
from yaml.loader import SafeLoader
import os


def parsing_yaml(file1, file2):
    f1, f1_extension = os.path.splitext(file1)
    f2, f2_extension = os.path.splitext(file2)
    if f1_extension == '.yml' or f1_extension == '.yaml':
        with open(file1) as file1:
            data1 = yaml.load(file1, Loader=SafeLoader)
            # return data1
    if f2_extension == '.yml' or f2_extension == '.yaml':
        with open(file2) as file2:
            data2 = yaml.load(file2, Loader=SafeLoader)
            # return data2
    else:
        return False
    return data1, data2


def parsing_json(file1, file2):
    f1, f1_extension = os.path.splitext(file1)
    f2, f2_extension = os.path.splitext(file2)
    if f1_extension == '.json':
        file1 = json.load(open(file1))
    if f2_extension == '.json':
        file2 = json.load(open(file2))
    else:
        return False
    return file1, file2
