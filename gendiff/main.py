from gendiff.logic import diff_calculator
from gendiff.tools import get_file_content
from gendiff.output import stylish, diff_to_plain, diff_to_json


def generate_diff(first_file, second_file, output_type='stylish'):
    dict1 = get_file_content(first_file)
    dict2 = get_file_content(second_file)
    diff = diff_calculator(dict1, dict2)
    if output_type == 'plain':
        return diff_to_plain(diff)
    elif output_type == 'json':
        return diff_to_json(diff)
    else:
        return stylish(diff)
