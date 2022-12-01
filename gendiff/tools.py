import os


def normalize_file_name(arg):  # normalize the file name for the current OS
    return arg.replace('/', os.sep).replace('\\', os.sep)
