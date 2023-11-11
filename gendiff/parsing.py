import json
import yaml


def parse_files(file_data, extension):
    """Getting a parsed JSON or YAML file."""

    if extension in ['.yaml', '.yml']:
        return yaml.safe_load(open(file_data))
    if extension == '.json':
        return json.load(open(file_data))
    else:
        raise ValueError(f"Unsupported file extension: {extension}")
