import json
from gendiff.formaters.diff_tree_utils import convert_diff_tree_to_dict


def format_json(diff):
    return json.dumps(convert_diff_tree_to_dict(diff), indent=5)
