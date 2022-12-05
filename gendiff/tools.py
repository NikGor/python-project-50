import os
import json
from collections import defaultdict

import yaml


def normalize_file_name(arg):  # normalize the file name for the current OS
    return arg.replace('/', os.sep).replace('\\', os.sep)


def get_file_extension(file_name):  # get file extension
    return os.path.splitext(file_name)[1]


def load_file(file_name):  # load file
    with open(normalize_file_name(file_name)) as _:
        return _.read()


def get_file_content(file_name):  # get file content as a dictionary
    file_extension = get_file_extension(file_name)
    if file_extension == '.json':
        return json.loads(load_file(file_name))
    elif file_extension in ('.yml', '.yaml'):
        return yaml.load(load_file(file_name), Loader=yaml.FullLoader)
    else:
        raise ValueError('Unknown file extension')


def map_value(value):  # map values according to the task
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value


def map_stylish(value):  # map boolean values according to the task
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def strip_dict(dict_to_strip):  # remove spaces from the beginning of the keys in the dictionary
    result = defaultdict(dict)
    for key, value in dict_to_strip.items():
        if isinstance(value, dict):
            result[key] = strip_dict(value)
        else:
            if isinstance(value, str):
                new_key = key.strip()
                result[new_key] = value.strip()
    return result
