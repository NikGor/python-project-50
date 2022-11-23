import os


def normalize_file_name(arg):
    basedir, _ = os.path.split(os.path.abspath(os.getcwd()))
    return os.path.join(basedir, os.path.normpath(arg))
