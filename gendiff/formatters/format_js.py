import json


def format_js(data_diff):
    """Return formatted data in JSON-String output."""

    output = json.dumps(data_diff, indent=2)
    return output
