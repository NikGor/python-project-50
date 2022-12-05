import os
import json
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
