from gendiff.diff_tree import build_diff_tree
from gendiff.tools import get_file_content
from gendiff.output import format_stylish, format_plain, format_json


def generate_diff(first_file, second_file, output_type='stylish'):
    dict1 = get_file_content(first_file)
    dict2 = get_file_content(second_file)
    diff_tree = build_diff_tree(dict1, dict2)
    if output_type == 'plain':
        return format_plain(diff_tree)[:-1]
    elif output_type == 'json':
        return format_json(diff_tree)
    else:
        return format_stylish(diff_tree)
