from gendiff.cli import parse_args
from gendiff.logic import generate_diff
from gendiff.tools import normalize_file_name
from gendiff.output import print_diff
import json


def gen_diff():
    # args = parse_args() # get two files from command line
    file1 = '//wsl$/Ubuntu-20.04/home/nikostolz/Hexlet/Python/python-project-50/tests/fixtures/file1.json'
    file2 = '//wsl$/Ubuntu-20.04/home/nikostolz/Hexlet/Python/python-project-50/tests/fixtures/file2.json'
    with open(normalize_file_name(file1)) as _:
        dict1 = json.load(_)
    with open(normalize_file_name(file2)) as _:
        dict2 = json.load(_)
    print_diff(generate_diff(dict1, dict2))


def main():
    gen_diff()


if __name__ == '__main__':
    main()
