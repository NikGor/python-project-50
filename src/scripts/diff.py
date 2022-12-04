#!/usr/bin/env python3
from src import gendiff
from src.cli import parse_args


def main():
    args = parse_args()
    print(gendiff.generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
