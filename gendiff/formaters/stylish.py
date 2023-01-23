import json
from gendiff.diff_tree import diff_to_dict


def format_stylish(diff):
    result = json.dumps(diff_to_dict(diff), indent=4)
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
