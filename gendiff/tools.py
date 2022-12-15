import os
from gendiff.parser import parse


def normalize_file_name(filename):  # normalize the file name for the current OS
    return filename.replace('/', os.sep).replace('\\', os.sep)


def get_file_extension(filename):  # get file extension
    return os.path.splitext(filename)[1]


def load_file(filename):  # load file
    with open(normalize_file_name(filename)) as file:
        return file.read()


def get_file_content(file_name):  # get file content
    file_extension = get_file_extension(file_name)
    with open(file_name) as f:
        data = f.read()
    return parse(data, file_extension)


def map_value(value):  # map values according to the task
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    else:
        return value


def map_stylish(value):  # map boolean values according to the task
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value
