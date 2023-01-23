import json
from gendiff.diff_tree import diff_to_dict


def format_json(diff):
    return json.dumps(diff_to_dict(diff), indent=5)
