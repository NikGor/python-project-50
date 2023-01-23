from gendiff.diff_tree import build_diff_tree
from gendiff.formaters.json import format_json
from gendiff.formaters.plain import format_plain
from gendiff.formaters.stylish import format_stylish
from gendiff.utils.file_utils import get_file_content


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
