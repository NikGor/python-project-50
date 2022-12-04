#!/usr/bin/env python3
from src import gendiff
from src.cli import parse_args


def main():
    args = parse_args()
    diff = gendiff.generate_diff(args.first_file, args.second_file, args.output_type)
    print(diff)


if __name__ == '__main__':
    main()
