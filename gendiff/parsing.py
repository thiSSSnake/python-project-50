import json
import yaml


def open_file(file_path: str):
    with open(file_path, 'r') as file:
        return parse_files(file_path, file)


def parse_files(path, file):
    """Getting a parsed JSON or YAML file."""

    if path.endswith('.yaml') or path.endswith('.yml'):
        return yaml.safe_load(file)
    if path.endswith('.json'):
        return json.load(file)

    raise ValueError(f"Unsupported file extension: {file}")
