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
