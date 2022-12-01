from src.cli import parse_args
from src.gendiff import generate_diff
from src.tools import normalize_file_name
from src.output import print_diff
import json


def gen_diff():
    args = parse_args()  # get two files from command line
    with open(normalize_file_name(args.first_file)) as _:  # open first file
        dict1 = json.load(_)
    with open(normalize_file_name(args.second_file)) as _:  # open second file
        dict2 = json.load(_)
    print_diff(generate_diff(dict1, dict2))


def main():
    gen_diff()


if __name__ == '__main__':
    main()
