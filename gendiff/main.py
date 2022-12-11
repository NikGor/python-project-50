from gendiff.logic import diff_calculator
from gendiff.tools import get_file_content
from gendiff.output import hexlet_stylish, diff_to_plain, diff_to_json


def generate_diff(first_file, second_file, output_type='stylish'):
    file1_content = get_file_content(first_file)
    file2_content = get_file_content(second_file)
    diff = diff_calculator(file1_content, file2_content)
    if output_type == 'plain':
        return diff_to_plain(diff)[:-1]
    elif output_type == 'json':
        return diff_to_json(diff)
    else:
        return hexlet_stylish(diff)
