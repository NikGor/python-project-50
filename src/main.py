from src.cli import parse_args
from src.gendiff import generate_diff
from src.tools import get_file_content
from src.output import diff_to_str


def gen_diff():
    args = parse_args()  # get two files from command line
    dict1 = get_file_content(args.first_file)
    dict2 = get_file_content(args.second_file)
    diff = generate_diff(dict1, dict2)
    return diff_to_str(diff)


def main():
    gen_diff()


if __name__ == '__main__':
    main()
