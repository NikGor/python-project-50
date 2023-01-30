import json
from gendiff.formaters.diff_tree_utils import convert_diff_tree_to_dict


def format_stylish(diff):
    result = json.dumps(convert_diff_tree_to_dict(diff), indent=4)
    replace = {
        '"': '',
        ',': '',
        '   +': ' +',
        '   -': ' -',
        '"true"': 'true',
        '"false"': 'false',
        '"null"': 'null',
    }
    for key, value in replace.items():
        result = result.replace(key, value)
    return result
